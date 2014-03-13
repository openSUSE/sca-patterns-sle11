#!/usr/bin/perl

# Title:       X Windows Security Advisory SUSE-SA:2011:016
# Description: xorg-x11 updated to fix remote code execution security issues, CVSS v2 Base Score: 9.3
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
	PROPERTY_NAME_COMPONENT."=X",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_Security",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_Security=http://www.novell.com/linux/security/advisories/2011_16_xorg.html"
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my $CHECKING            = 'X Windows';
	my $ADVISORY            = '9.3';
	my $TYPE                = 'Remote code execution';
	my @PKGS_TO_CHECK       = ();
	my $FIXED_VERSION       = '';

	if  ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel(SLE11SP2) < 0 ) {
		@PKGS_TO_CHECK       = qw(xorg-x11 xorg-x11-xauth);
		$FIXED_VERSION       = '7.4-9.39.1';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} elsif ( SDP::SUSE::compareKernel(SLE10SP4) >= 0 && SDP::SUSE::compareKernel(SLE10SP5) < 0 ) {
		@PKGS_TO_CHECK       = qw(xorg-x11 xorg-x11-debuginfo xorg-x11-devel-32bit xorg-x11-devel-64bit xorg-x11-devel xorg-x11-doc xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-cyrillic xorg-x11-fonts-scalable xorg-x11-fonts-syriac xorg-x11-libs-32bit xorg-x11-libs-64bit xorg-x11-libs xorg-x11-libs-x86 xorg-x11-man xorg-x11-sdk xorg-x11-server xorg-x11-server-glx xorg-x11-Xnest xorg-x11-Xvfb xorg-x11-Xvnc);
		$FIXED_VERSION       = '6.9.0-50.74.1';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} elsif ( SDP::SUSE::compareKernel(SLE10SP3) >= 0 && SDP::SUSE::compareKernel(SLE10SP4) < 0 ) {
		my %HOST_INFO = SDP::SUSE::getHostInfo();
		if ( $HOST_INFO{'architecture'} eq "s390x" ) {
			@PKGS_TO_CHECK       = qw(xorg-x11 xorg-x11-devel xorg-x11-doc xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-cyrillic xorg-x11-fonts-scalable xorg-x11-fonts-syriac xorg-x11-libs xorg-x11-man xorg-x11-Xnest xorg-x11-Xvfb xorg-x11-Xvnc);
			$FIXED_VERSION       = '6.9.0-50.68.70.8';
		} elsif ( $HOST_INFO{'architecture'} eq "x86_64" ) {
			@PKGS_TO_CHECK       = qw(xorg-x11 xorg-x11-debuginfo xorg-x11-devel xorg-x11-doc xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-cyrillic xorg-x11-fonts-scalable xorg-x11-fonts-syriac xorg-x11-libs xorg-x11-man xorg-x11-sdk xorg-x11-server xorg-x11-server-glx xorg-x11-Xnest xorg-x11-Xvfb xorg-x11-Xvnc);
			$FIXED_VERSION       = '6.9.0-50.68.70.3';
		} else {
			@PKGS_TO_CHECK       = qw(xorg-x11 xorg-x11-debuginfo xorg-x11-devel xorg-x11-fonts-100dpi xorg-x11-fonts-75dpi xorg-x11-fonts-cyrillic xorg-x11-fonts-scalable xorg-x11-fonts-syriac xorg-x11-libs xorg-x11-man xorg-x11-server xorg-x11-server-glx xorg-x11-Xnest xorg-x11-Xvfb xorg-x11-Xvnc);
			$FIXED_VERSION       = '6.9.0-50.68.70.1';
		}
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} elsif ( SDP::SUSE::compareKernel(SLE9GA) >= 0 && SDP::SUSE::compareKernel(SLE10GA) < 0 ) {
		@PKGS_TO_CHECK       = qw(km_drm XFree86 XFree86-devel XFree86-doc XFree86-driver-options XFree86-fonts-100dpi XFree86-fonts-75dpi XFree86-fonts-cyrillic XFree86-fonts-scalable XFree86-fonts-syriac XFree86-libs XFree86-man XFree86-Mesa XFree86-Mesa-devel XFree86-server XFree86-server-glx XFree86-Xnest XFree86-Xprt XFree86-Xvfb XFree86-Xvnc);
		$FIXED_VERSION       = '4.3.99.902-43.105';
		SDP::SUSE::securitySeverityPackageCheck($CHECKING, $ADVISORY, $TYPE, \@PKGS_TO_CHECK, $FIXED_VERSION);
	} else {
		SDP::Core::printDebug('DISTRIBUTION', 'None Selected');
		SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: $CHECKING Security Advisory: Outside the kernel scope");
	}

SDP::Core::printPatternResults();

exit;
