#!/usr/bin/python3

# Title:       Xen DomU fails to boot
# Description: Not able to load or install a DomU (Guest machine) using a disk from Multipath
# Modified:    2015 Jun 11
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
import SUSE
import Xen
import MPIO

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
# Main Program Execution
##############################################################################

if( Xen.isDom0() ):
	if( MPIO.devicesManaged() ):
		XenConfigFiles = Xen.getConfigFiles()
		MpioDevices = MPIO.getManagedDevices()
		VM_CRIT_LIST = []
		for XenConfig in XenConfigFiles: 												#process each xen config file in the xen.txt file
			if "phy:/dev/" in XenConfig['disk']: 									#if there are physical disks to process
				DISK_LIST = Xen.getDiskValueList(XenConfig['disk'])	#a list of the xen config file disk values
				for DISK in DISK_LIST: 															#process each disk from the disk= value in the xen config file
					if( 'phy' in DISK['type'] ): 											#we only care about phy type disks
 						if( not DISK['mode'].endswith('!') ): 					#process non disk locked devices only
							DISK_ID = MPIO.getDiskID(DISK['device'])			#get the disk id for this device
							if( DISK_ID ):																#process if the DISK_ID is found
								if( MPIO.partitionManagedDevice(DISK_ID, MpioDevices) ): #determine if the device is managed without no_partitions
									VM_CRIT_LIST.append(XenConfig['name'])		#add the managed mpio disks without no_partitions that match the xen configuration
									break
		VM_CRIT_LIST_CNT = len(VM_CRIT_LIST)
		if( VM_CRIT_LIST_CNT > 1 ): #print plural message
			Core.updateStatus(Core.CRIT, "Missing disk lock or no_partitions, probable boot failure for " + str(VM_CRIT_LIST_CNT) + " VMs: " + ' '.join(VM_CRIT_LIST))
		if( VM_CRIT_LIST_CNT > 0 ): #print single message
			Core.updateStatus(Core.CRIT, "Missing disk lock or no_partitions, probable boot failure for " + str(VM_CRIT_LIST_CNT) + " VM: " + ' '.join(VM_CRIT_LIST))
		else:
			Core.updateStatus(Core.IGNORE, "No VMs using MPIO devices")
	else:
		Core.updateStatus(Core.ERROR, "ERROR: No MPIO managed devices found")
else:
	Core.updateStatus(Core.ERROR, "ERROR: Not a Xen Dom0")

Core.printPatternResults()

