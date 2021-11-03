#!/usr/bin/python3

# Title:       Check Sandy Bridge GPU Lock ups
# Description: Random lock up or hang when in Gnome or KDE
# Modified:    2014 May 19
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
META_CATEGORY = "X"
META_COMPONENT = "Hang"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014951"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def guiLoaded():
	fileOpen = "boot.txt"
	section = "/var/log/boot.msg"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "runlevel 5 has been reached" in content[line]:
				return True
	return False

def sandyBridgeFound():
	fileOpen = "x.txt"
	section = "hwinfo --framebuffer"
	content = {}
	if Core.getSection(fileOpen, section, content):
		chkSandy = re.compile("Device:.*Sandybridge Desktop Graphics Controller")
		for line in content:
			if chkSandy.search(content[line]):
				return True
	return False

def notResolved():
	fileOpen = "boot.txt"
	section = "menu.lst"
	content = {}
	if Core.getSection(fileOpen, section, content):
		kernParam = re.compile("kernel.*i915.i915_enable_rc6=0")
		for line in content:
			if kernParam.search(content[line]):
				return False
	return True

##############################################################################
# Main Program Execution
##############################################################################

AFFECTED_KERNEL='3.0.42-0.7'
if( SUSE.compareKernel(AFFECTED_KERNEL) > 0 and SUSE.compareKernel(SUSE.SLE12GA) < 0 ):
	if( guiLoaded() ):
		if( sandyBridgeFound() ):
			if( notResolved() ):
				Core.updateStatus(Core.CRIT, "Susceptible to random GUI lockups, kernel startup paramenter needed")
			else:
				Core.updateStatus(Core.IGNORE, "Kernel parameter avoids Sandy Bridge lockups")
		else:
			Core.updateStatus(Core.IGNORE, "Sandy Bridge not found, skipping test")
	else:
		Core.updateStatus(Core.IGNORE, "GUI not loaded, skipping sandy bridge test")
else:
	Core.updateStatus(Core.IGNORE, "Outside the kernel scope, skipping sandy bridge test")

Core.printPatternResults()

