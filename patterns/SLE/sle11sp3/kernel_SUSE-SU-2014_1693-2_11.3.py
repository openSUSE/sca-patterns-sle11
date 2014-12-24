#!/usr/bin/python
#
# Title:       Important Security Announcement for kernel SUSE-SU-2014:1693-2
# Description: Security fixes for SUSE Linux Enterprise 11 SP3
# Source:      Security Announcement Parser v1.1.8
# Modified:    2014 Dec 24
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
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-12/msg00033.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:1693-2'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'cluster-network-kmp-default': '1.4_3.0.101_0.42-2.27.115',
			'cluster-network-kmp-ppc64': '1.4_3.0.101_0.42-2.27.115',
			'cluster-network-kmp-trace': '1.4_3.0.101_0.42-2.27.115',
			'gfs2-kmp-default': '2_3.0.101_0.42-0.16.121',
			'gfs2-kmp-ppc64': '2_3.0.101_0.42-0.16.121',
			'gfs2-kmp-trace': '2_3.0.101_0.42-0.16.121',
			'kernel-default': '3.0.101-0.42.1',
			'kernel-default-base': '3.0.101-0.42.1',
			'kernel-default-devel': '3.0.101-0.42.1',
			'kernel-default-man': '3.0.101-0.42.1',
			'kernel-ppc64': '3.0.101-0.42.1',
			'kernel-ppc64-base': '3.0.101-0.42.1',
			'kernel-ppc64-devel': '3.0.101-0.42.1',
			'kernel-source': '3.0.101-0.42.1',
			'kernel-syms': '3.0.101-0.42.1',
			'kernel-trace': '3.0.101-0.42.1',
			'kernel-trace-base': '3.0.101-0.42.1',
			'kernel-trace-devel': '3.0.101-0.42.1',
			'ocfs2-kmp-default': '1.6_3.0.101_0.42-0.20.115',
			'ocfs2-kmp-ppc64': '1.6_3.0.101_0.42-0.20.115',
			'ocfs2-kmp-trace': '1.6_3.0.101_0.42-0.20.115',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

