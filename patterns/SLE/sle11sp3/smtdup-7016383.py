#!/usr/bin/python3

# Title:       Duplicate SMT Entries
# Description: smt-sync fails with duplicate entry SLE11SP3
# Modified:    2015 Apr 06
#
##############################################################################
# Copyright (C) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany
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
META_COMPONENT = "Sync"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7016383|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=918568"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def duplicateEntriesFound():
	fileOpen = "smt.txt"
	section = "/smt-sync.log"
	content = {}
	duplicate = re.compile("SMT::SCCSync.*error.*DBD::mysql::db do failed: Duplicate entry.*for key.*PRODUCTLOWER.*at .*SCCSync.pm.*", re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if duplicate.search(content[line]):
				return True
	return False


##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'smt'
AFFECTED_RPM_VERSION = '2.0.9-0.7.1'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, AFFECTED_RPM_VERSION)
	if( INSTALLED_VERSION <= 0 ):
		if( duplicateEntriesFound() ):
			Core.updateStatus(Core.CRIT, "Detected duplicate entry errors from the smt-sync command, update system to resolve.")
		else:
			Core.updateStatus(Core.WARN, "The smt-sync command is susceptible to duplicate entry errors, update system to prevent errors.")
	else:
		Core.updateStatus(Core.IGNORE, "Duplicate entry issue resolved with updated " + str(RPM_NAME) + " package")
else:
	Core.updateStatus(Core.ERROR, "ERROR: Package " + RPM_NAME + " not installed")

Core.printPatternResults()

