#!/usr/bin/perl

# Title:       Ejecting CD in Dom0 from DomU fails
# Description: Ejecting a CD-ROM device medium on the virtual machine host (Dom0) from within a virtual machine (VM/DomU) with the wrong protocol will fail.
# Modified:    2013 Jun 28

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
	PROPERTY_NAME_CATEGORY."=Virtualization",
	PROPERTY_NAME_COMPONENT."=Xen",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7007356"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub xenProtocolCD {
	SDP::Core::printDebug('> xenProtocolCD', 'BEGIN');
	my $RCODE = 0;
	my @LINE_CONTENT = ();
	my $FILE_OPEN = 'xen.txt';
	my $SECTION = 'xm list -l';
	my @CONTENT = ();
	my ($IN_DOMAIN, $IN_DEVICE, $IN_TYPE) = (0, 0, 0);
	my $DOMAIN_NAME = "";
	my @BAD_DOMAINS = ();

	if ( SDP::Core::getSection($FILE_OPEN, $SECTION, \@CONTENT) ) {
		foreach my $LINE (@CONTENT) {
			next if ( $LINE =~ m/^\s*$/ ); # Skip blank lines
			if ( $IN_DOMAIN ) {
				if ( $LINE =~ m/^\)/ ) {
					SDP::Core::printDebug("<", "");
					$IN_DOMAIN = 0;
					$DOMAIN_NAME = '';
				} elsif ( $LINE =~ m/\(name (.*)\)/ ) {
					$DOMAIN_NAME = $1;
					SDP::Core::printDebug("", "$DOMAIN_NAME");
				} elsif ( $LINE =~ m/\(uname phy\:\/dev\/.*\)/ ) {
					SDP::Core::printDebug(" BAD", "Pushing Domain");
					push(@BAD_DOMAINS, $DOMAIN_NAME);
				}
			} elsif ( $LINE =~ m/^\(domain/ ) {
				SDP::Core::printDebug("DOMAIN >", "Name");
				$IN_DOMAIN = 1;
			}
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: xenProtocolCD(): Cannot find \"$SECTION\" section in $FILE_OPEN");
	}
	SDP::Core::printDebug("BAD DOMAINS", "'@BAD_DOMAINS'");
	$RCODE = scalar @BAD_DOMAINS;
	if ( $RCODE > 0 ) {
		SDP::Core::updateStatus(STATUS_WARNING, "Ejecting Dom0 CD from DomU may not eject properly from VMs: @BAD_DOMAINS");
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "No CD eject issue observed in VM configuration(s)");
	}
	SDP::Core::printDebug("< xenProtocolCD", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	if ( SDP::SUSE::compareKernel(SLE11SP1) >= 0 ) {
		xenProtocolCD();
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Outside kernel scope, skipping CD eject test");
	}
SDP::Core::printPatternResults();

exit;

