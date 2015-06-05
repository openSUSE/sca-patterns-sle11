#!/usr/bin/python

# Title:       Xen DomU fails to boot
# Description: Not able to load or install a DomU (Guest machine) using a disk from Multipath
# Modified:    2015 Jun 02
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

import os
import Core
import SUSE
import Xen

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Xen"
META_COMPONENT = "Load"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7011590|META_LINK_BUG1=https://bugzilla.suse.com/show_bug.cgi?id=792152|META_LINK_BUG2=https://bugzilla.suse.com/show_bug.cgi?id=787721"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def getDiskID(DEVICE_PATH):
	"""
	Gets the system disk (sd?) or world wide name ID for use in MPIO managed disk lookup
	"""
	ID = ''
	DEV = DEVICE_PATH.split("/")[-1]
	print "Evaluate", DEV
	if DEV.startswith("sd"):
		print " system"
	return ID

def mpioManagedDevice(DISK_ID):
	return True

##############################################################################
# Main Program Execution
##############################################################################

if( Xen.isDom0() ):
	if( SUSE.mpioDevicesManaged() ):
		XenConfigFiles = Xen.getConfigFiles()
		MpioDevices = SUSE.mpioGetManagedDevices()
		VM_CRIT_LIST = []
		for XenConfig in XenConfigFiles:
			if "phy:/dev/" in XenConfig['disk']: #there are physical disks to process
				DISK_LIST = Xen.getDiskValueList(XenConfig['disk'])
				for DISK in DISK_LIST:
					if( 'phy' in DISK['type'] ): #we only care about phy type disks
 						if( not DISK['mode'].endswith('!') ): #process non disk locked devices only
							#print "Checking", DISK['device']
							DISK_ID = getDiskID(DISK['device'])
							if( DISK_ID ):
								if( mpioManagedDevice(DISK_ID) ):
									VM_CRIT_LIST.append(XenConfig['name'])
								else:
									print " Not managed"
							else:
								print " Missing ID"
		if( len(VM_CRIT_LIST) > 0 ):
			Core.updateStatus(Core.CRIT, "Missing disk lock or no_partition, probable boot failure for VMs: " + ' '.join(VM_CRIT_LIST))
		else:
			Core.updateStatus(Core.IGNORE, "No VMs using MPIO devices")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: MPIO not active")
else:
	Core.updateStatus(Core.ERROR, "ERROR: Not a Xen Dom0")

Core.printPatternResults()

