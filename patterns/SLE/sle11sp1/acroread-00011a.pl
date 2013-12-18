#!/usr/bin/perl

# Title:       Acrobat Reader Security Advisory SUSE-SA:2011:044
# Description: Acrobat Reader was updated to fix remote code execution security issues, CVSS v2 Base Score: 6.8
# Modified:    2013 Jun 26

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
	PROPERTY_NAME_COMPONENT."=Acroread",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://www.suse.com/support/security/advisories/2011_44_acroread.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $CHECKING = 'Acroread';
	my $SEVERITY = '6.8';
	my $TYPE = 'Remote code execution';
	my @PKGS_TO_CHECK = ();
	my $FIXED_VERSION = '';
	if ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel(SLE11SP2) < 0 ) {
		@PKGS_TO_CHECK       = qw(acroread acroread-cmaps acroread-fonts-ja acroread-fonts-ko acroread-fonts-zh_CN acroread-fonts-zh_TW);
		$FIXED_VERSION       = '9.4.6-0.2.1';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} elsif ( SDP::SUSE::compareKernel(SLE10SP4) >= 0 && SDP::SUSE::compareKernel(SLE10SP5) < 0 ) {
		@PKGS_TO_CHECK       = qw(acroread acroread-cmaps acroread-fonts-ja acroread-fonts-ko acroread-fonts-zh_CN acroread-fonts-zh_TW);
		$FIXED_VERSION       = '9.4.6-0.5.1';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $SEVERITY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: Outside the kernel scope");
	}
SDP::Core::printPatternResults();

exit;

