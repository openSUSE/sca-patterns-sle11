#!/usr/bin/python3

# Title:       SLES NFS Mounts Hanging
# Description: SLES 11 NFS client mounts hang when using kernel 3.0.80-x
# Modified:    2014 May 22
#
##############################################################################
# Copyright (C) 2014 SUSE LLC
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

import sys, os, Core, SUSE, re

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "NFS"
META_COMPONENT = "Mount"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014392"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def nfsMountsFound():
	fileOpen = "fs-diskio.txt"
	section = "bin/mount"
	content = {}
	nfsMount = re.compile("type nfs", re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if nfsMount.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

AFFECTED_KERNEL='3.0.80'
FIXED_KERNEL='3.0.101-0.21'
if( SUSE.compareKernel(AFFECTED_KERNEL) >= 0 and SUSE.compareKernel(FIXED_KERNEL) < 0 ):
	if( nfsMountsFound() ): 
		Core.updateStatus(Core.WARN, "Detected NFS mounts susceptible to hanging, update system")
	else:
		Core.updateStatus(Core.IGNORE, "No NFS mounts found, skipping hang test")
else:
	Core.updateStatus(Core.ERROR, "Outside the kernel scope, skipping nfs hang test")

Core.printPatternResults()

