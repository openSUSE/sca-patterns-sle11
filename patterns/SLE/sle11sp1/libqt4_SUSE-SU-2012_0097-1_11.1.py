#!/usr/bin/python3
#
# Title:       Important Security Announcement for libqt4 SUSE-SU-2012:0097-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP1
# Source:      Security Announcement Parser v1.1.7
# Modified:    2014 Dec 05
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
META_COMPONENT = "libqt4"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2012-01/msg00046.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'libqt4'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2012:0097-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'libQtWebKit-devel': '4.6.3-5.12.1',
			'libQtWebKit4': '4.6.3-5.12.1',
			'libQtWebKit4-32bit': '4.6.3-5.12.1',
			'libQtWebKit4-x86': '4.6.3-5.12.1',
			'libqt4': '4.6.3-5.12.1',
			'libqt4-32bit': '4.6.3-5.12.1',
			'libqt4-devel': '4.6.3-5.12.1',
			'libqt4-qt3support': '4.6.3-5.12.1',
			'libqt4-qt3support-32bit': '4.6.3-5.12.1',
			'libqt4-qt3support-x86': '4.6.3-5.12.1',
			'libqt4-sql': '4.6.3-5.12.1',
			'libqt4-sql-32bit': '4.6.3-5.12.1',
			'libqt4-sql-sqlite': '4.6.3-5.12.1',
			'libqt4-sql-sqlite-32bit': '4.6.3-5.12.1',
			'libqt4-sql-sqlite-x86': '4.6.3-5.12.1',
			'libqt4-sql-x86': '4.6.3-5.12.1',
			'libqt4-x11': '4.6.3-5.12.1',
			'libqt4-x11-32bit': '4.6.3-5.12.1',
			'libqt4-x11-x86': '4.6.3-5.12.1',
			'libqt4-x86': '4.6.3-5.12.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

