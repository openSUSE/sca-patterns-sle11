#!/usr/bin/python

# Title:       GLX application failures
# Description: GLX applications fail to start on Intel GFX cards with MESA 9.0.x
# Modified:    2013 Oct 30
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
META_CATEGORY = "Video"
META_COMPONENT = "Card"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7005681|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=847068"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def intelCard():
	fileOpen = "x.txt"
	section = "sysp -c"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "Intel" in content[line]:
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( SUSE.compareKernel(SUSE.SLE11SP3) >= 0 and SUSE.compareKernel(SUSE.SLE11SP4) < 0 ):
	if( SUSE.packageInstalled('Mesa') ):
		if( SUSE.compareRPM('Mesa', '9.0.3-0.19.1') <= 0 ):
			if( intelCard() ):
				Core.updateStatus(Core.WARN, "GLX applications may fail to start")
			else:
				Core.updateStatus(Core.ERROR, "Error: Invalid graphics card, skipping")
		else:
			Core.updateStatus(Core.ERROR, "Valid version of Mesa installed, AVOIDED")
	else:
		Core.updateStatus(Core.ERROR, "Error: Mesa package not installed, skipping")
else:
	Core.updateStatus(Core.ERROR, "Error: Outside kernel scope, skipping")
Core.printPatternResults()

