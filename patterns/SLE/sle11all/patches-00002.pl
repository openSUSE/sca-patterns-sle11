#!/usr/bin/perl -w

# Title:       Checks applied patches on SLE11
# Description: Checks if security, recommended or optional patches have been applied for SLE11.
# Modified:    2013 Jun 25

##############################################################################
#  Copyright (C) 2013,2012 SUSE LLC
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
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#  Authors/Contributors:
#     Jason Record (jrecord@suse.com)
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
	PROPERTY_NAME_CATEGORY."=Update",
	PROPERTY_NAME_COMPONENT."=Patches",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7004974",
	"META_LINK_TID2=http://www.suse.com/support/kb/doc.php?id=7000387"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub patches_available {
	SDP::Core::printDebug('> patches_available', 'BEGIN');
	my $RCODE = 0; # No patches available
	my $FILE_OPEN = 'updates.txt';
	my $SECTION = 'zypper --non-interactive --no-gpg-checks patches';
	my @CONTENT = ();
	my @LINE_CONTENT = ();
	my $LINE = 0;

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			$LINE++;
			next if ( /^\s*$/ ); # Skip blank lines
			if ( /^Catalog\s/ ) {
				SDP::Core::printDebug("LINE $LINE", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	if ( ! $RCODE ) {
		SDP::Core::updateStatus(STATUS_ERROR, "No patches to check");
	}
	SDP::Core::printDebug("< patches_available", "Returns: $RCODE");
	return $RCODE;
}

sub check_patch_category() {
	SDP::Core::printDebug('>', 'check_patch_category');
	use constant CATEGORY_FIELD            => 3;
	use constant STATUS_FIELD              => 4;
	my $HEADER_LINES    = 4;
	my $FILE_OPEN       = 'updates.txt';
	my $SECTION         = 'zypper --non-interactive --no-gpg-checks patches';
	my @CONTENT         = ();
	my @LINE_DATA       = ();
	my $LINE            = 0;
	my $FOUND_PATCHES   = 0;
	my $CNT_SECURITY    = 0;
	my $CNT_RECOMMENDED = 0;
	my $CNT_OPTIONAL    = 0;
	my $CNT_OTHER       = 0;
	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			$LINE++;
			next if ( $LINE < $HEADER_LINES );
			next if ( m/^$/ );
			$_ =~ s/\s+\|\s+/\|/g;
			$_ =~ s/^\s+|\s+$//g;
			SDP::Core::printDebug("LINE $LINE", $_);
			@LINE_DATA = split(/\|/, $_);
			if ( $#LINE_DATA == STATUS_FIELD ) {
				if ( $LINE_DATA[STATUS_FIELD] =~ m/^needed/i ) {
					for ( $LINE_DATA[CATEGORY_FIELD] ) {
						if      ( /security/i ) {
							$CNT_SECURITY++;
						} elsif ( /recommended/i ) {
							$CNT_RECOMMENDED++;
						} elsif ( /optional/i ) {
							$CNT_OPTIONAL++;
						} else {
							$CNT_OTHER++;
						}
					}
				}
			}
		}
		SDP::Core::printDebug("SEC/REC/OPT/OTHER", "$CNT_SECURITY/$CNT_RECOMMENDED/$CNT_OPTIONAL/$CNT_OTHER");
		if ( $CNT_SECURITY ) {
			SDP::Core::updateStatus(STATUS_CRITICAL, "Patches Needed: $CNT_SECURITY Security, $CNT_RECOMMENDED Recommended, $CNT_OPTIONAL Optional");
		} elsif ( $CNT_RECOMMENDED ) {
			SDP::Core::updateStatus(STATUS_WARNING, "Patches Needed: $CNT_SECURITY Security, $CNT_RECOMMENDED Recommended, $CNT_OPTIONAL Optional");
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Patches Needed: $CNT_SECURITY Security, $CNT_RECOMMENDED Recommended, $CNT_OPTIONAL Optional");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug('<', 'check_patch_category');
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 ) {
		check_patch_category() if patches_available();
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Outside kernel scope, skipping");
	}
SDP::Core::printPatternResults();

exit;

