#!/usr/bin/perl

# Title:       System Crash after 208 Days
# Description: Identifies systems that may crash due to the time stamp counter
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
	PROPERTY_NAME_CLASS."=SLE",
	PROPERTY_NAME_CATEGORY."=Crash",
	PROPERTY_NAME_COMPONENT."=Base",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7009834",
	"META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=725709"
);

my $UPTIME_CRIT = 10;

##############################################################################
# Local Function Definitions
##############################################################################

sub nonXenKernel {
	SDP::Core::printDebug('> nonXenKernel', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'basic-environment.txt';
	my $SECTION = 'uname -a';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /xen/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: nonXenKernel(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	if ( $RCODE ) {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: nonXenKernel(): Xen Kernel Found");
	}
	SDP::Core::printDebug("< nonXenKernel", "Returns: $RCODE");
	return $RCODE;
}

sub cpuAffected {
	SDP::Core::printDebug('> cpuAffected', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'proc.txt';
	my $SECTION = '/proc/cpuinfo';
	my @CONTENT = ();
	my $VENDOR = 0;
	my $FLAGS = 0;

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /^vendor_id.*intel/i ) {
				$VENDOR = 1;
			}
			if ( /^flags.*constant_tsc.*nonstop_tsc|^flags.*nonstop_tsc.*constant_tsc/i ) {
				$FLAGS = 1;
			}
		}
		$RCODE = $VENDOR + $FLAGS;
		if ( $RCODE < 2 ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: cpuAffected(): Not Intel or insufficient cpu flags set");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: cpuAffected(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< cpuAffected", "Returns: $RCODE");
	return $RCODE;
}

sub stableTSC {
	SDP::Core::printDebug('> stableTSC', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'boot.txt';
	my $SECTION = 'dmesg';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /Marking TSC unstable/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
		if ( $RCODE ) {
			SDP::Core::updateStatus(STATUS_ERROR, "ERROR: stableTSC(): TSC marked unstable, not in use");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: stableTSC(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< stableTSC", "Returns: $RCODE");
	return $RCODE;
}

sub upTime {
	SDP::Core::printDebug('> upTime', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'basic-health-check.txt';
	my $SECTION = 'uptime';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /up\s(\d.*)\sdays/ ) {
				$RCODE = $1;
				SDP::Core::printDebug("PROCESSING", $_);
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: upTime(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< upTime", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel('2.6.32.54-0.3') < 0) {
		nonXenKernel();
		cpuAffected();
		stableTSC();
		my $UPTIME_SYSTEM = upTime();
		if ( $UPTIME_SYSTEM > $UPTIME_CRIT ) {
			SDP::Core::updateStatus(STATUS_CRITICAL, "System may crash after 208 days uptime, update the system or cold boot the server.");
		} else {
			SDP::Core::updateStatus(STATUS_WARNING, "System may crash after 208 days uptime, update the system or cold boot the server.");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ABORT: Skipping 208 Day Crash; Outside the kernel scope");
	}
SDP::Core::printPatternResults();

exit;


