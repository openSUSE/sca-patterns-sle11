#!/usr/bin/perl

# Title:       Firefox 3 Security Advisory SUSE-SA:2009:048
# Description: Firefox 3 was updated to fix remote code execution security issues, Severity 8 of 10.
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
	PROPERTY_NAME_COMPONENT."=Firefox",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://www.novell.com/linux/security/advisories/2009_48_firefox.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $CHECKING            = 'Firefox';
	my $ADVISORY            = '8';
	my $TYPE                = 'Remote code execution';
	my @PKGS_TO_CHECK       = ();
	my $FIXED_VERSION       = '';
	my $SUCCESS             = 0;

	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE11SP1) < 0 ) {
		SDP::Core::printDebug('DISTRIBUTION', 'SLE11GA');
		SDP::Core::setStatus(STATUS_SUCCESS, "Level $ADVISORY $CHECKING $TYPE AVOIDED");
		my %HOST_INFO = SDP::SUSE::getHostInfo();

		@PKGS_TO_CHECK       = qw(MozillaFirefox MozillaFirefox-debuginfo MozillaFirefox-debugsource MozillaFirefox-translations);
		$FIXED_VERSION       = '3.5.3-1.1.1';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(MozillaFirefox-branding-SLED);
		$FIXED_VERSION       = '3.5-1.1.5';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(mozilla-nspr-32bit mozilla-nspr mozilla-nspr-debuginfo-32bit mozilla-nspr-debuginfo mozilla-nspr-debugsource mozilla-nspr-devel mozilla-nspr-x86);
		$FIXED_VERSION       = '4.8-1.3.1';
		if ( $HOST_INFO{'architecture'} =~ /ppc/i ) { $FIXED_VERSION = ''; } else { $FIXED_VERSION = ''; }
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(mozilla-xulrunner191 mozilla-xulrunner191-32bit mozilla-xulrunner191-debuginfo mozilla-xulrunner191-debuginfo-32bit mozilla-xulrunner191-debugsource mozilla-xulrunner191-devel mozilla-xulrunner191-gnomevfs mozilla-xulrunner191-gnomevfs-32bit mozilla-xulrunner191-gnomevfs-x86 mozilla-xulrunner191-translations mozilla-xulrunner191-translations-32bit mozilla-xulrunner191-translations-x86 mozilla-xulrunner191-x86);
		$FIXED_VERSION       = '1.9.1.3-1.1.1';
		if ( $HOST_INFO{'architecture'} =~ /ppc/i ) { $FIXED_VERSION = ''; } else { $FIXED_VERSION = ''; }
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(mozilla-xulrunner190 mozilla-xulrunner190-32bit mozilla-xulrunner190-debuginfo mozilla-xulrunner190-debuginfo-32bit mozilla-xulrunner190-debugsource mozilla-xulrunner190-devel mozilla-xulrunner190-gnomevfs mozilla-xulrunner190-gnomevfs-32bit mozilla-xulrunner190-gnomevfs-x86 mozilla-xulrunner190-translations mozilla-xulrunner190-translations-32bit mozilla-xulrunner190-translations-x86);
		if ( $HOST_INFO{'architecture'} =~ /ppc/i ) { $FIXED_VERSION = '1.9.0.14-1.1.2'; } else { $FIXED_VERSION = '1.9.0.14-1.1.1'; }
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(libfreebl3 libfreebl3-32bit libfreebl3-x86 mozilla-nss mozilla-nss-32bit mozilla-nss-debuginfo mozilla-nss-debuginfo-32bit mozilla-nss-debugsource mozilla-nss-devel mozilla-nss-tools mozilla-nss-x86);
		$FIXED_VERSION       = '3.12.3.1-1.2.1';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		if ( ! $SUCCESS ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: No package(s) installed");
		}
	} elsif ( SDP::SUSE::compareKernel(SLE10SP3) >= 0 && SDP::SUSE::compareKernel(SLE10SP4) < 0 ) {
		SDP::Core::printDebug('DISTRIBUTION', 'SLE10SP3');
		SDP::Core::setStatus(STATUS_SUCCESS, "Level $ADVISORY $CHECKING $TYPE AVOIDED");

		@PKGS_TO_CHECK       = qw(MozillaFirefox MozillaFirefox-branding-upstream MozillaFirefox-debuginfo MozillaFirefox-translations);
		$FIXED_VERSION       = '3.5.3-1.5.3';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(MozillaFirefox-branding-SLED);
		$FIXED_VERSION       = '3.5-1.6.7';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(mozilla-xulrunner190 mozilla-xulrunner190-32bit mozilla-xulrunner190-debuginfo mozilla-xulrunner190-devel mozilla-xulrunner190-gnomevfs mozilla-xulrunner190-gnomevfs-32bit mozilla-xulrunner190-translations mozilla-xulrunner190-translations-32bit python-xpcom190);
		$FIXED_VERSION       = '1.9.0.14-0.6.6';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(mozilla-xulrunner191 mozilla-xulrunner191-32bit mozilla-xulrunner191-debuginfo mozilla-xulrunner191-devel mozilla-xulrunner191-gnomevfs mozilla-xulrunner191-gnomevfs-32bit mozilla-xulrunner191-translations mozilla-xulrunner191-translations-32bit python-xpcom191);
		$FIXED_VERSION       = '1.9.1.3-1.5.7';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		if ( ! $SUCCESS ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: No package(s) installed");
		}
	} elsif ( SDP::SUSE::compareKernel(SLE10SP2) >= 0 && SDP::SUSE::compareKernel(SLE10SP3) < 0 ) {
		SDP::Core::printDebug('DISTRIBUTION', 'SLE10SP2');
		SDP::Core::setStatus(STATUS_SUCCESS, "Level $ADVISORY $CHECKING $TYPE AVOIDED");

		@PKGS_TO_CHECK       = qw(MozillaFirefox MozillaFirefox-branding-upstream MozillaFirefox-debuginfo MozillaFirefox-translations);
		$FIXED_VERSION       = '3.5.3-1.4.2';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(MozillaFirefox-branding-SLED);
		$FIXED_VERSION       = '3.5-1.4.2';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(mozilla-nspr-32bit mozilla-nspr mozilla-nspr-64bit mozilla-nspr-devel mozilla-nspr-x86);
		$FIXED_VERSION       = '4.8-1.4.2';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(mozilla-nss mozilla-nss-32bit mozilla-nss-64bit mozilla-nss-devel mozilla-nss-tools mozilla-nss-x86);
		$FIXED_VERSION       = '3.12.3.1-1.4.2';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(mozilla-xulrunner190 mozilla-xulrunner190-32bit mozilla-xulrunner190-debuginfo mozilla-xulrunner190-devel mozilla-xulrunner190-gnomevfs mozilla-xulrunner190-gnomevfs-32bit mozilla-xulrunner190-translations mozilla-xulrunner190-translations-32bit python-xpcom190);
		$FIXED_VERSION       = '1.9.0.14-0.5.2';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		@PKGS_TO_CHECK       = qw(mozilla-xulrunner191 mozilla-xulrunner191-32bit mozilla-xulrunner191-debuginfo mozilla-xulrunner191-devel mozilla-xulrunner191-gnomevfs mozilla-xulrunner191-gnomevfs-32bit mozilla-xulrunner191-translations mozilla-xulrunner191-translations-32bit python-xpcom191);
		$FIXED_VERSION       = '1.9.1.3-1.4.2';
		SDP::Core::printDebug('ARGS', "$CHECKING, $ADVISORY, $TYPE, $#PKGS_TO_CHECK, $FIXED_VERSION");
		$SUCCESS++ if SDP::SUSE::securitySeverityPackageCheckNoError($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);

		if ( ! $SUCCESS ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: No package(s) installed");
		}
	} else {
		SDP::Core::printDebug('DISTRIBUTION', 'None Selected');
		SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: Outside the kernel scope");
	}

SDP::Core::printPatternResults();

exit;
