#!/usr/bin/python

# Title:       mcelog start failure
# Description: mcelog fails to start in VMware environments utilizing Ivy and Sandy Bridge CPUs
# Modified:    2013 Oct 31
#
##############################################################################
# Copyright (C) 2013 SUSE LLC
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
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
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
META_CATEGORY = "Service"
META_COMPONENT = "MCE"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7004434|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=827616"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def vmwareFound():
	fileOpen = "basic-environment.txt"
	section = "Virtualization"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "Virtual Machine" in content[line]:
				return True
	return False

def mceLoadError():
	fileOpen = "boot.txt"
	section = "/var/log/mcelog"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "mcelog: Failed to set imc_log on cpu" in content[line]:
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

PACKAGE = 'mcelog'
VERSION = '1.0.2013.01.18-0.11.9'
if( SUSE.compareKernel(SUSE.SLE11SP3) >= 0 and SUSE.compareKernel(SUSE.SLE11SP4) < 0 ):
	if( SUSE.packageInstalled(PACKAGE) ):
		if( SUSE.compareRPM(PACKAGE, VERSION) <= 0 ):
			if( vmwareFound() ):
				if( mceLoadError() ):
					Core.updateStatus(Core.CRIT, "Service " + PACKAGE + " failed to start")
				else:
					Core.updateStatus(Core.WARN, "Service " + PACKAGE + " may fail to start")
			else:
				Core.updateStatus(Core.ERROR, "Error: Missing VMware Machine, skipping mcelog check")
		else:
			Core.updateStatus(Core.ERROR, "Valid version of " + PACKAGE + " installed, AVOIDED")
	else:
		Core.updateStatus(Core.ERROR, "Error: " + PACKAGE + " package not installed, skipping mcelog check")
else:
	Core.updateStatus(Core.ERROR, "Error: Outside kernel scope, skipping mcelog check")
Core.printPatternResults()

