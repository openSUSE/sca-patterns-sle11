#!/usr/bin/python

# Title:       Windbind Error
# Description: winbindd failure: key length too large
# Modified:    2015 Aug 26
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

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Samba"
META_COMPONENT = "Windbind"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7016777|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=934299"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def excessiveWinBindKey():
	fileOpen = "samba.txt"
	section = "log.winbindd"
	content = []
	excessiveKeyLength = re.compile("cache_traverse_validate_fn.*key length too large", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if excessiveKeyLength.search(line):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( excessiveWinBindKey() ):
	Core.updateStatus(Core.CRIT, "Win Bind key length error, patch may be needed")
else:
	Core.updateStatus(Core.IGNORE, "Ignore this pattern, not applicable")

Core.printPatternResults()


