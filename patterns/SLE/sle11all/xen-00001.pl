#!/usr/bin/perl

# Title:       Xen Hypervisor Fails to Boot After Update
# Description: On reboot the boot loader gives an error - File not found
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
	PROPERTY_NAME_COMPONENT."=Boot",
	PROPERTY_NAME_PATTERN_ID."=$PATTERN_ID",
	PROPERTY_NAME_PRIMARY_LINK."=META_LINK_TID",
	PROPERTY_NAME_OVERALL."=$GSTATUS",
	PROPERTY_NAME_OVERALL_INFO."=None",
	"META_LINK_TID=http://www.suse.com/support/kb/doc.php?id=7008740",
	"META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=698564"
);

##############################################################################
# Local Function Definitions
##############################################################################

sub grubKernelMismatch {
	#SDP::Core::printDebug('> grubKernelMismatch', 'BEGIN');
	my $RCODE = 0;
	my $ARRAY_REF = $_[0];
	my $FILE_OPEN = 'boot.txt';
	my %KERNELS = ();
	my @CONTENT = ();
	my @LINE = ();
	my $STATE = 0;
	my $CONTENT_FOUND = 0;
	if ( SDP::Core::loadFile($FILE_OPEN, \@CONTENT) ) {
		foreach $_ (@CONTENT) { # first get the list of grub kernels
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( $STATE ) {
				if ( /^#==\[/ ) {
					$STATE = 0;
					#SDP::Core::printDebug(" DONE", "State Off");
				} elsif ( /^\s*kernel (\S*) / ) { # Section content needed
					my $THIS_KERNEL = $1;
					if ( $THIS_KERNEL =~ m/\)/ ) {
						my $TMP_KERNEL = '';
						(undef, $TMP_KERNEL) = split(/\)/, $THIS_KERNEL);
						$THIS_KERNEL = $TMP_KERNEL;
					}
					$THIS_KERNEL =~ s/^\/boot\/|^\///g;
					#SDP::Core::printDebug(" EVAL", "$_");
					$KERNELS{$THIS_KERNEL} = 1 if ( $THIS_KERNEL =~ m/xen/ );
					$CONTENT_FOUND = 1;
				}
			} elsif ( /^# \/boot\/grub\/menu\.lst/ ) { # Section
				$STATE = 1;
				#SDP::Core::printDebug("CHECK", "Section: $_");
			}
		}
		my @KTMP = keys %KERNELS;
		#SDP::Core::printDebug("GRUB KERNELS", "'@KTMP'");
		
		$STATE = 0;
		my $THIS_KERNEL = '';
		foreach $_ (@CONTENT) { # make sure each kernel is found in /boot
			next if ( m/^\s*$/ ); # Skip blank lines
			if ( $STATE ) {
				if ( /^#==\[|^\/boot\/grub:/ ) {
					$STATE = 0;
					#SDP::Core::printDebug(" DONE", "State Off, Source: $_");
				} else {
					@LINE = split(/\s+/, $_);
					if ( m/\s->\s/ ) {
						pop(@LINE);
						pop(@LINE);
					}
					if ( $#LINE >= 7 ) {
						#SDP::Core::printDebug(" FILE", "$LINE[$#LINE]");
						foreach $THIS_KERNEL (@KTMP) {
							if ( $LINE[$#LINE] eq $THIS_KERNEL ) {
								#SDP::Core::printDebug("  FOUND", "$_");
								$KERNELS{$THIS_KERNEL} = 0;
							}
						}
					}
				}
			} elsif ( /ls -lR.*\/boot/ ) { # Section
				$STATE = 1;
				#SDP::Core::printDebug("CHECK", "Section: $_");
			}
		}
		my $KGRUB = '';
		my $KBOOT = '';
		foreach $KGRUB (@KTMP) {
			#SDP::Core::printDebug("KGRUB", "$KGRUB");
			if ( $KERNELS{$KGRUB} > 0 ) {
				push(@$ARRAY_REF, $KGRUB);
			}
		}
		#SDP::Core::printDebug("KTMP", "@KTMP");
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "ERROR: grubKernelMismatch(): Cannot load file: $FILE_OPEN");
	}
	$RCODE = scalar @$ARRAY_REF;
	#SDP::Core::printDebug("< grubKernelMismatch", "Returns: $RCODE");
	return $RCODE;
}

##############################################################################
# Main Program Execution
##############################################################################

SDP::Core::processOptions();
	my @MISMATCHED_KERNELS = ();
	if ( SDP::SUSE::xenDom0installed() ) {
		if ( grubKernelMismatch(\@MISMATCHED_KERNELS) ) {
			SDP::Core::updateStatus(STATUS_CRITICAL, "Kernel(s) in menu.lst missing from /boot: @MISMATCHED_KERNELS");
		} else {
			SDP::Core::updateStatus(STATUS_ERROR, "Kernel(s) match in menu.lst and /boot");
		}
	} else {
		SDP::Core::updateStatus(STATUS_ERROR, "Xen Dom0 not installed, skipping xen boot test");
	}
SDP::Core::printPatternResults();

exit;

