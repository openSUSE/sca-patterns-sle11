#!/usr/bin/python3

# Title:       Detect audit message bug
# Description: Log files are flooded when enabling audit servers
# Modified:    2014 May 22
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
META_CATEGORY = "Audit"
META_COMPONENT = "Messages"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014614|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=857358"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def errorsFound():
	fileOpen = "messages.txt"
	errCount = 0
	MAX_ERRORS = 5
	err1 = re.compile("audit: name_count maxed, losing inode data")
	sections = ['/var/log/messages']

	for section in sections:
		content = {}
		if Core.getSection(fileOpen, section, content):
			for line in content:
				if err1.search(content[line]):
					errCount += 1
				if( errCount > MAX_ERRORS ):
#					print "Found in " + str(section)
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

FIXED_KERNEL = '3.0.101-0.21'
if( SUSE.compareKernel(SUSE.SLE11SP2) >= 0 and SUSE.compareKernel(FIXED_KERNEL) < 0 ):
	if( errorsFound() ):
		Core.updateStatus(Core.WARN, "Detected cosmetic audit name count messages, resolved in updated kernel")
	else:
		Core.updateStatus(Core.IGNORE, "No audit errors found")
else:
	Core.updateStatus(Core.ERROR, "Outside the kernel scope, skipping audit errors")

Core.printPatternResults()

