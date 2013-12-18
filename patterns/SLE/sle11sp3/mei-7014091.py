#!/usr/bin/python

# Title:       Reboot command shuts down
# Description: Command reboot shuts the system down instead of reboot
# Modified:    2013 Nov 12
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
META_CATEGORY = "Boot"
META_COMPONENT = "Driver"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014091|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=847858"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def driverBlackListed():
	fileOpen = "modules.txt"
	section = "/etc/modprobe.d/blacklist\n"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "blacklist mei" in content[line]:
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

DRIVER_INFO = SUSE.getDriverInfo('mei')
if( SUSE.compareKernel(SUSE.SLE11SP3) >= 0 and SUSE.compareKernel(SUSE.SLE11SP4) < 0 ):
	if ( DRIVER_INFO['loaded'] ):
		if( driverBlackListed() ):
			Core.updateStatus(Core.ERROR, "Driver is blacklisted: " + DRIVER_INFO['name'] + ", issue avoided")
		else:
			Core.updateStatus(Core.WARN, "Reboot command may shutdown server instead of rebooting")
	else:
		Core.updateStatus(Core.ERROR, "Driver not loaded: " + DRIVER_INFO['name'] + ", skipping test")
else:
	Core.updateStatus(Core.ERROR, "Outside kernel scope, skipping test")

Core.printPatternResults()

