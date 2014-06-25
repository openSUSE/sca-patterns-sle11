#!/usr/bin/perl

# Title:       OpenSSL 1.0 Security Module SA Critical SUSE-SU-2014:0762-1
# Description: fixes 5 vulnerabilities
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
"META_COMPONENT=OpenSSL SM",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_Security",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-06/msg00006.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'OpenSSL SM';
my $MAIN_PACKAGE = '';
my $SEVERITY = 'Critical';
my $TAG = 'SUSE-SU-2014:0762-1';
my	%PACKAGES = (
		'libopenssl1_0_0' => '1.0.1g-0.16.1',
		'libopenssl1_0_0-32bit' => '1.0.1g-0.16.1',
		'libopenssl1_0_0-x86' => '1.0.1g-0.16.1',
		'libopenssl1-devel' => '1.0.1g-0.16.1',
		'openssl1' => '1.0.1g-0.16.1',
		'openssl1-doc' => '1.0.1g-0.16.1',
	);
SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
SDP::Core::printPatternResults();

exit;

