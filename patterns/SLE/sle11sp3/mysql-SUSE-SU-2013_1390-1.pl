#!/usr/bin/perl

# Title:       MySQL SA Important SUSE-SU-2013:1390-1
# Description: Fixes 18 vulnerabilities
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
"META_COMPONENT=MySQL",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_Security",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-08/msg00022.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'MySQL';
my $MAIN_PACKAGE = '';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2013:1390-1';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP3) >= 0 && SDP::SUSE::compareKernel(SLE11SP4) < 0 ) {
	%PACKAGES = (
		'mysql' => '5.5.32-0.9.1',
		'mysql-client' => '5.5.32-0.9.1',
		'mysql-tools' => '5.5.32-0.9.1',
		'libmysql55client18-32bit' => '5.5.32-0.9.1',
		'libmysql55client18' => '5.5.32-0.9.1',
		'libmysql55client18-x86' => '5.5.32-0.9.1',
		'libmysql55client_r18-32bit' => '5.5.32-0.9.1',
		'libmysql55client_r18' => '5.5.32-0.9.1',
		'libmysql55client_r18-x86' => '5.5.32-0.9.1',
		'libmysqlclient15-32bit' => '5.0.96-0.6.9',
		'libmysqlclient15' => '5.0.96-0.6.9',
		'libmysqlclient15-x86' => '5.0.96-0.6.9',
		'libmysqlclient_r15-32bit' => '5.0.96-0.6.9',
		'libmysqlclient_r15' => '5.0.96-0.6.9',
		'libmysqlclient_r15-x86' => '5.0.96-0.6.9',
	);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

