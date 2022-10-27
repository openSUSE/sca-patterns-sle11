#!/usr/bin/perl -w

# Title:       Check for missing LVM UUIDs
# Description: Physical volumes can be removed or damaged and appear missing. This pattern looks for missing physical volumes.
# Modified:    2022 Oct 27

##############################################################################
#  Copyright (C) 2013,2022 SUSE LLC
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
#     Jason Record <jason.record@suse.com>
#
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
	PROPERTY_NAME_CATEGORY."=LVM",
	PROPERTY_NAME_COMPONENT."=Disk",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=3803380",
	"META_LINK_Blog=https://www.suse.com/c/recovering-lost-lvm-volume-disk/"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub check_missing_uuids {
	SDP::Core::printDebug('> check_missing_uuids', 'BEGIN');
	use constant HEADER_LINES   => 0;
	my $RCODE                    = 0;
	my $FILE_OPEN                = 'lvm.txt';
	my $SECTION                  = 'pvscan';
	my @CONTENT                  = ();
	my @LINE_CONTENT             = ();
	my $LINE                     = 0;

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( $LINE++ < HEADER_LINES ); # Skip header lines
			next if ( /^\s*$/ );                   # Skip blank lines
			if ( /Couldn\'t find device with uuid/i ) {
				s/[\',\.]|^\s+//g;
				SDP::Core::printDebug("LINE $LINE", $_);
				@LINE_CONTENT = split(/\s+/, $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	if ( $RCODE ) {
		SDP::Core::updateStatus(STATUS_CRITICAL, "Missing LVM disk with UUID $LINE_CONTENT[5]");
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "All LVM disk UUIDs found");
	}
	SDP::Core::printDebug("< check_missing_uuids", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	check_missing_uuids();
SDP::Core::printPatternResults();

exit;

