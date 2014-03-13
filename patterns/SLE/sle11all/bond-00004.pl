#!/usr/bin/perl

# Title:       SLES11 XEN Bridge bonding with bnx2x very slow
# Description: The solution is to switch off the tpx option of the interface
# Modified:    2013 Jun 24

##############################################################################
#  Copyright (C) 2013 SUSE LLC
##############################################################################
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; version 2 of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)

##############################################################################

##############################################################################
# Module Definition
##############################################################################

use strict;
use warnings;
use SDP::Core;
use SDP::SUSE;

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

@PATTERN_RESULTS = (
	PROPERTY_NAME_CLASS."=SLE",
	PROPERTY_NAME_CATEGORY."=Network",
	PROPERTY_NAME_COMPONENT."=Bond",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7007658"
);

my $DRV_NAME = 'bnx2x';

##############################################################################
# Local Function Definitions
##############################################################################

sub nicsBonded {
	SDP::Core::printDebug('> nicsBonded', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'network.txt';
	my $SEARCH_STRING = "BONDING_MASTER=.*yes";
	my $FOUND = SDP::Core::inSection($FILE_OPEN, $SEARCH_STRING);
	$RCODE++ if ( $FOUND );
	SDP::Core::printDebug("< nicsBonded", "Returns: $RCODE");
	return $RCODE;
}

sub tpxDisabled {
	SDP::Core::printDebug('> tpxDisabled', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'modules.txt';
	my $SEARCH_STRING = "options.*$DRV_NAME.*disable_tpx=1";
	my $FOUND = SDP::Core::inSection($FILE_OPEN, $SEARCH_STRING);
	$RCODE++ if ( $FOUND );
	SDP::Core::printDebug("< tpxDisabled", "Returns: $RCODE");
	return $RCODE;
}

sub lroError {
	SDP::Core::printDebug('> lroError', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'messages.txt';
	my $SECTION = '/var/log/messages';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (reverse(@CONTENT)) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /received packets cannot be forwarded while LRO is enabled/i ) {
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: lroError(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< lroError", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE12GA) < 0 && SDP::SUSE::xenDom0running() ) {
		my %DRIVER = SDP::SUSE::getDriverInfo($DRV_NAME);
		if ( $DRIVER{'loaded'} ) {
			if ( tpxDisabled() ) {
				SDP::Core::updateStatus(STATUS_ERROR, "TPX disabled on $DRV_NAME driver");
			} elsif ( nicsBonded() ) {
				if ( lroError() ) {
					SDP::Core::updateStatus(STATUS_CRITICAL, "LRO network error detected, disable TPX on $DRV_NAME driver");
				} else {
					SDP::Core::updateStatus(STATUS_WARNING, "Disable TPX on $DRV_NAME driver to avoid network issues");
				}
			} else {
				SDP::Core::updateStatus(STATUS_ERROR, "ERROR: No bonded nics found, skipping $DRV_NAME test");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $DRV_NAME driver NOT loaded");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Outside kernel scope, skipping $DRV_NAME driver check");
	}
SDP::Core::printPatternResults();

exit;

