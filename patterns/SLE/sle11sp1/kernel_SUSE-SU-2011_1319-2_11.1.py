#!/usr/bin/python
#
# Title:       Important Security Announcement for kernel SUSE-SU-2011:1319-2
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
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2011-12/msg00013.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2011:1319-2'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'btrfs-kmp-default': '0_2.6.32.49_0.3-0.3.66',
			'btrfs-kmp-pae': '0_2.6.32.49_0.3-0.3.66',
			'btrfs-kmp-xen': '0_2.6.32.49_0.3-0.3.66',
			'cluster-network-kmp-default': '1.4_2.6.32.49_0.3-2.5.18',
			'cluster-network-kmp-pae': '1.4_2.6.32.49_0.3-2.5.18',
			'cluster-network-kmp-trace': '1.4_2.6.32.49_0.3-2.5.18',
			'cluster-network-kmp-xen': '1.4_2.6.32.49_0.3-2.5.18',
			'ext4dev-kmp-default': '0_2.6.32.49_0.3-7.9.33',
			'ext4dev-kmp-pae': '0_2.6.32.49_0.3-7.9.33',
			'ext4dev-kmp-trace': '0_2.6.32.49_0.3-7.9.33',
			'ext4dev-kmp-xen': '0_2.6.32.49_0.3-7.9.33',
			'gfs2-kmp-default': '2_2.6.32.49_0.3-0.2.65',
			'gfs2-kmp-pae': '2_2.6.32.49_0.3-0.2.65',
			'gfs2-kmp-trace': '2_2.6.32.49_0.3-0.2.65',
			'gfs2-kmp-xen': '2_2.6.32.49_0.3-0.2.65',
			'hyper-v-kmp-default': '0_2.6.32.49_0.3-0.14.17',
			'hyper-v-kmp-pae': '0_2.6.32.49_0.3-0.14.17',
			'hyper-v-kmp-trace': '0_2.6.32.49_0.3-0.18.1',
			'kernel-default': '2.6.32.49-0.3.1',
			'kernel-default-base': '2.6.32.49-0.3.1',
			'kernel-default-devel': '2.6.32.49-0.3.1',
			'kernel-default-extra': '2.6.32.49-0.3.1',
			'kernel-default-man': '2.6.32.49-0.3.1',
			'kernel-desktop-devel': '2.6.32.49-0.3.1',
			'kernel-ec2': '2.6.32.49-0.3.1',
			'kernel-ec2-base': '2.6.32.49-0.3.1',
			'kernel-pae': '2.6.32.49-0.3.1',
			'kernel-pae-base': '2.6.32.49-0.3.1',
			'kernel-pae-devel': '2.6.32.49-0.3.1',
			'kernel-pae-extra': '2.6.32.49-0.3.1',
			'kernel-source': '2.6.32.49-0.3.1',
			'kernel-syms': '2.6.32.49-0.3.1',
			'kernel-trace': '2.6.32.49-0.3.1',
			'kernel-trace-base': '2.6.32.49-0.3.1',
			'kernel-trace-devel': '2.6.32.49-0.3.1',
			'kernel-xen': '2.6.32.49-0.3.1',
			'kernel-xen-base': '2.6.32.49-0.3.1',
			'kernel-xen-devel': '2.6.32.49-0.3.1',
			'kernel-xen-extra': '2.6.32.49-0.3.1',
			'ocfs2-kmp-default': '1.6_2.6.32.49_0.3-0.4.2.18',
			'ocfs2-kmp-pae': '1.6_2.6.32.49_0.3-0.4.2.18',
			'ocfs2-kmp-trace': '1.6_2.6.32.49_0.3-0.4.2.18',
			'ocfs2-kmp-xen': '1.6_2.6.32.49_0.3-0.4.2.18',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

