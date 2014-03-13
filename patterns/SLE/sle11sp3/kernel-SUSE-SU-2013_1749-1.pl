#!/usr/bin/perl

# Title:       Kernel SA Important SUSE-SU-2013:1749-1
# Description: Solves one vulnerability and has 70 fixes SLE11 SP3
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
"META_COMPONENT=Kernel",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_Security",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-11/msg00023.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'Kernel';
my $MAIN_PACKAGE = '';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2013:1749-1';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP3) >= 0 && SDP::SUSE::compareKernel(SLE11SP4) < 0 ) {
	%PACKAGES = (
		'cluster-network-kmp-default' => '1.4_3.0.101_0.8-2.27.22',
		'cluster-network-kmp-pae' => '1.4_3.0.101_0.8-2.27.22',
		'cluster-network-kmp-ppc64' => '1.4_3.0.101_0.8-2.27.22',
		'cluster-network-kmp-trace' => '1.4_3.0.101_0.8-2.27.22',
		'cluster-network-kmp-xen' => '1.4_3.0.101_0.8-2.27.22',
		'gfs2-kmp-default-2_3.0.101_0.8' => '0.16.28',
		'gfs2-kmp-pae-2_3.0.101_0.8' => '0.16.28',
		'gfs2-kmp-ppc64-2_3.0.101_0.8' => '0.16.28',
		'gfs2-kmp-trace-2_3.0.101_0.8' => '0.16.28',
		'gfs2-kmp-xen-2_3.0.101_0.8' => '0.16.28',
		'kernel-default' => '3.0.101-0.8.1',
		'kernel-default-base' => '3.0.101-0.8.1',
		'kernel-default-devel' => '3.0.101-0.8.1',
		'kernel-default-extra' => '3.0.101-0.8.1',
		'kernel-default-man' => '3.0.101-0.8.1',
		'kernel-ec2' => '3.0.101-0.8.1',
		'kernel-ec2-base' => '3.0.101-0.8.1',
		'kernel-ec2-devel' => '3.0.101-0.8.1',
		'kernel-pae' => '3.0.101-0.8.1',
		'kernel-pae-base' => '3.0.101-0.8.1',
		'kernel-pae-devel' => '3.0.101-0.8.1',
		'kernel-pae-extra' => '3.0.101-0.8.1',
		'kernel-ppc64' => '3.0.101-0.8.1',
		'kernel-ppc64-base' => '3.0.101-0.8.1',
		'kernel-ppc64-devel' => '3.0.101-0.8.1',
		'kernel-source' => '3.0.101-0.8.1',
		'kernel-syms' => '3.0.101-0.8.1',
		'kernel-trace' => '3.0.101-0.8.1',
		'kernel-trace-base' => '3.0.101-0.8.1',
		'kernel-trace-devel' => '3.0.101-0.8.1',
		'kernel-xen' => '3.0.101-0.8.1',
		'kernel-xen-base' => '3.0.101-0.8.1',
		'kernel-xen-devel' => '3.0.101-0.8.1',
		'kernel-xen-extra' => '3.0.101-0.8.1',
		'ocfs2-kmp-default' => '1.6_3.0.101_0.8-0.20.22',
		'ocfs2-kmp-pae' => '1.6_3.0.101_0.8-0.20.22',
		'ocfs2-kmp-ppc64' => '1.6_3.0.101_0.8-0.20.22',
		'ocfs2-kmp-trace' => '1.6_3.0.101_0.8-0.20.22',
		'ocfs2-kmp-xen' => '1.6_3.0.101_0.8-0.20.22',
		'xen-kmp-default' => '4.2.3_02_3.0.101_0.8-0.7.9',
		'xen-kmp-pae' => '4.2.3_02_3.0.101_0.8-0.7.9',
	);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

