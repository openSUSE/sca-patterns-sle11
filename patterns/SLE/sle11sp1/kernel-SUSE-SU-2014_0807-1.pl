#!/usr/bin/perl

# Title:       Kernel SA Important SUSE-SU-2014:0807-1
# Description: solves 17 vulnerabilities and has 9 fixes
# Modified:    2014 Jun 25
#
##############################################################################
# Copyright (C) 2014 SUSE LLC
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
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-06/msg00022.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'Kernel';
my $MAIN_PACKAGE = '';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2014:0807-1';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel(SLE11SP2) < 0 ) {
	%PACKAGES = (
		'btrfs-kmp-default-0_2.6.32.59_0.13' => '0.3.163',
		'btrfs-kmp-pae-0_2.6.32.59_0.13' => '0.3.163',
		'btrfs-kmp-xen-0_2.6.32.59_0.13' => '0.3.163',
		'ext4dev-kmp-default-0_2.6.32.59_0.13' => '7.9.130',
		'ext4dev-kmp-pae-0_2.6.32.59_0.13' => '7.9.130',
		'ext4dev-kmp-trace-0_2.6.32.59_0.13' => '7.9.130',
		'ext4dev-kmp-xen-0_2.6.32.59_0.13' => '7.9.130',
		'hyper-v-kmp-default-0_2.6.32.59_0.13' => '0.18.39',
		'hyper-v-kmp-pae-0_2.6.32.59_0.13' => '0.18.39',
		'hyper-v-kmp-trace-0_2.6.32.59_0.13' => '0.18.39',
		'kernel-default' => '2.6.32.59-0.13.1',
		'kernel-default-base' => '2.6.32.59-0.13.1',
		'kernel-default-devel' => '2.6.32.59-0.13.1',
		'kernel-default-extra' => '2.6.32.59-0.13.1',
		'kernel-default-man' => '2.6.32.59-0.13.1',
		'kernel-ec2' => '2.6.32.59-0.13.1',
		'kernel-ec2-base' => '2.6.32.59-0.13.1',
		'kernel-ec2-devel' => '2.6.32.59-0.13.1',
		'kernel-pae' => '2.6.32.59-0.13.1',
		'kernel-pae-base' => '2.6.32.59-0.13.1',
		'kernel-pae-devel' => '2.6.32.59-0.13.1',
		'kernel-pae-extra' => '2.6.32.59-0.13.1',
		'kernel-source' => '2.6.32.59-0.13.1',
		'kernel-syms' => '2.6.32.59-0.13.1',
		'kernel-trace' => '2.6.32.59-0.13.1',
		'kernel-trace-base' => '2.6.32.59-0.13.1',
		'kernel-trace-devel' => '2.6.32.59-0.13.1',
		'kernel-xen' => '2.6.32.59-0.13.1',
		'kernel-xen-base' => '2.6.32.59-0.13.1',
		'kernel-xen-devel' => '2.6.32.59-0.13.1',
		'kernel-xen-extra' => '2.6.32.59-0.13.1',
	);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

