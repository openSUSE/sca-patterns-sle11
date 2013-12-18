#!/usr/bin/perl

# Title:       LIP reset or device change
# Description: Check for potential kernel performance issue
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
	PROPERTY_NAME_COMPONENT."=Fibre",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7011398",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=789836"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub fibreCardFound {
	SDP::Core::printDebug('> fibreCardFound', 'BEGIN');
	my $RCODE = 0;
	my @LINE_CONTENT = ();
	my $FILE_OPEN = 'hardware.txt';
	my $SECTION = 'lspci -b';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /\sfibre\s|\sfiber\s/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: fibreCardFound(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< fibreCardFound", "Returns: $RCODE");
	return $RCODE;
}

sub rawSpinUnlock {
	SDP::Core::printDebug('> rawSpinUnlock', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'messages.txt';
	my $SECTION = '/var/log/warn';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /_raw_spin_unlock_irqrestore/ ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: rawSpinUnlock(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< rawSpinUnlock", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel('3.0.42-0.7') == 0) {
		if ( fibreCardFound() ) {
			if ( rawSpinUnlock() ) {
				SDP::Core::updateStatus(STATUS_CRITICAL, "Probable kernel crash on fibre card LIP reset");
			} else {
				SDP::Core::updateStatus(STATUS_WARNING, "Potential kernel crash on fibre card LIP reset");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Error: No Fibre Card detected, skipping rawSpinUnlock");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Error: Outside Kernel Scope, skipping rawSpinUnlock");
	}
SDP::Core::printPatternResults();

exit;


