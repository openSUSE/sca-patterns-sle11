#!/usr/bin/perl

# Title:       Updating kernel on SLE 11 SP1 breaks CIFS
# Description: The server can hang on read/writes after update
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
	PROPERTY_NAME_COMPONENT."=CIFS",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7006684",
	"META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=630171"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if  ( SDP::SUSE::compareKernel('2.6.32.13-0.5') == 0 ) {
		my @MOUNTS = SDP::SUSE::getFileSystems();
		my @CIFS_MOUNTS = ();
		my $TMP;
		foreach $TMP (@MOUNTS) {
			if ( $TMP->{'TYPE'} eq 'cifs' && $TMP->{'MOUNTED'} == 1 ) {
				push(@CIFS_MOUNTS, $TMP->{'DEV'});
			}
		}
		if ( $#CIFS_MOUNTS >= 0 ) {
			SDP::Core::updateStatus(STATUS_CRITICAL, "Update system to avoid CIFS mount server hang from: @CIFS_MOUNTS");
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "No CIFS device mounted");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Outside kernel scope for CIFS issue 630171");
	}
SDP::Core::printPatternResults();

exit;

