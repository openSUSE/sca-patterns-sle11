#!/usr/bin/perl

# Title:       Device-mapper does not use all available paths to a SAN
# Description: Under certain circumstances, Device-Mapper can create device maps using the physical paths to a LUN, rather than the multipath logical path.
# Modified:    2013 Jun 27

##############################################################################
#  Copyright (C) 2013,2012 SUSE LLC
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
	PROPERTY_NAME_CATEGORY."=Disk",
	PROPERTY_NAME_COMPONENT."=Device Mapper",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7005564",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=586834"
);

##############################################################################
# Local Function Definitions
##############################################################################

my @VGS = ();
my $BAD_VG;

sub oneLvmOnMultiMpioPvs {
	SDP::Core::printDebug('> oneLvmOnMultiMpioPvs', 'BEGIN');
	my $RCODE = 0;
	my @LINE_CONTENT = ();
	my $FILE_OPEN = 'mpio.txt';
	my $SECTION = 'multipath -ll';
	my @CONTENT = ();
	my $MPIO = 0;
	my $LVM = 0;

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( /^\s*$/ ); # Skip blank lines
			SDP::Core::printDebug("PROCESSING", $_);
			if ( /^\\/ ) {
				SDP::Core::printDebug(" CONFIRMED", "MPIO");
				$MPIO++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: oneLvmOnMultiMpioPvs(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	if ( $MPIO ) {
		$FILE_OPEN = 'lvm.txt';
		$SECTION = 'vgs$';
		@CONTENT = ();
		if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
			foreach $_ (@CONTENT) {
				next if ( /^\s*$/ ); # Skip blank lines
				SDP::Core::printDebug("PROCESSING", $_);
				if ( /\s+(\S+)\s+(\d+)/ ) { # white space, volume name-1, white space, PV count-2
					if ( $2 > 1 ) {
						push(@VGS, $1) if ( $2 > 1 );
						SDP::Core::printDebug(" CONFIRMED", "VG: $1, PV Count: $2");
					} else {
						SDP::Core::printDebug(" UNCONFIRMED", "VG: $1, PV Count: $2");
					}
				}
			}
			$RCODE++ if ( scalar(@VGS) > 0 );
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: oneLvmOnMultiMpioPvs(): Cannot find \"$SECTION\" section in $FILE_OPEN");
		}
	} else {
		SDP::Core::printDebug("FAILED", "MPIO Devices not found");
	}
	SDP::Core::printDebug("VGS", "@VGS");
	SDP::Core::printDebug("< oneLvmOnMultiMpioPvs", "Returns: $RCODE");
	return $RCODE;
}

sub patchApplied {
	SDP::Core::printDebug('> patchApplied', 'BEGIN');
	my $RCODE = 0; # assume the patch is not applied
	SDP::Core::printDebug("==TODO==", "REPLACE WHEN PATCH RELEASES");
	SDP::Core::printDebug('< patchApplied', "Returns: $RCODE");
	return $RCODE;
}

sub workAroundApplied {
	SDP::Core::printDebug('> workAroundApplied', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'lvm.txt';
	my $SECTION = 'rpm -V lvm2';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( /^\s*$/ ); # Skip blank lines
			SDP::Core::printDebug("PROCESSING", $_);
			if ( /missing\s+.*64-lvm2\.rules/i ) {
				$RCODE++;
				SDP::Core::printDebug(" CONFIRMED", $RCODE);
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: workAroundApplied(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< workAroundApplied", "Returns: $RCODE");
	return $RCODE;
}

sub invalidDmSetupTree {
	SDP::Core::printDebug('> invalidDmSetupTree', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'lvm.txt';
	my $SECTION = 'dmsetup ls --tree';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach my $VG (@VGS) {
			SDP::Core::printDebug("VOLUME GROUP:", $VG);
			my $STATE = 0;
			foreach my $LINE (@CONTENT) {
				next if ( $LINE =~ m/^$/ ); # Skip blank lines
				SDP::Core::printDebug(" LINE", $LINE);
				if ( $STATE ) { # one of the volume groups with >1 mpio pv
					if ( $LINE =~ m/^\s\S{6}\s\(\d+\:\d+\)/ ) { # line draw characters are treated as though they are three characters each
						$BAD_VG = $VG;
						SDP::Core::printDebug("  INVALID", "PUNT $BAD_VG");
						$RCODE++;
						last;
					} elsif ( $LINE =~ m/^\S/ ) { # The next volume group; begins with a non-white character
						SDP::Core::printDebug(" COMPLETE", $VG);
						last;
					}
				} elsif ( $LINE =~ m/^$VG/ ) { # found vg with >1 mpio pv; begins with the volume group name
					$STATE = 1;
					SDP::Core::printDebug(" STATE CHANGE", $STATE);
				}
			}
			last if $RCODE;
		}
	}
	SDP::Core::printDebug("< invalidDmSetupTree", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE11SP2) < 0 ) {
		if ( oneLvmOnMultiMpioPvs() ) {
			if ( patchApplied() ) {
				SDP::Core::updateStatus(STATUS_ERROR, "Patch Applied for one LVM on multiple MPIO PVs");
			} elsif ( workAroundApplied() ) {
				SDP::Core::updateStatus(STATUS_ERROR, "Workaround Applied for one LVM on multiple MPIO PVs");
			} elsif ( invalidDmSetupTree() ) {
				SDP::Core::updateStatus(STATUS_CRITICAL, "MPIO path failover issue, one LVM on multiple MPIO PVs: $BAD_VG");
			} else {
				SDP::Core::updateStatus(STATUS_WARNING, "Potential MPIO path failover issue, one LVM on multiple MPIO PVs: @VGS");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Skipping dmsetup test, one LVM on multiple MPIO PVs required");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Skipping dmsetup test, outside kernel scope");
	}
SDP::Core::printPatternResults();

exit;

