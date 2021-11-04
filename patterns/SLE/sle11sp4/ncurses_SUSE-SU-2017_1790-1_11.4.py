#!/usr/bin/python3
#
# Title:       Important Security Announcement for ncurses SUSE-SU-2017:1790-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP4
# Source:      Security Announcement Parser v1.3.6
# Modified:    2017 Jul 24
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
META_COMPONENT = "ncurses"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.opensuse.org/opensuse-security-announce/2017-07/msg00004.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'ncurses'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2017:1790-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'libncurses5': '5.6-92.1',
			'libncurses5-32bit': '5.6-92.1',
			'libncurses5-x86': '5.6-92.1',
			'libncurses6': '5.6-92.1',
			'libncurses6-32bit': '5.6-92.1',
			'libncurses6-x86': '5.6-92.1',
			'ncurses-debuginfo': '5.6-92.1',
			'ncurses-debugsource': '5.6-92.1',
			'ncurses-devel': '5.6-92.1',
			'ncurses-devel-32bit': '5.6-92.1',
			'ncurses-utils': '5.6-92.1',
			'tack': '5.6-92.1',
			'terminfo': '5.6-92.1',
			'terminfo-base': '5.6-92.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

