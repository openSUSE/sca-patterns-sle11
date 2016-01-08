#!/usr/bin/python
#
# Title:       Important Security Announcement for samba SUSE-SU-2016:0032-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP2
# Source:      Security Announcement Parser v1.3.0
# Modified:    2016 Jan 08
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
META_COMPONENT = "samba"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2016-01/msg00002.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'samba'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2016:0032-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'ldapsmb': '1.34b-45.2',
			'libldb1': '3.6.3-45.2',
			'libsmbclient0': '3.6.3-45.2',
			'libsmbclient0-32bit': '3.6.3-45.2',
			'libtalloc2': '3.6.3-45.2',
			'libtalloc2-32bit': '3.6.3-45.2',
			'libtdb1': '3.6.3-45.2',
			'libtdb1-32bit': '3.6.3-45.2',
			'libtevent0': '3.6.3-45.2',
			'libtevent0-32bit': '3.6.3-45.2',
			'libwbclient0': '3.6.3-45.2',
			'libwbclient0-32bit': '3.6.3-45.2',
			'samba': '3.6.3-45.2',
			'samba-32bit': '3.6.3-45.2',
			'samba-client': '3.6.3-45.2',
			'samba-client-32bit': '3.6.3-45.2',
			'samba-debuginfo': '3.6.3-45.2',
			'samba-debuginfo-32bit': '3.6.3-45.2',
			'samba-debugsource': '3.6.3-45.2',
			'samba-doc': '3.6.3-45.2',
			'samba-krb-printing': '3.6.3-45.2',
			'samba-winbind': '3.6.3-45.2',
			'samba-winbind-32bit': '3.6.3-45.2',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

