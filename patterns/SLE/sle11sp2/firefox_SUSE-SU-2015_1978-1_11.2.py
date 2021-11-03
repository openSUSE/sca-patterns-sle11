#!/usr/bin/python3
#
# Title:       Important Security Announcement for mozilla-nspr, SUSE-SU-2015:1978-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP2
# Source:      Security Announcement Parser v1.3.0
# Modified:    2015 Nov 18
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
META_COMPONENT = "Firefox"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2015-11/msg00020.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'Firefox'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2015:1978-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'MozillaFirefox': '38.4.0esr-25.3',
			'MozillaFirefox-branding-SLED': '38-12.19',
			'MozillaFirefox-debuginfo': '38.4.0esr-25.3',
			'MozillaFirefox-debugsource': '38.4.0esr-25.3',
			'MozillaFirefox-translations': '38.4.0esr-25.3',
			'libfreebl3': '3.19.2.1-12.1',
			'libfreebl3-32bit': '3.19.2.1-12.1',
			'mozilla-nspr': '4.10.10-16.1',
			'mozilla-nspr-32bit': '4.10.10-16.1',
			'mozilla-nspr-debuginfo': '4.10.10-16.1',
			'mozilla-nspr-debuginfo-32bit': '4.10.10-16.1',
			'mozilla-nspr-debugsource': '4.10.10-16.1',
			'mozilla-nspr-devel': '4.10.10-16.1',
			'mozilla-nss': '3.19.2.1-12.1',
			'mozilla-nss-32bit': '3.19.2.1-12.1',
			'mozilla-nss-debuginfo': '3.19.2.1-12.1',
			'mozilla-nss-debuginfo-32bit': '3.19.2.1-12.1',
			'mozilla-nss-debugsource': '3.19.2.1-12.1',
			'mozilla-nss-devel': '3.19.2.1-12.1',
			'mozilla-nss-tools': '3.19.2.1-12.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

