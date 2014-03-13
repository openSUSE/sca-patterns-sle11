#!/usr/bin/perl

# Title:       IBM Java 1.6 Security Advisory SUSE-SA:2011:014
# Description: IBM Java 1.4, 1.5, 1.6 was updated to fix remote code execution security issues, CVSS v2 Base Score: 10.0
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
	PROPERTY_NAME_COMPONENT."=Java",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://www.novell.com/linux/security/advisories/2011_14_ibmjava.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $CHECKING = '';
	my $SEVERITY = '10.0';
	my $TYPE = 'Remote code execution';
	my @PKGS_TO_CHECK = ();
	my $FIXED_VERSION = '';
	my $SUCCESS = 0;

	if ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel(SLE11SP2) < 0 ) {
		if ( SDP::SUSE::packageInstalled('java-1_6_0-ibm') ) {
			$CHECKING = 'IBM Java 1.6';
			@PKGS_TO_CHECK = qw(java-1_6_0-ibm java-1_6_0-ibm-alsa java-1_6_0-ibm-devel java-1_6_0-ibm-fonts java-1_6_0-ibm-jdbc java-1_6_0-ibm-plugin);
			$FIXED_VERSION = '1.6.0_sr9.1-1.5.1';
			SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		} elsif ( SDP::SUSE::packageInstalled('java-1_4_2-ibm') ) {
			$CHECKING = 'IBM Java 1.4';
			@PKGS_TO_CHECK = qw(java-1_4_2-ibm java-1_4_2-ibm-devel);
			$FIXED_VERSION = '1.4.2_sr13.8-1.5.1';
			SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: Applicable packages not installed.");
		}
	} elsif ( SDP::SUSE::compareKernel(SLE10SP3) >= 0 && SDP::SUSE::compareKernel(SLE10SP4) < 0 ) {
		if ( SDP::SUSE::packageInstalled('java-1_6_0-ibm') ) {
			$CHECKING = 'IBM Java 1.6';
			@PKGS_TO_CHECK = qw(java-1_6_0-ibm java-1_6_0-ibm-64bit java-1_6_0-ibm-devel java-1_6_0-ibm-fonts java-1_6_0-ibm-jdbc java-1_6_0-ibm-plugin);
			$FIXED_VERSION = '1.6.0_sr9.1-1.5.1';
			SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		} elsif ( SDP::SUSE::packageInstalled('java-1_5_0-ibm') ) {
			$CHECKING = 'IBM Java 1.5';
			@PKGS_TO_CHECK = qw(java-1_5_0-ibm java-1_5_0-ibm-32bit java-1_5_0-ibm-alsa-32bit java-1_5_0-ibm-demo java-1_5_0-ibm-devel java-1_5_0-ibm-devel-32bit java-1_5_0-ibm-fonts java-1_5_0-ibm-src);
			$FIXED_VERSION = '1.5.0_sr12.3-0.7.1';
			SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		} elsif ( SDP::SUSE::packageInstalled('java-1_4_2-ibm') ) {
			$CHECKING = 'IBM Java 1.4';
			@PKGS_TO_CHECK = qw(java-1_4_2-ibm java-1_4_2-ibm-devel java-1_4_2-ibm-jdbc java-1_4_2-ibm-plugin);
			$FIXED_VERSION = '1.4.2_sr13.8-1.7.1';
			SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: Applicable packages not installed.");
		}
	} elsif ( SDP::SUSE::compareKernel(SLE9GA) >= 0 && SDP::SUSE::compareKernel(SLE10GA) < 0 ) {
		$CHECKING = 'IBM Java';
		@PKGS_TO_CHECK = qw(IBMJava5-JRE IBMJava5-SDK);
		$FIXED_VERSION = '1.5.0_sr12.3-0.11';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
		@PKGS_TO_CHECK = qw(IBMJava2-JRE IBMJava2-SDK);
		$FIXED_VERSION = '1.4.2_sr13.8-0.15';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: Outside the kernel scope");
	}

SDP::Core::printPatternResults();

exit;
