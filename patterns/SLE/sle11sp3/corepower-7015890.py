#!/usr/bin/python

# Title:       Core power limitation messages
# Description: Core power limit notification messages flooding the logs
# Modified:    2014 Nov 14
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

import re
import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Kernel"
META_COMPONENT = "Power"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7015890|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=882317"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def bootFlagSet():
	fileOpen = "boot.txt"
	section = "/proc/cmdline"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "int_pln_disable" in content[line].lower():
				return True
	return False

def notificationsFound():
	fileOpen = "messages.txt"
	section = "/var/log/messages"
	content = {}
	ERR_NOTE = re.compile('CPU\d*: Core power limit notification', re.IGNORECASE)
	ERR_NORM = re.compile('CPU\d*: Package power limit notification', re.IGNORECASE)
	ERR_PACK = re.compile('CPU\d*: Core power limit normal', re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if ERR_NOTE.search(content[line]):
				return True
			elif ERR_NORM.search(content[line]):
				return True
			elif ERR_PACK.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

SERVER = SUSE.getHostInfo()
if( SERVER['DistroVersion'] == 11 and SERVER['DistroPatchLevel'] == 3 ):
	if( SUSE.compareKernel('3.0.101-0.40') <= 0 ):
		if( notificationsFound() ):
			Core.updateStatus(Core.REC, "Harmless core power notifications found in the logs, review your options")
		else:
			Core.updateStatus(Core.IGNORE, "Kernel affected, but no core power notifications found")
	else:
		if( bootFlagSet() ):
			Core.updateStatus(Core.IGNORE, "Boot flag 'int_pln_disable' is set")
		elif( notificationsFound() ):
			Core.updateStatus(Core.REC, "Harmless core power notifications found in the logs, use int_pln_disable to ignore")
		else:
			Core.updateStatus(Core.IGNORE, "Kernel updated and boot flag not set, but no core power notifications found")
else:
	Core.updateStatus(Core.ERROR, "Outside the distribution scope, skipping core power test")

Core.printPatternResults()


