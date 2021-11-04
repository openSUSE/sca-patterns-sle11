#!/usr/bin/python3

# Title:       shim for upgrade
# Description: Upgrading to SLE12 SP2 with UEFI generates shim error
# Modified:    2018 May 02
#
##############################################################################
# Copyright (C) 2018 SUSE LLC
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
#   Jason Record
#
##############################################################################

##############################################################################
# Module Definition
##############################################################################

import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Upgrade"
META_COMPONENT = "UEFI"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7022915"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def uefiBoot():
	FILE_OPEN = "boot.txt"
	SECTION = "efibootmgr"
	CONTENT = []
	if Core.getRegExSectionRaw(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if "BootOrder" in LINE:
				return True
	return False

def missingShim():
	PACKAGE_NAME = 'shim'
	if ( SUSE.packageInstalled(PACKAGE_NAME) ):
		return False
	else:
		return True


##############################################################################
# Main Program Execution
##############################################################################

if( uefiBoot() ):
	if( missingShim() ):
		Core.updateStatus(Core.CRIT, "Missing shim package, boot failure probable after upgrade")
	else:
		Core.updateStatus(Core.IGNORE, "Shim package installed, not applicable")
else:
	Core.updateStatus(Core.IGNORE, "Not booting with uefi, not applicable")

Core.printPatternResults()


