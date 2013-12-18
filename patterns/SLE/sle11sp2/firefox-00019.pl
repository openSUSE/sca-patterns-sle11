#!/usr/bin/perl

# Title:       Firefox SA SUSE-SU-2013:0410-1
# Description: Fixes 9 vulnerabilities
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
	PROPERTY_NAME_COMPONENT."=Firefox",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-03/msg00008.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $NAME = 'Firefox';
	my $MAIN_PACKAGE = 'MozillaFirefox';
	my $SEVERITY = 'Important';
	my $TAG = 'SUSE-SU-2013:0410-1';
	my %PACKAGES = ();
	if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
		%PACKAGES = (
			'beagle' => '0.3.8-56.51.1',
			'beagle-devel' => '0.3.8-56.51.1',
			'beagle-evolution' => '0.3.8-56.51.1',
			'beagle-firefox' => '0.3.8-56.51.1',
			'beagle-gui' => '0.3.8-56.51.1',
			'beagle-lang' => '0.3.8-56.51.1',
			'libfreebl3' => '3.14.2-0.4.3.2',
			'libfreebl3-32bit' => '3.14.2-0.4.3.2',
			'libfreebl3-x86' => '3.14.2-0.4.3.2',
			'mhtml-firefox' => '0.5-1.47.51.5',
			'MozillaFirefox' => '17.0.3esr-0.4.4.1',
			'MozillaFirefox-branding-SLED-7' => '0.6.9.5',
			'MozillaFirefox-translations' => '17.0.3esr-0.4.4.1',
			'mozilla-nspr-32bit' => '4.9.5-0.3.2',
			'mozilla-nspr' => '4.9.5-0.3.2',
			'mozilla-nspr-devel' => '4.9.5-0.3.2',
			'mozilla-nspr-x86' => '4.9.5-0.3.2',
			'mozilla-nss' => '3.14.2-0.4.3.2',
			'mozilla-nss-32bit' => '3.14.2-0.4.3.2',
			'mozilla-nss-devel' => '3.14.2-0.4.3.2',
			'mozilla-nss-tools' => '3.14.2-0.4.3.2',
			'mozilla-nss-x86' => '3.14.2-0.4.3.2',		);
		SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
	}
SDP::Core::printPatternResults();

exit;

