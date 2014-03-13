#!/usr/bin/perl

# Title:       IBM Java 1.7.0 SA Important SUSE-SU-2013:1677-3
# Description: Fixes 47 vulnerabilities SLE11 SP2-3
# Modified:    2013 Dec 11
#
##############################################################################
# Copyright (C) 2013 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)
#
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
"META_CLASS=Security",
"META_CATEGORY=SLE",
"META_COMPONENT=Java",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_Security",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-11/msg00022.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'IBM Java 1.7.0';
my $MAIN_PACKAGE = 'java-1_7_0-ibm';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2013:1677-3';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP4) < 0 ) {
	%PACKAGES = (
		'java-1_7_0-ibm' => '1.7.0_sr6.0-0.7.1',
		'java-1_7_0-ibm-alsa' => '1.7.0_sr6.0-0.7.1',
		'java-1_7_0-ibm-devel' => '1.7.0_sr6.0-0.7.1',
		'java-1_7_0-ibm-jdbc' => '1.7.0_sr6.0-0.7.1',
		'java-1_7_0-ibm-plugin' => '1.7.0_sr6.0-0.7.1',
	);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

