#!/usr/bin/python

# Title:       PHP5 SA Important SUSE-SU-2014:0868-1
# Description: fixes two vulnerabilities
# Modified:    2014 Jul 17
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
META_COMPONENT = "PHP"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-07/msg00001.html"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Main Program Execution
##############################################################################

LTSS = True
NAME = 'PHP5'
MAIN = 'php5'
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:0868-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11 and SERVER['DistroPatchLevel'] == 2 ):
	PACKAGES = {
		'apache2-mod_php5': '5.2.14-0.7.30.54.1',
		'php5': '5.2.14-0.7.30.54.1',
		'php5-bcmath': '5.2.14-0.7.30.54.1',
		'php5-bz2': '5.2.14-0.7.30.54.1',
		'php5-calendar': '5.2.14-0.7.30.54.1',
		'php5-ctype': '5.2.14-0.7.30.54.1',
		'php5-curl': '5.2.14-0.7.30.54.1',
		'php5-dba': '5.2.14-0.7.30.54.1',
		'php5-dbase': '5.2.14-0.7.30.54.1',
		'php5-dom': '5.2.14-0.7.30.54.1',
		'php5-exif': '5.2.14-0.7.30.54.1',
		'php5-fastcgi': '5.2.14-0.7.30.54.1',
		'php5-ftp': '5.2.14-0.7.30.54.1',
		'php5-gd': '5.2.14-0.7.30.54.1',
		'php5-gettext': '5.2.14-0.7.30.54.1',
		'php5-gmp': '5.2.14-0.7.30.54.1',
		'php5-hash': '5.2.14-0.7.30.54.1',
		'php5-iconv': '5.2.14-0.7.30.54.1',
		'php5-json': '5.2.14-0.7.30.54.1',
		'php5-ldap': '5.2.14-0.7.30.54.1',
		'php5-mbstring': '5.2.14-0.7.30.54.1',
		'php5-mcrypt': '5.2.14-0.7.30.54.1',
		'php5-mysql': '5.2.14-0.7.30.54.1',
		'php5-odbc': '5.2.14-0.7.30.54.1',
		'php5-openssl': '5.2.14-0.7.30.54.1',
		'php5-pcntl': '5.2.14-0.7.30.54.1',
		'php5-pdo': '5.2.14-0.7.30.54.1',
		'php5-pear': '5.2.14-0.7.30.54.1',
		'php5-pgsql': '5.2.14-0.7.30.54.1',
		'php5-pspell': '5.2.14-0.7.30.54.1',
		'php5-shmop': '5.2.14-0.7.30.54.1',
		'php5-snmp': '5.2.14-0.7.30.54.1',
		'php5-soap': '5.2.14-0.7.30.54.1',
		'php5-suhosin': '5.2.14-0.7.30.54.1',
		'php5-sysvmsg': '5.2.14-0.7.30.54.1',
		'php5-sysvsem': '5.2.14-0.7.30.54.1',
		'php5-sysvshm': '5.2.14-0.7.30.54.1',
		'php5-tokenizer': '5.2.14-0.7.30.54.1',
		'php5-wddx': '5.2.14-0.7.30.54.1',
		'php5-xmlreader': '5.2.14-0.7.30.54.1',
		'php5-xmlrpc': '5.2.14-0.7.30.54.1',
		'php5-xmlwriter': '5.2.14-0.7.30.54.1',
		'php5-xsl': '5.2.14-0.7.30.54.1',
		'php5-zip': '5.2.14-0.7.30.54.1',
		'php5-zlib': '5.2.14-0.7.30.54.1',
	}
	SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")

Core.printPatternResults()


