#!/usr/bin/python

# Title:       vmware guest kernel crashes
# Description: SLES11 SP3 VMware guest crashes with kernel BUG at ../blk-core.c:2392
# Modified:    2016 Aug 23
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
META_CATEGORY = "Kernel"
META_COMPONENT = "Crash"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc?id=7017971|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=930934"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def VMWareGuest():
	SYSTEM = SUSE.getBasicVirtualization()
	if( SYSTEM ):
		if "vmware" in SYSTEM['Manufacturer'].lower():
			if "virtual machine" in SYSTEM['Identity'].lower():
				return True
	return False

def errorFound():
	ERROR = re.compile("kernel BUG at.*block/blk-core.c:2392", re.IGNORECASE)
	FILE_OPEN = "boot.txt"
	SECTION = "/dmesg"
	CONTENT = []
	if Core.getRegExSection(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if ERROR.search(LINE):
				return True
	FILE_OPEN = "messages.txt"
	SECTION = "/var/log/warn"
	CONTENT = []
	if Core.getRegExSection(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if ERROR.search(LINE):
				return True
	SECTION = "/var/log/messages"
	CONTENT = []
	if Core.getRegExSection(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if ERROR.search(LINE):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( VMWareGuest() ):
	KERNEL_VERSION = '3.0.101-0.46'
	INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION)
	if( INSTALLED_VERSION <= 0 ):
		if( errorFound() ):
			Core.updateStatus(Core.CRIT, "Detected kernel crash from known issue, update system to apply newer kernel")
		else:
			Core.updateStatus(Core.WARN, "Kernel crash from known issue probable, update system to apply newer kernel")
	else:
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for blk-core")
else:
	Core.updateStatus(Core.IGNORE, "Not a VMWare Guest, not applicable")

Core.printPatternResults()


