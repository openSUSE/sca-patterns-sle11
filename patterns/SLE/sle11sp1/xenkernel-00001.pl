#!/usr/bin/perl

# Title:       VMs may not start after SLES 11 SP1 update
# Description: Looking for Xen kernel issue causing VM load problems
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
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7006491",
	"META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=619120"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub hotplugScriptFailure {
	SDP::Core::printDebug('> hotplugScriptFailure', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'xen.txt';
	my $SECTION = 'virt-manager.log';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /Device.*could not be connected.*Hotplug scripts not working/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: hotplugScriptFailure(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< hotplugScriptFailure", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel('2.6.32.13-0.4-xen') == 0 ) {
		if ( hotplugScriptFailure() ) {
			SDP::Core::updateStatus(STATUS_CRITICAL, "VMs will fail to load, update Xen kernel");
		} else {
			SDP::Core::updateStatus(STATUS_WARNING, "VMs may fail to load, update Xen kernel");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ABORT: Outside the kernel scope, skipping Xen VM load test");
	}
SDP::Core::printPatternResults();

exit;

