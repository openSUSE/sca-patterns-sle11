#!/usr/bin/perl

# Title:       Possible kernel oops with balance-alb mode
# Description: SLES11 SP1 can crash when a network with bonding devices is stopped
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
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7006170",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=602969"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub isBonded {
	SDP::Core::printDebug('> isBonded', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'network.txt';
	my $SECTION = $_[0];
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /BONDING_MASTER=.*yes/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: isBonded(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< isBonded", "Returns: $RCODE");
	return $RCODE;
}

sub isMiiMonitorZero {
	SDP::Core::printDebug('> isMiiMonitorZero', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'boot.txt';
	my $SECTION = 'dmesg';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /bonding:.*Setting MII monitoring interval to 0/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: isMiiMonitorZero(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< isMiiMonitorZero", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if  ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel(SLE11SP2) < 0 ) {
		my $FILE_OPEN = 'network.txt';
		my @FILE_SECTIONS = ();
		my $CHECK = '';
		my $BONDING = 0;

		if ( SDP::Core::listSections($FILE_OPEN, \@FILE_SECTIONS) ) {
			foreach $CHECK (@FILE_SECTIONS) {
				if ( $CHECK =~ /\/etc\/sysconfig\/network\/ifcfg-/ ) {
					if ( isBonded($CHECK) ) {
						$BONDING = 1;
						if ( isMiiMonitorZero() ) {
							SDP::Core::updateStatus(STATUS_ERROR, "Network bonding MII monitoring set to 0");
						} else {
							SDP::Core::updateStatus(STATUS_WARNING, "Stopping and starting network may contribute to kernel oops");
						}
					}
				}
			}
			if ( ! $BONDING ) {
				SDP::Core::updateStatus(STATUS_ERROR, "ERROR: No network bonding, aborting bond oops check");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: myFunction(): No sections found in $FILE_OPEN");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Outside kernel scope, skipping bonding mode kernel oops test");
	}
SDP::Core::printPatternResults();

exit;

