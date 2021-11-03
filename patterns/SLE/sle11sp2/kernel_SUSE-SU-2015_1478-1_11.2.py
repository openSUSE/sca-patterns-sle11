#!/usr/bin/python3
#
# Title:       Important Security Announcement for Kernel SUSE-SU-2015:1478-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP2
# Source:      Security Announcement Parser v1.3.0
# Modified:    2015 Sep 17
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
META_COMPONENT = "Kernel"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2015-09/msg00004.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'Kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2015:1478-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'kernel-default': '3.0.101-0.7.37.1',
			'kernel-default-base': '3.0.101-0.7.37.1',
			'kernel-default-debuginfo': '3.0.101-0.7.37.1',
			'kernel-default-debugsource': '3.0.101-0.7.37.1',
			'kernel-default-devel': '3.0.101-0.7.37.1',
			'kernel-default-devel-debuginfo': '3.0.101-0.7.37.1',
			'kernel-default-man': '3.0.101-0.7.37.1',
			'kernel-ec2': '3.0.101-0.7.37.1',
			'kernel-ec2-base': '3.0.101-0.7.37.1',
			'kernel-ec2-debuginfo': '3.0.101-0.7.37.1',
			'kernel-ec2-debugsource': '3.0.101-0.7.37.1',
			'kernel-ec2-devel': '3.0.101-0.7.37.1',
			'kernel-pae': '3.0.101-0.7.37.1',
			'kernel-pae-base': '3.0.101-0.7.37.1',
			'kernel-pae-debuginfo': '3.0.101-0.7.37.1',
			'kernel-pae-debugsource': '3.0.101-0.7.37.1',
			'kernel-pae-devel': '3.0.101-0.7.37.1',
			'kernel-pae-devel-debuginfo': '3.0.101-0.7.37.1',
			'kernel-source': '3.0.101-0.7.37.1',
			'kernel-syms': '3.0.101-0.7.37.1',
			'kernel-trace': '3.0.101-0.7.37.1',
			'kernel-trace-base': '3.0.101-0.7.37.1',
			'kernel-trace-debuginfo': '3.0.101-0.7.37.1',
			'kernel-trace-debugsource': '3.0.101-0.7.37.1',
			'kernel-trace-devel': '3.0.101-0.7.37.1',
			'kernel-trace-devel-debuginfo': '3.0.101-0.7.37.1',
			'kernel-xen': '3.0.101-0.7.37.1',
			'kernel-xen-base': '3.0.101-0.7.37.1',
			'kernel-xen-debuginfo': '3.0.101-0.7.37.1',
			'kernel-xen-debugsource': '3.0.101-0.7.37.1',
			'kernel-xen-devel': '3.0.101-0.7.37.1',
			'kernel-xen-devel-debuginfo': '3.0.101-0.7.37.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

