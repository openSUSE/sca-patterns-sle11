#!/usr/bin/python

# Title:       Using ipset results in error
# Description: Using ipset to create user-defined IP sets for iptables results in error
# Modified:    2014 Mar 04
#
##############################################################################
# Copyright (C) 2014 SUSE LLC
##############################################################################
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)
#
##############################################################################

##############################################################################
# Module Definition
##############################################################################

import sys, os, Core, SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Firewall"
META_COMPONENT = "iptables"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014180|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=851066"
FIXED_KERNEL = '3.0.101'

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def activeNetFilters():
	fileOpen = "network.txt"
	section = "iptables -t filter"
	content = {}
	if Core.getSection(fileOpen, section, content):
		if( len(content) > 1 ):
			return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( SUSE.compareKernel(SUSE.SLE11SP2) >= 0 and SUSE.compareKernel(FIXED_KERNEL) < 0 ):
	if( activeNetFilters() ):
		Core.updateStatus(Core.WARN, "Using ipset may fail to create firewall filter, update system")
	else:
		Core.updateStatus(Core.IGNORE, "Firewall filters are not active")
else:
	Core.updateStatus(Core.ERROR, "Outside kernel scope, skipping ipset test")

Core.printPatternResults()

