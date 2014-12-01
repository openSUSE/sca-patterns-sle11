#!/usr/bin/python

# Title:       mcelog fails to start in VMware environments
# Description: mcelog fails to start in VMware environments utilizing Ivy and Sandy Bridge CPUs
# Modified:    2014 Dec 01
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

import re
import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Hardware"
META_COMPONENT = "mcelog"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7004434|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=827616"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def isVMwareVM():
	fileOpen = "basic-environment.txt"
	section = "Virtualization"
	content = {}
	IN_VMWARE = False
	VMWARE = re.compile("Manufacturer:\s*VMware", re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if( IN_VMWARE ):
				if "virtual machine" in content[line].lower():
					return True
			elif VMWARE.search(content[line]):
				IN_VMWARE = True
	return False

def errorsFound():
	fileOpen = "boot.txt"
	section = "/var/log/mcelog"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "failed to set imc_log on cpu" in content[line].lower():
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( isVMwareVM() ):
	RPM_NAME = 'mcelog'
	RPM_VERSION = '1.0.2013.01.18.0.15.1'
	if( SUSE.packageInstalled(RPM_NAME) ):
		INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION)
		if( INSTALLED_VERSION <= 0 ):
			SERVICE = RPM_NAME
			SERVICE_INFO = SUSE.getServiceInfo(SERVICE)
			if( SERVICE_INFO['Running'] > 0 ):
				Core.updateStatus(Core.IGNORE, "Service is running: " + str(SERVICE))
			elif( SERVICE_INFO['OnForRunLevel'] ):
				if( errorsFound() ):
					Core.updateStatus(Core.CRIT, "Failed mcelog service, update system to apply " + str(RPM_NAME) + "-" + str(RPM_VERSION) + " or better")
				else:
					Core.updateStatus(Core.WARN, "Service mcelog is down, consider updating system to apply " + str(RPM_NAME) + "-" + str(RPM_VERSION) + " or better")
			else:
				Core.updateStatus(Core.ERROR, "ERROR: Service is not enabled for current runlevel")
		else:
			Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + RPM_NAME + " not installed")
else:
	Core.updateStatus(Core.ERROR, "ERROR: VMware Virtual Machine not found")

Core.printPatternResults()

