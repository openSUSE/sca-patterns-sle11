#!/usr/bin/perl

# Title:       Bind SA Important SUSE-SU-2013:1310-1
# Description: Fixes one vulnerability
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
"META_COMPONENT=Bind",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_Security",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-08/msg00004.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'Bind';
my $MAIN_PACKAGE = 'bind';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2013:1310-1';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
	%PACKAGES = (
		'bind' => '9.9.3P2-0.5.1',
		'bind-chrootenv' => '9.9.3P2-0.5.1',
		'bind-devel-32bit' => '9.9.3P2-0.5.1',
		'bind-devel' => '9.9.3P2-0.5.1',
		'bind-doc' => '9.9.3P2-0.5.1',
		'bind-libs-32bit' => '9.9.3P2-0.5.1',
		'bind-libs' => '9.9.3P2-0.5.1',
		'bind-libs-x86' => '9.9.3P2-0.5.1',
		'bind-utils' => '9.9.3P2-0.5.1',
	);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

