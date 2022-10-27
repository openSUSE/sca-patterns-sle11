#!/usr/bin/perl

# Title:       Unknown Qlogic Parameters
# Description: Qlogic HBA drivers fail to load at boot time
# Modified:    2013 Jun 27

##############################################################################
#  Copyright (C) 2013,2012 SUSE LLC
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
	PROPERTY_NAME_COMPONENT."=HBA",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=3331914",
	"META_LINK_MISC=http://www.suse.com/support/php/search.do?cmd=displayKC&docType=kc&externalId=3864925"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub qlogicFibre {
	SDP::Core::printDebug('> qlogicFibre', 'BEGIN');
	my $RCODE = 0;
	my $LINE = 0;
	my $HEADER_LINES = 0;
	my @LINE_CONTENT = ();
	my $FILE_OPEN = 'mpio.txt';
	my $SECTION = 'lspci -b';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( /^\s*$/ ); # Skip blank lines
			if ( /fibre.*qlogic/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: qlogicFibre(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< qlogicFibre", "Returns: $RCODE");
	return $RCODE;
}

sub unknownParameter {
	SDP::Core::printDebug('> unknownParameter', 'BEGIN');
	my $RCODE = 0;
	my $LINE = 0;
	my $HEADER_LINES = 0;
	my @LINE_CONTENT = ();
	my $FILE_OPEN = 'boot.txt';
	my $SECTION = 'dmesg';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( /^\s*$/ ); # Skip blank lines
			if ( /qla.*: Unknown parameter .*|qla.*: Unknown symbol .*/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: unknownParameter(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< unknownParameter", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( qlogicFibre() ) {
		if ( unknownParameter() ) {
			SDP::Core::updateStatus(STATUS_CRITICAL, "Qlogic Unknown Parameter Error");
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "No Qlogic parameter errors observed");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Skipping Qlogic parameter test, missing fibre card");
	}
SDP::Core::printPatternResults();

exit;

