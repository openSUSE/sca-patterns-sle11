#!/usr/bin/perl

# Title:       Kernel SA Important SUSE-SU-2013:1748-1
# Description: Solves one vulnerability and has 42 fixes SLE11 SP2
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
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
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
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-11/msg00021.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'Kernel';
my $MAIN_PACKAGE = '';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2013:1748-1';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
	%PACKAGES = (
		'cluster-network-kmp-default' => '1.4_3.0.101_0.5-2.18.69',
		'cluster-network-kmp-pae' => '1.4_3.0.101_0.5-2.18.69',
		'cluster-network-kmp-ppc64' => '1.4_3.0.101_0.5-2.18.69',
		'cluster-network-kmp-trace' => '1.4_3.0.101_0.5-2.18.69',
		'cluster-network-kmp-xen' => '1.4_3.0.101_0.5-2.18.69',
		'gfs2-kmp-default-2_3.0.101_0.5' => '0.7.98',
		'gfs2-kmp-pae-2_3.0.101_0.5' => '0.7.98',
		'gfs2-kmp-ppc64-2_3.0.101_0.5' => '0.7.98',
		'gfs2-kmp-trace-2_3.0.101_0.5' => '0.7.98',
		'gfs2-kmp-xen-2_3.0.101_0.5' => '0.7.98',
		'kernel-default' => '3.0.101-0.5.1',
		'kernel-default-base' => '3.0.101-0.5.1',
		'kernel-default-devel' => '3.0.101-0.5.1',
		'kernel-default-extra' => '3.0.101-0.5.1',
		'kernel-default-man' => '3.0.101-0.5.1',
		'kernel-ec2' => '3.0.101-0.5.1',
		'kernel-ec2-base' => '3.0.101-0.5.1',
		'kernel-ec2-devel' => '3.0.101-0.5.1',
		'kernel-pae' => '3.0.101-0.5.1',
		'kernel-pae-base' => '3.0.101-0.5.1',
		'kernel-pae-devel' => '3.0.101-0.5.1',
		'kernel-pae-extra' => '3.0.101-0.5.1',
		'kernel-ppc64' => '3.0.101-0.5.1',
		'kernel-ppc64-base' => '3.0.101-0.5.1',
		'kernel-ppc64-devel' => '3.0.101-0.5.1',
		'kernel-source' => '3.0.101-0.5.1',
		'kernel-syms' => '3.0.101-0.5.1',
		'kernel-trace' => '3.0.101-0.5.1',
		'kernel-trace-base' => '3.0.101-0.5.1',
		'kernel-trace-devel' => '3.0.101-0.5.1',
		'kernel-trace-extra' => '3.0.101-0.5.1',
		'kernel-xen' => '3.0.101-0.5.1',
		'kernel-xen-base' => '3.0.101-0.5.1',
		'kernel-xen-devel' => '3.0.101-0.5.1',
		'kernel-xen-extra' => '3.0.101-0.5.1',
		'ocfs2-kmp-default' => '1.6_3.0.101_0.5-0.11.68',
		'ocfs2-kmp-pae' => '1.6_3.0.101_0.5-0.11.68',
		'ocfs2-kmp-ppc64' => '1.6_3.0.101_0.5-0.11.68',
		'ocfs2-kmp-trace' => '1.6_3.0.101_0.5-0.11.68',
		'ocfs2-kmp-xen' => '1.6_3.0.101_0.5-0.11.68',
		'xen-kmp-default' => '4.1.6_02_3.0.101_0.5-0.5.5',
		'xen-kmp-pae' => '4.1.6_02_3.0.101_0.5-0.5.5',
		'xen-kmp-trace' => '4.1.6_02_3.0.101_0.5-0.5.5',
	);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

