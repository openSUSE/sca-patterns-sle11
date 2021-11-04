#!/usr/bin/python3

# Title:       System crash with be2net
# Description: System may crash if the kernel module be2net is loaded
# Modified:    2016 Jun 20
#
##############################################################################
# Copyright (C) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany
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

import re
import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Network"
META_COMPONENT = "be2net"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc?id=7017676|META_LINK_DRIVERS=https://drivers.suse.com/emulex/Emulex_Adapters/sle-11-sp4-x86_64/1.2/install-readme.html|META_LINK_IBM-TID=https://www-947.ibm.com/support/entry/portal/docdisplay?lndocid=migr-5095763"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def be2netError():
	FILE_OPEN = "messages.txt"
	SECTION = "/var/log/messages"
	CONTENT = []
	oopsError = re.compile("Modules linked in:.*be2net", re.IGNORECASE)
	if Core.getRegExSection(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if oopsError.search(LINE):
				return True
	return False

def be2netLoaded():
	DRIVER_NAME = 'be2net'
	DRIVER_INFO = SUSE.getDriverInfo(DRIVER_NAME)
	if( DRIVER_INFO['loaded'] ):
		return True
	return False	

##############################################################################
# Main Program Execution
##############################################################################

SYSTEM = SUSE.getBasicVirtualization()
if 'Hardware' not in list(SYSTEM.keys()):
	Core.updateStatus(Core.ERROR, "ERROR: Cannot detect hardware, aborting")
elif "x3850 x6" in SYSTEM['Hardware'].lower():
	RPM_NAME='elx-be2net-kmp'
	if "xen" in SYSTEM['Hypervisor'].lower():
		RPM_NAME = RPM_NAME + str('-xen')
	else:
		RPM_NAME = RPM_NAME + str('-default')

	RPM_VERSION = '11.0.232.0_3.0.101_63-2'
	if( SUSE.packageInstalled(RPM_NAME) ):
		INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION)
		if( INSTALLED_VERSION < 0 ):
			if( be2netError() ):
				Core.updateStatus(Core.CRIT, "Detected be2net driver failure")
			else:
				Core.updateStatus(Core.WARN, "Loading the be2net driver may cause system failure")
		else:
			Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME)
	else:
		if( be2netLoaded() ):
			Core.updateStatus(Core.IGNORE, "Driver be2net loaded")
		else:
			if( be2netError() ):
				Core.updateStatus(Core.CRIT, "Detected be2net driver failure")
			else:
				Core.updateStatus(Core.WARN, "Loading the be2net driver may cause system failure")
else:
	Core.updateStatus(Core.IGNORE, "No x3850 X6 hardware found")	

Core.printPatternResults()


