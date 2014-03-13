#!/usr/bin/perl

# Title:       Missing characters or line breaks with telnet
# Description: telnet or rlogin session missing some characters and line breaks
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
	PROPERTY_NAME_CATEGORY."=Kernel",
	PROPERTY_NAME_COMPONENT."=Telnet",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7011700",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=797042"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::packageInstalled('telnet') && SDP::SUSE::packageInstalled('rsh') ) {
		my $LAST_KERNEL_VERSION = '3.0.51-0.7.9';
		if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel($LAST_KERNEL_VERSION) <= 0 ) {
			my $RPM_NAME = 'login';
			my $VERSION_TO_COMPARE = '3.41-0.4.2';
			my $RPM_COMPARISON = SDP::SUSE::compareRpm($RPM_NAME, $VERSION_TO_COMPARE);
			if ( $RPM_COMPARISON == 2 ) {
				SDP::Core::updateStatus(STATUS_ERROR, "ERROR: RPM $RPM_NAME Not Installed");
			} elsif ( $RPM_COMPARISON > 2 ) {
				SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Multiple Versions of $RPM_NAME RPM are Installed");
			} else {
				if ( $RPM_COMPARISON >= 0 ) {
					SDP::Core::updateStatus(STATUS_WARNING, "Detected kernel reset TTY packet mode issue, update system for a new kernel package");
				} else {
					SDP::Core::updateStatus(STATUS_ERROR, "Error: Earlier login package does not expose kernel, skipping TTY reset test");
				}			
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Error: Outside kernel scope, skipping TTY reset test");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Error: telnet or rsh packges required, skipping TTY reset test");
	}
SDP::Core::printPatternResults();

exit;


