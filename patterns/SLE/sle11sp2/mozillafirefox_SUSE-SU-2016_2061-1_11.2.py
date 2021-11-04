#!/usr/bin/python3
#
# Title:       Important Security Announcement for MozillaFirefox SUSE-SU-2016:2061-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP2
# Source:      Security Announcement Parser v1.3.2
# Modified:    2016 Aug 23
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
META_COMPONENT = "MozillaFirefox"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2016-08/msg00036.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'MozillaFirefox'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2016:2061-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'MozillaFirefox': '45.3.0esr-48.1',
			'MozillaFirefox-branding-SLED': '45.0-20.38',
			'MozillaFirefox-debuginfo': '45.3.0esr-48.1',
			'MozillaFirefox-debugsource': '45.3.0esr-48.1',
			'MozillaFirefox-translations': '45.3.0esr-48.1',
			'firefox-fontconfig': '2.11.0-4.2',
			'firefox-fontconfig-debuginfo': '2.11.0-4.2',
			'firefox-fontconfig-debugsource': '2.11.0-4.2',
			'libfreebl3': '3.21.1-26.2',
			'libfreebl3-32bit': '3.21.1-26.2',
			'mozilla-nspr': '4.12-25.2',
			'mozilla-nspr-32bit': '4.12-25.2',
			'mozilla-nspr-debuginfo': '4.12-25.2',
			'mozilla-nspr-debuginfo-32bit': '4.12-25.2',
			'mozilla-nspr-debugsource': '4.12-25.2',
			'mozilla-nspr-devel': '4.12-25.2',
			'mozilla-nss': '3.21.1-26.2',
			'mozilla-nss-32bit': '3.21.1-26.2',
			'mozilla-nss-debuginfo': '3.21.1-26.2',
			'mozilla-nss-debuginfo-32bit': '3.21.1-26.2',
			'mozilla-nss-debugsource': '3.21.1-26.2',
			'mozilla-nss-devel': '3.21.1-26.2',
			'mozilla-nss-tools': '3.21.1-26.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

