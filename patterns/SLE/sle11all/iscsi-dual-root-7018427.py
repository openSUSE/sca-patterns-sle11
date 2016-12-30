#!/usr/bin/python

# Title:       iSCSI fails with duplicate root user
# Description: iSCSI initiator does not discover iSCSI target when TCP/IP is working
# Modified:    2016 Dec 30
#
##############################################################################
# Copyright (C) 2016 SUSE LINUX Products GmbH, Nuernberg, Germany
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
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "iSCSI"
META_COMPONENT = "Connection"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc?id=7018427"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def iscsiClientEnabled():
	SERVICE = 'open-iscsi'
#	SERVICE_INFO = SUSE.getServiceInfo(SERVICE)
#	return SERVICE_INFO['OnForRunLevel']
	return SUSE.getServiceInfo(SERVICE)['OnForRunLevel']

def getRootUsers():
	FILE_OPEN = "pam.txt"
	SECTION = "getent passwd"
	CONTENT = []
	ROOT_USER = re.compile(":x:0:", re.IGNORECASE)
	ROOT_USER_LIST = []
	if Core.getRegExSection(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if ROOT_USER.search(LINE):
				ROOT_USER_LIST.append(LINE.split(':')[0])
	return ROOT_USER_LIST

def rootUserOrderedLast(USER_LIST):
	if( USER_LIST[0] == "root" ):
		return False
	return True

def rootUserRenamed(USER_LIST):
	if( USER_LIST[0] == "root" ):
		return False
	return True

def iscsiDrivesFound():
	FILE_OPEN = "fs-iscsi.txt"
	SECTION = "iscsiadm -m node"
	CONTENT = []
	if Core.getRegExSection(FILE_OPEN, SECTION, CONTENT):
		for LINE in CONTENT:
			if "No records found" in LINE:
				return False
	return True

##############################################################################
# Main Program Execution
##############################################################################

if( iscsiClientEnabled() ):
	ROOT_USERS = getRootUsers()
#	print ROOT_USERS
	if( len(ROOT_USERS) > 1 ):
		if( rootUserOrderedLast(ROOT_USERS) ):
			if( iscsiDrivesFound() ):
				Core.updateStatus(Core.WARN, "iSCSI connections may fail from duplicate root users: " + str(" ".join(ROOT_USERS)))
			else:
				Core.updateStatus(Core.CRIT, "iSCSI connections may have failed from duplicate root users: " + str(" ".join(ROOT_USERS)))
		else:
			Core.updateStatus(Core.WARN, "Check iSCSI connections, duplicate root users found: " + str(" ".join(ROOT_USERS)))
	else:
		if( rootUserRenamed(ROOT_USERS) ):
			Core.updateStatus(Core.WARN, "iSCSI connection may fail from renamed root user: " + str(" ".join(ROOT_USERS)))
		else:
			Core.updateStatus(Core.IGNORE, "No additional root users found")
else:
	Core.updateStatus(Core.ERROR, "iSCSI is not enabled")

Core.printPatternResults()


