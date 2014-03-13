#!/usr/bin/perl

# Title:       MySQL SA SUSE-SU-2013:0262-1
# Description: Fixes four vulnerabilities
# Modified:    2013 Jun 27

##############################################################################
#  Copyright (C) 2013 SUSE LLC
##############################################################################
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; version 2 of the License.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)

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
	PROPERTY_NAME_CLASS."=Security",
	PROPERTY_NAME_CATEGORY."=SLE",
	PROPERTY_NAME_COMPONENT."=MySQL",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-02/msg00000.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $NAME = 'MySQL';
	my $MAIN_PACKAGE = '';
	my $SEVERITY = 'Important';
	my $TAG = 'SUSE-SU-2013:0262-1';
	my %PACKAGES = ();
	if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
		%PACKAGES = (
			'libmysqlclient15-32bit' => '5.0.96-0.6.1',
			'libmysqlclient15' => '5.0.96-0.6.1',
			'libmysqlclient15-x86' => '5.0.96-0.6.1',
			'libmysqlclient-devel' => '5.0.96-0.6.1',
			'libmysqlclient_r15-32bit' => '5.0.96-0.6.1',
			'libmysqlclient_r15' => '5.0.96-0.6.1',
			'libmysqlclient_r15-x86' => '5.0.96-0.6.1',
			'mysql' => '5.0.96-0.6.1',
			'mysql-client' => '5.0.96-0.6.1',
			'mysql-Max' => '5.0.96-0.6.1',
			'mysql-tools' => '5.0.96-0.6.1',
		);
		SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
	}
SDP::Core::printPatternResults();

exit;

