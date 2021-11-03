#!/usr/bin/python3

# Title:       NFS Directory Listing Performance
# Description: Directory listing on NFS mount takes excessive time
# Affected:    SLES11 SP2 SP3 & SP4
# Modified:    2017 Sep 08
#
##############################################################################
# Copyright (C) 2017 SUSE LINUX Products GmbH, Nuernberg, Germany
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

import os
import Core
import SUSE

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "NFS"
META_COMPONENT = "Performance"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7021345|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=1048232"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Main Program Execution
##############################################################################

KERNEL_VERSION = '3.0.101-107'
INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION)
if( INSTALLED_VERSION <= 0 ):
	NFSFOUND = False
	NFSMOUNTED = False
	FSLIST = SUSE.getFileSystems()
	for FS in FSLIST:
		if( "nfs" in FS['Type'].lower() ):
			NFSFOUND = True
			#print "Found NFS Device: " + str(FS['ActiveDevice'])
			if( FS['Mounted'] ):
				#print "  MOUNTED"
				NFSMOUNTED = True
	if( NFSMOUNTED ):
		Core.updateStatus(Core.WARN, "Mounted NFS Filesystems may experience long file list delays")
	elif( NFSFOUND ):
		Core.updateStatus(Core.WARN, "NFS Filesystems may experience long file list delays")
	else:
		Core.updateStatus(Core.ERROR, "No NFS filesystems found")
else:
	Core.updateStatus(Core.IGNORE, "Bug fixes applied for kernel versions newer than " + KERNEL_VERSION)

Core.printPatternResults()


