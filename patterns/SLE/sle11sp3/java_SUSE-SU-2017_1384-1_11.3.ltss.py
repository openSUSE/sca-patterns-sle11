#!/usr/bin/python3
#
# Title:       Important Security Announcement for Java SUSE-SU-2017:1384-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP3 LTSS
# Source:      Security Announcement Parser v1.3.6
# Modified:    2017 May 25
#
##############################################################################
# Copyright (C) 2017 SUSE LLC
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
#   Jason Record (jason.record@suse.com)
#
##############################################################################

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "Java"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2017-05/msg00063.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'Java'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2017:1384-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'java-1_7_0-ibm': '1.7.0_sr10.5-64.1',
			'java-1_7_0-ibm-alsa': '1.7.0_sr10.5-64.1',
			'java-1_7_0-ibm-devel': '1.7.0_sr10.5-64.1',
			'java-1_7_0-ibm-jdbc': '1.7.0_sr10.5-64.1',
			'java-1_7_0-ibm-plugin': '1.7.0_sr10.5-64.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

