#!/usr/bin/perl

# Title:       LTSS Firefox SA SUSE-SU-2013:0292-1
# Description: Resolves 5 vulnerabilities
# Modified:    2013 Jun 27

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
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

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
	PROPERTY_NAME_COMPONENT."=Firefox",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-02/msg00008.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $NAME = 'LTSS Firefox';
	my $MAIN_PACKAGE = 'MozillaFirefox';
	my $SEVERITY = 'Important';
	my $TAG = 'SUSE-SU-2013:0292-1';
	my %PACKAGES = ();
	if ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel(SLE11SP2) < 0 ) {
		%PACKAGES = (
			'libfreebl3' => '3.14.1-0.3.1',
			'libfreebl3-32bit' => '3.14.1-0.3.1',
			'MozillaFirefox' => '10.0.12-0.4.3',
			'MozillaFirefox-branding-SLED-7' => '0.6.7.103',
			'MozillaFirefox-branding-SLES-for-VMware-7' => '0.4.2.102',
			'MozillaFirefox-translations' => '10.0.12-0.4.3',
			'mozilla-nspr-32bit' => '4.9.4-0.3.1',
			'mozilla-nspr' => '4.9.4-0.3.1',
			'mozilla-nss' => '3.14.1-0.3.1',
			'mozilla-nss-32bit' => '3.14.1-0.3.1',
			'mozilla-nss-tools' => '3.14.1-0.3.1',
		);
		SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
	}
SDP::Core::printPatternResults();

exit;

