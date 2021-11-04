#!/usr/bin/python3
#
# Title:       Important Security Announcement for glibc SUSE-SU-2015:1424-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP4
# Source:      Security Announcement Parser v1.3.0
# Modified:    2015 Aug 24
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

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "glibc"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2015-08/msg00019.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'glibc'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2015:1424-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'glibc': '2.11.3-17.87.3',
			'glibc-32bit': '2.11.3-17.87.3',
			'glibc-debuginfo': '2.11.3-17.87.3',
			'glibc-debugsource': '2.11.3-17.87.3',
			'glibc-devel': '2.11.3-17.87.3',
			'glibc-devel-32bit': '2.11.3-17.87.3',
			'glibc-html': '2.11.3-17.87.3',
			'glibc-i18ndata': '2.11.3-17.87.3',
			'glibc-info': '2.11.3-17.87.3',
			'glibc-locale': '2.11.3-17.87.3',
			'glibc-locale-32bit': '2.11.3-17.87.3',
			'glibc-locale-x86': '2.11.3-17.87.3',
			'glibc-profile': '2.11.3-17.87.3',
			'glibc-profile-32bit': '2.11.3-17.87.3',
			'glibc-profile-x86': '2.11.3-17.87.3',
			'glibc-x86': '2.11.3-17.87.3',
			'nscd': '2.11.3-17.87.3',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

