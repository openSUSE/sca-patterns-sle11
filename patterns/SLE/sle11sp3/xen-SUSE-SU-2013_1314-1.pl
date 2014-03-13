#!/usr/bin/perl

# Title:       Xen SA Important SUSE-SU-2013:1314-1
# Description: Solves three vulnerabilities and has 6 fixes
# Modified:    2013 Oct 21
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
"META_CATEGORY=Virtualization",
"META_COMPONENT=Xen",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_Security",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-08/msg00005.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'Xen';
my $MAIN_PACKAGE = 'xen-tools';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2013:1314-1';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP3) >= 0 && SDP::SUSE::compareKernel(SLE11SP4) < 0 ) {
	%PACKAGES = (
		'xen' => '4.2.2_06-0.7.1',
		'xen-devel' => '4.2.2_06-0.7.1',
		'xen-doc-html' => '4.2.2_06-0.7.1',
		'xen-doc-pdf' => '4.2.2_06-0.7.1',
		'xen-kmp-default' => '4.2.2_06_3.0.82_0.7-0.7.1',
		'xen-kmp-pae' => '4.2.2_06_3.0.82_0.7-0.7.1',
		'xen-libs-32bit' => '4.2.2_06-0.7.1',
		'xen-libs' => '4.2.2_06-0.7.1',
		'xen-tools' => '4.2.2_06-0.7.1',
		'xen-tools-domU' => '4.2.2_06-0.7.1',
	);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

