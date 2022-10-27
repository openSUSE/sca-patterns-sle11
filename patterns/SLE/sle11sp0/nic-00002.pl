#!/usr/bin/perl

# Title:       SLES11 Network Card fails due to tmpfs
# Description: tmpfs file system causes SLES11 network to not come up when booting
# Modified:    2013 Aug 30
# SLE11 FCS only

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
	PROPERTY_NAME_CLASS."=SLE",
	PROPERTY_NAME_CATEGORY."=Network",
	PROPERTY_NAME_COMPONENT."=NIC",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7006027",
	"META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=516769",
	"META_LINK_BUG2=https://bugzilla.suse.com/show_bug.cgi?id=549721"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub getDownInterfaces {
	SDP::Core::printDebug('> getDownInterfaces', 'BEGIN');
	my %RCODE = ();
	my $FILE_OPEN = 'boot.txt';
	my $SECTION = 'boot.msg';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /^interface (.*) is not up/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE{$1} = 1;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: getDownInterfaces(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	my $FOUND = scalar keys(%RCODE);
	SDP::Core::printDebug("< getDownInterfaces", "Returns: $FOUND");
	return %RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my %NIC_FAILURES = getDownInterfaces();
	my @FAILED_CARDS = keys(%NIC_FAILURES);
	my $FAILURES = scalar keys(%NIC_FAILURES);
	if ( $FAILURES ) {
		my @MOUNTS = SDP::SUSE::getFileSystems();
		my $TMP;
		my $FOUND = 0;
		foreach $TMP (@MOUNTS) {
			if ( $TMP->{'DEVF'} eq 'shmfs' && $TMP->{'TYPE'} eq 'tmpfs' ) {
				SDP::Core::updateStatus(STATUS_CRITICAL, "Shmfs mounting tmpfs; Network interfaces not started at boot time: @FAILED_CARDS");
				$FOUND = 1;
				last;
			}
		}
		SDP::Core::updateStatus(STATUS_ERROR, "No tmpfs failures observed") if ( ! $FOUND );
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Network interfaces started at boot, skipping shmfs test");
	}
SDP::Core::printPatternResults();

exit;

