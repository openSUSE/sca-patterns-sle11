#!/usr/bin/perl

# Title:       Xen VM Fails to Boot
# Description: Xen VMs using MPIO on both the host and vm may fail
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
	PROPERTY_NAME_CATEGORY."=Xen",
	PROPERTY_NAME_COMPONENT."=MPIO",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7011590",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=787721"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub mpioDevicesFound {
	SDP::Core::printDebug('> mpioDevicesFound', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'mpio.txt';
	my $SECTION = 'multipath -ll';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /\sdm-\d*\s/ ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: mpioDevicesFound(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< mpioDevicesFound", "Returns: $RCODE");
	return $RCODE;
}

sub mpioNoPartitionsFound {
	SDP::Core::printDebug('> mpioNoPartitionsFound', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'mpio.txt';
	my $SECTION = 'multipath.conf';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /features.*no_partitions"/ ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: mpioDevicesFound(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< mpioNoPartitionsFound", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if  ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
		if ( 	SDP::SUSE::xenDom0running() ) {
			if ( mpioDevicesFound() ) {
				if ( mpioNoPartitionsFound() ) {
					SDP::Core::updateStatus(STATUS_RECOMMEND, "Confirm virutal machines using MPIO devices");
				} else {
					SDP::Core::updateStatus(STATUS_CRITICAL, "Virtual machines assigned MPIO devices may fail to boot");
				}
			} else {
				SDP::Core::updateStatus(STATUS_ERROR, "SP2 Error, MPIO devices assigned to VMs required, skipping MPIO test");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "SP2 Error, Xen Dom0 required, skipping MPIO test");
		}
	} elsif ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel(SLE11SP2) < 0 ) {
		if ( 	SDP::SUSE::xenDom0running() ) {
			if ( mpioDevicesFound() ) {
				if ( mpioNoPartitionsFound() ) {
					SDP::Core::updateStatus(STATUS_RECOMMEND, "Confirm virtual machines using MPIO devices before updating");
				} else {
					SDP::Core::updateStatus(STATUS_WARNING, "Prepare virtual machines using MPIO devices before updating");
				}
			} else {
				SDP::Core::updateStatus(STATUS_ERROR, "SP1 Error, MPIO devices assigned to VMs required, skipping MPIO test");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "SP1 Error, Xen Dom0 required, skipping MPIO test");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Outside kernel scope, SP1-SP2 required");
	}
SDP::Core::printPatternResults();

exit;


