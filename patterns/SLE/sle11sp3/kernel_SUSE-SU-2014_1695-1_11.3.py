#!/usr/bin/python3
#
# Title:       Important Security Announcement for kernel SUSE-SU-2014:1695-1
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
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-12/msg00029.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:1695-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'cluster-network-kmp-bigsmp': '1.4_3.0.101_0.46-2.27.120',
			'cluster-network-kmp-default': '1.4_3.0.101_0.46-2.27.120',
			'cluster-network-kmp-trace': '1.4_3.0.101_0.46-2.27.120',
			'cluster-network-kmp-xen': '1.4_3.0.101_0.46-2.27.120',
			'gfs2-kmp-bigsmp': '2_3.0.101_0.46-0.16.126',
			'gfs2-kmp-default': '2_3.0.101_0.46-0.16.126',
			'gfs2-kmp-trace': '2_3.0.101_0.46-0.16.126',
			'gfs2-kmp-xen': '2_3.0.101_0.46-0.16.126',
			'kernel-bigsmp': '3.0.101-0.46.1',
			'kernel-bigsmp-base': '3.0.101-0.46.1',
			'kernel-bigsmp-devel': '3.0.101-0.46.1',
			'kernel-default': '3.0.101-0.46.1',
			'kernel-default-base': '3.0.101-0.46.1',
			'kernel-default-devel': '3.0.101-0.46.1',
			'kernel-default-extra': '3.0.101-0.46.1',
			'kernel-ec2': '3.0.101-0.46.1',
			'kernel-ec2-base': '3.0.101-0.46.1',
			'kernel-ec2-devel': '3.0.101-0.46.1',
			'kernel-source': '3.0.101-0.46.1',
			'kernel-syms': '3.0.101-0.46.1',
			'kernel-trace': '3.0.101-0.46.1',
			'kernel-trace-base': '3.0.101-0.46.1',
			'kernel-trace-devel': '3.0.101-0.46.1',
			'kernel-xen': '3.0.101-0.46.1',
			'kernel-xen-base': '3.0.101-0.46.1',
			'kernel-xen-devel': '3.0.101-0.46.1',
			'kernel-xen-extra': '3.0.101-0.46.1',
			'ocfs2-kmp-bigsmp': '1.6_3.0.101_0.46-0.20.120',
			'ocfs2-kmp-default': '1.6_3.0.101_0.46-0.20.120',
			'ocfs2-kmp-trace': '1.6_3.0.101_0.46-0.20.120',
			'ocfs2-kmp-xen': '1.6_3.0.101_0.46-0.20.120',
			'xen-kmp-default': '4.2.5_02_3.0.101_0.46-0.7.9',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

