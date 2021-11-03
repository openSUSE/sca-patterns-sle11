#!/usr/bin/python3

# Title:       Microcode causes hang
# Description: SLES11SP3 HP (any model) Gen9 systems crashing after installing latest updates
# Modified:    2015 Jun 24
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

import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Kernel"
META_COMPONENT = "Microcode"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7016594|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=932708"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'microcode_ctl'
RPM_VERSION = '1.17-102.78.1'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, RPM_VERSION)
	if( INSTALLED_VERSION == 0 ):
		SYSTEM = SUSE.getBasicVirtualization()
		if ( "hp" in SYSTEM['Manufacturer'].lower() and "gen9" in SYSTEM['Hardware'].lower() ):
			Core.updateStatus(Core.CRIT, "Susceptible to system crash, update server to apply " + RPM_NAME + " fixes")
		else:
			Core.updateStatus(Core.IGNORE, "Unaffected hardware")
	else:
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + RPM_NAME)
else:
	Core.updateStatus(Core.ERROR, "ERROR: RPM package not installed: " + RPM_NAME)

Core.printPatternResults()


