#!/usr/bin/python

# Title:       kdump fails on Hyper-V
# Description: Confirm valid configuration
# Modified:    2014 Jun 23
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

import os
import re
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Hyper-V"
META_COMPONENT = "Kdump"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014585|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=839510 |META_LINK_Web=http://support.microsoft.com/kb/2858695"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def hyperV():
	fileOpen = "basic-environment.txt"
	section = "Virtualization"
	content = {}
	Found = 0
	hyper = re.compile('Hypervisor:\s+Microsoft', re.IGNORECASE)
	identity = re.compile('Identity:\s+Virtual Machine', re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if hyper.search(content[line]):
				Found += 1
			elif identity.search(content[line]):
				Found += 1
	if( Found >= 2 ):
		return True
	else:
		return False

def kdumpEnabled():
	FILE_OPEN = "crash.txt"
	CONTENT = {}
	Enabled = 0
	if SUSE.packageInstalled('kdump'):
		Enabled += 1
	if SUSE.packageInstalled('kexec-tools'):
		Enabled += 1
	if Core.listSections(FILE_OPEN, CONTENT):
		for LINE in CONTENT:
			if "/etc/sysconfig/kdump" in CONTENT[LINE]:
				Enabled += 1
				break
	if( Enabled >= 3 ):
		return True
	else:
		return False

def preferHyperEnabled():
	fileOpen = "crash.txt"
	section = "/etc/sysconfig/kdump"
	content = {}
	if Core.getSection(fileOpen, section, content):
		validKdumpCmdLine = re.compile('KDUMP_COMMANDLINE_APPEND=.*ata_piix.prefer_ms_hyperv=0')
		for line in content:
			if validKdumpCmdLine.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

#Applies to sle11sp2 and sle11sp3
if( hyperV() ):
	if ( kdumpEnabled() ):
		if ( preferHyperEnabled() ):
			Core.updateStatus(Core.IGNORE, "Found ata_piix.prefer_ms_hyperv=0, configured correctly.")
		else:
			Core.updateStatus(Core.WARN, "Kernel core dumps may fail, consider ata_piix.prefer_ms_hyperv=0")
	else:
		Core.updateStatus(Core.ERROR, "Kdump Not Installed, not applicable")
else:
	Core.updateStatus(Core.ERROR, "HyperV not installed, not applicable")

Core.printPatternResults()

