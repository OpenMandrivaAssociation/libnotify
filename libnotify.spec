%define major 4
%define girmajor 0.7
%define libname %mklibname notify %{major}
%define girname %mklibname notify-gir %{girmajor}
%define develname %mklibname -d notify

Summary:	Desktop notifications library
Name:		libnotify
Version:	0.7.5
Release:	3
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.galago-project.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

Buildrequires:	gtk-doc
Buildrequires:	pkgconfig(dbus-glib-1)
Buildrequires:	pkgconfig(gtk+-3.0) >= 2.90
Buildrequires:	pkgconfig(gobject-introspection-1.0)
Buildrequires:	pkgconfig(popt)

Requires:	virtual-notification-daemon

%description
A library that sends desktop notifications to a notification daemon, as
defined in the Desktop Notifications spec. These notifications can be
used to inform the user about an event or display some form of
information without getting in the user's way.

%package -n %{libname}
Group:		System/Libraries
Summary:	Desktop notifications library - shared library

%description -n %{libname}
A library that sends desktop notifications to a notification daemon, as
defined in the Desktop Notifications spec. These notifications can be
used to inform the user about an event or display some form of
information without getting in the user's way.

%package -n %{girname}
Group:		System/Libraries
Summary:	GObject Introspection interface library for %{name}
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{develname}
Group:		Development/C
Summary:	Desktop notifications library - headers
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d notify 1} < 0.7

%description -n %{develname}
A library that sends desktop notifications to a notification daemon, as
defined in the Desktop Notifications spec. These notifications can be
used to inform the user about an event or display some form of
information without getting in the user's way.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make LIBS='-lgmodule-2.0'

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Notify-%{girmajor}.typelib

%files -n %{develname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/*
%{_datadir}/gir-1.0/Notify-%{girmajor}.gir



%changelog
* Thu Apr 26 2012 Guilherme Moro <guilherme@mandriva.com> 0.7.5-2
+ Revision: 793626
- rebuild for typelib generation

* Tue Mar 27 2012 Götz Waschk <waschk@mandriva.org> 0.7.5-1
+ Revision: 787408
- new version

* Wed Feb 15 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.7.4-5
+ Revision: 774340
- added fix for gmodule-2.0 build error
- rebuild for ffi5

* Wed Nov 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.7.4-4
+ Revision: 732810
- rebuild
- clean up spec
- moved require for virtual-notification-daemon to main pkg
- that drops the need to bootstrap
- removed .la files
- disabled static build
- removed defattr
- split out gir pkg
- removed clean section
- removed mkrel & BuildRoot

* Sun Nov 20 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.4-3
+ Revision: 731963
- rebuild
- slight cleanups
- remove some quite annoying /usr/usr

* Thu Sep 22 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.4-2
+ Revision: 700997
- rebuild for new libpng15

* Sun Aug 28 2011 Götz Waschk <waschk@mandriva.org> 0.7.4-1
+ Revision: 697263
- new version
- xz tarball

* Mon May 09 2011 Götz Waschk <waschk@mandriva.org> 0.7.3-1
+ Revision: 673064
- update to new version 0.7.3

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.7.2-2
+ Revision: 662387
- mass rebuild

* Mon Apr 04 2011 Götz Waschk <waschk@mandriva.org> 0.7.2-1
+ Revision: 650373
- new version
- new major
- update build deps
- enable introspection

* Wed Dec 22 2010 Götz Waschk <waschk@mandriva.org> 0.5.2-1mdv2011.0
+ Revision: 623866
- new version
- update source URL

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.5-4mdv2011.0
+ Revision: 602584
- rebuild

* Sun Sep 27 2009 Olivier Blin <blino@mandriva.org> 0.4.5-3mdv2010.0
+ Revision: 449905
- add bootstrap flag for build loop libnotify1 <-> notification-daemon
  (from Arnaud Patard)

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 0.4.5-2mdv2010.0
+ Revision: 374456
- fix license
- new devel name

* Thu Nov 20 2008 Götz Waschk <waschk@mandriva.org> 0.4.5-1mdv2009.1
+ Revision: 305258
- update to new version 0.4.5

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.4.4-7mdv2009.0
+ Revision: 225682
- rebuild
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.4-5mdv2008.1
+ Revision: 178979
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Jun 02 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.4-3mdv2008.0
+ Revision: 34662
- requires virtual-notification-daemon

* Sat Jun 02 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.4.4-2mdv2008.0
+ Revision: 34506
- drop requires on notification-daemon - as it is conflicts with xfce's one
- spec file clean


* Wed Feb 28 2007 Jérôme Soyer <saispo@mandriva.org> 0.4.4-1mdv2007.0
+ Revision: 126923
- New release 0.4.4
- Bump release
- Switch virtual-notification-daemon to notification-daemon

* Wed Jan 10 2007 Jérôme Soyer <saispo@mandriva.org> 0.4.3-2mdv2007.1
+ Revision: 107078
- Add Provides

* Wed Nov 08 2006 Colin Guthrie <cguthrie@mandriva.org> 0.4.3-1mdv2007.0
+ Revision: 78549
- New Release
- Import libnotify

* Wed Aug 02 2006 Götz Waschk <waschk@mandriva.org> 0.4.2-2mdv2007.0
- fix buildrequires

* Mon Jun 19 2006 Götz Waschk <waschk@mandriva.org> 0.4.2-1mdv2007.0
- update file list
- New release 0.4.2

* Thu Apr 27 2006 Götz Waschk <waschk@mandriva.org> 0.4.0-1mdk
- New release 0.4.0

* Thu Jan 26 2006 Götz Waschk <waschk@mandriva.org> 0.3.2-2mdk
- fix buildrequires

* Wed Jan 25 2006 Götz Waschk <waschk@mandriva.org> 0.3.2-1mdk
- major 1
- update deps
- New release 0.3.2

* Wed Jan 25 2006 Götz Waschk <waschk@mandriva.org> 0.3.0-1mdk
- change deps
- New release 0.3.0
- use mkrel

* Thu Nov 24 2005 Götz Waschk <waschk@mandriva.org> 0.2.2-3mdk
- depend on notification-daemon

* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 0.2.2-2mdk
- fix buildrequires

* Wed Oct 26 2005 Götz Waschk <waschk@mandriva.org> 0.2.2-1mdk
- initial mdk package

* Wed Jul 13 2005 Richard Hughes <richard@hughsie.com> 0.0.1-1
- initial packaging of 0.0.1

