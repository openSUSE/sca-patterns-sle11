#!/usr/bin/python3
#
# Title:       Important Security Announcement for MozillaFirefox SUSE-SU-2017:2235-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP4
# Source:      Security Announcement Parser v1.3.6
# Modified:    2017 Sep 08
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
META_COMPONENT = "MozillaFirefox"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.opensuse.org/opensuse-security-announce/2017-08/msg00061.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'MozillaFirefox'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2017:2235-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'MozillaFirefox': '52.2.0esr-72.5.2',
			'MozillaFirefox-branding-SLED': '52-24.3.44',
			'MozillaFirefox-debuginfo': '52.2.0esr-72.5.2',
			'MozillaFirefox-devel': '52.2.0esr-72.5.2',
			'MozillaFirefox-translations': '52.2.0esr-72.5.2',
			'firefox-libffi4': '5.3.1+r233831-7.1',
			'firefox-libstdc++6': '5.3.1+r233831-7.1',
			'libfreebl3': '3.29.5-47.3.2',
			'libfreebl3-32bit': '3.29.5-47.3.2',
			'libfreebl3-x86': '3.29.5-47.3.2',
			'libsoftokn3': '3.29.5-47.3.2',
			'libsoftokn3-32bit': '3.29.5-47.3.2',
			'libsoftokn3-x86': '3.29.5-47.3.2',
			'mozilla-nss': '3.29.5-47.3.2',
			'mozilla-nss-32bit': '3.29.5-47.3.2',
			'mozilla-nss-debuginfo': '3.29.5-47.3.2',
			'mozilla-nss-debugsource': '3.29.5-47.3.2',
			'mozilla-nss-devel': '3.29.5-47.3.2',
			'mozilla-nss-tools': '3.29.5-47.3.2',
			'mozilla-nss-x86': '3.29.5-47.3.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

