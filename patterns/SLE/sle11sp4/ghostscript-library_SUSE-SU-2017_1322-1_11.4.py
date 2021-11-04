#!/usr/bin/python3
#
# Title:       Important Security Announcement for ghostscript-library SUSE-SU-2017:1322-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP4
# Source:      Security Announcement Parser v1.3.6
# Modified:    2017 May 18
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
META_COMPONENT = "ghostscript-library"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2017-05/msg00052.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'ghostscript-library'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2017:1322-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'ghostscript-devel': '8.62-32.46.1',
			'ghostscript-fonts-other': '8.62-32.46.1',
			'ghostscript-fonts-rus': '8.62-32.46.1',
			'ghostscript-fonts-std': '8.62-32.46.1',
			'ghostscript-ijs-devel': '8.62-32.46.1',
			'ghostscript-library': '8.62-32.46.1',
			'ghostscript-library-debuginfo': '8.62-32.46.1',
			'ghostscript-library-debugsource': '8.62-32.46.1',
			'ghostscript-omni': '8.62-32.46.1',
			'ghostscript-x11': '8.62-32.46.1',
			'libgimpprint': '4.2.7-32.46.1',
			'libgimpprint-devel': '4.2.7-32.46.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

