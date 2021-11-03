#!/usr/bin/python3
#
# Title:       Important Security Announcement for openssl SUSE-SU-2016:2458-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP4
# Source:      Security Announcement Parser v1.3.2
# Modified:    2016 Oct 24
#
##############################################################################
# Copyright (C) 2016 SUSE LLC
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
META_COMPONENT = "openssl"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2016-10/msg00005.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'openssl'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2016:2458-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'libopenssl-devel': '0.9.8j-0.102.2',
			'libopenssl-devel-32bit': '0.9.8j-0.102.2',
			'libopenssl0_9_8': '0.9.8j-0.102.2',
			'libopenssl0_9_8-32bit': '0.9.8j-0.102.2',
			'libopenssl0_9_8-hmac': '0.9.8j-0.102.2',
			'libopenssl0_9_8-hmac-32bit': '0.9.8j-0.102.2',
			'libopenssl0_9_8-x86': '0.9.8j-0.102.2',
			'openssl': '0.9.8j-0.102.2',
			'openssl-debuginfo': '0.9.8j-0.102.2',
			'openssl-debugsource': '0.9.8j-0.102.2',
			'openssl-doc': '0.9.8j-0.102.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

