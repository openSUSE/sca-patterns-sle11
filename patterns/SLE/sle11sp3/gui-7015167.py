#!/usr/bin/python

# Title:       GUI fails with Secure Boot
# Description: SLES 11 SP3 Does Not Run in GUI Mode on Systems with ASPEED AST2400 Graphics Controller and Secure Boot Enabled
# Modified:    2014 Jul 21
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
META_CATEGORY = "X"
META_COMPONENT = "Secure Boot"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7015167|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=880007"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def deviceFound():
	fileOpen = "hardware.txt"
	section = "hwinfo"
	content = {}
	STATE = False
	if Core.getSection(fileOpen, section, content):
		Vendor = re.compile("\s+Vendor:.*pci 0x1a03", re.IGNORECASE)
		Device = re.compile("\s+Device:.*pci 0x2000", re.IGNORECASE)
		EndState = re.compile("^\d+:")
		for line in content:
			if( STATE ):
				if Device.search(content[line]):
					return True
				elif EndState.search(content[line]):
					STATE = False
			elif Vendor.search(content[line]):
				STATE = True
	return False

def guiMode():
	fileOpen = "boot.txt"
	section = "/etc/inittab"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "id:5:initdefault" in content[line]:
				return True
	return False

def guiModeActive():
	Service = SUSE.getServiceInfo('X')
	if( Service['Running'] > 0 ):
		return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( guiMode() ):
	if( guiModeActive() ):
		Core.updateStatus(Core.IGNORE, "X is already running")
	else:
		if( deviceFound() ):
			Core.updateStatus(Core.WARN, "If UEFI Secure Boot is enabled, Graphical mode may fail")
		else:
			Core.updateStatus(Core.ERROR, "ASPEED device not found, skipping test")
else:
	Core.updateStatus(Core.IGNORE, "Running in text mode anyway")

Core.printPatternResults()

