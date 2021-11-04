#!/usr/bin/python3

# Title:       XFS Filesystem Corruption
# Description: XFS filesystem corruption after update to Kernel 3.0.101-100.1
# Modified:    2017 Jun 12
#
##############################################################################
# Copyright (C) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany
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
META_CATEGORY = "Filesystem"
META_COMPONENT = "XFS"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc?id=7020905|META_LINK_BUG1=https://bugzilla.suse.com/show_bug.cgi?id=1042200|META_LINK_BUG2=https://bugzilla.suse.com/show_bug.cgi?id=1040146"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def xfsFileSystemsFound():
	FSLIST = SUSE.getFileSystems()
	for FS in FSLIST:
		if 'xfs' in FS['Type'].lower():
			return True
	return False

def xfsCorruption():
#XFS (sda3): corrupt dinode 805392820, has realtime flag set
#XFS (sda3): Internal error xfs_iformat(realtime) at line 345 of file
#XFS (sda3): Corruption detected. Unmount and run xfs_repair
	FILE_OPEN = "messages.txt"
	ERROR_STRING = re.compile("XFS.*: corrupt dinode.*has realtime flag set|XFS.*: Internal error xfs_iformat.*realtime|XFS.*: Corruption detected.*Unmount and run xfs_repair", re.IGNORECASE)
	SECTION = "/var/log/warn"
	CONTENT = []
	if Core.getRegExSection(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if ERROR_STRING.search(LINE):
				return True
	SECTION = "/var/log/messages"
	CONTENT = []
	if Core.getRegExSection(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if ERROR_STRING.search(LINE):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

KERNEL_VERSION = '3.0.101-100'
INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION)
if( INSTALLED_VERSION == 0 ):
	if( xfsFileSystemsFound() ):
		if( xfsCorruption() ):
			Core.updateStatus(Core.CRIT, "Detected XFS filesystem corruption, update system to apply fixes")
		else:
			Core.updateStatus(Core.WARN, "Detected possible XFS filesystem corruption, update system to apply fixes")
	else:
		Core.updateStatus(Core.IGNORE, "IGNORE: No XFS Filesystems in Use")
else:
	Core.updateStatus(Core.IGNORE, "IGNORE: Outside the kernel scope")


Core.printPatternResults()


