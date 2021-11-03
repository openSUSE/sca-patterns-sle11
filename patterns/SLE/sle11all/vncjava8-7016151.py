#!/usr/bin/python3

# Title:       VNC fails on SLE11 with Java 8
# Description: Error:access denied java.net.SocketPermission
# Modified:    2015 Feb 05
#
##############################################################################
# Copyright (C) 2015 SUSE LLC
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

import re
import os
import Core

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "VNC"
META_COMPONENT = "Connections"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7016151|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=907806"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def vncActive():
	fileOpen = "chkconfig.txt"
	section = "chkconfig --list"
	content = {}
	VNC_ON = re.compile("^\s+vnc:\s+on", re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if VNC_ON.search(content[line]):
				return True
	return False

def errorFound():
	fileOpen = "messages.txt"
	section = "/var/log/messages"
	content = {}
	ERROR_STRING = re.compile("Error:access denied.*java\.net\.SocketPermission.*connect.*resolve", re.IGNORECASE)
	if Core.getSection(fileOpen, section, content):
		for line in content:
			if ERROR_STRING.search(content[line]):
				return True
	return False

##############################################################################
# Main Program Execution
##############################################################################

if( vncActive() ):
	if( errorFound() ):
		Core.updateStatus(Core.WARN, "Detected java.net.SocketPermission connection errors, possibly from Java 8 clients")
	else:
		Core.updateStatus(Core.IGNORE, "No java.net.SocketPermission connection errors detected")
else:
	Core.updateStatus(Core.ERROR, "ERROR: VNC not active, skipping connection issue")

Core.printPatternResults()


