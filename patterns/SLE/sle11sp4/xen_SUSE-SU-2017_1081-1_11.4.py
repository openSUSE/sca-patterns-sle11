#!/usr/bin/python3
#
# Title:       Important Security Announcement for xen SUSE-SU-2017:1081-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP4
# Source:      Security Announcement Parser v1.3.6
# Modified:    2017 Apr 21
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
META_COMPONENT = "xen"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2017-04/msg00027.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'xen'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2017:1081-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'xen': '4.4.4_16-54.1',
			'xen-debuginfo': '4.4.4_16-54.1',
			'xen-debugsource': '4.4.4_16-54.1',
			'xen-devel': '4.4.4_16-54.1',
			'xen-doc-html': '4.4.4_16-54.1',
			'xen-kmp-default': '4.4.4_16_3.0.101_97-54.1',
			'xen-kmp-pae': '4.4.4_16_3.0.101_97-54.1',
			'xen-libs': '4.4.4_16-54.1',
			'xen-libs-32bit': '4.4.4_16-54.1',
			'xen-tools': '4.4.4_16-54.1',
			'xen-tools-domU': '4.4.4_16-54.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

