#!/usr/bin/python3
#
# Title:       Important Security Announcement for kernel SUSE-SU-2014:1319-1
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
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-10/msg00007.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:1319-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'kernel-syms-rt': '3.0.101.rt130-0.28.1',
			'ocfs2-kmp-rt': '1.6_3.0.101_rt130_0.28-0.20.99',
			'ofed-kmp-rt': '1.5.4.1_3.0.101_rt130_0.28-0.13.90',
			'kernel-pae-devel': '3.0.101-0.40.1',
			'drbd-kmp-rt_trace': '8.4.4_3.0.101_rt130_0.28-0.22.65',
			'kernel-xen-devel': '3.0.101-0.40.1',
			'cluster-network-kmp-rt': '1.4_3.0.101_rt130_0.28-2.27.99',
			'kernel-source': '3.0.101-0.40.1',
			'ocfs2-kmp-xen': '1.6_3.0.101_0.40-0.20.98',
			'iscsitarget-kmp-rt': '1.4.20_3.0.101_rt130_0.28-0.38.84',
			'ofed-kmp-rt_trace': '1.5.4.1_3.0.101_rt130_0.28-0.13.90',
			'kernel-default-man': '3.0.101-0.40.1',
			'gfs2-kmp-default': '2_3.0.101_0.40-0.16.104',
			'gfs2-kmp-trace': '2_3.0.101_0.40-0.16.104',
			'cluster-network-kmp-xen': '1.4_3.0.101_0.40-2.27.98',
			'kernel-trace': '3.0.101-0.40.1',
			'xen-kmp-pae': '4.2.4_04_3.0.101_0.40-0.7.3',
			'kernel-default': '3.0.101-0.40.1',
			'kernel-ec2-base': '3.0.101-0.40.1',
			'kernel-ppc64-base': '3.0.101-0.40.1',
			'cluster-network-kmp-trace': '1.4_3.0.101_0.40-2.27.98',
			'gfs2-kmp-pae': '2_3.0.101_0.40-0.16.104',
			'kernel-rt': '3.0.101.rt130-0.28.1',
			'kernel-ec2': '3.0.101-0.40.1',
			'ocfs2-kmp-default': '1.6_3.0.101_0.40-0.20.98',
			'kernel-default-devel': '3.0.101-0.40.1',
			'ocfs2-kmp-ppc64': '1.6_3.0.101_0.40-0.20.98',
			'kernel-xen-extra': '3.0.101-0.40.1',
			'cluster-network-kmp-pae': '1.4_3.0.101_0.40-2.27.98',
			'gfs2-kmp-ppc64': '2_3.0.101_0.40-0.16.104',
			'kernel-default-base': '3.0.101-0.40.1',
			'kernel-ppc64': '3.0.101-0.40.1',
			'kernel-source-rt': '3.0.101.rt130-0.28.1',
			'kernel-syms': '3.0.101-0.40.1',
			'kernel-rt_trace-base': '3.0.101.rt130-0.28.1',
			'gfs2-kmp-xen': '2_3.0.101_0.40-0.16.104',
			'cluster-network-kmp-ppc64': '1.4_3.0.101_0.40-2.27.98',
			'ocfs2-kmp-rt_trace': '1.6_3.0.101_rt130_0.28-0.20.99',
			'kernel-default-extra': '3.0.101-0.40.1',
			'ocfs2-kmp-trace': '1.6_3.0.101_0.40-0.20.98',
			'kernel-xen-base': '3.0.101-0.40.1',
			'iscsitarget-kmp-rt_trace': '1.4.20_3.0.101_rt130_0.28-0.38.84',
			'kernel-trace-devel': '3.0.101-0.40.1',
			'kernel-rt_trace': '3.0.101.rt130-0.28.1',
			'kernel-rt_trace-devel': '3.0.101.rt130-0.28.1',
			'xen-kmp-default': '4.2.4_04_3.0.101_0.40-0.7.3',
			'kernel-xen': '3.0.101-0.40.1',
			'kernel-rt-devel': '3.0.101.rt130-0.28.1',
			'lttng-modules-kmp-rt': '2.1.1_3.0.101_rt130_0.28-0.11.75',
			'kernel-pae-base': '3.0.101-0.40.1',
			'kernel-trace-base': '3.0.101-0.40.1',
			'kernel-ec2-devel': '3.0.101-0.40.1',
			'kernel-rt-base': '3.0.101.rt130-0.28.1',
			'lttng-modules-kmp-rt_trace': '2.1.1_3.0.101_rt130_0.28-0.11.75',
			'drbd-kmp-rt': '8.4.4_3.0.101_rt130_0.28-0.22.65',
			'kernel-ppc64-devel': '3.0.101-0.40.1',
			'ocfs2-kmp-pae': '1.6_3.0.101_0.40-0.20.98',
			'cluster-network-kmp-default': '1.4_3.0.101_0.40-2.27.98',
			'kernel-pae': '3.0.101-0.40.1',
			'kernel-pae-extra': '3.0.101-0.40.1',
			'cluster-network-kmp-rt_trace': '1.4_3.0.101_rt130_0.28-2.27.99',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

