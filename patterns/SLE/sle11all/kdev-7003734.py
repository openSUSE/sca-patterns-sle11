#!/usr/bin/python

# Title:       Check kernel device usage
# Description: SLE11 update reports unreliable mount system found
# Modified:    2013 Dec 11
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
META_CATEGORY = "Disk"
META_COMPONENT = "Device"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=http://www.novell.com/support/kb/doc.php?id=7003734"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def kernelDeviceMount():
	fileOpen = "fs-diskio.txt"
	section = "/etc/fstab"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if( content[line].startswith('/dev/sd') ):
#				print content[line]
				return True
	return False

def kernelDeviceBoot():
	fileOpen = "boot.txt"
	section = "/boot/grub/menu.lst"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "root=/dev/sd" in content[line]:
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( kernelDeviceMount() ):
	if( kernelDeviceBoot() ):
		Core.updateStatus(Core.WARN, "Using kernel disk devices, check /etc/fstab and /boot/grub/menu.lst")
	else:
		Core.updateStatus(Core.WARN, "Using kernel disk devices, check /etc/fstab")
else:
	if( kernelDeviceBoot() ):
		Core.updateStatus(Core.WARN, "Using kernel disk devices, check /boot/grub/menu.lst")
	else:
		Core.updateStatus(Core.ERROR,"Kernel disk devices not in use")

Core.printPatternResults()

