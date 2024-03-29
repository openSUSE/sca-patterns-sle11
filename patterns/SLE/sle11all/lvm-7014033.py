#!/usr/bin/python3

# Title:       Check for Deactivated LVM Volumes
# Description: Confirm LVM volumes are active
# Modified:    2013 Nov 01
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
# along with this program; if not, see <http://www.gnu.org/licenses/>.
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
META_CATEGORY = "LVM"
META_COMPONENT = "Volume"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014033"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def getInactiveVolumes():
	fileOpen = "lvm.txt"
	section = "/sbin/lvs\n"
	content = {}
	VOLS = []
	ACTIVE_FLAG = 4
	STATUS_FIELD = 2
	VOL_NAME = 0
	START = 0
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if( START ):
				THIS_VOL = content[line].split()
				if( THIS_VOL[STATUS_FIELD][ACTIVE_FLAG] != 'a' ):
					VOLS.append(THIS_VOL[VOL_NAME])
			else:
				#skips past the command header
				if "LSize" in content[line]:
					START = 1
	return VOLS

##############################################################################
# Main Program Execution
##############################################################################

NOTACTIVE = getInactiveVolumes()
if( len(NOTACTIVE) > 0 ):
	Core.updateStatus(Core.WARN, "Inactive LVM logical volumes found: " + " ".join(NOTACTIVE))
else:
	Core.updateStatus(Core.ERROR,"No LVM volumes or all are active")

Core.printPatternResults()


