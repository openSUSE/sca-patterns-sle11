#!/usr/bin/perl

# Title:       Xen host having issues rebooting windows 2008 guest
# Description: Detects Out of populate-on-demand memory error
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
	PROPERTY_NAME_COMPONENT."=Xen",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7008837",
	"META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=626262"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub podMemError {
	SDP::Core::printDebug('> podMemError', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'xen.txt';
	my $SECTION = 'xm dmesg';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /Out of populate-on-demand memory/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: podMemError(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< podMemError", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $RPM_NAME = 'xen';
	my $VERSION_TO_COMPARE = '4.0.1_21326_03-0.3.1';
	my $RPM_COMPARISON = SDP::SUSE::compareRpm($RPM_NAME, $VERSION_TO_COMPARE);
	if ( $RPM_COMPARISON == 2 ) {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: RPM $RPM_NAME Not Installed");
	} elsif ( $RPM_COMPARISON > 2 ) {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Multiple Versions of $RPM_NAME RPM are Installed");
	} else {
		if ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 ) {
			if ( $RPM_COMPARISON < 0 ) { # outdated rpm
				if ( podMemError() ) {
					SDP::Core::updateStatus(STATUS_CRITICAL, "Hardware VMs Will Fail to Boot, Update System to Apply $RPM_NAME-$VERSION_TO_COMPARE or higher");
				} else {
					SDP::Core::updateStatus(STATUS_WARNING, "Hardware VMs May Fail to Boot, Update System to Apply $RPM_NAME-$VERSION_TO_COMPARE or higher");
				}
			} else {
				if ( podMemError() ) {
					SDP::Core::updateStatus(STATUS_CRITICAL, "Hardware VMs Will Fail to Boot, Reboot the Server for Xen Fixes to Take Affect");
				} else {
					SDP::Core::updateStatus(STATUS_ERROR, "IGNORED: Xen Updates Applied, Skipping Xen POD Memory Error Test");
				}
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Outside Kernel Scope, skipping Xen POD Memory Error Test");
		}			
	}
SDP::Core::printPatternResults();

exit;

