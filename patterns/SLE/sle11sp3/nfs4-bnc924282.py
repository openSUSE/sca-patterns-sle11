#!/usr/bin/python3

# Title:       Updated kernel with nfs4 causes panic
# Description: SLES 11 SP3 kernel 3.0.101-0.47.50.1 with NFS4 panics
# Modified:    2015 Apr 01
#
##############################################################################
# Copyright (C) 2015 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)
#
##############################################################################

##############################################################################
# Module Definition
##############################################################################

import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "NFS"
META_COMPONENT = "Crash"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_BUG"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=924282"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def nfs4Mounts():
	fileOpen = "fs-diskio.txt"
	section = "/mount"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "type nfs4" in content[line]:
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

AFFECTED_KERNEL='3.0.101-0.47.50'
INSTALLED_VERSION = SUSE.compareKernel(AFFECTED_KERNEL)
if( INSTALLED_VERSION == 0 ):
	if( nfs4Mounts() ):
		Core.updateStatus(Core.CRIT, "System hang or crash imminent, update or backrev kernel for NFS4 mount access")
	else:
		Core.updateStatus(Core.WARN, "Accessing NFS4 mounts will hang or crash the system, update or backrev the kernel")
else:
	Core.updateStatus(Core.ERROR, "Error: Outside kernel scope")

Core.printPatternResults()

