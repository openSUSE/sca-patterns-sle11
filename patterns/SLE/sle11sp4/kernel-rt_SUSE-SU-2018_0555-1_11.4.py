#!/usr/bin/python3
#
# Title:       Important Security Announcement for Kernel-rt SUSE-SU-2018:0555-1
# Description: Security fixes for SUSE Linux Enterprise Real Time Kernel 11 SP4
# Source:      Security Announcement Parser v1.3.7
# Modified:    2018 May 02
#
##############################################################################
# Copyright (C) 2018 SUSE LLC
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
META_COMPONENT = "Kernel-rt"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=https://lists.opensuse.org/opensuse-security-announce/2018-02/msg00047.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'Kernel-rt'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2018:0555-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'cluster-network-kmp-bigmem': '1.4_3.0.101_108.35-2.32.4.6',
			'cluster-network-kmp-default': '1.4_3.0.101_108.35-2.32.4.6',
			'cluster-network-kmp-pae': '1.4_3.0.101_108.35-2.32.4.6',
			'cluster-network-kmp-ppc64': '1.4_3.0.101_108.35-2.32.4.6',
			'cluster-network-kmp-rt': '1.4_3.0.101_rt130_69.14-2.32.4.6',
			'cluster-network-kmp-rt_trace': '1.4_3.0.101_rt130_69.14-2.32.4.6',
			'cluster-network-kmp-trace': '1.4_3.0.101_108.35-2.32.4.6',
			'cluster-network-kmp-xen': '1.4_3.0.101_108.35-2.32.4.6',
			'drbd': '8.4.4-0.27.4.2',
			'drbd-bash-completion': '8.4.4-0.27.4.2',
			'drbd-debuginfo': '8.4.4-0.27.4.2',
			'drbd-debugsource': '8.4.4-0.27.4.2',
			'drbd-heartbeat': '8.4.4-0.27.4.2',
			'drbd-kmp-bigmem': '8.4.4_3.0.101_108.35-0.27.4.6',
			'drbd-kmp-default': '8.4.4_3.0.101_108.35-0.27.4.6',
			'drbd-kmp-pae': '8.4.4_3.0.101_108.35-0.27.4.6',
			'drbd-kmp-ppc64': '8.4.4_3.0.101_108.35-0.27.4.6',
			'drbd-kmp-rt': '8.4.4_3.0.101_rt130_69.14-0.27.4.6',
			'drbd-kmp-rt_trace': '8.4.4_3.0.101_rt130_69.14-0.27.4.6',
			'drbd-kmp-trace': '8.4.4_3.0.101_108.35-0.27.4.6',
			'drbd-kmp-xen': '8.4.4_3.0.101_108.35-0.27.4.6',
			'drbd-pacemaker': '8.4.4-0.27.4.2',
			'drbd-udev': '8.4.4-0.27.4.2',
			'drbd-utils': '8.4.4-0.27.4.2',
			'drbd-xen': '8.4.4-0.27.4.2',
			'gfs2-kmp-bigmem': '2_3.0.101_108.35-0.24.4.6',
			'gfs2-kmp-default': '2_3.0.101_108.35-0.24.4.6',
			'gfs2-kmp-pae': '2_3.0.101_108.35-0.24.4.6',
			'gfs2-kmp-ppc64': '2_3.0.101_108.35-0.24.4.6',
			'gfs2-kmp-rt': '2_3.0.101_rt130_69.14-0.24.4.6',
			'gfs2-kmp-rt_trace': '2_3.0.101_rt130_69.14-0.24.4.6',
			'gfs2-kmp-trace': '2_3.0.101_108.35-0.24.4.6',
			'gfs2-kmp-xen': '2_3.0.101_108.35-0.24.4.6',
			'kernel-bigmem': '3.0.101-108.35.1',
			'kernel-bigmem-base': '3.0.101-108.35.1',
			'kernel-bigmem-debuginfo': '3.0.101-108.35.1',
			'kernel-bigmem-debugsource': '3.0.101-108.35.1',
			'kernel-bigmem-devel': '3.0.101-108.35.1',
			'kernel-default': '3.0.101-108.35.1',
			'kernel-default-base': '3.0.101-108.35.1',
			'kernel-default-debuginfo': '3.0.101-108.35.1',
			'kernel-default-debugsource': '3.0.101-108.35.1',
			'kernel-default-devel': '3.0.101-108.35.1',
			'kernel-default-devel-debuginfo': '3.0.101-108.35.1',
			'kernel-default-man': '3.0.101-108.35.1',
			'kernel-docs': '3.0.101-108.35.1',
			'kernel-ec2': '3.0.101-108.35.1',
			'kernel-ec2-base': '3.0.101-108.35.1',
			'kernel-ec2-debuginfo': '3.0.101-108.35.1',
			'kernel-ec2-debugsource': '3.0.101-108.35.1',
			'kernel-ec2-devel': '3.0.101-108.35.1',
			'kernel-pae': '3.0.101-108.35.1',
			'kernel-pae-base': '3.0.101-108.35.1',
			'kernel-pae-debuginfo': '3.0.101-108.35.1',
			'kernel-pae-debugsource': '3.0.101-108.35.1',
			'kernel-pae-devel': '3.0.101-108.35.1',
			'kernel-pae-devel-debuginfo': '3.0.101-108.35.1',
			'kernel-ppc64': '3.0.101-108.35.1',
			'kernel-ppc64-base': '3.0.101-108.35.1',
			'kernel-ppc64-debuginfo': '3.0.101-108.35.1',
			'kernel-ppc64-debugsource': '3.0.101-108.35.1',
			'kernel-ppc64-devel': '3.0.101-108.35.1',
			'kernel-source': '3.0.101-108.35.1',
			'kernel-syms': '3.0.101-108.35.1',
			'kernel-trace': '3.0.101-108.35.1',
			'kernel-trace-base': '3.0.101-108.35.1',
			'kernel-trace-debuginfo': '3.0.101-108.35.1',
			'kernel-trace-debugsource': '3.0.101-108.35.1',
			'kernel-trace-devel': '3.0.101-108.35.1',
			'kernel-trace-devel-debuginfo': '3.0.101-108.35.1',
			'kernel-xen': '3.0.101-108.35.1',
			'kernel-xen-base': '3.0.101-108.35.1',
			'kernel-xen-debuginfo': '3.0.101-108.35.1',
			'kernel-xen-debugsource': '3.0.101-108.35.1',
			'kernel-xen-devel': '3.0.101-108.35.1',
			'kernel-xen-devel-debuginfo': '3.0.101-108.35.1',
			'ocfs2-kmp-bigmem': '1.6_3.0.101_108.35-0.28.5.6',
			'ocfs2-kmp-default': '1.6_3.0.101_108.35-0.28.5.6',
			'ocfs2-kmp-pae': '1.6_3.0.101_108.35-0.28.5.6',
			'ocfs2-kmp-ppc64': '1.6_3.0.101_108.35-0.28.5.6',
			'ocfs2-kmp-rt': '1.6_3.0.101_rt130_69.14-0.28.5.6',
			'ocfs2-kmp-rt_trace': '1.6_3.0.101_rt130_69.14-0.28.5.6',
			'ocfs2-kmp-trace': '1.6_3.0.101_108.35-0.28.5.6',
			'ocfs2-kmp-xen': '1.6_3.0.101_108.35-0.28.5.6',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

