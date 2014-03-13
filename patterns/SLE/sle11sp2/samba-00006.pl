#!/usr/bin/perl

# Title:       Samba SA SUSE-SU-2013:0326-1
# Description: Solves two vulnerabilities and has four fixes
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
	PROPERTY_NAME_COMPONENT."=Samba",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-02/msg00019.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $NAME = 'Samba';
	my $MAIN_PACKAGE = '';
	my $SEVERITY = 'Important';
	my $TAG = 'SUSE-SU-2013:0326-1';
	my %PACKAGES = ();
	if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
		%PACKAGES = (
			'ldapsmb' => '1.34b-12.30.1',
			'libldb1-32bit' => '3.6.3-0.30.1',
			'libldb1' => '3.6.3-0.30.1',
			'libldb-devel' => '3.6.3-0.30.1',
			'libnetapi0' => '3.6.3-0.30.1',
			'libnetapi-devel' => '3.6.3-0.30.1',
			'libsmbclient0-32bit' => '3.6.3-0.30.1',
			'libsmbclient0' => '3.6.3-0.30.1',
			'libsmbclient0-x86' => '3.6.3-0.30.1',
			'libsmbclient-devel' => '3.6.3-0.30.1',
			'libsmbsharemodes0' => '3.6.3-0.30.1',
			'libsmbsharemodes-devel' => '3.6.3-0.30.1',
			'libtalloc1-32bit' => '3.4.3-1.42.11',
			'libtalloc1' => '3.4.3-1.42.11',
			'libtalloc1-x86' => '3.4.3-1.42.11',
			'libtalloc2-32bit' => '3.6.3-0.30.1',
			'libtalloc2' => '3.6.3-0.30.1',
			'libtalloc2-x86' => '3.6.3-0.30.1',
			'libtalloc-devel' => '3.6.3-0.30.1',
			'libtdb1-32bit' => '3.6.3-0.30.1',
			'libtdb1' => '3.6.3-0.30.1',
			'libtdb1-x86' => '3.6.3-0.30.1',
			'libtdb-devel' => '3.6.3-0.30.1',
			'libtevent0-32bit' => '3.6.3-0.30.1',
			'libtevent0' => '3.6.3-0.30.1',
			'libtevent-devel' => '3.6.3-0.30.1',
			'libwbclient0-32bit' => '3.6.3-0.30.1',
			'libwbclient0' => '3.6.3-0.30.1',
			'libwbclient0-x86' => '3.6.3-0.30.1',
			'libwbclient-devel' => '3.6.3-0.30.1',
			'samba-32bit' => '3.6.3-0.30.1',
			'samba' => '3.6.3-0.30.1',
			'samba-client-32bit' => '3.6.3-0.30.1',
			'samba-client' => '3.6.3-0.30.1',
			'samba-client-x86' => '3.6.3-0.30.1',
			'samba-devel' => '3.6.3-0.30.1',
			'samba-krb-printing' => '3.6.3-0.30.1',
			'samba-winbind-32bit' => '3.6.3-0.30.1',
			'samba-winbind' => '3.6.3-0.30.1',
			'samba-winbind-x86' => '3.6.3-0.30.1',
			'samba-x86' => '3.6.3-0.30.1',
		);
		SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
	}
SDP::Core::printPatternResults();

exit;

