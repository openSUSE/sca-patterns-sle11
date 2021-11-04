#!/usr/bin/python3

# Title:       Check Xen kdump memory configuration
# Description: Could not find a free area of memory of a000 bytes
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
import re


##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Xen"
META_COMPONENT = "Kdump"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014586"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def xenServerActive():
	fileOpen = "basic-environment.txt"
	section = "Virtualization"
	content = {}
	XENHYP = re.compile("^Hypervisor:.*Xen")
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if XENHYP.search(content[line]):
				return True
	return False

def kdumpOn():
	fileOpen = "crash.txt"
	section = "chkconfig boot.kdump"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "B:on" in content[line]:
				return True
	return False

def memReserved():
	fileOpen = "boot.txt"
	section = "menu.lst"
	content = {}
	KERNMEM = re.compile("kernel.*xen.gz.*crashkernel=\d")
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if KERNMEM.search(content[line]):
				return True
	return False

def validKdumpFormat():
	fileOpen = "crash.txt"
	section = "/etc/sysconfig/kdump"
	content = {}
	ELFMT = re.compile("KDUMP_DUMPFORMAT=.ELF")
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if ELFMT.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( xenServerActive() ):
	if( kdumpOn() ):
		MEM = memReserved()
		FMT = validKdumpFormat()
		if( MEM and FMT ):
			Core.updateStatus(Core.IGNORE, "Xen kdump memory and dump format configured correctly")
		elif( MEM ):
			Core.updateStatus(Core.CRIT, "Xen kdump memory not configured, server core dumps will fail")
		elif( FMT ):
			Core.updateStatus(Core.CRIT, "Invalid Xen dump format, server core dumps will fail")
		else:
			Core.updateStatus(Core.CRIT, "Invalid Xen kdump memory and dump format, server core dumps will fail")
	else:
		Core.updateStatus(Core.ERROR, "KDump is not active, skipping configuration tests")
else:
	Core.updateStatus(Core.ERROR, "Xen Hypervisor is not active, skipping configuration tests")

Core.printPatternResults()

