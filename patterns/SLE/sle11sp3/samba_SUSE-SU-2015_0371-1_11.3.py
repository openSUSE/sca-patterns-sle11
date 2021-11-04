#!/usr/bin/python3
#
# Title:       Important Security Announcement for Samba SUSE-SU-2015:0371-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP3
# Source:      Security Announcement Parser v1.2.5
# Modified:    2015 Feb 26
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
META_COMPONENT = "Samba"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2015-02/msg00030.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'Samba'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2015:0371-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'ldapsmb': '1.34b-12.56.1',
			'libldb-devel': '3.6.3-0.56.1',
			'libldb1': '3.6.3-0.56.1',
			'libldb1-32bit': '3.6.3-0.56.1',
			'libnetapi-devel': '3.6.3-0.56.1',
			'libnetapi0': '3.6.3-0.56.1',
			'libsmbclient-devel': '3.6.3-0.56.1',
			'libsmbclient0': '3.6.3-0.56.1',
			'libsmbclient0-32bit': '3.6.3-0.56.1',
			'libsmbclient0-x86': '3.6.3-0.56.1',
			'libsmbsharemodes-devel': '3.6.3-0.56.1',
			'libsmbsharemodes0': '3.6.3-0.56.1',
			'libtalloc-devel': '3.6.3-0.56.1',
			'libtalloc2': '3.6.3-0.56.1',
			'libtalloc2-32bit': '3.6.3-0.56.1',
			'libtalloc2-x86': '3.6.3-0.56.1',
			'libtdb-devel': '3.6.3-0.56.1',
			'libtdb1': '3.6.3-0.56.1',
			'libtdb1-32bit': '3.6.3-0.56.1',
			'libtdb1-x86': '3.6.3-0.56.1',
			'libtevent-devel': '3.6.3-0.56.1',
			'libtevent0': '3.6.3-0.56.1',
			'libtevent0-32bit': '3.6.3-0.56.1',
			'libwbclient-devel': '3.6.3-0.56.1',
			'libwbclient0': '3.6.3-0.56.1',
			'libwbclient0-32bit': '3.6.3-0.56.1',
			'libwbclient0-x86': '3.6.3-0.56.1',
			'samba': '3.6.3-0.56.1',
			'samba-32bit': '3.6.3-0.56.1',
			'samba-client': '3.6.3-0.56.1',
			'samba-client-32bit': '3.6.3-0.56.1',
			'samba-client-x86': '3.6.3-0.56.1',
			'samba-devel': '3.6.3-0.56.1',
			'samba-doc': '3.6.3-0.56.1',
			'samba-krb-printing': '3.6.3-0.56.1',
			'samba-winbind': '3.6.3-0.56.1',
			'samba-winbind-32bit': '3.6.3-0.56.1',
			'samba-winbind-x86': '3.6.3-0.56.1',
			'samba-x86': '3.6.3-0.56.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

