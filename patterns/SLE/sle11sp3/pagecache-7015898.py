#!/usr/bin/python

# Title:       Page cache limit check
# Description: Memory corruption regression with kernel 3.0.101-0.35 and using pagecache limit
# Modified:    2015 Mar 26
#
##############################################################################
# Copyright (C) 2014,2015 SUSE LLC
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

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Kernel"
META_COMPONENT = "Memory"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7015898|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=895680"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def pageCacheSet():
	fileOpen = "env.txt"
	section = "/sysctl -a"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if content[line].startswith('vm.pagecache_limit_mb'):
				VALUE = int(content[line].split()[-1])
				if( VALUE > 0 ):
					return True
				else:
					return False
	return False

##############################################################################
# Main Program Execution
##############################################################################
SERVER = SUSE.getHostInfo()
AFFECTED_VERSION = '3.0.101-0.35'
if( SERVER['DistroVersion'] == 11 and SERVER['DistroPatchLevel'] == 3 ):
	if( Core.compareVersions(SERVER['KernelVersion'], AFFECTED_VERSION) == 0 ):
		if( pageCacheSet() ):
			Core.updateStatus(Core.CRIT, "The vm.pagecache_limit_mb is non-zero and may cause memory corruption, update system to apply fixed kernel")
		else:
			Core.updateStatus(Core.IGNORE, "The vm.pagecache_limit_mb is zero, memory corruption AVOID")
	else:
		Core.updateStatus(Core.ERROR, "Outside the kernel version scope, not applicable")
else:
	Core.updateStatus(Core.ERROR, "Outside the distribution and patch level scope, not applicable")

Core.printPatternResults()


