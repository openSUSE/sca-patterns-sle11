#!/usr/bin/python3
#
# Title:       Important Security Announcement for kernel SUSE-SU-2014:1316-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP3
# Source:      Security Announcement Parser v1.0.3
# Modified:    2014 Oct 27
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
META_COMPONENT = "kernel"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-10/msg00006.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:1316-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'kernel-bigsmp-base': '3.0.101-0.40.1',
			'cluster-network-kmp-bigsmp': '1.4_3.0.101_0.40-2.27.98',
			'kernel-bigsmp-devel': '3.0.101-0.40.1',
			'kernel-bigsmp': '3.0.101-0.40.1',
			'iscsitarget-kmp-bigsmp': '1.4.20_3.0.101_0.40-0.38.83',
			'ofed-kmp-bigsmp': '1.5.4.1_3.0.101_0.40-0.13.89',
			'oracleasm-kmp-bigsmp': '2.0.5_3.0.101_0.40-7.39.89',
			'drbd-kmp-bigsmp': '8.4.4_3.0.101_0.40-0.22.64',
			'gfs2-kmp-bigsmp': '2_3.0.101_0.40-0.16.104',
			'ocfs2-kmp-bigsmp': '1.6_3.0.101_0.40-0.20.98',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

