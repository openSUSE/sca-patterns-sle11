#!/usr/bin/perl

# Title:       Update registration fails with curl error
# Description: Update/registration failing with "Error occurred while setting download (curl) options"
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
	PROPERTY_NAME_COMPONENT."=Curl",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7004839",
	"META_LINK_TID2=http://www.suse.com/support/kb/doc.php?id=3303599"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub outdatedCurlPackages {
	SDP::Core::printDebug('> outdatedCurlPackages', 'BEGIN');
	my $RCODE = 0;
	my $INSTALLED = 0;
	my @RPMS_TO_COMPARE = qw(curl libcurl4 libcurl4-32bit);
	my $RPM_NAME = '';
	my $VERSION_TO_COMPARE = '7.19.0-11.22.1';
	foreach $RPM_NAME (@RPMS_TO_COMPARE) {
		my $RPM_COMPARISON = SDP::SUSE::compareRpm($RPM_NAME, $VERSION_TO_COMPARE);
		if ( $RPM_COMPARISON < 2 ) {
			$INSTALLED++;
			if ( $RPM_COMPARISON < 0 ) {
				$RCODE++;
			}                       
		}
	}
	if ( ! $INSTALLED ) {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Curl packages are not installed");
	}
	SDP::Core::printDebug("< outdatedCurlPackages", "Returns: $RCODE");
	return $RCODE;
}

sub failedRegistration {
	SDP::Core::printDebug('> failedRegistration', 'BEGIN');
	my $RCODE = 0;
	my $FILE_OPEN = 'y2log.txt';
	my $SECTION = '/var/log/YaST2/y2log$';
	my @CONTENT = ();
	my @LINE_CONTENT = ();
	my $LINE = 0;

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach $_ (@CONTENT) {
			$LINE++;
			next if ( /^\s*$/ ); # Skip blank lines
			if ( /Exception\.cc.*MediaCurl\.cc.*Error occurred while setting download \(curl\) options for 'https:\/\/nu\.novell\.com.*credentials=NCCcredentials/i ) {
				$RCODE++;
				last;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("< failedRegistration", "Returns: $RCODE");
	return $RCODE;
}
##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11GA) >= 0 && SDP::SUSE::compareKernel(SLE11SP1) < 0 ) {
		if ( outdatedCurlPackages() ) {
			if ( failedRegistration() ) {
				SDP::Core::updateStatus(STATUS_CRITICAL, "Registering for Novell updates has failed due to outdated curl packages");
			} else {
				SDP::Core::updateStatus(STATUS_WARNING, "Registering for Novell updates may fail due to outdated curl packages");
			}
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Curl packages should not affect update registration");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ABORT: Outside the kernel scope, curl check aborted.");
	}
SDP::Core::printPatternResults();

exit;

