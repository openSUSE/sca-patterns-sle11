#!/usr/bin/perl -w

# Title:       Virtual Machine manager fails to create VMs
# Description: Detects a known issue with the SLE11 shipping Virtual Machine Manager that fails to create paravirtual VMs.
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
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#  Authors/Contributors:
#     Jason Record (jrecord@suse.com)
#     Ben Howard (bhoward@novell.com)
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
	PROPERTY_NAME_CATEGORY."=Virtualization",
	PROPERTY_NAME_COMPONENT."=Xen",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7002815"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub virtManError {
	SDP::Core::printDebug('>', 'virtManError');
	my $RCODE                    = 0;
	my $FILE_OPEN                = 'xen.txt';
	my $SECTION                  = 'virt-manager.log';
	my @CONTENT                  = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( /^\s*$/ );                   # Skip blank lines
			if ( /vminstall\.Error.*Boot loader didn\'t return any data/ ) {
				SDP::Core::printDebug("LINE", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< Returns: $RCODE", 'virtManError');
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	use constant SLE11 => '2.6.27.19';
	use constant SLE11VMAN => '0.5.3-66.37';
	my %HOST_INFO = SDP::SUSE::getHostInfo();
	my $RPMSTATUS = SDP::SUSE::compareRpm('virt-manager', SLE11VMAN);

	if ( $RPMSTATUS < 2 ) {
		if ( SDP::SUSE::compareKernel(SLE11) >= 0 && $RPMSTATUS <= 0) {
			printDebug('XEN', $HOST_INFO{'kernel'});
			if ( $HOST_INFO{'kernel'} !~ m/xen/i ) {
				SDP::Core::updateStatus(STATUS_ERROR, "Xen kernel is not running");
			} elsif ( virtManError() ) {
				SDP::Core::updateStatus(STATUS_CRITICAL, "Detected failed paravirtual VM creation attempts");
			} else {
				SDP::Core::updateStatus(STATUS_ERROR, "Virtual Machine Manager can create Paravirtual VMs");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Virtual Machine Manager can create Paravirtual VMs");
		}
	} elsif ( $RPMSTATUS == 2 ) {
		SDP::Core::updateStatus(STATUS_ERROR, "Virtual Machine Manager not installed");
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Too many virt-manager packages installed.");
	}

SDP::Core::printPatternResults();

exit;

