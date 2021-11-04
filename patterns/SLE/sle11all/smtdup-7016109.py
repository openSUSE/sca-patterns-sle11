#!/usr/bin/python3

# Title:       Checking SCCSync Duplicates 725
# Description: smt-ncc-scc-migration displays duplicate entry messages
# Modified:    2015 Jan 29
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
META_CATEGORY = "SMT"
META_COMPONENT = "SCCSync"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7016109|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=914293"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def foundDuplicateErrors():
	fileOpen = "smt.txt"
	section = "smt-sync.log"
	content = {}
	DUP_ERROR = re.compile("SCCSync.*Duplicate entry.*/SCCSync.pm line 725", re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if DUP_ERROR.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

SMT = SUSE.getServiceInfo('smt')
if( SMT['OnForRunLevel'] or SMT['Running'] > 0 ):
	if foundDuplicateErrors():
		Core.updateStatus(Core.REC, "Detected inconsequential duplicate SCCSync.pm line 725 errors, run smt-repos to confirm functionality.")
	else:
		Core.updateStatus(Core.IGNORE, "No duplicate SCCSync.pm line 725 errors found, AVOIDED")
else:
	Core.updateStatus(Core.ERROR, "ERROR: SMT not enable or running, skipping")

Core.printPatternResults()


