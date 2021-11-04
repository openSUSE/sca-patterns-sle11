#!/usr/bin/python3

# Title:       ACPI 5.0 on SLE11
# Description: SLES 11 reports an ACPI warning message on systems supporting ACPI 5.0
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
META_CATEGORY = "ACPI"
META_COMPONENT = "Versions"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7016776"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def foundACPI5():
	fileOpen = "boot.txt"
	section = "/dmesg"
	content = []
	acpi5msg = re.compile("ACPI Warning.*FADT.*revision 5.*is longer than ACPI 2.0 version", re.IGNORECASE)
	if Core.getRegExSection(fileOpen, section, content):
		for line in content:
			if acpi5msg.search(line):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( foundACPI5() ):
	Core.updateStatus(Core.REC, "SLE11 on ACPI 5.0 Machine, FADT messages expected")
else:
	Core.updateStatus(Core.IGNORE, "Ignore this pattern, not applicable")

Core.printPatternResults()


