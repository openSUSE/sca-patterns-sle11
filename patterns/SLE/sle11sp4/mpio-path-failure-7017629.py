#!/usr/bin/python

# Title:       MPIO LUN Hang
# Description: Losing a single device with multipath-tools 0.4.9-112.1 leads to loss of complete LUN map
# Modified:    2016 Jun 15
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
#   Jason Record (jason.record@suse.com)
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
META_CATEGORY = "MPIO"
META_COMPONENT = "Path"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc?id=7017629|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=980933"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def pathFailure():
	FILE_OPEN = "messages.txt"
	SECTION = "/var/log/messages"
	CONTENT = []
	Failure = re.compile("multipath.*failed path|multipath.*failing path|multipath.*mark as failed", re.IGNORECASE)
	if Core.getRegExSection(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if Failure.search(LINE):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'multipath-tools'
RPM_VERSION = '0.4.9-112.1'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION)
	if( INSTALLED_VERSION == 0 ):
		if( pathFailure() ):
			Core.updateStatus(Core.CRIT, "MPIO path failure detected, all paths will fail - update multipath-tools")
		else:
			Core.updateStatus(Core.WARN, "Susceptible to multiple MPIO path failures - update multipath-tools")
	else:
		Core.updateStatus(Core.IGNORE, "Bug fix applied for " + RPM_NAME)
else:
	Core.updateStatus(Core.ERROR, "ERROR: RPM package not installed: " + RPM_NAME)

Core.printPatternResults()


