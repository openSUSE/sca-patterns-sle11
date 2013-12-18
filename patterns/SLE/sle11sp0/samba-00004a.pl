#!/usr/bin/perl

# Title:       Samba Security Advisory SUSE-SA:2010:025
# Description: samba was updated to fix potential remote code execution security issues, CVSS v2 Base Score: 7.5
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
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

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
	"META_LINK_Security=http://www.novell.com/linux/security/advisories/2010_25_samba.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $CHECKING = 'Samba';
	my $SEVERITY = '7.5';
	my $TYPE = 'Potential remote code execution';
	my @PKGS_TO_CHECK = ();
	my $FIXED_VERSION = '';

	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE11SP1) < 0 ) {
		@PKGS_TO_CHECK = qw(samba samba-32bit samba-client cifs-mount libsmbclient0 libsmbclient0-32bit libsmbclient0-x86 libtalloc1 libtalloc1-32bit libtalloc1-x86 libtdb1 libtdb1-32bit libtdb1-x86 libwbclient0 libwbclient0-32bit libwbclient0-x86 samba-client-32bit samba-client-x86 samba-krb-printing samba-winbind samba-winbind-32bit samba-winbind-x86 samba-x86);
		$FIXED_VERSION = '3.2.7-11.20.1';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} elsif ( SDP::SUSE::compareKernel(SLE10SP3) >= 0 && SDP::SUSE::compareKernel(SLE10SP4) < 0 ) {
		@PKGS_TO_CHECK = qw(samba samba-32bit samba-64bit cifs-mount libmsrpc libmsrpc-devel libsmbclient libsmbclient-32bit libsmbclient-64bit libsmbclient-devel libsmbclient-x86 samba-client samba-client-32bit samba-client-64bit samba-client-x86 samba-krb-printing samba-python samba-winbind samba-winbind-32bit samba-winbind-64bit samba-winbind-x86 samba-x86);
		$FIXED_VERSION = '3.0.36-0.11.1';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} elsif ( SDP::SUSE::compareKernel(SLE9GA) >= 0 && SDP::SUSE::compareKernel(SLE10GA) < 0 ) {
		@PKGS_TO_CHECK = qw(samba samba-client libsmbclient libsmbclient-devel samba-doc samba-pdb samba-python samba-winbind);
		$FIXED_VERSION = '3.0.26a-0.15';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: Outside the kernel scope");
	}

SDP::Core::printPatternResults();

exit;
