#!/usr/bin/python3

# Title:       NFS transfers failing with RPC error 88 (ENOTSOCK)
# Description: NFS transfers failing with RPC error 88 (ENOTSOCK) SLES 11 sp1 issue patch in kernel 2.6.32.54-0.3.1.
# Modified:    2014 Sep 05
#version 0.2
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
#############################################################################

import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################
META_CLASS = "SLE"
META_CATEGORY = "Network"
META_COMPONENT = "NFS"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7010007|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=733146"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def checkMessages():
	fileOpen = "messages.txt"
	section = "/var/log/warn"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "nfs: RPC call returned error 88" in content[line]:
				return True
	return False

        section = "/var/log/messages"
        content = {}
        if Core.getSection(fileOpen, section, content):
                for line in content:
                        if "nfs: RPC call returned error 88" in content[line]:
                                return True
        return False

##############################################################################
# Main Program Execution
##############################################################################
KERNEL_VERSION = '2.6.32.54-0.3.1'
INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION)
if( INSTALLED_VERSION < 0 ):
        Core.updateStatus(Core.WARN, "\"RPC call returned error 88\" bug detected in kernel version " + str(INSTALLED_VERSION) + " or before, update server for fixes")
	if( checkMessages() ):
		Core.updateStatus(Core.CRIT, "\"RPC call returned error 88\" bug detected in kernel version " + str(INSTALLED_VERSION) + " or before, update server for fixes")
	else: Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + KERNEL_VERSION)
else:
        Core.updateStatus(Core.IGNORE, "Ignore this pattern, not applicable")
Core.printPatternResults()

