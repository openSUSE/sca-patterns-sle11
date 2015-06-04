#!/usr/bin/python

# Title:       Leap second June 2015
# Description: Minimum Kernel versions
# Modified:    2015 Jun 03
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
from datetime import *

##############################################################################
# Overriden (eventually or in part) from SDP::Core Module
##############################################################################

META_CLASS = "SLE"
META_CATEGORY = "Kernel"
META_COMPONENT = "Time"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_TID"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_TID=https://www.suse.com/support/kb/doc.php?id=7016150|META_LINK_TID2=https://www.suse.com/support/kb/doc.php?id=7010351|META_LINK_BUG=https://bugzilla.suse.com/show_bug.cgi?id=912916|META_LINK_IERS=http://hpiers.obspm.fr/iers/bul/bulc/bulletinc.dat"

PRE_DEADLINE = -1
POST_DEADLINE = 0
EXPIRED_DEADLINE = 1

Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

##############################################################################
# Local Function Definitions
##############################################################################

def kernelAffected():
	SERVER = SUSE.getHostInfo()
	if( SERVER['DistroVersion'] == 11 ):
		if( SERVER['DistroPatchLevel'] == 2 ):
			KERNEL_VERSION = '3.0.38-0.5'
		elif( SERVER['DistroPatchLevel'] == 1 ):
			KERNEL_VERSION = '2.6.32.59-0.7'
		else:
			KERNEL_VERSION = SERVER['KernelVersion']
		INSTALLED_VERSION = SUSE.compareKernel(KERNEL_VERSION)
		if( INSTALLED_VERSION < 0 ):
			return True
	return False

def leapSecondDeadlineExceeded():
	TODAY = date.today()
	DEADLINE = datetime.strptime('20150702', "%Y%m%d").date()
	EXPIRES = datetime.strptime('20151231', "%Y%m%d").date()
	if( TODAY <= DEADLINE ):
		return PRE_DEADLINE
	elif( TODAY >= EXPIRES ):
		return EXPIRED_DEADLINE
	else:
		return POST_DEADLINE

##############################################################################
# Main Program Execution
##############################################################################

if( kernelAffected() ):
	DATE_VALUE = leapSecondDeadlineExceeded()
	if( DATE_VALUE >= EXPIRED_DEADLINE ):
		Core.updateStatus(Core.ERROR, "Kernel is affected by leap second, but ignoring -- too much time has passed.")
	elif( DATE_VALUE == POST_DEADLINE ):
		Core.updateStatus(Core.WARN, "The running kernel was affected by the positive leap second in June 2015, update to the latest kernel.")
	elif( DATE_VALUE == PRE_DEADLINE ):
		Core.updateStatus(Core.CRIT, "The system will be affected by the June 2015 leap second, update to the latest kernel")
else:
	Core.updateStatus(Core.IGNORE, "Kernel unaffected by leap second -- AVOIDED")

Core.printPatternResults()


