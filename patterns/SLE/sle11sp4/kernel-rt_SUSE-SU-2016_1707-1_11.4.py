#!/usr/bin/python
#
# Title:       Important Security Announcement for Kernel-rt SUSE-SU-2016:1707-1
# Description: Security fixes for SUSE Linux Enterprise Real Time Kernel 11 SP4
# Source:      Security Announcement Parser v1.3.1
# Modified:    2016 Jul 05
#
##############################################################################
# Copyright (C) 2016 SUSE LLC
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
META_COMPONENT = "Kernel-rt"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2016-06/msg00059.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'Kernel-rt'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2016:1707-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 4 ):
		PACKAGES = {
			'kernel-rt': '3.0.101.rt130-54.1',
			'kernel-rt-base': '3.0.101.rt130-54.1',
			'kernel-rt-debuginfo': '3.0.101.rt130-54.1',
			'kernel-rt-debugsource': '3.0.101.rt130-54.1',
			'kernel-rt-devel': '3.0.101.rt130-54.1',
			'kernel-rt_debug-debuginfo': '3.0.101.rt130-54.1',
			'kernel-rt_debug-debugsource': '3.0.101.rt130-54.1',
			'kernel-rt_trace': '3.0.101.rt130-54.1',
			'kernel-rt_trace-base': '3.0.101.rt130-54.1',
			'kernel-rt_trace-debuginfo': '3.0.101.rt130-54.1',
			'kernel-rt_trace-debugsource': '3.0.101.rt130-54.1',
			'kernel-rt_trace-devel': '3.0.101.rt130-54.1',
			'kernel-source-rt': '3.0.101.rt130-54.1',
			'kernel-syms-rt': '3.0.101.rt130-54.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

