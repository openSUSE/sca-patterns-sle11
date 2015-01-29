#!/usr/bin/python
#
# Title:       Critical Security Announcement for glibc SUSE-SU-2015:0158-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP3
# Source:      Security Announcement Parser v1.2.5
# Modified:    2015 Jan 29
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
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7016113|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=913646|META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2015-01/msg00028.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'glibc'
MAIN = ''
SEVERITY = 'Critical'
TAG = 'SUSE-SU-2015:0158-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'glibc': '2.11.3-17.74.13',
			'glibc-32bit': '2.11.3-17.74.13',
			'glibc-devel': '2.11.3-17.74.13',
			'glibc-devel-32bit': '2.11.3-17.74.13',
			'glibc-html': '2.11.3-17.74.13',
			'glibc-i18ndata': '2.11.3-17.74.13',
			'glibc-info': '2.11.3-17.74.13',
			'glibc-locale': '2.11.3-17.74.13',
			'glibc-locale-32bit': '2.11.3-17.74.13',
			'glibc-locale-x86': '2.11.3-17.74.13',
			'glibc-profile': '2.11.3-17.74.13',
			'glibc-profile-32bit': '2.11.3-17.74.13',
			'glibc-profile-x86': '2.11.3-17.74.13',
			'glibc-x86': '2.11.3-17.74.13',
			'nscd': '2.11.3-17.74.13',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

