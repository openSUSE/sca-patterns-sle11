#!/usr/bin/python3
#
# Title:       Important Security Announcement for Kernel SUSE-SU-2014:1138-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP1 LTSS
# Source:      Security Announcement Parser v1.0.1
# Modified:    2014 Sep 23
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
META_COMPONENT = "Kernel"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-09/msg00023.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = True
NAME = 'Kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:1138-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 1 ):
		PACKAGES = {
			'xen-kmp-trace': '4.0.3_21548_16_2.6.32.59_0.15-0.5.26',
			'kernel-pae': '2.6.32.59-0.15.2',
			'kernel-default-man': '2.6.32.59-0.15.2',
			'kernel-pae-base': '2.6.32.59-0.15.2',
			'kernel-trace': '2.6.32.59-0.15.2',
			'xen-kmp-pae': '4.0.3_21548_16_2.6.32.59_0.15-0.5.26',
			'kernel-default': '2.6.32.59-0.15.2',
			'kernel-trace-base': '2.6.32.59-0.15.2',
			'kernel-syms': '2.6.32.59-0.15.2',
			'kernel-xen-base': '2.6.32.59-0.15.2',
			'kernel-xen-devel': '2.6.32.59-0.15.2',
			'kernel-source': '2.6.32.59-0.15.2',
			'kernel-trace-devel': '2.6.32.59-0.15.2',
			'kernel-default-devel': '2.6.32.59-0.15.2',
			'kernel-ec2-devel': '2.6.32.59-0.15.2',
			'kernel-pae-devel': '2.6.32.59-0.15.2',
			'kernel-ec2': '2.6.32.59-0.15.2',
			'kernel-ec2-base': '2.6.32.59-0.15.2',
			'kernel-xen': '2.6.32.59-0.15.2',
			'kernel-default-base': '2.6.32.59-0.15.2',
			'xen-kmp-default': '4.0.3_21548_16_2.6.32.59_0.15-0.5.26',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

