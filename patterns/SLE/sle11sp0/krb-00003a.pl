#!/usr/bin/perl

# Title:       Kerberos Security Advisory SUSE-SA:2010:006
# Description: krb5 was updated to fix remote code execution security issues, CVSS v2 Base Score: 9.3
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
#

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
	PROPERTY_NAME_COMPONENT."=Kerberos",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7005185",
	"META_LINK_Security=http://www.novell.com/linux/security/advisories/2010_06_krb5.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $CHECKING            = 'Kerberos';
	my $ADVISORY            = '9.3';
	my $TYPE                = 'Remote code execution';
	my @PKGS_TO_CHECK       = ();
	my $FIXED_VERSION       = '';

	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE11SP1) < 0 ) {
		$FIXED_VERSION       = '1.6.3-133.26.1';
		@PKGS_TO_CHECK       = qw(krb5 krb5-32bit krb5-apps-clients krb5-apps-servers krb5-client krb5-debuginfo krb5-debuginfo-32bit krb5-debuginfo-x86 krb5-debugsource krb5-server krb5-x86);
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} elsif ( SDP::SUSE::compareKernel(SLE10SP3) >= 0 && SDP::SUSE::compareKernel(SLE10SP4) < 0 ) {
		$FIXED_VERSION       = '1.4.3-19.44.1';
		@PKGS_TO_CHECK       = qw(krb5 krb5-32bit krb5-64bit krb5-apps-clients krb5-apps-servers krb5-client krb5-debuginfo krb5-devel krb5-devel-32bit krb5-devel-64bit krb5-server krb5-x86);
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} elsif ( SDP::SUSE::compareKernel(SLE10SP2) >= 0 && SDP::SUSE::compareKernel(SLE10SP3) < 0 ) {
		$FIXED_VERSION       = '1.4.3-19.43.2';
		@PKGS_TO_CHECK       = qw(krb5 krb5-32bit krb5-64bit krb5-apps-clients krb5-apps-servers krb5-client krb5-debuginfo krb5-devel krb5-devel-32bit krb5-devel-64bit krb5-server krb5-x86);
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory $ADVISORY: Outside the kernel scope");
	}

SDP::Core::printPatternResults();

exit;
