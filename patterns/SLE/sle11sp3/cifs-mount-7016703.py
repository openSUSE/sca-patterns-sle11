#!/usr/bin/python3

# Title:       cifs mounts broken
# Description: Kernel 3.0.101-0.47.55 cifs mounts broken
# Modified:    2015 Jul 31
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

import re
import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "CIFS"
META_COMPONENT = "Mounts"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7016703|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=937402"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def fatalErrors():
	fileOpen = "messages.txt"
	section = "/var/log/warn"
	content = []
	MountError = re.compile("kernel.*CIFS VFS.*cifs_mount failed", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for LINE in content:
			if MountError.search(LINE):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

KERNEL_VERSION = '3.0.101-0.47.55'
CIFS_FOUND = False
INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION)
if( INSTALLED_VERSION == 0 ):
	FSLIST = SUSE.getFileSystems()
	for FS in FSLIST:
		if( 'cifs' in FS['Type'].lower() ):
			CIFS_FOUND = True
			break
	if( CIFS_FOUND ):
		if( fatalErrors() ):
			Core.updateStatus(Core.CRIT, "CIFS Filesystem mount failures detected, update system to apply latest kernel")
		else:
			Core.updateStatus(Core.WARN, "CIFS Filesystems may fail to mount, update system to apply latest kernel")
	else:
		Core.updateStatus(Core.IGNORE, "No CIFS filesystems found")
else:
	Core.updateStatus(Core.ERROR, "ERROR: Outside kernel scope, CFIS mount error")

Core.printPatternResults()


