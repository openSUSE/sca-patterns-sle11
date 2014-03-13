#!/usr/bin/perl

# Title:       PHP5 SA Important SUSE-SU-2013:1285-2
# Description: fixes four vulnerabilities
# Modified:    2013 Oct 21
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
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-08/msg00008.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'PHP53';
my $MAIN_PACKAGE = 'php53';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2013:1285-2';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
	%PACKAGES = (
		'apache2-mod_php53' => '5.3.8-0.41.1',
		'php53' => '5.3.8-0.41.1',
		'php53-bcmath' => '5.3.8-0.41.1',
		'php53-bz2' => '5.3.8-0.41.1',
		'php53-calendar' => '5.3.8-0.41.1',
		'php53-ctype' => '5.3.8-0.41.1',
		'php53-curl' => '5.3.8-0.41.1',
		'php53-dba' => '5.3.8-0.41.1',
		'php53-devel' => '5.3.8-0.41.1',
		'php53-dom' => '5.3.8-0.41.1',
		'php53-exif' => '5.3.8-0.41.1',
		'php53-fastcgi' => '5.3.8-0.41.1',
		'php53-fileinfo' => '5.3.8-0.41.1',
		'php53-ftp' => '5.3.8-0.41.1',
		'php53-gd' => '5.3.8-0.41.1',
		'php53-gettext' => '5.3.8-0.41.1',
		'php53-gmp' => '5.3.8-0.41.1',
		'php53-iconv' => '5.3.8-0.41.1',
		'php53-imap' => '5.3.8-0.41.1',
		'php53-intl' => '5.3.8-0.41.1',
		'php53-json' => '5.3.8-0.41.1',
		'php53-ldap' => '5.3.8-0.41.1',
		'php53-mbstring' => '5.3.8-0.41.1',
		'php53-mcrypt' => '5.3.8-0.41.1',
		'php53-mysql' => '5.3.8-0.41.1',
		'php53-odbc' => '5.3.8-0.41.1',
		'php53-openssl' => '5.3.8-0.41.1',
		'php53-pcntl' => '5.3.8-0.41.1',
		'php53-pdo' => '5.3.8-0.41.1',
		'php53-pear' => '5.3.8-0.41.1',
		'php53-pgsql' => '5.3.8-0.41.1',
		'php53-posix' => '5.3.8-0.41.1',
		'php53-pspell' => '5.3.8-0.41.1',
		'php53-readline' => '5.3.8-0.41.1',
		'php53-shmop' => '5.3.8-0.41.1',
		'php53-snmp' => '5.3.8-0.41.1',
		'php53-soap' => '5.3.8-0.41.1',
		'php53-sockets' => '5.3.8-0.41.1',
		'php53-sqlite' => '5.3.8-0.41.1',
		'php53-suhosin' => '5.3.8-0.41.1',
		'php53-sysvmsg' => '5.3.8-0.41.1',
		'php53-sysvsem' => '5.3.8-0.41.1',
		'php53-sysvshm' => '5.3.8-0.41.1',
		'php53-tidy' => '5.3.8-0.41.1',
		'php53-tokenizer' => '5.3.8-0.41.1',
		'php53-wddx' => '5.3.8-0.41.1',
		'php53-xmlreader' => '5.3.8-0.41.1',
		'php53-xmlrpc' => '5.3.8-0.41.1',
		'php53-xmlwriter' => '5.3.8-0.41.1',
		'php53-xsl' => '5.3.8-0.41.1',
		'php53-zip' => '5.3.8-0.41.1',
		'php53-zlib' => '5.3.8-0.41.1',
	);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

