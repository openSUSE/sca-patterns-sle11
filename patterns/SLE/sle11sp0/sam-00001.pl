#!/usr/bin/perl

# Title:       Missing SAM log file
# Description: The sam.log file is missing
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
	PROPERTY_NAME_CATEGORY."=SAM",
	PROPERTY_NAME_COMPONENT."=Log",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7006331"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 ) {
		if ( SDP::SUSE::packageInstalled('suse-sam') ) {
			if ( SDP::SUSE::packageInstalled('suse-sam-data') ) {
				SDP::Core::updateStatus(STATUS_ERROR, "SUSE SAM Meta Data Package Installed");
			} else {
				SDP::Core::updateStatus(STATUS_WARNING, "Missing suse-sam-data package causes log and dependency errors");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: SAM package not installed, metadata package unnecessary");			
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: SAM log file check: Outside the kernel scope");
	}
SDP::Core::printPatternResults();

exit;


