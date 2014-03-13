#!/usr/bin/perl

# Title:       Hyper-V Bond Failing
# Description: Bonding on SLES11SP2 Hyper-V guest fails after update
# Modified:    2013 Jun 28

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
	PROPERTY_NAME_CATEGORY."=Virtualization",
	PROPERTY_NAME_COMPONENT."=Network",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7011418",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=790943"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub hyperVM {
	SDP::Core::printDebug('> hyperVM', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'basic-environment.txt';
	my $SECTION = 'Virtualization';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /^Hypervisor.*Microsoft/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: hyperVM(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< hyperVM", "Returns: $RCODE");
	return $RCODE;
}

sub bondFailure {
	SDP::Core::printDebug('> bondFailure', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'boot.txt';
	my $SECTION = '\/boot.msg$';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /Removing bonding interface/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: bondFailure(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< bondFailure", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( hyperVM() ) {
		if ( SDP::SUSE::compareKernel('3.0.38-0.5') >= 0 && SDP::SUSE::compareKernel('3.0.42-0.7') <= 0) {
			if ( bondFailure() ) {
				SDP::Core::updateStatus(STATUS_CRITICAL, "Hyper-V related network bond failure");
			} else {
				SDP::Core::updateStatus(STATUS_ERROR, "Network bond seems to be working or not configured");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Error: Outside kernel scope, skipping");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Error: Hyper-V not found, skipping");
	}
SDP::Core::printPatternResults();

exit;


