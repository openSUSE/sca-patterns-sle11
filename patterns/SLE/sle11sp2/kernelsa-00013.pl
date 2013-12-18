#!/usr/bin/perl

# Title:       Kernel SA SUSE-SU-2013:0845-1
# Description: Fixes one vulnerability
# Modified:    2013 Jun 25

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
	PROPERTY_NAME_COMPONENT."=Kernel",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-05/msg00017.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $NAME = 'Kernel';
	my $MAIN_PACKAGE = '';
	my $SEVERITY = 'Critical';
	my $TAG = 'SUSE-SU-2013:0845-1';
	my %PACKAGES = ();
	if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
		%PACKAGES = (
			'cluster-network-kmp-default' => '1.4_3.0.74_0.6.10-2.18.41',
			'cluster-network-kmp-pae' => '1.4_3.0.74_0.6.10-2.18.41',
			'cluster-network-kmp-ppc64' => '1.4_3.0.74_0.6.10-2.18.41',
			'cluster-network-kmp-rt' => '1.4_3.0.74_rt98_0.6.6-2.18.42',
			'cluster-network-kmp-rt_trace' => '1.4_3.0.74_rt98_0.6.6-2.18.42',
			'cluster-network-kmp-trace' => '1.4_3.0.74_0.6.10-2.18.41',
			'cluster-network-kmp-xen' => '1.4_3.0.74_0.6.10-2.18.41',
			'drbd-kmp-rt' => '8.4.2_3.0.74_rt98_0.6.6-0.6.6.33',
			'drbd-kmp-rt_trace' => '8.4.2_3.0.74_rt98_0.6.6-0.6.6.33',
			'ext4-writeable-kmp-default' => '0_3.0.74_0.6.10-0.14.54',
			'ext4-writeable-kmp-pae' => '0_3.0.74_0.6.10-0.14.54',
			'ext4-writeable-kmp-ppc64' => '0_3.0.74_0.6.10-0.14.54',
			'ext4-writeable-kmp-trace' => '0_3.0.74_0.6.10-0.14.54',
			'ext4-writeable-kmp-xen' => '0_3.0.74_0.6.10-0.14.54',
			'gfs2-kmp-default' => '2_3.0.74_0.6.10-0.7.73',
			'gfs2-kmp-pae' => '2_3.0.74_0.6.10-0.7.73',
			'gfs2-kmp-ppc64' => '2_3.0.74_0.6.10-0.7.73',
			'gfs2-kmp-trace' => '2_3.0.74_0.6.10-0.7.73',
			'gfs2-kmp-xen' => '2_3.0.74_0.6.10-0.7.73',
			'iscsitarget-kmp-rt' => '1.4.20_3.0.74_rt98_0.6.6-0.23.39',
			'iscsitarget-kmp-rt_trace' => '1.4.20_3.0.74_rt98_0.6.6-0.23.39',
			'kernel-default' => '3.0.74-0.6.10.1',
			'kernel-default-base' => '3.0.74-0.6.10.1',
			'kernel-default-devel' => '3.0.74-0.6.10.1',
			'kernel-default-extra' => '3.0.74-0.6.10.1',
			'kernel-default-man' => '3.0.74-0.6.10.1',
			'kernel-ec2' => '3.0.74-0.6.10.1',
			'kernel-ec2-base' => '3.0.74-0.6.10.1',
			'kernel-ec2-devel' => '3.0.74-0.6.10.1',
			'kernel-pae' => '3.0.74-0.6.10.1',
			'kernel-pae-base' => '3.0.74-0.6.10.1',
			'kernel-pae-devel' => '3.0.74-0.6.10.1',
			'kernel-pae-extra' => '3.0.74-0.6.10.1',
			'kernel-ppc64' => '3.0.74-0.6.10.1',
			'kernel-ppc64-base' => '3.0.74-0.6.10.1',
			'kernel-ppc64-devel' => '3.0.74-0.6.10.1',
			'kernel-ppc64-extra' => '3.0.74-0.6.10.1',
			'kernel-rt' => '3.0.74.rt98-0.6.6.1',
			'kernel-rt-base' => '3.0.74.rt98-0.6.6.1',
			'kernel-rt-devel' => '3.0.74.rt98-0.6.6.1',
			'kernel-rt_trace' => '3.0.74.rt98-0.6.6.1',
			'kernel-rt_trace-base' => '3.0.74.rt98-0.6.6.1',
			'kernel-rt_trace-devel' => '3.0.74.rt98-0.6.6.1',
			'kernel-source' => '3.0.74-0.6.10.1',
			'kernel-source-rt' => '3.0.74.rt98-0.6.6.1',
			'kernel-syms' => '3.0.74-0.6.10.1',
			'kernel-syms-rt' => '3.0.74.rt98-0.6.6.1',
			'kernel-trace' => '3.0.74-0.6.10.1',
			'kernel-trace-base' => '3.0.74-0.6.10.1',
			'kernel-trace-devel' => '3.0.74-0.6.10.1',
			'kernel-trace-extra' => '3.0.74-0.6.10.1',
			'kernel-xen' => '3.0.74-0.6.10.1',
			'kernel-xen-base' => '3.0.74-0.6.10.1',
			'kernel-xen-devel' => '3.0.74-0.6.10.1',
			'kernel-xen-extra' => '3.0.74-0.6.10.1',
			'lttng-modules-kmp-rt' => '2.0.4_3.0.74_rt98_0.6.6-0.7.33',
			'lttng-modules-kmp-rt_trace' => '2.0.4_3.0.74_rt98_0.6.6-0.7.33',
			'ocfs2-kmp-default' => '1.6_3.0.74_0.6.10-0.11.40',
			'ocfs2-kmp-pae' => '1.6_3.0.74_0.6.10-0.11.40',
			'ocfs2-kmp-ppc64' => '1.6_3.0.74_0.6.10-0.11.40',
			'ocfs2-kmp-rt' => '1.6_3.0.74_rt98_0.6.6-0.11.41',
			'ocfs2-kmp-rt_trace' => '1.6_3.0.74_rt98_0.6.6-0.11.41',
			'ocfs2-kmp-trace' => '1.6_3.0.74_0.6.10-0.11.40',
			'ocfs2-kmp-xen' => '1.6_3.0.74_0.6.10-0.11.40',
			'ofed-kmp-rt' => '1.5.2_3.0.74_rt98_0.6.6-0.28.28.13',
			'ofed-kmp-rt_trace' => '1.5.2_3.0.74_rt98_0.6.6-0.28.28.13',
			'xen-kmp-default' => '4.1.4_02_3.0.74_0.6.10-0.5.32',
			'xen-kmp-trace' => '4.1.4_02_3.0.74_0.6.10-0.5.32',
		);
		SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
	}
SDP::Core::printPatternResults();

exit;

