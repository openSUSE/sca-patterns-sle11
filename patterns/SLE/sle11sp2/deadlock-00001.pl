#!/usr/bin/perl

# Title:       Kernel deadlock
# Description: Kernel deadlock when using ext2/3/4 or GPFS
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
	PROPERTY_NAME_CATEGORY."=Filesystem",
	PROPERTY_NAME_COMPONENT."=Deadlock",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7011397",
	"META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=779699"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub deadLocks {
	SDP::Core::printDebug('> deadLocks', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'messages.txt';
	my $SECTION = '/var/log/warn';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /soft lockup.*CPU.*stuck for.*nfsd/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: deadLocks(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< deadLocks", "Returns: $RCODE");
	return $RCODE;
}

sub nfsExportsFound {
	SDP::Core::printDebug('> nfsExportsFound', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'nfs.txt';
	my $SECTION = '/etc/exports';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /\// ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: nfsExportsFound(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< nfsExportsFound", "Returns: $RCODE");
	return $RCODE;
}

sub extFSFound {
	SDP::Core::printDebug('> extFSFound', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'fs-diskio.txt';
	my $SECTION = 'bin/mount';
	my @CONTENT = ();
	my @LINE_CONTENT = ();
	my $FSTYPE = '';

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			(undef,undef,undef,undef,$FSTYPE,undef) = split(/\s+/, $_);
			if ( $FSTYPE =~ m/ext/ ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: extFSFound(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< extFSFound", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11SP2) >= 0 && SDP::SUSE::compareKernel('3.0.42-0.7') < 0) {
		if ( nfsExportsFound() ) {
			if ( extFSFound() ) {
				if ( deadLocks() ) {
					SDP::Core::updateStatus(STATUS_CRITICAL, "Detected NFS kernel dead lock, update system to apply latest kernel");
				} else {
					SDP::Core::updateStatus(STATUS_WARNING, "Potential NFS kernel dead lock, review NFS exports and consider updating kernel");
				}
			} else {
				SDP::Core::updateStatus(STATUS_ERROR, "Error: No ext2/3/4 found, skipping deadlock");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Error: No NFS exports, skipping deadlock");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Error: Outside Kernel Scope, skipping deadlock");
	}
SDP::Core::printPatternResults();

exit;


