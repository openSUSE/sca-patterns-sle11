#!/usr/bin/python3
#
# Title:       Important Security Announcement for libvirt SUSE-SU-2012:1043-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP2
# Source:      Security Announcement Parser v1.1.7
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
META_COMPONENT = "libvirt"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2012-08/msg00024.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'libvirt'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2012:1043-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'libvirt': '0.9.6-0.21.3',
			'libvirt-client': '0.9.6-0.21.3',
			'libvirt-client-32bit': '0.9.6-0.21.3',
			'libvirt-devel': '0.9.6-0.21.3',
			'libvirt-devel-32bit': '0.9.6-0.21.3',
			'libvirt-doc': '0.9.6-0.21.3',
			'libvirt-python': '0.9.6-0.21.3',
			'virt-manager': '0.9.0-3.19.1',
			'vm-install': '0.5.10-0.5.1',
			'xen': '4.1.2_20-0.5.2',
			'xen-devel': '4.1.2_20-0.5.2',
			'xen-doc-html': '4.1.2_20-0.5.2',
			'xen-doc-pdf': '4.1.2_20-0.5.2',
			'xen-kmp-default': '4.1.2_20_3.0.38_0.5-0.5.2',
			'xen-kmp-trace': '4.1.2_20_3.0.38_0.5-0.5.2',
			'xen-libs': '4.1.2_20-0.5.2',
			'xen-libs-32bit': '4.1.2_20-0.5.2',
			'xen-tools': '4.1.2_20-0.5.2',
			'xen-tools-domU': '4.1.2_20-0.5.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

