#!/usr/bin/python

# Title:       qla2xxx: Ramping down queue depth
# Description: SLES 11 SP3 introduced the message
# Modified:    2015 Apr 01
#
##############################################################################
# Copyright (C) 2015 SUSE LLC
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
META_CATEGORY = "MPIO"
META_COMPONENT = "Message"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7016375"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def qlaRampFound():
	fileOpen = "messages.txt"
	msg = re.compile("kernel:.*qla2xxx.*Ramping down queue depth", re.IGNORECASE)
	section = "/var/log/warn"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if msg.search(content[line]):
				return True
	section = "/var/log/messages"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if msg.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

SERVER = SUSE.getHostInfo()
if( SERVER['DistroVersion'] >= 11 and SERVER['DistroPatchLevel'] >= 3 ):
	if( qlaRampFound() ):
		Core.updateStatus(Core.REC, "Found qla2xxx ramping messages, heavy I/O load indicated")
	else:
		Core.updateStatus(Core.IGNORE, "QLogic ramping messages not found")
else:
	Core.updateStatus(Core.ERROR, "Error: Outside kernel scope")

Core.printPatternResults()

