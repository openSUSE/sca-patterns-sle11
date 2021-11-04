#!/usr/bin/python3
#
# Title:       Important Security Announcement for mozilla-nss SUSE-SU-2017:1175-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP3 LTSS
# Source:      Security Announcement Parser v1.3.6
# Modified:    2017 May 10
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
META_COMPONENT = "mozilla-nss"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2017-05/msg00010.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'mozilla-nss'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2017:1175-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'MozillaFirefox': '45.9.0esr-71.2',
			'MozillaFirefox-translations': '45.9.0esr-71.2',
			'libfreebl3': '3.29.5-46.1',
			'libfreebl3-32bit': '3.29.5-46.1',
			'libsoftokn3': '3.29.5-46.1',
			'libsoftokn3-32bit': '3.29.5-46.1',
			'mozilla-nspr': '4.13.1-32.1',
			'mozilla-nspr-32bit': '4.13.1-32.1',
			'mozilla-nss': '3.29.5-46.1',
			'mozilla-nss-32bit': '3.29.5-46.1',
			'mozilla-nss-tools': '3.29.5-46.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

