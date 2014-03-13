#!/usr/bin/perl

# Title:       SLP Directory Agent on SLE11
# Description: SLES11 does not work as an SLP Directory Agent
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
#

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
	PROPERTY_NAME_CATEGORY."=SLP",
	PROPERTY_NAME_COMPONENT."=DA",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7005104",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=510228"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub slpDAconfigured {
	SDP::Core::printDebug('> slpDAconfigured', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'slp.txt';
	my $SECTION = '/etc/slp.conf';
	my @CONTENT = ();
	my $LINE = 0;

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			$LINE++;
			next if ( /^\s*$/ ); # Skip blank lines
			if ( /net.slp.isDA.*true/i ) {
				SDP::Core::printDebug("LINE $LINE", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< slpDAconfigured", "Returns: $RCODE");
	return $RCODE;
}

sub checkIP {
	SDP::Core::printDebug('> checkIP', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'network.txt';
	my $SECTION = '/etc/hosts';
	my @CONTENT = ();
	my @LINE_CONTENT = ();
	my $LINE = 0;
	my %INFO = SDP::SUSE::getHostInfo();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			$LINE++;
			next if ( /^\s*$/ ); # Skip blank lines
			if ( /$INFO{'hostname'}/ ) {
				SDP::Core::printDebug("LINE $LINE", $_);
				@LINE_CONTENT = split(/\s+/, $_);
				if ( $LINE_CONTENT[0] =~ /^127\./ ) {
					if ( $LINE_CONTENT[0] =~ /^127\.0\.0\.1/ ) {
						SDP::Core::updateStatus(STATUS_ERROR, "Observed a valid SLP DA address");
					} else {
						$RCODE++;
						SDP::Core::updateStatus(STATUS_CRITICAL, "SLP DA failure due to loopback address");
					}
				} else {
					SDP::Core::updateStatus(STATUS_ERROR, "Observed a valid SLP DA address");
				}
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< checkIP", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE12GA) < 0 ) {
		slpDAconfigured() ? checkIP() : SDP::Core::updateStatus(STATUS_ERROR, "Error: No SLP DA configured, skipping test");
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Error: Outside kernel scope, skipping SLP DA test");
	}
	slpDAconfigured();
SDP::Core::printPatternResults();

exit;

