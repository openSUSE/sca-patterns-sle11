#!/usr/bin/perl

# Title:       Firefox SA Important SUSE-SU-2013:1678-1 SLE11SP2
# Description: Fixes one vulnerability
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
"META_COMPONENT=Firefox",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_Security",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-11/msg00014.html",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
my $NAME = 'Firefox';
my $MAIN_PACKAGE = 'MozillaFirefox';
my $SEVERITY = 'Important';
my $TAG = 'SUSE-SU-2013:1678-1';
my %PACKAGES = ();
if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
	%PACKAGES = (
		'libfreebl3' => '3.15.2-0.3.1',
		'libfreebl3-32bit' => '3.15.2-0.3.1',
		'libfreebl3-x86' => '3.15.2-0.3.1',
		'MozillaFirefox' => '17.0.10esr-0.4.2.4',
		'MozillaFirefox-branding-SLED-7' => '0.6.9.62',
		'MozillaFirefox-translations' => '17.0.10esr-0.4.2.4',
		'mozilla-nspr-32bit' => '4.10.1-0.3.1',
		'mozilla-nspr' => '4.10.1-0.3.1',
		'mozilla-nspr-devel' => '4.10.1-0.3.1',
		'mozilla-nspr-x86' => '4.10.1-0.3.1',
		'mozilla-nss' => '3.15.2-0.3.1',
		'mozilla-nss-32bit' => '3.15.2-0.3.1',
		'mozilla-nss-devel' => '3.15.2-0.3.1',
		'mozilla-nss-tools' => '3.15.2-0.3.1',
		'mozilla-nss-x86' => '3.15.2-0.3.1',
	);
	SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
}
SDP::Core::printPatternResults();

exit;

