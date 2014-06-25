#!/usr/bin/perl

# Title:       Kernel SA Important SUSE-SU-2014:0837-2
# Description: fixes one vulnerability
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
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-06/msg00028.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'LTSS Kernel';
my $MAIN_PACKAGE = '';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2014:0837-2';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
	%PACKAGES = (
		'kernel-default' => '3.0.101-0.7.21.1',
		'kernel-default-base' => '3.0.101-0.7.21.1',
		'kernel-default-devel' => '3.0.101-0.7.21.1',
		'kernel-default-man' => '3.0.101-0.7.21.1',
		'kernel-ec2' => '3.0.101-0.7.21.1',
		'kernel-ec2-base' => '3.0.101-0.7.21.1',
		'kernel-ec2-devel' => '3.0.101-0.7.21.1',
		'kernel-pae' => '3.0.101-0.7.21.1',
		'kernel-pae-base' => '3.0.101-0.7.21.1',
		'kernel-pae-devel' => '3.0.101-0.7.21.1',
		'kernel-source' => '3.0.101-0.7.21.1',
		'kernel-syms' => '3.0.101-0.7.21.1',
		'kernel-trace' => '3.0.101-0.7.21.1',
		'kernel-trace-base' => '3.0.101-0.7.21.1',
		'kernel-trace-devel' => '3.0.101-0.7.21.1',
		'kernel-xen' => '3.0.101-0.7.21.1',
		'kernel-xen-base' => '3.0.101-0.7.21.1',
		'kernel-xen-devel' => '3.0.101-0.7.21.1',
		'xen-kmp-default' => '4.1.6_06_3.0.101_0.7.21-0.5.16',
		'xen-kmp-pae' => '4.1.6_06_3.0.101_0.7.21-0.5.16',
		'xen-kmp-trace' => '4.1.6_06_3.0.101_0.7.21-0.5.16',
	);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

