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
%define mode 544
%define category SLE

Name:         sca-patterns-sle11
Summary:      Supportconfig Analysis Patterns for SLE11
URL:          https://bitbucket.org/g23guy/sca-patterns-sle11
Group:        Documentation/SuSE
Distribution: SUSE Linux Enterprise
Vendor:       SUSE Support
License:      GPL-2.0
Autoreqprov:  on
Version:      1.2
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

%prep
%setup -q

%build

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/sle11all
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/sle11sp0
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/sle11sp1
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/sle11sp2
install -d $RPM_BUILD_ROOT/%{patdir}/%{category}/sle11sp3
install -m %{mode} patterns/%{category}/sle11all/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle11all
install -m %{mode} patterns/%{category}/sle11sp0/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle11sp0
install -m %{mode} patterns/%{category}/sle11sp1/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle11sp1
install -m %{mode} patterns/%{category}/sle11sp2/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle11sp2
install -m %{mode} patterns/%{category}/sle11sp3/* $RPM_BUILD_ROOT/%{patdir}/%{category}/sle11sp3

%files
%defattr(-,%{patuser},%{patgrp})
%dir /var/opt/%{produser}
%dir %{patdir}
%dir %{patdir}/%{category}
%dir %{patdir}/%{category}/sle11all
%dir %{patdir}/%{category}/sle11sp0
%dir %{patdir}/%{category}/sle11sp1
%dir %{patdir}/%{category}/sle11sp2
%dir %{patdir}/%{category}/sle11sp3
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle11all/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle11sp0/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle11sp1/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle11sp2/*
%attr(%{mode},%{patuser},%{patgrp}) %{patdir}/%{category}/sle11sp3/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Dec 20 2013 jrecord@suse.com
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

