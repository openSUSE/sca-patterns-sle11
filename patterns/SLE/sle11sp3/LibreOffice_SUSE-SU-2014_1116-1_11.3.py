#!/usr/bin/python
#
# Title:       Important Security Announcement for LibreOffice SUSE-SU-2014:1116-1
# Description: Security fixes for SUSE Linux Enterprise 11 SP3
# Source:      Security Announcement Parser v1.0.1
# Modified:    2014 Sep 23
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

import os
import Core
import SUSE

META_CLASS = "Security"
META_CATEGORY = "SLE"
META_COMPONENT = "LibreOffice"
PATTERN_ID = os.path.basename(__file__)
PRIMARY_LINK = "META_LINK_Security"
OVERALL = Core.TEMP
OVERALL_INFO = "NOT SET"
OTHER_LINKS = "META_LINK_Security=http://lists.opensuse.org/opensuse-security-announce/2014-09/msg00010.html"
Core.init(META_CLASS, META_CATEGORY, META_COMPONENT, PATTERN_ID, PRIMARY_LINK, OVERALL, OVERALL_INFO, OTHER_LINKS)

LTSS = False
NAME = 'LibreOffice'
MAIN = 'libreoffice'
SEVERITY = 'Important'
TAG = 'SUSE-SU-2014:1116-1'
PACKAGES = {}
SERVER = SUSE.getHostInfo()

if ( SERVER['DistroVersion'] == 11):
	if ( SERVER['DistroPatchLevel'] == 3 ):
		PACKAGES = {
			'libreoffice-l10n-ko': '4.0.3.3.26-0.6.2',
			'libreoffice-impress': '4.0.3.3.26-0.6.2',
			'libreoffice-help-ko': '4.0.3.3.26-0.6.1',
			'libreoffice-officebean': '4.0.3.3.26-0.6.2',
			'libreoffice-base': '4.0.3.3.26-0.6.2',
			'libreoffice-help-cs': '4.0.3.3.26-0.6.1',
			'libreoffice-l10n-ru': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-sv': '4.0.3.3.26-0.6.2',
			'libreoffice-help-zh-CN': '4.0.3.3.26-0.6.1',
			'libreoffice-help-es': '4.0.3.3.26-0.6.1',
			'libreoffice-help-zh-TW': '4.0.3.3.26-0.6.1',
			'libreoffice-l10n-hi-IN': '4.0.3.3.26-0.6.2',
			'libreoffice-help-hi-IN': '4.0.3.3.26-0.6.1',
			'libreoffice-pyuno': '4.0.3.3.26-0.6.2',
			'libreoffice-kde': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-fi': '4.0.3.3.26-0.6.2',
			'libreoffice-writer-extensions': '4.0.3.3.26-0.6.2',
			'libreoffice-branding-upstream': '4.0.3.3.26-0.6.1',
			'libreoffice-l10n-sk': '4.0.3.3.26-0.6.2',
			'libreoffice-help-it': '4.0.3.3.26-0.6.1',
			'libreoffice-l10n-xh': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-da': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-nb': '4.0.3.3.26-0.6.2',
			'libreoffice': '4.0.3.3.26-0.6.2',
			'libreoffice-draw-extensions': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-fr': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-en-GB': '4.0.3.3.26-0.6.2',
			'libreoffice-help-pl': '4.0.3.3.26-0.6.1',
			'libreoffice-base-drivers-postgresql': '4.0.3.3.26-0.6.2',
			'libreoffice-help-hu': '4.0.3.3.26-0.6.1',
			'libreoffice-gnome': '4.0.3.3.26-0.6.2',
			'libreoffice-icon-themes': '4.0.3.3.26-0.6.2',
			'libreoffice-help-nl': '4.0.3.3.26-0.6.1',
			'libreoffice-help-ja': '4.0.3.3.26-0.6.1',
			'libreoffice-help-pt': '4.0.3.3.26-0.6.1',
			'libreoffice-kde4': '4.0.3.3.26-0.6.2',
			'libreoffice-math': '4.0.3.3.26-0.6.2',
			'libreoffice-help-ru': '4.0.3.3.26-0.6.1',
			'libreoffice-calc-extensions': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-ar': '4.0.3.3.26-0.6.2',
			'libreoffice-sdk': '4.0.3.3.26-0.6.2',
			'libreoffice-help-en-GB': '4.0.3.3.26-0.6.1',
			'libreoffice-calc': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-pt': '4.0.3.3.26-0.6.2',
			'libreoffice-help-sv': '4.0.3.3.26-0.6.1',
			'libreoffice-l10n-nl': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-ja': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-nn': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-gu-IN': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-prebuilt': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-pl': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-hu': '4.0.3.3.26-0.6.2',
			'libreoffice-help-fr': '4.0.3.3.26-0.6.1',
			'libreoffice-l10n-zh-TW': '4.0.3.3.26-0.6.2',
			'libreoffice-filters-optional': '4.0.3.3.26-0.6.2',
			'libreoffice-writer': '4.0.3.3.26-0.6.2',
			'libreoffice-help-de': '4.0.3.3.26-0.6.1',
			'libreoffice-help-pt-BR': '4.0.3.3.26-0.6.1',
			'libreoffice-help-da': '4.0.3.3.26-0.6.1',
			'libreoffice-l10n-pt-BR': '4.0.3.3.26-0.6.2',
			'libreoffice-mono': '4.0.3.3.26-0.6.2',
			'libreoffice-impress-extensions': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-it': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-ca': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-zu': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-de': '4.0.3.3.26-0.6.2',
			'libreoffice-base-extensions': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-es': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-af': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-el': '4.0.3.3.26-0.6.2',
			'libreoffice-mailmerge': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-cs': '4.0.3.3.26-0.6.2',
			'libreoffice-draw': '4.0.3.3.26-0.6.2',
			'libreoffice-l10n-zh-CN': '4.0.3.3.26-0.6.2',
			'libreoffice-help-en-US': '4.0.3.3.26-0.6.1',
			'libreoffice-help-gu-IN': '4.0.3.3.26-0.6.1',
		}
		SUSE.securityAnnouncementPackageCheck(NAME, MAIN, LTSS, SEVERITY, TAG, PACKAGES)
	else:
		Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the service pack scope")
else:
	Core.updateStatus(Core.ERROR, "ERROR: " + NAME + " Security Announcement: Outside the distribution scope")
Core.printPatternResults()

