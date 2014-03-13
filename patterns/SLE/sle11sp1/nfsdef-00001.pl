#!/usr/bin/perl

# Title:       NFS server does not load
# Description: The nfs server errors out when starting
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
	PROPERTY_NAME_CATEGORY."=Filesystem",
	PROPERTY_NAME_COMPONENT."=NFS",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7008046"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub validNFSService {
	SDP::Core::printDebug('> validNFSService', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'network.txt';
	my $SECTION = '/etc/services';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /^nfs\s\s*\d/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
			}
		}
	} else {
		$RCODE = 2; # assume /etc/services is valid for NFS
	}
	$RCODE = 0 if ( $RCODE < 2 );
	SDP::Core::printDebug("< validNFSService", "Returns: $RCODE");
	return $RCODE;
}

sub nfsError {
	SDP::Core::printDebug('> nfsError', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'boot.txt';
	my $SECTION = 'boot.msg';
	my @CONTENT = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( /nfs.*Servname not supported for ai_socktype/i ) {
				SDP::Core::printDebug("PROCESSING", $_);
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: nfsError(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< nfsError", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 && SDP::SUSE::compareKernel(SLE12GA) < 0 ) {
		my $SERVICE_NAME = 'nfsserver';
		my %SERVICE_INFO = SDP::SUSE::getServiceInfo($SERVICE_NAME);
		if ( $SERVICE_INFO{'running'} > 0 ) {
			if ( nfsError() ) {
				if ( validNFSService() ) {
					SDP::Core::updateStatus(STATUS_WARNING, "Detected NFS Servname not supported for ai_socktype, check /etc/services.");
				} else {
					SDP::Core::updateStatus(STATUS_CRITICAL, "Detected NFS Servname not supported for ai_socktype, invalid /etc/services.");
				} 
			} else {
				if ( validNFSService() ) {
					SDP::Core::updateStatus(STATUS_ERROR, "NFS services configured with no ai_socktype errors");
				} else {
					SDP::Core::updateStatus(STATUS_WARNING, "Susceptible to NFS ai_socktype error, invalid /etc/services.");
				}
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Service $SERVICE_INFO{'name'} is NOT running, skip NFS services check.");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ABORTED: NFS Load Check: Outside the kernel scope");
	}
SDP::Core::printPatternResults();

exit;

