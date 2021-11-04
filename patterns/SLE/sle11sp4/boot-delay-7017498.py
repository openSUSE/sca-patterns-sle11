#!/usr/bin/python3

# Title:       Kernel boot delay
# Description: Delayed boot after updating to kernel version 3.0.101-71
# Modified:    2016 Apr 26
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
META_COMPONENT = "Boot"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7017498|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=974428|META_LINK_MASSPTF=https://ptf.suse.com/f2cf38b50ed714a8409693060195b235/sles11-sp4/10543/x86_64/20160407/"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def delayedBootMessages():
	FILE_OPEN = "boot.txt"
	SECTION = "/dmesg"
	CONTENT = []
	ERROR_STRING = re.compile("pci.*vpd.*failed.*firmware bug", re.IGNORECASE)
	if Core.getRegExSection(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if ERROR_STRING.search(LINE):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

SERVER = SUSE.getHostInfo()
thisVersion = '3.0.101-71'
thatVersion = SERVER['KernelVersion']
if( Core.compareVersions(thisVersion, thatVersion) == 0 ):
	Core.updateStatus(Core.WARN, "Kernel is susceptible to delayed boots, update system to resolve")
	if( delayedBootMessages() ):
		Core.updateStatus(Core.CRIT, "Boot delays due to kernel issue, update system to resolve")
else:
	Core.updateStatus(Core.IGNORE, "The kernel version " + str(SERVER['KernelVersion']) + " is sufficient")

Core.printPatternResults()

