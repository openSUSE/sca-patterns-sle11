#!/usr/bin/python3
#
# Title:       Important Security Announcement for kernel SUSE-SU-2015:0652-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP1 LTSS
# Source:      Security Announcement Parser v1.2.5
# Modified:    2015 Apr 02
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
META_COMPONENT = "kernel"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2015-04/msg00000.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2015:0652-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'kernel-default': '2.6.32.59-0.19.1',
			'kernel-default-base': '2.6.32.59-0.19.1',
			'kernel-default-devel': '2.6.32.59-0.19.1',
			'kernel-default-man': '2.6.32.59-0.19.1',
			'kernel-ec2': '2.6.32.59-0.19.1',
			'kernel-ec2-base': '2.6.32.59-0.19.1',
			'kernel-ec2-devel': '2.6.32.59-0.19.1',
			'kernel-pae': '2.6.32.59-0.19.1',
			'kernel-pae-base': '2.6.32.59-0.19.1',
			'kernel-pae-devel': '2.6.32.59-0.19.1',
			'kernel-source': '2.6.32.59-0.19.1',
			'kernel-syms': '2.6.32.59-0.19.1',
			'kernel-trace': '2.6.32.59-0.19.1',
			'kernel-trace-base': '2.6.32.59-0.19.1',
			'kernel-trace-devel': '2.6.32.59-0.19.1',
			'kernel-xen': '2.6.32.59-0.19.1',
			'kernel-xen-base': '2.6.32.59-0.19.1',
			'kernel-xen-devel': '2.6.32.59-0.19.1',
			'xen-kmp-default': '4.0.3_21548_18_2.6.32.59_0.19-0.9.17',
			'xen-kmp-pae': '4.0.3_21548_18_2.6.32.59_0.19-0.9.17',
			'xen-kmp-trace': '4.0.3_21548_18_2.6.32.59_0.19-0.9.17',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

