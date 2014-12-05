#!/usr/bin/python
#
# Title:       Important Security Announcement for PHP5 SUSE-SU-2012:0721-1
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
META_COMPONENT = "PHP5"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2012-06/msg00004.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'PHP5'
MAIN = ''
SEVERITY = 'Important'
TAG = 'SUSE-SU-2012:0721-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 2 ):
		PACKAGES = {
			'apache2-mod_php5': '5.2.14-0.7.30.40.1',
			'php5': '5.2.14-0.7.30.40.1',
			'php5-bcmath': '5.2.14-0.7.30.40.1',
			'php5-bz2': '5.2.14-0.7.30.40.1',
			'php5-calendar': '5.2.14-0.7.30.40.1',
			'php5-ctype': '5.2.14-0.7.30.40.1',
			'php5-curl': '5.2.14-0.7.30.40.1',
			'php5-dba': '5.2.14-0.7.30.40.1',
			'php5-dbase': '5.2.14-0.7.30.40.1',
			'php5-devel': '5.2.14-0.7.30.40.1',
			'php5-dom': '5.2.14-0.7.30.40.1',
			'php5-exif': '5.2.14-0.7.30.40.1',
			'php5-fastcgi': '5.2.14-0.7.30.40.1',
			'php5-ftp': '5.2.14-0.7.30.40.1',
			'php5-gd': '5.2.14-0.7.30.40.1',
			'php5-gettext': '5.2.14-0.7.30.40.1',
			'php5-gmp': '5.2.14-0.7.30.40.1',
			'php5-hash': '5.2.14-0.7.30.40.1',
			'php5-iconv': '5.2.14-0.7.30.40.1',
			'php5-imap': '5.2.14-0.7.30.40.1',
			'php5-json': '5.2.14-0.7.30.40.1',
			'php5-ldap': '5.2.14-0.7.30.40.1',
			'php5-mbstring': '5.2.14-0.7.30.40.1',
			'php5-mcrypt': '5.2.14-0.7.30.40.1',
			'php5-mysql': '5.2.14-0.7.30.40.1',
			'php5-ncurses': '5.2.14-0.7.30.40.1',
			'php5-odbc': '5.2.14-0.7.30.40.1',
			'php5-openssl': '5.2.14-0.7.30.40.1',
			'php5-pcntl': '5.2.14-0.7.30.40.1',
			'php5-pdo': '5.2.14-0.7.30.40.1',
			'php5-pear': '5.2.14-0.7.30.40.1',
			'php5-pgsql': '5.2.14-0.7.30.40.1',
			'php5-posix': '5.2.14-0.7.30.40.1',
			'php5-pspell': '5.2.14-0.7.30.40.1',
			'php5-readline': '5.2.14-0.7.30.40.1',
			'php5-shmop': '5.2.14-0.7.30.40.1',
			'php5-snmp': '5.2.14-0.7.30.40.1',
			'php5-soap': '5.2.14-0.7.30.40.1',
			'php5-sockets': '5.2.14-0.7.30.40.1',
			'php5-sqlite': '5.2.14-0.7.30.40.1',
			'php5-suhosin': '5.2.14-0.7.30.40.1',
			'php5-sysvmsg': '5.2.14-0.7.30.40.1',
			'php5-sysvsem': '5.2.14-0.7.30.40.1',
			'php5-sysvshm': '5.2.14-0.7.30.40.1',
			'php5-tidy': '5.2.14-0.7.30.40.1',
			'php5-tokenizer': '5.2.14-0.7.30.40.1',
			'php5-wddx': '5.2.14-0.7.30.40.1',
			'php5-xmlreader': '5.2.14-0.7.30.40.1',
			'php5-xmlrpc': '5.2.14-0.7.30.40.1',
			'php5-xmlwriter': '5.2.14-0.7.30.40.1',
			'php5-xsl': '5.2.14-0.7.30.40.1',
			'php5-zip': '5.2.14-0.7.30.40.1',
			'php5-zlib': '5.2.14-0.7.30.40.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

