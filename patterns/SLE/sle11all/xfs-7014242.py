#!/usr/bin/python

# Title:       Checks for XFS error
# Description: XFS error: xlog_space_left: head behind tail
# Modified:    2014 Mar 4
#
##############################################################################
# Copyright (C) 2013,2014 SUSE LLC
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
# along with this program; if not, see <http://www.gnu.org/licenses/>.
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
META_CATEGORY = "Filesystem"
META_COMPONENT = "XFS"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014242|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=849950"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def xfsVolumesMounted():
	fileOpen = "fs-diskio.txt"
	section = "/bin/mount"
	content = {}
	FSTYPE = 4
	if Core.getSection(fileOpen, section, content):
		for line in content:
			FIELDS = content[line].split()
			FIELDS_LEN = len(FIELDS)
			if( FIELDS_LEN > FSTYPE ):
#				print "len(FIELDS) = " + str(FIELDS_LEN)
#				print "FIELDS = " + str(FIELDS)
				if "xfs" in FIELDS[FSTYPE]:
					return True
	return False

def xlogError():
	fileOpen = "boot.txt"
	section = "dmesg"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "xlog_space_left: head behind tail" in content[line]:
				if "XFS" in content[line]:
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

LAST_VERSION = '3.0.101-0.8'
if( SUSE.compareKernel(SUSE.SLE11SP2) >= 0 and SUSE.compareKernel(LAST_VERSION) <= 0 ):
	if( xfsVolumesMounted() ):
		if( xlogError() ):
			Core.updateStatus(Core.CRIT, "Detected XFS filesystem xlog_space_left errors, update system for patched kernel")
		else:
			Core.updateStatus(Core.WARN, "Susceptible to XFS filesystem xlog_space_left errors, update system for patched kernel")
	else:
		Core.updateStatus(Core.ERROR, "No xfs filesystems mounted, skipping xlog_space_left test")
else:
	Core.updateStatus(Core.ERROR, "Outside kernel scope, skipping xlog_space_left test")

Core.printPatternResults()

