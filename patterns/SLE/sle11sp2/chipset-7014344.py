#!/usr/bin/python3

# Title:       Checks for faulty Intel chipsets
# Description: Faulty Intel chipsets cause problems with interrupt remapping
# Modified:    2014 Jul 22
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

import os
import Core
import SUSE
import re

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Hardware"
META_COMPONENT = "Chipset"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014344|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=844513"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def faultyChipSet():
	fileOpen = "hardware.txt"
	section = "lspci -nn"
	content = {}
	CHIPSET = re.compile('8086:(340[36].*rev 13|3405.*rev (12|13|22))')
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if CHIPSET.search(content[line]):
				return True
	return False

def notFixed():
	fileOpen = "boot.txt"
	section = "/proc/cmdline"
	content = {}
	SERVER = SUSE.getHostInfo()
#	print "SERVER = " + str(SERVER)
	if( SERVER['DistroVersion'] == 11 ):
		if( SERVER['DistroPatchLevel'] == 3 ):
			FIXED_VERSION = '3.0.101-0.21'
		elif( SERVER['DistroPatchLevel'] == 2 ):
			FIXED_VERSION = '3.0.101-0.7.19'
		else:
			Core.updateStatus(Core.ERROR, "Outside Service Pack scope, skipping IRQ remap test")
			return False

		if( SUSE.compareKernel(FIXED_VERSION) >= 0 ):
			Core.updateStatus(Core.IGNORE, "Patch applied, IRQ remap issue AVOIDED")
			return False
	else:
		Core.updateStatus(Core.ERROR, "Outside Distribution scope, skipping IRQ remap test")
		return False
		
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "intremap=off" in content[line]:
				Core.updateStatus(Core.IGNORE, "Found interrupt remapping issue intremap=off work around")
				return False
	return True

def irqErrors():
	fileOpen = "messages.txt"
	section = "/var/log/messages"
	content = {}
	ERROR = re.compile('kernel.*No irq handler for vector (irq -1)', re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if ERROR.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( faultyChipSet() ):
	if( notFixed() ):
		if( irqErrors() ):
			Core.updateStatus(Core.CRIT, "Detected interrupt remap error, update system to apply fixes")
		else:
			Core.updateStatus(Core.WARN, "Detected potential interrupt remap issue, update system to avoid it")
else:
	Core.updateStatus(Core.ERROR, "No faulty chipsets with interrupt remapping error")

Core.printPatternResults()


