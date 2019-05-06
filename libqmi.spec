%global _hardened_build 1

Name: libqmi
Summary: Support library to use the Qualcomm MSM Interface (QMI) protocol
Version: 1.22.4
Release: 1%{?dist}
License: LGPLv2+
URL: http://freedesktop.org/software/libqmi
Source: http://freedesktop.org/software/libqmi/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: glib2-devel >= 2.32.0
BuildRequires: libgudev-devel >= 147
BuildRequires: python3
BuildRequires: gtk-doc
BuildRequires: libmbim-devel >= 1.18.0

%description
This package contains the libraries that make it easier to use QMI functionality
from applications that use glib.


%package devel
Summary: Header files for adding QMI support to applications that use glib
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: glib2-devel
Requires: pkgconfig

%description devel
This package contains the header and pkg-config files for development
applications using QMI functionality from applications that use glib.

%package utils
Summary: Utilities to use the QMI protocol from the command line
Requires: %{name}%{?_isa} = %{version}-%{release}
License: GPLv2+

%description utils
This package contains the utilities that make it easier to use QMI functionality
from the command line.


%prep
%setup -q

%build
%configure --disable-static --enable-gtk-doc --enable-mbim-qmux

# Uses private copy of libtool:
# http://fedoraproject.org/wiki/Packaging:Guidelines#Beware_of_Rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

LD_LIBRARY_PATH="$PWD/src/libqmi-glib/.libs" make %{?_smp_mflags} V=1

%install
make install DESTDIR=$RPM_BUILD_ROOT
%{__rm} -f $RPM_BUILD_ROOT%{_libdir}/*.la
find %{buildroot}%{_datadir}/gtk-doc |xargs touch --reference configure.ac


%ldconfig_scriptlets


%files
%doc NEWS AUTHORS README
%license COPYING
%{_libdir}/libqmi-glib.so.*
%{_datadir}/bash-completion

%files devel
%dir %{_includedir}/libqmi-glib
%{_includedir}/libqmi-glib/*.h
%{_libdir}/pkgconfig/qmi-glib.pc
%{_libdir}/libqmi-glib.so
%dir %{_datadir}/gtk-doc/html/libqmi-glib
%{_datadir}/gtk-doc/html/libqmi-glib/*

%files utils
%{_bindir}/qmicli
%{_bindir}/qmi-network
%{_bindir}/qmi-firmware-update
%{_mandir}/man1/*
%{_libexecdir}/qmi-proxy


%changelog
* Mon May 06 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.22.4-1
- Update to 1.22.4

* Thu Apr 11 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.22.2-1
- Update to 1.22.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 15 2019 Lubomir Rintel <lkundrak@v3.sk> - 1.20.0-1
- Update to 1.22.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.20.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Lubomir Rintel <lkundrak@v3.sk> - 1.20.0-1
- Update to 1.20.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.18.0-1
- Update to 1.18.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.16.2-1
- Update to 1.16.2

* Tue Oct 04 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.16.0-2
- Enable hardening

* Fri Jul 08 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.16.0-1
- Update to 1.16.0

* Tue May 03 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.14.2-1
- Update to 1.14.2

* Mon Mar 21 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.14.0-1
- Update to 1.14.0 release

* Tue Mar 01 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.12.6-3
- Fix FTBFS with GCC 6 (#1307733)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Aug 18 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.12.6-1
- Update to 1.12.6 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.12.4-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Wed Feb 11 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.12.4-1
- Update to 1.12.4 release

* Tue Feb 10 2015 Lubomir Rintel <lkundrak@v3.sk> - 1.12.2-1
- Clean up the spec file a bit
- Update to 1.12.2 release

* Thu Jan 15 2015 Dan Williams <dcbw@redhat.com> - 1.12.0-1
- Update to 1.12.0 release

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug  5 2014 Dan Williams <dcbw@redhat.com> - 1.10.2
- Update to 1.10.2 release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Feb  1 2014 poma <poma@gmail.com> - 1.8.0-1
- Update to 1.8.0 release

* Fri Sep  6 2013 Dan Williams <dcbw@redhat.com> - 1.6.0-1
- Update to 1.6.0 release

* Fri Jun  7 2013 Dan Williams <dcbw@redhat.com> - 1.4.0-1
- Update to 1.4.0 release

* Fri May 10 2013 Dan Williams <dcbw@redhat.com> - 1.3.0-1.git20130510
- Initial Fedora release

