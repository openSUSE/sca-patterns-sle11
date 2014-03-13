#!/usr/bin/perl -w

# Title:       Checks Subscription to SLE11 Update Channel
# Description: The server must be subscribed to an update channel to receive updates. 
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
#  along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#     Jason Record (jrecord@suse.com)
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
	PROPERTY_NAME_CLASS."=SLE",
	PROPERTY_NAME_CATEGORY."=Update",
	PROPERTY_NAME_COMPONENT."=Subscription",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7000387"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub check_subscribed_channel() {
	SDP::Core::printDebug('> check_subscribed_channel', 'BEGIN');
	my $FILE_OPEN = 'updates.txt';
	my $SECTION = 'zypper --non-interactive --no-gpg-checks repos';
	my @CONTENT = ();
	my @LINE_CONTENT = ();
	my $UP_SLE = '';
	my $UPE_SLE = -1; # no channel
	my $UPR_SLE = 0; # channel refresh disabled

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( /^\s*$/ ); # Skip blank lines
			next if ( /-*\+-*\+-*/ ); # skip header line
			next if ( /waking up zmd/i);
			$_ =~ s/\s+\|\s+/\|/g; # remove white space
			$_ =~ s/^\s+|\s+$//g;
			# get the update channels needed if subscribed to them
			@LINE_CONTENT = split(/\|/, $_);
			if ( $LINE_CONTENT[2] =~ /SLE.11.*-Updates/i ) {
				if ( $LINE_CONTENT[3] =~ /yes|ja/i ) {
					$UPE_SLE = 1; # channel enabled
					if ( $LINE_CONTENT[4] =~ /yes|ja/i ) {
						$UPR_SLE = 1; # channel refresh enabled
					}
				} else {
					$UPE_SLE = 0; # channel disabled
				}
				$UP_SLE = $LINE_CONTENT[1];
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	if ( $UPE_SLE == 1 ) {
		if ( $UPR_SLE > 0 ) {
			SDP::Core::updateStatus(STATUS_ERROR, "$UP_SLE is enabled and refreshes");
		} else {
			SDP::Core::updateStatus(STATUS_CRITICAL, "$UP_SLE is enabled, but refresh is disabled");
		}
	} elsif ( $UPE_SLE == 0 ) {
		SDP::Core::updateStatus(STATUS_CRITICAL, "$UP_SLE is registered but not enabled");
	} else {
		SDP::Core::updateStatus(STATUS_CRITICAL, "Server is not registered or subscribed to an update channel");
	}
	SDP::Core::printDebug('< check_subscribed_channel', "Returns: $UPE_SLE");
	return $UPE_SLE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( compareKernel(SLE11GA) >= 0 && compareKernel(SLE12GA) < 0 ) {
		check_subscribed_channel();
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Outside the kernel scope, requires SLE11GA to SLE12GA");
	}
SDP::Core::printPatternResults();

exit;

