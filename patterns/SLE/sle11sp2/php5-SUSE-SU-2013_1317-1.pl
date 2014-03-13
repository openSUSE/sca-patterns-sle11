#!/usr/bin/perl

# Title:       PHP5 SA Important SUSE-SU-2013:1317-1
# Description: Fixes four vulnerabilities
# Modified:    2013 Oct 23
#
##############################################################################
# Copyright (C) 2013 SUSE LLC
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
use strict;
use warnings;
use SDP::Core;
use SDP::SUSE;

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

@PATTERN_RESULTS = (
"META_CLASS=Security",
"META_CATEGORY=SLE",
"META_COMPONENT=PHP5",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_Security",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-08/msg00009.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'PHP5';
my $MAIN_PACKAGE = 'php5';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2013:1317-1';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
	%PACKAGES = (
		'apache2-mod_php5' => '5.2.14-0.7.30.48.1',
		'php5' => '5.2.14-0.7.30.48.1',
		'php5-bcmath' => '5.2.14-0.7.30.48.1',
		'php5-bz2' => '5.2.14-0.7.30.48.1',
		'php5-calendar' => '5.2.14-0.7.30.48.1',
		'php5-ctype' => '5.2.14-0.7.30.48.1',
		'php5-curl' => '5.2.14-0.7.30.48.1',
		'php5-dba' => '5.2.14-0.7.30.48.1',
		'php5-dbase' => '5.2.14-0.7.30.48.1',
		'php5-devel' => '5.2.14-0.7.30.48.1',
		'php5-dom' => '5.2.14-0.7.30.48.1',
		'php5-exif' => '5.2.14-0.7.30.48.1',
		'php5-fastcgi' => '5.2.14-0.7.30.48.1',
		'php5-ftp' => '5.2.14-0.7.30.48.1',
		'php5-gd' => '5.2.14-0.7.30.48.1',
		'php5-gettext' => '5.2.14-0.7.30.48.1',
		'php5-gmp' => '5.2.14-0.7.30.48.1',
		'php5-hash' => '5.2.14-0.7.30.48.1',
		'php5-iconv' => '5.2.14-0.7.30.48.1',
		'php5-imap' => '5.2.14-0.7.30.48.1',
		'php5-json' => '5.2.14-0.7.30.48.1',
		'php5-ldap' => '5.2.14-0.7.30.48.1',
		'php5-mbstring' => '5.2.14-0.7.30.48.1',
		'php5-mcrypt' => '5.2.14-0.7.30.48.1',
		'php5-mysql' => '5.2.14-0.7.30.48.1',
		'php5-ncurses' => '5.2.14-0.7.30.48.1',
		'php5-odbc' => '5.2.14-0.7.30.48.1',
		'php5-openssl' => '5.2.14-0.7.30.48.1',
		'php5-pcntl' => '5.2.14-0.7.30.48.1',
		'php5-pdo' => '5.2.14-0.7.30.48.1',
		'php5-pear' => '5.2.14-0.7.30.48.1',
		'php5-pgsql' => '5.2.14-0.7.30.48.1',
		'php5-posix' => '5.2.14-0.7.30.48.1',
		'php5-pspell' => '5.2.14-0.7.30.48.1',
		'php5-readline' => '5.2.14-0.7.30.48.1',
		'php5-shmop' => '5.2.14-0.7.30.48.1',
		'php5-snmp' => '5.2.14-0.7.30.48.1',
		'php5-soap' => '5.2.14-0.7.30.48.1',
		'php5-sockets' => '5.2.14-0.7.30.48.1',
		'php5-sqlite' => '5.2.14-0.7.30.48.1',
		'php5-suhosin' => '5.2.14-0.7.30.48.1',
		'php5-sysvmsg' => '5.2.14-0.7.30.48.1',
		'php5-sysvsem' => '5.2.14-0.7.30.48.1',
		'php5-sysvshm' => '5.2.14-0.7.30.48.1',
		'php5-tidy' => '5.2.14-0.7.30.48.1',
		'php5-tokenizer' => '5.2.14-0.7.30.48.1',
		'php5-wddx' => '5.2.14-0.7.30.48.1',
		'php5-xmlreader' => '5.2.14-0.7.30.48.1',
		'php5-xmlrpc' => '5.2.14-0.7.30.48.1',
		'php5-xmlwriter' => '5.2.14-0.7.30.48.1',
		'php5-xsl' => '5.2.14-0.7.30.48.1',
		'php5-zip' => '5.2.14-0.7.30.48.1',
		'php5-zlib' => '5.2.14-0.7.30.48.1',
	);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

