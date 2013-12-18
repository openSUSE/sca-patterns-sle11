#!/usr/bin/python

# Title:       xfs_growfs causes kernel Oops
# Description: Using xfs_growfs to expand an XFS filesystem causes a kernel Oops
# Modified:    2013 Dec 10
#
##############################################################################
# Copyright (C) 2013 SUSE LLC
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
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)
#
##############################################################################

##############################################################################
# Module Definition
##############################################################################

import sys, os, Core, SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Filesystem"
META_COMPONENT = "XFS"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=http://www.novell.com/support/kb/doc.php?id=7013481|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=842604"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def xfsVolumesMounted():
	fileOpen = "fs-diskio.txt"
	section = "/bin/mount"
	content = {}
	FSTYPE = 4
	if Core.getSection(fileOpen, section, content):
		for line in content:
			FIELDS = content[line].split()
			if "xfs" in FIELDS[FSTYPE]:
				return True
	return False

def oopsFound():
	fileOpen = "messages.txt"
	section = "/var/log/messages"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "comm: xfs_growfs" in content[line]:
				if "Pid:" in content[line]:
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

FIXED_VERSION = '3.0.101-0.8'
if( SUSE.compareKernel(SUSE.SLE11SP3) >= 0 and SUSE.compareKernel(FIXED_VERSION) < 0 ):
	if( xfsVolumesMounted() ):
		if( oopsFound() ):
			Core.updateStatus(Core.CRIT, "XFS Filesystem Oops detected using xfs_growfs, update system for patched kernel")
		else:
			Core.updateStatus(Core.WARN, "XFS Filesystem susceptible to Oops using xfs_growfs, update system for patched kernel")
	else:
		Core.updateStatus(Core.ERROR, "No xfs filesystems mounted, skipping xfs_growfs test")
else:
	Core.updateStatus(Core.ERROR, "Outside kernel scope, skipping xfs_growfs test")

Core.printPatternResults()

