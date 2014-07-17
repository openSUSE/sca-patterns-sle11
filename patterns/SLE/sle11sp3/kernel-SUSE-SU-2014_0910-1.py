#!/usr/bin/python

# Title:       Kernel SA Important SUSE-SU-2014:0910-1
# Description: solves 29 vulnerabilities and has 76 fixes, SUSE-SU-2014:0910-1, SUSE-SU-2014:0911-1, SUSE-SU-2014:0912-1
# Modified:    2014 Jul 17
#
##############################################################################
# Copyright (C) 2014
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
#   Jason Record
#
##############################################################################

##############################################################################
# Module Definition
##############################################################################

import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "Kernel"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-07/msg00014.html"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Main Program Execution
##############################################################################

LTSS = False
NAME = 'Kernel'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:0910-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11 ):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
		'cluster-network-kmp-default': '1.4_3.0.101_0.35-2.27.78',
		'cluster-network-kmp-pae': '1.4_3.0.101_0.35-2.27.78',
		'cluster-network-kmp-ppc64': '1.4_3.0.101_0.35-2.27.78',
		'cluster-network-kmp-trace': '1.4_3.0.101_0.35-2.27.78',
		'cluster-network-kmp-xen': '1.4_3.0.101_0.35-2.27.78',
		'gfs2-kmp-default-2_3.0.101_0.35': '0.16.84',
		'gfs2-kmp-pae-2_3.0.101_0.35': '0.16.84',
		'gfs2-kmp-ppc64-2_3.0.101_0.35': '0.16.84',
		'gfs2-kmp-trace-2_3.0.101_0.35': '0.16.84',
		'gfs2-kmp-xen-2_3.0.101_0.35': '0.16.84',
		'kernel-default': '3.0.101-0.35.1',
		'kernel-default-base': '3.0.101-0.35.1',
		'kernel-default-devel': '3.0.101-0.35.1',
		'kernel-default-extra': '3.0.101-0.35.1',
		'kernel-default-man': '3.0.101-0.35.1',
		'kernel-ec2': '3.0.101-0.35.1',
		'kernel-ec2-base': '3.0.101-0.35.1',
		'kernel-ec2-devel': '3.0.101-0.35.1',
		'kernel-pae': '3.0.101-0.35.1',
		'kernel-pae-base': '3.0.101-0.35.1',
		'kernel-pae-devel': '3.0.101-0.35.1',
		'kernel-pae-extra': '3.0.101-0.35.1',
		'kernel-ppc64': '3.0.101-0.35.1',
		'kernel-ppc64-base': '3.0.101-0.35.1',
		'kernel-ppc64-devel': '3.0.101-0.35.1',
		'kernel-ppc64-extra': '3.0.101-0.35.1',
		'kernel-source': '3.0.101-0.35.1',
		'kernel-syms': '3.0.101-0.35.1',
		'kernel-trace': '3.0.101-0.35.1',
		'kernel-trace-base': '3.0.101-0.35.1',
		'kernel-trace-devel': '3.0.101-0.35.1',
		'kernel-xen': '3.0.101-0.35.1',
		'kernel-xen-base': '3.0.101-0.35.1',
		'kernel-xen-devel': '3.0.101-0.35.1',
		'kernel-xen-extra': '3.0.101-0.35.1',
		'ocfs2-kmp-default': '1.6_3.0.101_0.35-0.20.78',
		'ocfs2-kmp-pae': '1.6_3.0.101_0.35-0.20.78',
		'ocfs2-kmp-ppc64': '1.6_3.0.101_0.35-0.20.78',
		'ocfs2-kmp-trace': '1.6_3.0.101_0.35-0.20.78',
		'ocfs2-kmp-xen': '1.6_3.0.101_0.35-0.20.78',
		'xen-kmp-default': '4.2.4_02_3.0.101_0.35-0.7.45',
		'xen-kmp-pae': '4.2.4_02_3.0.101_0.35-0.7.45',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")

Core.printPatternResults()


