#!/usr/bin/python3

# Title:       The regcode is locked by another email address
# Description: The regcode is locked by another email address, needs to be fixed in NCC.
# Modified:    2014 Mar 04
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

import re, sys, os, Core, SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "SLES"
META_COMPONENT = "Registration"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=http://www.novell.com/support/kb/doc.php?id=7014660"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def emailConflict():
	fileOpen = "updates.txt"
	section = "suse_register.log"
	content = {}
	EMAIL_CONFLICT = False
	REGISTERED = False
	if Core.getSection(fileOpen, section, content):
		registered = re.compile("<subscription status=\"ACTIVE\".*<message>No errors", re.IGNORECASE)
		for line in content:
			if "regcode is locked by another email address" in content[line]:
				EMAIL_CONFLICT = True
			if registered.search(content[line]):
				REGISTERED = True

	if( EMAIL_CONFLICT ):
		if( REGISTERED ):
			return False
		else:
			return True
	else:
		return False

##############################################################################
# Main Program Execution
##############################################################################

if( emailConflict() ):
	Core.updateStatus(Core.WARN, "Detected registration failure from email conflict")
else:
	Core.updateStatus(Core.IGNORE, "No registration email conflict detected")

Core.printPatternResults()


