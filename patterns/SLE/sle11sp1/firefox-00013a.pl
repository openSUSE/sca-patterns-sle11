#!/usr/bin/perl

# Title:       Firefox Security Advisory SUSE-SA:2010:056
# Description: Firefox was updated to fix remote code execution issues, CVSS v2 Base Score: 9.3
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
	PROPERTY_NAME_COMPONENT."=Firefox",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://www.novell.com/linux/security/advisories/2010_56_mozilla.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $CHECKING            = 'Firefox';
	my $SEVERITY            = '9.3';
	my $TYPE                = 'Remote code execution';
	my @PKGS_TO_CHECK       = ();
	my $FIXED_VERSION       = '';
	my $SUCCESS             = 0;

	if ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel(SLE11SP2) < 0 ) {
		SDP::Core::setStatus(STATUS_SUCCESS, "Level $SEVERITY $CHECKING $TYPE AVOIDED");

		@PKGS_TO_CHECK = qw(MozillaFirefox MozillaFirefox-translations);
		$FIXED_VERSION = '3.6.12-0.6.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK = qw(mozilla-xulrunner192 mozilla-xulrunner192-32bit mozilla-xulrunner192-devel mozilla-xulrunner192-gnome mozilla-xulrunner192-gnome-32bit mozilla-xulrunner192-translations mozilla-xulrunner192-translations-32bit mozilla-xulrunner192-x86);
		$FIXED_VERSION = '1.9.2.12-0.6.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK = qw(mozilla-nspr-32bit mozilla-nspr mozilla-nspr-devel);
		$FIXED_VERSION = '4.8.6-1.2.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK = qw(libfreebl3 libfreebl3-32bit mozilla-nss mozilla-nss-32bit mozilla-nss-devel mozilla-nss-tools);
		$FIXED_VERSION = '3.12.8-1.2.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		if ( ! $SUCCESS ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: No package(s) installed");
		}
	} elsif ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE11SP1) < 0 ) {
		SDP::Core::setStatus(STATUS_SUCCESS, "Level $SEVERITY $CHECKING $TYPE AVOIDED");

		@PKGS_TO_CHECK = qw(MozillaFirefox MozillaFirefox-translations);
		$FIXED_VERSION = '3.6.12-0.6.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK = qw(mozilla-xulrunner192 mozilla-xulrunner192-32bit mozilla-xulrunner192-devel mozilla-xulrunner192-gnome mozilla-xulrunner192-gnome-32bit mozilla-xulrunner192-translations mozilla-xulrunner192-translations-32bit mozilla-xulrunner192-x86);
		$FIXED_VERSION = '1.9.2.12-0.6.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK = qw(mozilla-nspr-32bit mozilla-nspr mozilla-nspr-devel mozilla-nspr-x86);
		$FIXED_VERSION = '4.8.6-1.2.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK = qw(libfreebl3 libfreebl3-32bit libfreebl3-x86 mozilla-nss mozilla-nss-32bit mozilla-nss-devel mozilla-nss-tools mozilla-nss-x86);
		$FIXED_VERSION = '3.12.8-1.2.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		if ( ! $SUCCESS ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: No package(s) installed");
		}
	} elsif ( SDP::SUSE::compareKernel(SLE10SP3) >= 0 && SDP::SUSE::compareKernel(SLE10SP4) < 0 ) {
		SDP::Core::setStatus(STATUS_SUCCESS, "Level $SEVERITY $CHECKING $TYPE AVOIDED");

		@PKGS_TO_CHECK = qw(mozilla-nss mozilla-nss-32bit mozilla-nss-64bit mozilla-nss-devel mozilla-nss-tools mozilla-nss-x86);
		$FIXED_VERSION = '3.12.8-1.4.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK = qw(mozilla-nspr-32bit mozilla-nspr mozilla-nspr-64bit mozilla-nspr-devel mozilla-nspr-x86);
		$FIXED_VERSION = '4.8.6-1.6.1';
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		if ( ! $SUCCESS ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: No package(s) installed");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: Outside the kernel scope");
	}

SDP::Core::printPatternResults();

exit;
