#!/usr/bin/perl

# Title:       GLIBC Security Advisory SUSE-SA:2010:052
# Description: GLIBC was updated to fix local privilege escalation security issues, CVSS v2 Base Score: 7.2
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
	PROPERTY_NAME_COMPONENT."=GLIBC",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://www.novell.com/linux/security/advisories/2010_52_glibc.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $CHECKING            = 'GLIBC';
	my $SECURITY            = '7.2';
	my $TYPE                = 'Local privilege escalation';
	my @PKGS_TO_CHECK       = ();
	my $FIXED_VERSION       = '';

	if  ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel(SLE11SP2) < 0 ) {
		@PKGS_TO_CHECK       = qw(glibc glibc-32bit glibc-devel glibc-devel-32bit glibc-html glibc-i18ndata glibc-info glibc-locale glibc-locale-32bit glibc-locale-x86 glibc-profile glibc-profile-32bit glibc-profile-x86 glibc-x86 nscd);
		$FIXED_VERSION       = '2.11.1-0.20.1';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SECURITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} elsif ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE11SP1) < 0 ) {
		@PKGS_TO_CHECK       = qw(glibc glibc-32bit glibc-devel glibc-devel-32bit glibc-html glibc-i18ndata glibc-info glibc-locale glibc-locale-32bit glibc-locale-x86 glibc-profile glibc-profile-32bit glibc-profile-x86 glibc-x86 nscd);
		$FIXED_VERSION       = '2.9-13.11.1';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SECURITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} elsif  ( SDP::SUSE::compareKernel(SLE10SP3) >= 0 && SDP::SUSE::compareKernel(SLE10SP4) < 0 ) {
		@PKGS_TO_CHECK       = qw(glibc glibc-32bit glibc-64bit glibc-debuginfo glibc-devel glibc-devel-32bit glibc-devel-64bit glibc-html glibc-i18ndata glibc-info glibc-locale glibc-locale-32bit glibc-locale-64bit glibc-locale-x86 glibc-profile glibc-profile-32bit glibc-profile-64bit glibc-profile-x86 glibc-x86 nscd);
		$FIXED_VERSION       = '2.4-31.77.76.1';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SECURITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security SECURITY: Outside the kernel scope");
	}

SDP::Core::printPatternResults();

exit;
