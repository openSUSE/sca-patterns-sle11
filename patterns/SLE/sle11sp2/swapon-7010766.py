#!/usr/bin/python3

# Title:       Kernel failure from swapon
# Description: SLES11SP2 crashs on boot with "Bug: Soft lock up - CPU#0 stuck for 22s! [swapon:472]"
# Modified:    2014 May 21
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

import sys, os, Core, SUSE, re

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Kernel"
META_COMPONENT = "Swapon"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=http://www.novell.com/support/kb/doc.php?id=7010766|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=773319"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def swapOnSoftLock():
	fileOpen = "messages.txt"
	softLock = re.compile("BUG: soft lockup - CPU.*stuck for.*[swapon:.*]")
	section = "/var/log/warn"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if softLock.search(content[line]):
				return True

	section = "/var/log/messages"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if softLock.search(content[line]):
				return True

	return False

##############################################################################
# Main Program Execution
##############################################################################

AFFECTED_KERNEL = '3.0.34-0.7'
FIXED_KERNEL = '3.0.101-0.7.17'
if ( SUSE.compareKernel(AFFECTED_KERNEL) >= 0 and SUSE.compareKernel(FIXED_KERNEL) < 0 ):
	if( swapOnSoftLock() ):
		Core.updateStatus(Core.CRIT, "Kernel failure due to swapon soft lock issue, update system")
	else:
		Core.updateStatus(Core.IGNORE, "Kernel failure errors not found")		
else:
	Core.updateStatus(Core.ERROR, "Outside kernel scope, skipping swapon soft lock")

Core.printPatternResults()

