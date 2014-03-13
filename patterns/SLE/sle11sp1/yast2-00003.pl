#!/usr/bin/perl

# Title:       YaST2 browse dialog may hang
# Description: Yast2 appears to hang when using the Browse dialog
# Modified:    2013 Jun 27

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
	PROPERTY_NAME_CATEGORY."=YaST",
	PROPERTY_NAME_COMPONENT."=Base",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7008966"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub checkSomething {
	SDP::Core::printDebug('> checkSomething', 'BEGIN');
	my $RCODE = 0;
	my $LINE = 0;
	my $HEADER_LINES = 0;
	my @LINE_CONTENT = ();
	my $FILE_OPEN = 'filename.txt';
	my $SECTION = 'CommandToIdentifyFileSection';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			$LINE++;
			next if ( $LINE < $HEADER_LINES ); # Skip header lines
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /^SearchForThisConentatBeginningofLine/ ) {
				SDP::Core::printDebug("PROCESSING", $_);
				@LINE_CONTENT = split(/\s+/, $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: checkSomething(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< checkSomething", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 ) {
		my $RPM_NAME = 'yast2-qt';
		my $VERSION_TO_COMPARE = '2.18.13';
		my $RPM_COMPARISON = SDP::SUSE::compareRpm($RPM_NAME, $VERSION_TO_COMPARE);
		if ( $RPM_COMPARISON == 2 ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: RPM $RPM_NAME Not Installed");
		} elsif ( $RPM_COMPARISON > 2 ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Multiple Versions of $RPM_NAME RPM are Installed");
		} else {
			if ( $RPM_COMPARISON < 0 ) {
				SDP::Core::updateStatus(STATUS_WARNING, "YaST2 dialog browse features may hang, update system to apply $RPM_NAME-$VERSION_TO_COMPARE or later");
			} else {
				SDP::Core::updateStatus(STATUS_ERROR, "YaST2 browse hang avoided, $RPM_NAME version is sufficient.");
			}			
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Outside the kernel scope, skipping yast2 browse test");
	}
SDP::Core::printPatternResults();

exit;

