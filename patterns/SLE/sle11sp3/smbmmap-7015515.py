#!/usr/bin/python3

# Title:       Samba response on s390
# Description: Samba running on s390 system stops responding and needs to be restarted
# Modified:    2014 Aug 14
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

import os
import re
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Samba"
META_COMPONENT = "MMAP"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7015515|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=882356"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def sambaMmapFixed():
	fileOpen = "samba.txt"
	section = "/smb.conf"
	content = {}
	GLOBAL = False
	if Core.getSection(fileOpen, section, content):
		mmapset = re.compile('\s*use\s*mmap\s*=\s*no\s*$', re.IGNORECASE)
		for line in content:
			if( GLOBAL ):
				if content[line].startswith('['):
					GLOBAL = False
				elif mmapset.search(content[line]):
					return True
			elif "[global]" in content[line].lower():
				GLOBAL = True
	return False

##############################################################################
# Main Program Execution
##############################################################################

SERVER = SUSE.getHostInfo()
if "s390" in SERVER['Architecture'].lower():
	if( SERVER['DistroVersion'] == 11 and SERVER['DistroPatchLevel'] == 3 ):
		if( sambaMmapFixed() ):
			Core.updateStatus(Core.IGNORE, "Issue AVOIDED, Samba mmap set to no")
		else:
			SERVICE = SUSE.getServiceInfo('smb')
			if( SERVICE['OnForRunLevel'] ):
				if( SERVICE['Running'] < 1 ):
					Core.updateStatus(Core.CRIT, "Samba not running due to incorrect mmap setting in [global] smb.conf")
				else:
					Core.updateStatus(Core.CRIT, "Samba may stop running due to incorrect mmap setting in [global] smb.conf")
			else:
				Core.updateStatus(Core.WARN, "Samba may fail if enabled due to incorrect mmap setting in [global] smb.conf")
	else: 
		Core.updateStatus(Core.ERROR, "Outside the distribution and patch level scope")
else:
	Core.updateStatus(Core.ERROR, "Outside the architecture scope")

Core.printPatternResults()

