#!/usr/bin/python

# Title:       Custom repos fail with SMT
# Description: smt-setup-custom-repos fails with mysql::db error
# Modified:    2014 Dec 08
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
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "SMT"
META_COMPONENT = "Repositories"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7015946|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=903847 "

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Main Program Execution
##############################################################################

RPM_NAME = 'smt'
AFFECTED_RPM_VERSION = '2.0.7-0.7.1'
if( SUSE.packageInstalled(RPM_NAME) ):
	INSTALLED_VERSION = SUSE.compareRPM(RPM_NAME, AFFECTED_RPM_VERSION)
	if( INSTALLED_VERSION <= 0 ):
		Core.updateStatus(Core.WARN, "The command smt-setup-custom-repos may fail with unknown column ID errors, update system resolve.")
	else:
		Core.updateStatus(Core.IGNORE, "Bug fixes applied for " + str(RPM_NAME) + ", AVOIDED")
else:
	Core.updateStatus(Core.ERROR, "ERROR: Package " + RPM_NAME + " not installed")

Core.printPatternResults()

