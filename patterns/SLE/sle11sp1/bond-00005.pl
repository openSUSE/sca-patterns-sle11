#!/usr/bin/perl

# Title:       Enabling hotplug support for bonded network cards
# Description: Replaced hotplug network card never gets enslaved into the bond.
# Modified:    2013 Jun 24

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
	PROPERTY_NAME_CATEGORY."=Network",
	PROPERTY_NAME_COMPONENT."=Bond",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7008625"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub nicsBonded {
	SDP::Core::printDebug('> nicsBonded', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'network.txt';
	my $SEARCH_STRING = "BONDING_MASTER=.*yes";
	my $FOUND = SDP::Core::inSection($FILE_OPEN, $SEARCH_STRING);
	$RCODE++ if ( $FOUND );
	SDP::Core::printDebug("< nicsBonded", "Returns: $RCODE");
	return $RCODE;
}

sub noBusidNaming {
	SDP::Core::printDebug('> noBusidNaming', 'BEGIN');
	my $RCODE = 0;
	my $ARRAY_REF = $_[0];
	my @NICS = ();
	my %FAILED_NICS = ();
	my $SLAVE_IFACE = '';

	my $FILE_OPEN = 'network.txt';
	my @CONTENT = ();
	my $STATE = 0;
	my $CONTENT_FOUND = 0;
	if ( SDP::Core::loadFile($FILE_OPEN, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( $STATE ) {
				if ( /^#==\[/ ) {
					$STATE = 0;
					@NICS = keys %FAILED_NICS;
					SDP::Core::printDebug(" DONE", "State Off");
				} elsif ( /BONDING_SLAVE.*='(.*)'/ ) { # Section content needed
					my $SLAVE_IFACE = $1;
					$FAILED_NICS{$SLAVE_IFACE} = 1; # assume NIC will fail
					SDP::Core::printDebug(" SLAVE PUSHED", $SLAVE_IFACE);
					$CONTENT_FOUND = 1;
				}
			} elsif ( /^# \/etc\/sysconfig\/network\/ifcfg-bond/ ) { # Section
				$STATE = 1;
				SDP::Core::printDebug("NET CHECK", "Section: $_");
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: noBusidNaming(): Cannot load file: $FILE_OPEN");
	}

	$FILE_OPEN = 'udev.txt';
	@CONTENT = ();
	$STATE = 0;
	$CONTENT_FOUND = 0;
	if ( SDP::Core::loadFile($FILE_OPEN, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( $STATE ) {
				if ( /^#==\[/ ) {
					$STATE = 0;
					SDP::Core::printDebug(" DONE", "State Off");
				} elsif ( /\sKERNELS==/i ) { # Section content needed
					SDP::Core::printDebug(" KERNELS", $_);
					foreach $SLAVE_IFACE (@NICS) {
						if ( /\sNAME=.*$SLAVE_IFACE/i ) { # Validate nics with bus id naming
							SDP::Core::printDebug("  VALID", $SLAVE_IFACE);
							$FAILED_NICS{$SLAVE_IFACE} = 0;
						}
					}
				}
			} elsif ( /^# \/etc\/udev\/.*net.*rules/ ) { # Section
				$STATE = 1;
				SDP::Core::printDebug("UDEV CHECK", "Section: $_");
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: noBusidNaming(): Cannot load file: $FILE_OPEN");
	}
	foreach $SLAVE_IFACE (@NICS) {
		if ( $FAILED_NICS{$SLAVE_IFACE} > 0 ) {
			push(@$ARRAY_REF, $SLAVE_IFACE);
		}
	}
	$RCODE = scalar @$ARRAY_REF;
	SDP::Core::printDebug("< noBusidNaming", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( nicsBonded() ) {
		if ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 ) {
			my $RPM_NAME = 'sysconfig';
			my $VERSION_TO_COMPARE = '0.71.30-0.10.1';
			my $RPM_COMPARISON = SDP::SUSE::compareRpm($RPM_NAME, $VERSION_TO_COMPARE);
			if ( $RPM_COMPARISON == 2 ) {
				SDP::Core::updateStatus(STATUS_ERROR, "ERROR: RPM $RPM_NAME Not Installed, skipping Bond check");
			} elsif ( $RPM_COMPARISON > 2 ) {
				SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Multiple Versions of $RPM_NAME RPM are Installed, skipping Bond check");
			} else {
				my @BIDNICS = ();
				if ( $RPM_COMPARISON < 0 ) {
					if ( noBusidNaming(\@BIDNICS) ) {
						SDP::Core::updateStatus(STATUS_WARNING, "If you have bonded hotplug NICs, they may fail to enslave if replaced; Update system for $RPM_NAME-$VERSION_TO_COMPARE or higher, and configure Bus ID based udev rules for: @BIDNICS");
					} else {
						SDP::Core::updateStatus(STATUS_WARNING, "If you have bonded hotplug NICs, they may fail to enslave if replaced; Update system for $RPM_NAME-$VERSION_TO_COMPARE or higher.");
					}
				} else {
					if ( noBusidNaming(\@BIDNICS) ) {
						SDP::Core::updateStatus(STATUS_WARNING, "If you have bonded hotplug NICs, they may fail to enslave if replaced; Configure Bus ID based udev rules for: @BIDNICS");
					} else {
						SDP::Core::updateStatus(STATUS_ERROR, "Bonded hotplug NICs appear to be configured properly");
					}
				}			
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: SLE11SP1 required, skipping Bond check");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Bonded NICS required, skipping Bond check");
	}
SDP::Core::printPatternResults();

exit;

