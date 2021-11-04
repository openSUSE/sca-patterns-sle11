#!/usr/bin/python3
#
# Title:       Important Security Announcement for MozillaFirefox SUSE-SU-2014:1458-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP1
# Source:      Security Announcement Parser v1.0.6
# Modified:    2014 Nov 21
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
META_COMPONENT = "MozillaFirefox"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-11/msg00017.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'MozillaFirefox'
MAIN = 'MozillaFirefox'
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:1458-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
		'libfreebl3': '3.17.2-0.3.1',
		'libfreebl3-32bit': '3.17.2-0.3.1',
		'MozillaFirefox': '31.2.0esr-0.11.11.1',
		'MozillaFirefox-branding-SLED': '31.0-0.5.5.1',
		'MozillaFirefox-translations': '31.2.0esr-0.11.11.1',
		'mozilla-nspr-32bit': '4.10.7-0.3.3',
		'mozilla-nspr': '4.10.7-0.3.3',
		'mozilla-nss': '3.17.2-0.3.1',
		'mozilla-nss-32bit': '3.17.2-0.3.1',
		'mozilla-nss-tools': '3.17.2-0.3.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

