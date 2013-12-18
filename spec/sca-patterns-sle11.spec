#
# spec file for package scdiag (Version 1.0)
#
# Copyright (C) 2013 SUSE LLC
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild

%define produser sca
%define prodgrp sdp
%define patuser root
%define patgrp root
%define patdir /var/opt/%{produser}/patterns

Name:         sca-patterns-sle11
Summary:      Supportconfig Analysis Patterns for SLE11
Group:        Documentation/SuSE
Distribution: SUSE Linux Enterprise
Vendor:       SUSE Support
License:      GPLv2
Autoreqprov:  on
Version:      1.1
Release:      1
Source:       %{name}-%{version}.tar.gz
BuildRoot:    %{_tmppath}/%{name}-%{version}
Buildarch:    noarch
Requires:     sca-patterns-base
%description
Supportconfig Analysis (SCA) appliance patterns to identify known
issues relating to all versions of SLES/SLED 11

Authors:
--------
    Jason Record <jrecord@suse.com>

%files
%defattr(-,%{patuser},%{patgrp})
%dir /var/opt/%{produser}
%dir %{patdir}
%dir %{patdir}/SLE
%dir %{patdir}/SLE/sle11all
%dir %{patdir}/SLE/sle11sp0
%dir %{patdir}/SLE/sle11sp1
%dir %{patdir}/SLE/sle11sp2
%dir %{patdir}/SLE/sle11sp3
%attr(555,%{patuser},%{patgrp}) %{patdir}/SLE/sle11all/*
%attr(555,%{patuser},%{patgrp}) %{patdir}/SLE/sle11sp0/*
%attr(555,%{patuser},%{patgrp}) %{patdir}/SLE/sle11sp1/*
%attr(555,%{patuser},%{patgrp}) %{patdir}/SLE/sle11sp2/*
%attr(555,%{patuser},%{patgrp}) %{patdir}/SLE/sle11sp3/*

%prep
%setup -q

%build
make build

%install
make install

%changelog
* Wed Dec 18 2013 jrecord@suse.com
- separated as individual RPM package
- updated vmware-00001.pl link
- added time consideration to lastdown-3301593.py
- additional error checking in lastdown-3301593.py
- added
  tmp-7002723.py sleall
  firefox-SUSE-SU-2013_1678-1a.pl sle11sp3
  firefox-SUSE-SU-2013_1678-1b.pl sle11sp2
  firefox-SUSE-SU-2013_1678-1c.pl sle11sp1
  flash-SUSE-SU-2013_1716-1a.pl sle11sp3
  flash-SUSE-SU-2013_1716-1b.pl sle11sp2
  java-SUSE-SU-2013_1677-2a.pl sle11sp3
  java-SUSE-SU-2013_1677-2b.pl sle11sp2
  java-SUSE-SU-2013_1677-2c.pl sle11sp1
  java-SUSE-SU-2013_1677-3a.pl sle11sp3
  java-SUSE-SU-2013_1677-3b.pl sle11sp2
  kdev-7003734.py sle11all
  kernel-SUSE-SU-2013_1748-1.pl sle11sp2
  kernel-SUSE-SU-2013_1749-1.pl sle11sp3
  xfs-7013481a.py sle11sp2
  xfs-7013481b.py sle11sp3
  xfs-7014242.py sle11all

