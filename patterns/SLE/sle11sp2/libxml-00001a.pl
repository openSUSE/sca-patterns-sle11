#!/usr/bin/perl

# Title:       LibXML SA SUSE-SU-2012:1636-1
# Description: Fixes one vulnerability
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
	PROPERTY_NAME_COMPONENT."=LibXML",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2012-12/msg00010.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $NAME = 'LibXML';
	my $MAIN_PACKAGE = 'libxml2';
	my $SEVERITY = 'Important';
	my $TAG = 'SUSE-SU-2012:1636-1';
	my %PACKAGES = ();
	if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
		%PACKAGES = (
			'libxml2' => '2.7.6-0.21.1',
			'libxml2-32bit' => '2.7.6-0.21.1',
			'libxml2-devel' => '2.7.6-0.21.1',
			'libxml2-devel-32bit' => '2.7.6-0.21.1',
			'libxml2-doc' => '2.7.6-0.21.1',
			'libxml2-python' => '2.7.6-0.21.1',
			'libxml2-x86' => '2.7.6-0.21.1',
		);
		SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
	} elsif ( SDP::SUSE::compareKernel(SLE10SP4) >= 0 && SDP::SUSE::compareKernel(SLE10SP5) < 0 ) {
		%PACKAGES = (
			'libxml2' => '2.6.23-15.35.1',
			'libxml2-32bit' => '2.6.23-15.35.1',
			'libxml2-64bit' => '2.6.23-15.35.1',
			'libxml2-devel' => '2.6.23-15.35.1',
			'libxml2-devel-32bit' => '2.6.23-15.35.1',
			'libxml2-devel-64bit' => '2.6.23-15.35.1',
			'libxml2-python' => '2.6.23-15.35.1',
			'libxml2-test' => '2.6.23-15.35.1',
			'libxml2-x86' => '2.6.23-15.35.1',
		);
		SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
	}
SDP::Core::printPatternResults();

exit;

