#!/usr/bin/python3
#Version 0.1.4

# Title:       BUG: soft lockup and scale_rt_power: clock: messages
# Description: /var/log/messages will have errors such as these: linuxhost kernel: [7094858.932823] scale_rt_power: clock:1934bc9263add7 age:1934bc789fc900, avg:3878006d linuxhost kernel: [7094858.936806] scale_rt_power: clock:1934bc92a2ea81 age:1934bc789fc900, avg:38788ea3 linuxhost kernel: [7194543.949072] BUG: soft lockup - CPU#0 stuck for 40s! [kjournald:2058] linuxhost kernel: [7194543.949080] BUG: soft lockup - CPU#1 stuck for 40s! [flush-253:0:2019]
# Modified:    2014 Aug 12
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
#   Sean Barlow (sbarlow@novell.com)
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
META_CATEGORY = "Kernel"
META_COMPONENT = "SoftLock"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.novell.com/support/kb/doc.php?id=7015154|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=834473 "

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

###Run through check. Check message files for errors
def checkMessages():
	fileOpen = "messages.txt"
	section = "/var/log/warn"
	content = {}
	errorString = re.compile('scale_rt_power:.*clock:.*age:.*avg:', re.IGNORECASE)

	if Core.getSection(fileOpen, section, content):
		for line in content:
			if errorString.search(content[line]):
				return True

	section = "/var/log/messages"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if errorString.search(content[line]):
				return True

	return False

def testKernelFor(FIXED_VERSION):
	if( SUSE.compareKernel(FIXED_VERSION) < 0 ):
		if( checkMessages() ):
			Core.updateStatus(Core.CRIT, "Bug: Soft Lockups and scale_rt_power messages, update kernel to apply version " + str(FIXED_VERSION) + " or higher")
		else:
			Core.updateStatus(Core.WARN, "Possible Soft Lockups and scale_rt_power issue, update kernel to apply version " + str(FIXED_VERSION) + " or higher")
	else:
		Core.updateStatus(Core.IGNORE, "Kernel was patched")

##############################################################################
# Main Program Execution
##############################################################################

#Check suse version
SERVER = SUSE.getHostInfo()
VER = SERVER['DistroVersion']
SP = SERVER['DistroPatchLevel']
if (VER == 11):
	if (SP == 3):
		FIXED_VERSION = '3.0.101-0.15'
		testKernelFor(FIXED_VERSION)
	elif (SP == 2):
		FIXED_VERSION = '3.0.101-0.7.15'
		testKernelFor(FIXED_VERSION)
	else:
		Core.updateStatus(Core.ERROR, "Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "Outside the distribution scope")

Core.printPatternResults()


