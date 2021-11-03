#!/usr/bin/python3

# Title:       NTP Host Name Resolution
# Description: NTP server does not resolve host names on ntp version 4.2.8, affects SLES11SP4 and SLES12SP1
# Modified:    2016 Jan 27
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
#   Colin Hamilton (chamilton@suse.com)
#
##############################################################################

##############################################################################
# Module Definition
##############################################################################

import os
import re
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Core"
META_COMPONENT = "NTP"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7016873|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=943017"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)
 ##############################################################################
# Local Function Definitions
##############################################################################

def ntpchrootinfo():
	fileOpen = "sysconfig.txt"
	section = "/etc/sysconfig/ntp"
	content = []
	regresults = re.compile("CHROOTED.*yes", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if regresults.search(line):
				return True
	return False

def ntpdnsinfo():
	fileOpen = "ntp.txt"
	section = "/etc/ntp.conf"
	content = []
	regresults = re.compile("^(server|fudge|restrict)[ \t][a-zA-Z0-9\.]*[a-zA-Z]", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if regresults.search(line):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'ntp'
RPM_VERSION = '4.2.8'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION)
	if( INSTALLED_VERSION == 0 ):
		if ( ntpchrootinfo() ):
			SERVICE_INFO = SUSE.getServiceInfo(RPM_NAME)
			if( SERVICE_INFO['OnForRunLevel'] ): # SLES11 SP4 specific
				if ( ntpdnsinfo() ):
					Core.updateStatus(Core.CRIT, "NTP issue resolving DNS detected, disable NTP chroot to resolve.")
				else:
					Core.updateStatus(Core.IGNORE, "Bug not applicate when NTP isn't using DNS.")
			else:
				Core.updateStatus(Core.IGNORE, "Bug not applicable when NTP is not in use.")
		else:
			Core.updateStatus(Core.IGNORE, "Bug not applicable when chroot is disabled.")
	else:
		Core.updateStatus(Core.IGNORE, "Bug doesn't exist in " + RPM_VERSION)
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")

Core.printPatternResults()
