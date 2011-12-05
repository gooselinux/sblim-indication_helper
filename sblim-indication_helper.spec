Name:		sblim-indication_helper
Version:	0.5.0
Release:	1%{?dist}
Summary:	Toolkit for CMPI indication providers

Group:		Development/Libraries
License:	CPL
URL:		http://sblim.wiki.sourceforge.net/
Source0:	http://downloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch0:		missing-stderr-def.patch
BuildRequires:	sblim-cmpi-devel 

%description
This package contains a developer library for helping out when writing
CMPI providers. This library polls the registered functions for data
and, if it changes, a CMPI indication is set with the values of the
indication class properties (also set by the developer).

%Package	devel
Summary:	Toolkit for CMPI indication providers (Development Files)
Requires:	%{name} = %{version}-%{release} sblim-cmpi-devel glibc-devel
Group:		Development/Libraries


%description devel
This package contain developer library for helping out when writing
CMPI providers. This library polls the registered functions for data
and if they change an CMPI indication is set with the values of the
indication class properties (also set by the developer).

This package holds the development files for sblim-indication_helper.


%prep
%setup -q
%patch0 -p1 -b .missing-stderr-def


%build
%configure --disable-static --with-pic
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm %{buildroot}/%{_libdir}/libind_helper.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%doc README COPYING ChangeLog TODO
%{_libdir}/libind_helper.so.*



%files devel
%defattr(-,root,root,-)
%{_includedir}/sblim
%{_libdir}/libind_helper.so
%doc COPYING


%changelog
* Tue Jun 29 2010 Vitezslav Crhonk <vcrhonek@redhat.com> - 0.5.0-1
- Update to sblim-indication_helper-0.5.0

* Thu Nov 19 2009 Praveen K Paladugu <praveen_paladugu@dell.com> - 0.4.2-4
- missing the stderr definition in a file
 
* Fri Jul 31 2009 Praveen K Paladugu <praveen_paladugu@dell.com> - 0.4.2-3
- fixed the rpmlint message. Removed Requries for glibc-devel.

* Tue Jun 30 2009 Praveen K Paladugu <praveen_paladugu@dell.com> - 0.4.2-1
- Standardized the spec file and changed the build number to 1 

* Thu Oct 23 2008 Matt Domsch <Matt_Domsch@dell.com> - 0.4.2-134
- update for Fedora packaging guidelines
* Fri May 30 2008 npaxton@novell.com
- Change openwbem-devel dependency to sblim-cmpi-devel, to be
  cimom neutral
* Wed Feb 27 2008 crrodriguez@suse.de
- fix library-without-ldconfig* errors
- disable static libraries
* Wed Mar 01 2006 mrueckert@suse.de
- update to 0.4.2
  ind_helper.c, ind_helper.h:
  Bugs: 1203849 (side effect) made a lot of function arguments
  const in order to remove the cmpi-base warnings.
  added sblim-indication_helper-0.4.2_warnings.patch
  fixes a small warning regarding pointer size
* Wed Jan 25 2006 mls@suse.de
- created the package

