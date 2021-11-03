#!/usr/bin/python3
#
# Title:       Important Security Announcement for kernel-rt SUSE-SU-2014:0909-1
# Description: Security fixes for SUSE Linux Enterprise Real Time Kernel 11 SP3
# Source:      Security Announcement Parser v1.2.0
# Modified:    2015 Jan 26
#
##############################################################################
# Copyright (C) 2015 SUSE LLC
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
META_COMPONENT = "kernel-rt"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-07/msg00013.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kernel-rt'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:0909-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'cluster-network-kmp-rt': '1.4_3.0.101_rt130_0.24-2.27.79',
			'cluster-network-kmp-rt_trace': '1.4_3.0.101_rt130_0.24-2.27.79',
			'drbd-kmp-rt': '8.4.4_3.0.101_rt130_0.24-0.22.45',
			'drbd-kmp-rt_trace': '8.4.4_3.0.101_rt130_0.24-0.22.45',
			'iscsitarget-kmp-rt': '1.4.20_3.0.101_rt130_0.24-0.38.64',
			'iscsitarget-kmp-rt_trace': '1.4.20_3.0.101_rt130_0.24-0.38.64',
			'kernel-rt': '3.0.101.rt130-0.24.1',
			'kernel-rt-base': '3.0.101.rt130-0.24.1',
			'kernel-rt-devel': '3.0.101.rt130-0.24.1',
			'kernel-rt_trace': '3.0.101.rt130-0.24.1',
			'kernel-rt_trace-base': '3.0.101.rt130-0.24.1',
			'kernel-rt_trace-devel': '3.0.101.rt130-0.24.1',
			'kernel-source-rt': '3.0.101.rt130-0.24.1',
			'kernel-syms-rt': '3.0.101.rt130-0.24.1',
			'lttng-modules-kmp-rt': '2.1.1_3.0.101_rt130_0.24-0.11.57',
			'lttng-modules-kmp-rt_trace': '2.1.1_3.0.101_rt130_0.24-0.11.57',
			'ocfs2-kmp-rt': '1.6_3.0.101_rt130_0.24-0.20.79',
			'ocfs2-kmp-rt_trace': '1.6_3.0.101_rt130_0.24-0.20.79',
			'ofed-kmp-rt': '1.5.4.1_3.0.101_rt130_0.24-0.13.70',
			'ofed-kmp-rt_trace': '1.5.4.1_3.0.101_rt130_0.24-0.13.70',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

