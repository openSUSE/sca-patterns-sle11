#!/usr/bin/python

# Title:       Detect kernel oops in 3.0.101-0.18.1
# Description: kernel Oops/BUG during network operation
# Modified:    2014 Mar 31
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

import sys, os, Core, SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Kernel"
META_COMPONENT = "Oops"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014823|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=870801"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def checkSomething():
	fileOpen = "filename.txt"
	section = "CommandToIdentifyFileSection"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "something" in content[line]:
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

KERNEL_VERSION = '3.0.101-0.18'
INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION)
if( INSTALLED_VERSION == 0 ):
	Core.updateStatus(Core.CRIT, "Kernel susceptible to oops on network operations, update system to apply newest kernel")
else:
	Core.updateStatus(Core.IGNORE, "Bug fixes applied, not applicable to installed kernel")

Core.printPatternResults()

