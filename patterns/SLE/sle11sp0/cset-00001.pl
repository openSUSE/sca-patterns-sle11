#!/usr/bin/perl

# Title:       Check for SLERT cset Service
# Description: SLERTE uses cset to make CPUSets persistent across reboots
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
	PROPERTY_NAME_COMPONENT."=CSet",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7007601",
	"META_LINK_MISC=http://www.suse.com/documentation/slerte_11/"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub csetRecommended {
	SDP::Core::printDebug('> csetRecommended', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'slert.txt';
	my @FILE_SECTIONS = ();
	my $CHECK = '';
	my $SLERT = 0;

	if ( SDP::Core::listSections($FILE_OPEN, \@FILE_SECTIONS) ) {
		foreach $CHECK (@FILE_SECTIONS) {
			if ( $CHECK =~ m/uname -r/ ) {
				SDP::Core::printDebug("SLERT", "INSTALLED");
				$SLERT++;
			} elsif ( $CHECK =~ m/\/etc\/init.d\/cset$/ ) {
				SDP::Core::printDebug(" SERVICE", "/etc/init.d/cset");
				$SLERT++;
			} elsif ( $CHECK =~ m/\/etc\/init.d\/cset.init.d$/ ) {
				SDP::Core::printDebug(" SERVICE", "/etc/init.d/cset.init.d");
				$SLERT++;
			}
			last if ( $SLERT > 1 );
		}
		if ( $SLERT ) {
			if ( $SLERT < 2 ) {
				$RCODE++;
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: SLERT not installed");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: No sections found in $FILE_OPEN");
	}
	SDP::Core::printDebug("< csetRecommended", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( csetRecommended() ) {
		if  ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE12GA) < 0 ) {
			SDP::Core::updateStatus(STATUS_RECOMMEND, "Consider configuring CPU sets persistent across reboots");
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Outside kernel scope, skipping CSET");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Persistent CPU Sets Configured per cset(1)");
	}
SDP::Core::printPatternResults();

exit;

