#!/usr/bin/perl

# Title:       Update failure after migration
# Description: Attempting to register or run a zypper ref returns Valid metadata not found at specified URL(s)
# Modified:    2013 Oct 11
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
"META_CLASS=SLE",
"META_CATEGORY=Update",
"META_COMPONENT=Registration",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_TID",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7013434",
);

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel(SLE11SP4) < 0) {
	my @CHECK_PACKAGES = qw(libgpg-error0 libgpg-error0-32bit);
	my $RPM_NAME = '';
	my $VERSION_TO_COMPARE = '1.6-8.6';
	my $WARNING = 0;
	foreach $RPM_NAME (@CHECK_PACKAGES) {
		my $RPM_COMPARISON = SDP::SUSE::compareRpm($RPM_NAME, $VERSION_TO_COMPARE);
		if ( $RPM_COMPARISON == 0 ) {
			$WARNING = 1;
		}
	}
	if ( $WARNING > 0 ) {
		SDP::Core::updateStatus(STATUS_CRITICAL, "Repository registration failure, update packages: @CHECK_PACKAGES suse-build-key");
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Repository registration per valid @CHECK_PACKAGES packages");
	}
} else {
	SDP::Core::updateStatus(STATUS_ERROR, "Outside kernel scope, skipping registration error");
}
SDP::Core::printPatternResults();
exit;


