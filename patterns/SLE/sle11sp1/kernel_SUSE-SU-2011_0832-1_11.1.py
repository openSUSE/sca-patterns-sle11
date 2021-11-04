#!/usr/bin/python3
#
# Title:       Important Security Announcement for kernel SUSE-SU-2011:0832-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP1
# Source:      Security Announcement Parser v1.1.8
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
META_COMPONENT = "kernel"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2011-07/msg00012.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2011:0832-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'btrfs-kmp-default': '0_2.6.32.43_0.4-0.3.50',
			'btrfs-kmp-pae': '0_2.6.32.43_0.4-0.3.50',
			'btrfs-kmp-xen': '0_2.6.32.43_0.4-0.3.50',
			'cluster-network-kmp-default': '1.4_2.6.32.43_0.4-2.5.1',
			'cluster-network-kmp-pae': '1.4_2.6.32.43_0.4-2.5.1',
			'cluster-network-kmp-ppc64': '1.4_2.6.32.43_0.4-2.5.1',
			'cluster-network-kmp-xen': '1.4_2.6.32.43_0.4-2.5.1',
			'ext4dev-kmp-default': '0_2.6.32.43_0.4-7.9.17',
			'ext4dev-kmp-pae': '0_2.6.32.43_0.4-7.9.17',
			'ext4dev-kmp-ppc64': '0_2.6.32.43_0.4-7.9.17',
			'ext4dev-kmp-xen': '0_2.6.32.43_0.4-7.9.17',
			'gfs2-kmp-default': '2_2.6.32.43_0.4-0.2.49',
			'gfs2-kmp-pae': '2_2.6.32.43_0.4-0.2.49',
			'gfs2-kmp-ppc64': '2_2.6.32.43_0.4-0.2.49',
			'gfs2-kmp-xen': '2_2.6.32.43_0.4-0.2.49',
			'hyper-v-kmp-default': '0_2.6.32.43_0.4-0.14.8',
			'hyper-v-kmp-pae': '0_2.6.32.43_0.4-0.14.8',
			'kernel-default': '2.6.32.43-0.4.1',
			'kernel-default-base': '2.6.32.43-0.4.1',
			'kernel-default-devel': '2.6.32.43-0.4.1',
			'kernel-default-extra': '2.6.32.43-0.4.1',
			'kernel-default-man': '2.6.32.43-0.4.1',
			'kernel-desktop-devel': '2.6.32.43-0.4.1',
			'kernel-ec2': '2.6.32.43-0.4.1',
			'kernel-ec2-base': '2.6.32.43-0.4.1',
			'kernel-pae': '2.6.32.43-0.4.1',
			'kernel-pae-base': '2.6.32.43-0.4.1',
			'kernel-pae-devel': '2.6.32.43-0.4.1',
			'kernel-pae-extra': '2.6.32.43-0.4.1',
			'kernel-ppc64': '2.6.32.43-0.4.1',
			'kernel-ppc64-base': '2.6.32.43-0.4.1',
			'kernel-ppc64-devel': '2.6.32.43-0.4.1',
			'kernel-source': '2.6.32.43-0.4.1',
			'kernel-syms': '2.6.32.43-0.4.1',
			'kernel-trace': '2.6.32.43-0.4.1',
			'kernel-trace-base': '2.6.32.43-0.4.1',
			'kernel-trace-devel': '2.6.32.43-0.4.1',
			'kernel-xen': '2.6.32.43-0.4.1',
			'kernel-xen-base': '2.6.32.43-0.4.1',
			'kernel-xen-devel': '2.6.32.43-0.4.1',
			'kernel-xen-extra': '2.6.32.43-0.4.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

