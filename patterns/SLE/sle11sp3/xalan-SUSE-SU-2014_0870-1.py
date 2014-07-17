#!/usr/bin/python

# Title:       Xalan SA Important SUSE-SU-2014:0870-1
# Description: fixes one vulnerability
# Modified:    2014 Jul 17
#
##############################################################################
# Copyright (C) 2014
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

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "Xalan"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-07/msg00003.html"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Main Program Execution
##############################################################################

LTSS = False
NAME = 'Xalan'
MAIN = 'xalan-j2'
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:0870-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11 and SERVER['DistroPatchLevel'] == 3 ):
	PACKAGES = {
		'xalan-j2': '2.7.0-217.26.1',
		'xalan-j2-demo': '2.7.0-217.26.1',
		'xalan-j2-javadoc': '2.7.0-217.26.1',
		'xalan-j2-manual': '2.7.0-217.26.1',
	}
	SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")

Core.printPatternResults()

