#!/usr/bin/python3
#
# Title:       Critical Security Announcement for bash SUSE-SU-2014:1212-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP1 LTSS
# Source:      Security Announcement Parser v1.0.1
# Modified:    2014 Sep 25
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
META_COMPONENT = "bash"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7015702|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=896776|META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-09/msg00028.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'bash'
MAIN = ''
SEVERITY = 'Critical'
TAG = 'SUSE-SU-2014:1212-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'libreadline5': '5.2-147.14.20.1',
			'libreadline5-32bit': '5.2-147.14.20.1',
			'readline-doc': '5.2-147.14.20.1',
			'bash': '3.2-147.14.20.1',
			'bash-doc': '3.2-147.14.20.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

