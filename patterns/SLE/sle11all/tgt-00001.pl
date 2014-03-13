#!/usr/bin/perl

# Title:       iscsitarget gets replaced by tgt
# Description: Update process fails to preserve iscsitarget
# Modified:    2013 Jun 25

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
	PROPERTY_NAME_CATEGORY."=Update",
	PROPERTY_NAME_COMPONENT."=iSCSI",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7009913",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=732751"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub iscsiTargetInstall {
	SDP::Core::printDebug('> iscsiTargetInstall', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'y2log.txt';
	my $SECTION = '\/y2log$';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /Install.*iscsitarget-\d.*SUSE-Linux-Enterprise/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: iscsiTargetInstall(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< iscsiTargetInstall", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $PKG_NAME = 'tgt';
	if ( SDP::SUSE::packageInstalled($PKG_NAME) ) {
		if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE12GA) < 0 ) {
			if ( iscsiTargetInstall() ) {
				SDP::Core::updateStatus(STATUS_CRITICAL, "The iscsitarget package was probably replaced by tgt after update");
			} else {
				my $SERVICE_NAME = 'tgtd';
				my %SERVICE_INFO = SDP::SUSE::getServiceInfo($SERVICE_NAME);
				if ( $SERVICE_INFO{'runlevelstatus'} == 0 ) {
					SDP::Core::updateStatus(STATUS_CRITICAL, "Confirm tgt did not replace the iscsitarget package");
				} else {
					SDP::Core::updateStatus(STATUS_WARNING, "Confirm tgt did not replace the iscsitarget package");
				}
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Outside kernel scope, skipping");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Error: Package $PKG_NAME not installed, skipping");
	}
SDP::Core::printPatternResults();

exit;


