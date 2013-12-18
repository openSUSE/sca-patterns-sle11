#!/usr/bin/perl

# Title:       Applicaitons Display Incorrectly with 8bit Color Depth
# Description: When GUI is set to 8bit color depth some applications display incorrect colors and patterns making the text unreadable.
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
	PROPERTY_NAME_CATEGORY."=X",
	PROPERTY_NAME_COMPONENT."=Color",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7006249",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=610991"
);
use constant MIN_COLOR_DEPTH => 8;

##############################################################################
# Local Function Definitions
##############################################################################

sub checkColorDepth {
	SDP::Core::printDebug('> checkColorDepth', 'BEGIN');
	my $RCODE = 0;
	my @LINE_CONTENT = ();
	my $FILE_OPEN = 'x.txt';
	my $SECTION = 'xorg.conf';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /DefaultDepth/ ) {
				s/^\s*//g; # remove leading white space
				SDP::Core::printDebug("PROCESSING", $_);
				@LINE_CONTENT = split(/\s+/, $_);
				$RCODE = $LINE_CONTENT[1];
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: checkColorDepth(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	if ( $RCODE > MIN_COLOR_DEPTH ) {
		SDP::Core::updateStatus(STATUS_ERROR, "Graphical Color Depth Detected: $RCODE");
	} elsif ( $RCODE == 0 ) {
		SDP::Core::updateStatus(STATUS_RECOMMEND, "Cannot Determine Color Depth, Make Sure it's Set to More Than " . MIN_COLOR_DEPTH);
	} else {
		SDP::Core::updateStatus(STATUS_WARNING, "Insufficient Color Depth for Some Applications: $RCODE");
	}
	SDP::Core::printDebug("< checkColorDepth", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 ) {
		checkColorDepth();
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Skipping X Color Depth: Outside Kernel Scope");
	}
SDP::Core::printPatternResults();

exit;

