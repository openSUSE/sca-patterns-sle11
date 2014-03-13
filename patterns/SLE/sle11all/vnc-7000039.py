#!/usr/bin/python

# Title:       VNC Connection Failures
# Description: VNC connection fails with Invalid Protocol
# Modified:    2013 Nov 11
#
##############################################################################
# Copyright (C) 2013 SUSE LLC
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
META_CATEGORY = "X"
META_COMPONENT = "VNC"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7000039"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def xServerError():
	fileOpen = "x.txt"
	section = "/var/log/xdm.errors"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "XIO:" in content[line]:
				if "fatal IO error 11" in content[line]:
					if "on X server" in content[line]:
						return True
	return False

def vncListening():
	fileOpen = "network.txt"
	section = "/bin/netstat -nlp"
	content = {}
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if "LISTEN " in content[line]:
				if "/Xvnc" in content[line]:
					return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( vncListening() ):
	if( xServerError() ):
		Core.updateStatus(Core.WARN, "Confirm possible VNC connection failures")
	else:
		Core.updateStatus(Core.ERROR, "No XIO errors")
else:
	Core.updateStatus(Core.ERROR,"VNC is not listening")

Core.printPatternResults()

