#!/usr/bin/python

# Title:       vx_iget - inode table overflow
# Description: Full error is vxfs: msgcnt 637 mesg 014: V-2-14: vx_iget - inode table overflow and can be seen in /var/log/warn and /var/log/messages
# Modified:    2014 May 21
# Version:     1.2
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
#   Sean Barlow (sbarlow@novell.com)
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
META_CATEGORY = "Disk"
META_COMPONENT = "Filesystem"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7015089|META_LINK_Symantec1=http://www.symantec.com/business/support/index?page=content&id=TECH22652|META_LINK_Symantec2=http://www.symantec.com/business/support/index?page=content&id=TECH172133"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def checkVFX():
	fileOpen = "messages.txt"
	section = "/var/log/warn"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "vx_iget - inode table overflow" in content[line]:
				return True

	section = "/var/log/messages"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "vx_iget - inode table overflow" in content[line]:
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( checkVFX() ):
	Core.updateStatus(Core.WARN, "VFX Inode table overflow: Consider increasing the maximum inodes")
else:
	Core.updateStatus(Core.IGNORE, "VFX inode error not found, not applicable")

Core.printPatternResults()


