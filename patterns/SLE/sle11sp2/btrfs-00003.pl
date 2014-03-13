#!/usr/bin/perl

# Title:       Panic in btrfs_end_transaction
# Description: Fix use-after-free in __btrfs_end_transaction
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
use constant BTRFS_FIXED_VERSION => '3.0.58-0.6';

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

@PATTERN_RESULTS = (
	PROPERTY_NAME_CLASS."=SLE",
	PROPERTY_NAME_CATEGORY."=Filesystem",
	PROPERTY_NAME_COMPONENT."=btrfs",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7004074",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=756628"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub loadErrorFound {
	SDP::Core::printDebug('> loadErrorFound', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'messages.txt';
	my $SECTION = '/var/log/warn';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /[<.*>].*__btrfs_end_transaction.*[btrfs]/ ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: loadErrorFound(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< loadErrorFound", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $DRIVER_NAME = 'btrfs';
	my %DRIVER_INFO = SDP::SUSE::getDriverInfo($DRIVER_NAME);
	if ( $DRIVER_INFO{'loaded'} ) {
		if  ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(BTRFS_FIXED_VERSION) < 0 ) {
			if ( loadErrorFound() ) {
				SDP::Core::updateStatus(STATUS_CRITICAL, "Detected use-after-free in __btrfs_end_transaction, upgrade system to apply latest kernel");
			} else {
				SDP::Core::updateStatus(STATUS_WARNING, "System susceptible to btrfs kernel panic, upgrade system to apply latest kernel");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Outside kernel scope, skipping btrfs panic");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Driver $DRIVER_NAME is NOT loaded");
	}

SDP::Core::printPatternResults();

exit;


