#!/usr/bin/python
#
# Title:       Important Security Announcement for kernel SUSE-SU-2013:0786-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP2
# Source:      Security Announcement Parser v1.1.6
# Modified:    2014 Dec 04
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
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-05/msg00002.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2013:0786-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'kernel-syms-rt': '3.0.74.rt98-0.6.2.1',
			'kernel-source-rt': '3.0.74.rt98-0.6.2.1',
			'ocfs2-kmp-rt': '1.6_3.0.74_rt98_0.6.2-0.11.36',
			'lttng-modules-kmp-rt': '2.0.4_3.0.74_rt98_0.6.2-0.7.30',
			'drbd-kmp-rt': '8.4.2_3.0.74_rt98_0.6.2-0.6.6.28',
			'drbd-kmp-rt_trace': '8.4.2_3.0.74_rt98_0.6.2-0.6.6.28',
			'ocfs2-kmp-rt_trace': '1.6_3.0.74_rt98_0.6.2-0.11.36',
			'kernel-rt_trace-base': '3.0.74.rt98-0.6.2.1',
			'lttng-modules-kmp-rt_trace': '2.0.4_3.0.74_rt98_0.6.2-0.7.30',
			'cluster-network-kmp-rt': '1.4_3.0.74_rt98_0.6.2-2.18.37',
			'kernel-rt-base': '3.0.74.rt98-0.6.2.1',
			'kernel-rt': '3.0.74.rt98-0.6.2.1',
			'iscsitarget-kmp-rt_trace': '1.4.20_3.0.74_rt98_0.6.2-0.23.34',
			'ofed-kmp-rt_trace': '1.5.2_3.0.74_rt98_0.6.2-0.28.28.8',
			'kernel-rt_trace': '3.0.74.rt98-0.6.2.1',
			'kernel-rt_trace-devel': '3.0.74.rt98-0.6.2.1',
			'iscsitarget-kmp-rt': '1.4.20_3.0.74_rt98_0.6.2-0.23.34',
			'kernel-rt-devel': '3.0.74.rt98-0.6.2.1',
			'cluster-network-kmp-rt_trace': '1.4_3.0.74_rt98_0.6.2-2.18.37',
			'ofed-kmp-rt': '1.5.2_3.0.74_rt98_0.6.2-0.28.28.8',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

