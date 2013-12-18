#!/usr/bin/perl

# Title:       PCP SA SUSE-SU-2013:0190-1
# Description: Solves four vulnerabilities and has two fixes
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
	PROPERTY_NAME_COMPONENT."=PCP",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2013-01/msg00024.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $NAME = 'PCP';
	my $MAIN_PACKAGE = 'pcp';
	my $SEVERITY = 'Important';
	my $TAG = 'SUSE-SU-2013:0190-1';
	my %PACKAGES = ();
	if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP3) < 0 ) {
		%PACKAGES = (
			'libpcp3' => '3.6.10-0.3.1',
			'pcp' => '3.6.10-0.3.1',
			'pcp-devel' => '3.6.10-0.3.1',
			'pcp-import-iostat2pcp' => '3.6.10-0.3.1',
			'pcp-import-mrtg2pcp' => '3.6.10-0.3.1',
			'pcp-import-sar2pcp' => '3.6.10-0.3.1',
			'pcp-import-sheet2pcp' => '3.6.10-0.3.1',
			'perl-PCP-LogImport' => '3.6.10-0.3.1',
			'perl-PCP-LogSummary' => '3.6.10-0.3.1',
			'perl-PCP-MMV' => '3.6.10-0.3.1',
			'perl-PCP-PMDA' => '3.6.10-0.3.1',
			'permissions' => '2013.1.7-0.3.1',
		);
		SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
	} elsif ( SDP::SUSE::compareKernel(SLE10SP4) >= 0 && SDP::SUSE::compareKernel(SLE10SP5) < 0 ) {
		%PACKAGES = (
			'libpcp3' => '3.6.10-0.5.1',
			'pcp' => '3.6.10-0.5.1',
			'pcp-devel' => '3.6.10-0.5.1',
			'pcp-import-iostat2pcp' => '3.6.10-0.5.1',
			'pcp-import-mrtg2pcp' => '3.6.10-0.5.1',
			'pcp-import-sar2pcp' => '3.6.10-0.5.1',
			'pcp-import-sheet2pcp' => '3.6.10-0.5.1',
			'perl-PCP-LogImport' => '3.6.10-0.5.1',
			'perl-PCP-LogSummary' => '3.6.10-0.5.1',
			'perl-PCP-MMV' => '3.6.10-0.5.1',
			'perl-PCP-PMDA' => '3.6.10-0.5.1',
			'permissions' => '2013.1.7-0.5.1',
		);
		SDP::SUSE::securityAnnouncementPackageCheck($NAME, $MAIN_PACKAGE, $SEVERITY, $TAG, \%PACKAGES);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: $NAME Security Announcement: Outside the kernel scope");
	}
SDP::Core::printPatternResults();

exit;

