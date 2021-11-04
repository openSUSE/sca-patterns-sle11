#!/usr/bin/python3
#
# Title:       Important Security Announcement for MySQL SUSE-SU-2014:1072-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP3
# Source:      Security Announcement Parser v1.0.1
# Modified:    2014 Sep 09
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
META_COMPONENT = "MySQL"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-08/msg00012.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'MySQL'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:1072-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'libmysqlclient_r15-x86': '5.0.96-0.6.13',
			'mysql-tools': '5.5.39-0.7.1',
			'libmysql55client_r18-32bit': '5.5.39-0.7.1',
			'libmysql55client18-x86': '5.5.39-0.7.1',
			'mysql': '5.5.39-0.7.1',
			'mysql-client': '5.5.39-0.7.1',
			'libmysqlclient15': '5.0.96-0.6.13',
			'libmysqlclient15-x86': '5.0.96-0.6.13',
			'libmysqlclient_r15-32bit': '5.0.96-0.6.13',
			'libmysql55client18': '5.5.39-0.7.1',
			'libmysql55client_r18': '5.5.39-0.7.1',
			'libmysql55client_r18-x86': '5.5.39-0.7.1',
			'libmysql55client18-32bit': '5.5.39-0.7.1',
			'libmysqlclient_r15': '5.0.96-0.6.13',
			'libmysqlclient15-32bit': '5.0.96-0.6.13',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

