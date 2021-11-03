#!/usr/bin/python3
#
# Title:       Important Security Announcement for Samba SUSE-SU-2012:0575-1
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
META_COMPONENT = "Samba"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2012-04/msg00024.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'Samba'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2012:0575-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'cifs-mount': '3.4.3-1.40.3',
			'ldapsmb': '1.34b-11.28.40.3',
			'libnetapi-devel': '3.4.3-1.40.3',
			'libnetapi0': '3.4.3-1.40.3',
			'libsmbclient-devel': '3.4.3-1.40.3',
			'libsmbclient0': '3.4.3-1.40.3',
			'libsmbclient0-32bit': '3.4.3-1.40.3',
			'libsmbclient0-x86': '3.4.3-1.40.3',
			'libsmbsharemodes-devel': '3.4.3-1.40.3',
			'libsmbsharemodes0': '3.4.3-1.40.3',
			'libtalloc-devel': '3.4.3-1.40.3',
			'libtalloc1': '3.4.3-1.40.3',
			'libtalloc1-32bit': '3.4.3-1.40.3',
			'libtalloc1-x86': '3.4.3-1.40.3',
			'libtdb-devel': '3.4.3-1.40.3',
			'libtdb1': '3.4.3-1.40.3',
			'libtdb1-32bit': '3.4.3-1.40.3',
			'libtdb1-x86': '3.4.3-1.40.3',
			'libwbclient-devel': '3.4.3-1.40.3',
			'libwbclient0': '3.4.3-1.40.3',
			'libwbclient0-32bit': '3.4.3-1.40.3',
			'libwbclient0-x86': '3.4.3-1.40.3',
			'samba': '3.4.3-1.40.3',
			'samba-32bit': '3.4.3-1.40.3',
			'samba-client': '3.4.3-1.40.3',
			'samba-client-32bit': '3.4.3-1.40.3',
			'samba-client-x86': '3.4.3-1.40.3',
			'samba-devel': '3.4.3-1.40.3',
			'samba-doc': '3.4.3-1.40.3',
			'samba-krb-printing': '3.4.3-1.40.3',
			'samba-winbind': '3.4.3-1.40.3',
			'samba-winbind-32bit': '3.4.3-1.40.3',
			'samba-winbind-x86': '3.4.3-1.40.3',
			'samba-x86': '3.4.3-1.40.3',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

