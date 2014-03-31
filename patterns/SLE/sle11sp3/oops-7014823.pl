#!/usr/bin/perl

# Title:       Detect kernel oops in 3.0.101-0.18.1
# Description: kernel Oops/BUG during network operation
# Modified:    2014 Mar 31
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
"META_CLASS=SLE",
"META_CATEGORY=Kernel",
"META_COMPONENT=Oops",
"PATTERN_ID=$PATTERN_ID",
"PRIMARY_LINK=META_LINK_TID",
"OVERALL=$GSTATUS",
"OVERALL_INFO=NOT SET",
"META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014823",
"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=870801",
);

##############################################################################
# Main Program Execution
##############################################################################

my $AFFECTED_KERNEL = "3.0.101-0.18";

SDP::Core::processOptions();
if ( SDP::SUSE::compareKernel($AFFECTED_KERNEL) == 0 ) {
	SDP::Core::updateStatus(STATUS_CRITICAL, "Kernel susceptible to oops on network operations, update system to apply newest kernel");
} else {
	SDP::Core::updateStatus(STATUS_IGNORE, "Bug fixes applied, not applicable to installed kernel");
}
SDP::Core::printPatternResults();
exit;

