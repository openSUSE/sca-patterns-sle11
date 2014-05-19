#!/usr/bin/python

# Title:       Check ACPI Errors
# Description: Frequent ACPI errors starting with SMBus or IPMI write requires Buffer of length 42
# Modified:    2014 May 19
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
META_CATEGORY = "ACPI"
META_COMPONENT = "Exception"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7010449"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def errorsFound():
	fileOpen = "messages.txt"
	section = "/var/log/messages"
	content = {}
	err1Found = False
	err2Found = False
	err3Found = False
	if Core.getSection(fileOpen, section, content):
		err1 = re.compile("ACPI Error: SMBus or IPMI write requires Buffer of length")
		err2 = re.compile("ACPI Error.*Method parse/execution failed.*AE_AML_BUFFER_LIMIT")
		err3 = re.compile("ACPI Exception.*AE_AML_BUFFER_LIMIT")
		for line in content:
			if err1.search(content[line]):
				err1Found = True
			elif err2.search(content[line]):
				err2Found = True
			elif err3.search(content[line]):
				err3Found = True
			if( err1Found and err2Found and err3Found ):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

FIXED_KERNEL='3.0.26-0.7'
if( SUSE.compareKernel(SUSE.SLE11SP1) >= 0 and SUSE.compareKernel(FIXED_KERNEL) < 0 ):
	if( errorsFound() ):
		Core.updateStatus(Core.WARN, "Detected ACPI warning errors that are resolved in a kernel update")
	else:
		Core.updateStatus(Core.IGNORE, "No ACPI errors found")
else:
	Core.updateStatus(Core.IGNORE, "Outside the kernel scope, skipping ACPI error test")

Core.printPatternResults()

