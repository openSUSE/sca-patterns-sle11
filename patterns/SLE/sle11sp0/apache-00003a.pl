#!/usr/bin/perl

# Title:       Apache Security Advisory SUSE-SA:2009:050
# Description: Apache was updated to fix potential code execution and remote denial of service security issues, Severity 8 of 10.
# Modified:    2013 Jun 26

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
	PROPERTY_NAME_COMPONENT."=Apache",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://www.novell.com/linux/security/advisories/2009_50_apache.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $CHECKING            = 'Apache';
	my $ADVISORY            = '8';
	my $TYPE                = 'Potential code execution and remote denial of service';
	my @PKGS_TO_CHECK       = ();
	my $FIXED_VERSION       = '';
	my $SUCCESS             = 0;

	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE11SP1) < 0 ) {
		SDP::Core::setStatus(STATUS_SUCCESS, "Level $ADVISORY $CHECKING $TYPE AVOIDED");
		@PKGS_TO_CHECK       = qw(apache2 apache2-debuginfo apache2-debugsource apache2-devel apache2-doc apache2-example-pages apache2-prefork apache2-utils apache2-worker);
		$FIXED_VERSION       = '2.2.10-2.21.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		@PKGS_TO_CHECK       = qw(libapr1 libapr1-32bit libapr1-debuginfo libapr1-debugsource libapr1-devel libapr1-devel-32bit);
		$FIXED_VERSION       = '1.3.3-11.16.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		@PKGS_TO_CHECK       = qw(libapr-util1 libapr-util1-32bit libapr-util1-debuginfo libapr-util1-debugsource libapr-util1-devel libapr-util1-devel-32bit);
		$FIXED_VERSION       = '1.3.4-12.20.2';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		if ( ! $SUCCESS ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: No package(s) installed");
		}
	} elsif ( SDP::SUSE::compareKernel(SLE10SP3) >= 0 && SDP::SUSE::compareKernel(SLE10SP4) < 0 ) {
		SDP::Core::setStatus(STATUS_SUCCESS, "Level $ADVISORY $CHECKING $TYPE AVOIDED");
		@PKGS_TO_CHECK       = qw(apache2 apache2-debuginfo apache2-devel apache2-doc apache2-example-pages apache2-prefork apache2-worker);
		$FIXED_VERSION       = '2.2.3-16.28.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		@PKGS_TO_CHECK       = qw(libapr1 libapr1-64bit libapr1-devel libapr1-devel-64bit);
		$FIXED_VERSION       = '1.2.2-13.8.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		@PKGS_TO_CHECK       = qw(libapr-util1 libapr-util1-64bit libapr-util1-devel libapr-util1-devel-64bit);
		$FIXED_VERSION       = '1.2.2-13.9.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		if ( ! $SUCCESS ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: No package(s) installed");
		}
	} elsif ( SDP::SUSE::compareKernel(SLE10SP2) >= 0 && SDP::SUSE::compareKernel(SLE10SP3) < 0 ) {
		SDP::Core::setStatus(STATUS_SUCCESS, "Level $ADVISORY $CHECKING $TYPE AVOIDED");
		@PKGS_TO_CHECK       = qw(apache2 apache2-debuginfo apache2-devel apache2-doc apache2-example-pages apache2-prefork apache2-worker);
		$FIXED_VERSION       = '2.2.3-16.25.4';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		@PKGS_TO_CHECK       = qw(libapr1 libapr1-64bit libapr1-devel libapr1-devel-64bit);
		$FIXED_VERSION       = '1.2.2-13.8.2';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		@PKGS_TO_CHECK       = qw(libapr-util1 libapr-util1-64bit libapr-util1-devel libapr-util1-devel-64bit);
		$FIXED_VERSION       = '1.2.2-13.10.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		if ( ! $SUCCESS ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: No package(s) installed");
		}
	} elsif ( SDP::SUSE::compareKernel(SLE9GA) >= 0 && SDP::SUSE::compareKernel(SLE10GA) < 0 ) {
		@PKGS_TO_CHECK       = qw(apache2 apache2-devel apache2-doc apache2-example-pages apache2-prefork apache2-worker libapr0);
		$FIXED_VERSION       = '2.0.59-1.14';
		SDP::SUSE::securityPackageCheck($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} else {
		SDP::Core::printDebug('DISTRIBUTION', 'None Selected');
		SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: Outside the kernel scope");
	}

SDP::Core::printPatternResults();

exit;
