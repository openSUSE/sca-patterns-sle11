#!/usr/bin/perl

# Title:       Potential pvscan and vgscan segfault during boot
# Description: During one in about three boots vgscan or pvscan may segfault
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
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
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
	PROPERTY_NAME_CATEGORY."=Disk",
	PROPERTY_NAME_COMPONENT."=Device Mapper",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7004924",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=550363"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub lvmSegfaults {
	SDP::Core::printDebug('> lvmSegfaults', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'boot.txt';
	my $SECTION = 'boot.msg';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( /^\s*$/ ); # Skip blank lines
			if ( /boot\.lvm.*Segmentation fault/i ) {
				SDP::Core::printDebug("SEGFAULT", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< lvmSegfaults", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $RPM_NAME = 'device-mapper';
	my $VERSION_TO_COMPARE = '';
	my $RPM_COMPARISON = '';

	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE12GA) < 0 ) {
		$VERSION_TO_COMPARE = '1.02.27-8.9.1';
		$RPM_COMPARISON = SDP::SUSE::compareRpm($RPM_NAME, $VERSION_TO_COMPARE);
		if ( $RPM_COMPARISON == 2 ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: RPM $RPM_NAME Not Installed");
		} elsif ( $RPM_COMPARISON > 2 ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Multiple Versions of $RPM_NAME RPM are Installed");
		} else {
			if ( $RPM_COMPARISON < 0 ) {
				if ( lvmSegfaults() ) {
					SDP::Core::updateStatus(STATUS_CRITICAL, "Device mapper segfaults observed, update system to apply $RPM_NAME-$VERSION_TO_COMPARE");
				} else {
					SDP::Core::updateStatus(STATUS_WARNING, "Device mapper susceptible to segfaults, update system to apply $RPM_NAME-$VERSION_TO_COMPARE");
				}
			} else {
				SDP::Core::updateStatus(STATUS_ERROR, "Device mapper segfault bug 550363 not observed");
			}
		}
	} elsif ( SDP::SUSE::compareKernel(SLE10GA) >= 0 && SDP::SUSE::compareKernel(SLE11GA) < 0 ) {
		$VERSION_TO_COMPARE = '1.02.13-6.17.1';
		$RPM_COMPARISON = SDP::SUSE::compareRpm($RPM_NAME, $VERSION_TO_COMPARE);
		if ( $RPM_COMPARISON == 2 ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: RPM $RPM_NAME Not Installed");
		} elsif ( $RPM_COMPARISON > 2 ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Multiple Versions of $RPM_NAME RPM are Installed");
		} else {
			if ( $RPM_COMPARISON < 0 ) {
				if ( lvmSegfaults() ) {
					SDP::Core::updateStatus(STATUS_CRITICAL, "Device mapper segfaults observed, update system to apply $RPM_NAME-$VERSION_TO_COMPARE");
				} else {
					SDP::Core::updateStatus(STATUS_WARNING, "Device mapper susceptible to segfaults, update system to apply $RPM_NAME-$VERSION_TO_COMPARE");
				}
			} else {
				SDP::Core::updateStatus(STATUS_ERROR, "Device mapper segfault bug 550363 not observed");
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Outside the kernel scope, skipping device mapper test");
	}
SDP::Core::printPatternResults();

exit;

