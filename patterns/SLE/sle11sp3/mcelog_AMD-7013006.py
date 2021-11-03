#!/usr/bin/python3

# Title:       mcelog failures
# Description: mcelog not working with AMD processor family 16 or higher and SLES11 sp3.
# Modified:    2014 Apr 09
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
#   Sean Barlow (sbarlow@novell.com)
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
META_CATEGORY = "Hardware"
META_COMPONENT = "MCE"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=http://www.novell.com/support/kb/doc.php?id=7013006|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=807336|META_LINK_Download=http://download.novell.com/Download?buildid=Hp-QDHVE-oM~ "

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def checkProcessorFamily():
	fileOpen = "boot.txt"
	section = "/usr/sbin/mcelog --ignorenodev --filter --dmi"
	content = {}
	NOT_FOUND = 1
	if Core.getSection(fileOpen, section, content):
		failure = re.compile("mcelog: AMD Processor family.*Please load edac_mce_amd module.")		
		for line in content:
			if failure.search(content[line]):
				FAMILY = content[line].split()[4].split(':')[0]
				if( FAMILY.isdigit() ):
					if( int(FAMILY) > 15 ):					
						Core.updateStatus(Core.CRIT, "Compatibility issue with AMD processor family and mcelog, update system to apply: " + RPM_NAME + '-' + RPM_VERSION)
						NOT_FOUND = 0
					elif( int(FAMILY) == 15 ):
						Core.updateStatus(Core.WARN, "Potential compatibility issue with AMD processor family and mcelog, update system to apply: " + RPM_NAME + '-' + RPM_VERSION)
						NOT_FOUND = 0
	if( NOT_FOUND ):
		Core.updateStatus(Core.IGNORE, "Valid processor family found, not applicable")


##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'mcelog'
RPM_VERSION = '1.0.2013.01.18-0.15.1'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION)
	if( INSTALLED_VERSION < 0 ):
		checkProcessorFamily()
	else:
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME + "-" + RPM_VERSION)
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")

Core.printPatternResults()


