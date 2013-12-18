#!/usr/bin/python
# -*- coding: utf-8 -*-

# Title:       AD Lookups Fail with Winbind
# Description: AD users and groups unable to be looked up via winbind
# Modified:    2013 Oct 16
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
META_CATEGORY = "Samba"
META_COMPONENT = "Winbind"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7013409"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def winBindRunning():
	fileOpen = "samba.txt"
	section = "winbind status"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			#if something in section
			if ".running" in content[line]:
				return True
	return False

def winBindFailures():
	fileOpen = "samba.txt"
	section = "wbinfo -u"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			#if something in section
			if "Error looking up domain users" in content[line]:
				return True
	return False


##############################################################################
# Main Program Execution
##############################################################################
if( SUSE.compareKernel(SUSE.SLE11SP2) >= 0 and SUSE.compareKernel(SUSE.SLE11SP3) < 0 ):
	if( SUSE.packageInstalled("samba") and SUSE.packageInstalled("samba-winbind") ):
		if( SUSE.compareRPM("samba", "3.6.3-0.30.1") == 0 ):
			if( winBindRunning() ):
				Core.updateStatus(Core.WARN, "Winbind AD lookups may fail, update system for newer Samba packages")
				if( winBindFailures() ):
					Core.updateStatus(Core.CRIT, "Winbind AD lookup failure, update system for newer Samba packages")
			else:
				Core.updateStatus(Core.ERROR, "Winbind service is not running, skipping test")
		else:
			Core.updateStatus(Core.ERROR, "Samba version has been verified, skipping test")
	else:
		Core.updateStatus(Core.ERROR, "Samba/Winbind not installed, skipping test")
else:
	Core.updateStatus(Core.ERROR, "Outside the kernel scope")

Core.printPatternResults()


