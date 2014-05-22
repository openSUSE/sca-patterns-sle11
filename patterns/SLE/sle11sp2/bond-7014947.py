#!/usr/bin/python

# Title:       Check BONDING_MASTER_UP_ENSLAVE
# Description: Bond not keeping MTU of 9000 after ifdown/ifup - See also BONDING_MASTER_UP_ENSLAVE option
# Modified:    2014 May 22
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
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
#  Authors/Contributors:
#   Jason Record (jrecord@suse.com)
#
##############################################################################

##############################################################################
# Module Definition
##############################################################################

import sys, os, Core, SUSE, re

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Network"
META_COMPONENT = "Bond"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7014947|META_LINK_BUG=https://bugzilla.novell.com/show_bug.cgi?id=737833|META_LINK_BUG2=https://bugzilla.novell.com/show_bug.cgi?id=874648"

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)
MTU_DEF = int(1500)
STATE_MTU_UNCHANGED = 0
STATE_MTU_CHANGEABLE = 1
STATE_MTU_CHANGED = 2

##############################################################################
# Local Function Definitions
##############################################################################

def getBondInterfaces():
	fileOpen = "network.txt"
	section = "ifconfig -a"
	content = {}
	bonded = []
	if Core.getSection(fileOpen, section, content):
		ifaceName = re.compile("^\S")
		for line in content:
			if "Link encap" in content[line]:
				iface = content[line].split()[0] # the first name in the string is the interface name
			elif "MASTER" in content[line]:
				MTU_ACTIVE = content[line].split()[-2].split(':')[-1]
				bonded.append(iface + ',' + MTU_ACTIVE)
#	print "bonded interfaces = " + str(bonded)
	return bonded

def changeableMTU(bond):
	fileOpen = "network.txt"
	(NAME, MTU_ACTIVE) = bond.split(',')
	if( len(MTU_ACTIVE) > 0 ):
		MTU_ACTIVE = int(MTU_ACTIVE)
	else:
		MTU_ACTIVE = MTU_DEF
	section = "/etc/sysconfig/network/ifcfg-" + NAME
	content = {}
	UP_ENSLAVE = False
	MTU_CONFIG = MTU_DEF
	if Core.getSection(fileOpen, section, content):
		mtu = re.compile("^MTU=")
		config = re.compile("^BONDING_MASTER_UP_ENSLAVE=.*yes", re.IGNORECASE)
		for line in content:
			if mtu.search(content[line]):
				MTU_CONFIG = content[line].split("=")[1].replace("'", '').replace('"', '').strip()
				if ( len(MTU_CONFIG) > 0 ):
					MTU_CONFIG = int(MTU_CONFIG)
				else:
					MTU_CONFIG = MTU_DEF
			elif config.search(content[line]):
				UP_ENSLAVE = True
#		print str(bond)+ ": MTU_ACTIVE = " + str(MTU_ACTIVE) + " MTU_CONFIG = " + str(MTU_CONFIG) + " UP_ENSLAVE = " + str(UP_ENSLAVE)
		if( UP_ENSLAVE ):
			if( MTU_CONFIG != MTU_ACTIVE ):
				return STATE_MTU_CHANGED
			else:
				return STATE_MTU_UNCHANGED
		elif( MTU_CONFIG != MTU_DEF ):
			if( MTU_CONFIG != MTU_ACTIVE ):
				return STATE_MTU_CHANGED
			else:
				return STATE_MTU_CHANGEABLE
	return STATE_MTU_UNCHANGED

##############################################################################
# Main Program Execution
##############################################################################

bondInterfaces = getBondInterfaces()
bondCrit = ''
bondWarn = ''
msg = "MTU Reverts to Default on Bonded Interfaces - "
if( len(bondInterfaces) > 0 ):
	for bondInfo in bondInterfaces:
		bondState = changeableMTU(bondInfo)
		if( bondState == STATE_MTU_CHANGED ):
			bondCrit = bondInfo.split(',')[0] + ' ' + bondCrit
		elif( bondState == STATE_MTU_CHANGEABLE ):
			bondWarn = bondInfo.split(',')[0] + ' ' + bondWarn
	if( len(bondCrit) > 0 ): # MTU Reverts on Bonded Interfaces, Failed: None, At Risk: None
		if( len(bondWarn) > 0 ):
			Core.updateStatus(Core.CRIT, msg + "Failed: " + str(bondCrit.strip()) + ", At Risk: " + str(bondWarn.strip()))
		else:
			Core.updateStatus(Core.CRIT, msg + "Failed: " + str(bondCrit.strip()))
	elif( len(bondWarn) > 0 ):
		Core.updateStatus(Core.WARN, msg + "Failed: None, At Risk: " + str(bondWarn.strip()))
	else:
		Core.updateStatus(Core.IGNORE, "No bonded interfaces affected")
else:
	Core.updateStatus(Core.ERROR, "ERROR: No bonded interfaces found")

Core.printPatternResults()


