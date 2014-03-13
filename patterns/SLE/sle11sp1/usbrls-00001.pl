#!/usr/bin/perl

# Title:       USB Keyboards in Runlevel S Fail
# Description: USB keyboard driver fails to load in runlevel S
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
	PROPERTY_NAME_COMPONENT."=USB",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7007690"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub usbKeyboard {
	SDP::Core::printDebug('> usbKeyboard', 'BEGIN');
	my $RCODE = 0;
	my @LINE_CONTENT = ();
	my $FILE_OPEN = 'hardware.txt';
	my $SECTION = 'hwinfo';
	my @CONTENT = ();
	my $HALSECTION = 0;
	my $DEVICE = 0;
	my $KEYBOARD = 0;
	my $USBHID = 0;

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			if ( $HALSECTION ) { # process hal device list
				if ( $DEVICE ) { # process device values
					if ( m/usb.interface.description\s*=\s*.*Keyboard/i ) {
						$KEYBOARD = 1;
					} elsif ( m/info.linux.driver\s*=\s*.*usbhid/i ) {
						$USBHID = 1;
					} elsif ( m/^\s*$/ ) { # end of device information
						if ( $KEYBOARD ) { # this device was a keyboard
							if ( $USBHID ) { # this keyboard uses the usbhid driver
								SDP::Core::printDebug("DETECTED", "USB Keyboard using usbhid");
								$RCODE = 1;
								last;
							} else { # this keyboard does not use the usbhid driver
								SDP::Core::printDebug("INGORNED", "Not a USB Keyboard using usbhid");
							}
						}
						$DEVICE = 0; # start over
						$KEYBOARD = 0; # start over
						$USBHID = 0; # start over
					}
				} elsif ( /^\s*\d*:\s/ ) { # found a device
					$DEVICE = 1;
				} elsif ( /- hal device list end -/ ) { # no more devices to process, end of hal section
					$HALSECTION = 0;
					last;
				}
			} elsif ( /- hal device list -/ ) { # found the hal device list
				$HALSECTION = 1;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: usbKeyboard(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< usbKeyboard", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if  ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel(SLE11SP2) < 0 ) {
		my $DRIVER_NAME = 'usbhid';
		my %DRIVER_INFO = SDP::SUSE::getDriverInfo($DRIVER_NAME);
		if ( $DRIVER_INFO{'loaded'} ) {
			if ( usbKeyboard() ) {
				SDP::Core::updateStatus(STATUS_WARNING, "Server may be unresponsive in runlevel S due to USB keyboard");
			} else {
				SDP::Core::updateStatus(STATUS_WARNING, "USB devices may not work in runlevel S");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Driver $DRIVER_NAME is NOT loaded");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Outside Kernel Scope, skipping usbdriver test");
	}
SDP::Core::printPatternResults();

exit;


