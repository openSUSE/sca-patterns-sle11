#!/usr/bin/python3
#
# Title:       Important Security Announcement for glibc SUSE-SU-2014:1122-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP1 LTSS
# Source:      Security Announcement Parser v1.0.1
# Modified:    2014 Sep 23
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
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-09/msg00013.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'glibc'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:1122-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'glibc-devel': '2.11.1-0.58.1',
			'glibc-locale': '2.11.1-0.58.1',
			'glibc-locale-32bit': '2.11.1-0.58.1',
			'glibc': '2.11.1-0.58.1',
			'glibc-profile': '2.11.1-0.58.1',
			'glibc-info': '2.11.1-0.58.1',
			'glibc-devel-32bit': '2.11.1-0.58.1',
			'nscd': '2.11.1-0.58.1',
			'glibc-i18ndata': '2.11.1-0.58.1',
			'glibc-profile-32bit': '2.11.1-0.58.1',
			'glibc-html': '2.11.1-0.58.1',
			'glibc-32bit': '2.11.1-0.58.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

