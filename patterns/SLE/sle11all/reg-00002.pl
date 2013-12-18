#!/usr/bin/perl

# Title:       Repositories are not registered after running suse_register
# Description: After a successful execution of suse_register against a Subscription Management Tool (SMT), server the update repositories are not visible.
# Modified:    2013 Jun 25

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
#

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
	PROPERTY_NAME_CLASS."=SLE",
	PROPERTY_NAME_CATEGORY."=Update",
	PROPERTY_NAME_COMPONENT."=Registration",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7003779"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub updateReposVisible {
	SDP::Core::printDebug('> updateReposVisible', 'BEGIN');
	my $RCODE = 1; # All repos are visible
	my $FILE_OPEN = 'updates.txt';
	my $SECTION = 'zypper --non-interactive --no-gpg-checks service-list';
	my @CONTENT = ();
	my @LINE_CONTENT = ();
	my @NO_SERVICE = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( /^\s*$/ );                  # Skip blank lines
			next if ( /^\D/ ); # Skip non-digit lines
			@LINE_CONTENT = split(/\s+\|\s+/, $_);
			if ( $LINE_CONTENT[5] =~ /NONE/i && $LINE_CONTENT[3] =~ /yes/i ) {
				SDP::Core::printDebug("TAKE ACTION ON", $_);
				SDP::Core::updateStatus(STATUS_WARNING, "Update Repository NOT Visible: $LINE_CONTENT[2]");
				$RCODE = 0;
				push(@NO_SERVICE, $LINE_CONTENT[2]);
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	if ( $RCODE ) {
		SDP::Core::updateStatus(STATUS_ERROR, "All Update Repositories Appear Visible");
	} else {
		SDP::Core::updateStatus(STATUS_CRITICAL, "Manual Action Required, Update Repositories NOT Visible: @NO_SERVICE");
	}
	SDP::Core::printDebug("< updateReposVisible", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 ) {
		updateReposVisible();
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, 'Outside kernel scope, requires SLE11 or greater');
	}
SDP::Core::printPatternResults();

exit;

