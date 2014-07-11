%define major	4
%define gimajor	0.7
%define libname	%mklibname notify %{major}
%define girname	%mklibname notify-gir %{gimajor}
%define devname	%mklibname -d notify

Summary:	Desktop notifications library
Name:		libnotify
Version:	0.7.6
Release:	7
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.galago-project.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

Buildrequires:	gtk-doc
Buildrequires:	pkgconfig(dbus-glib-1)
Buildrequires:	pkgconfig(gobject-introspection-1.0)
Buildrequires:	pkgconfig(gtk+-3.0) >= 2.90
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

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Desktop notifications library - headers
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make LIBS='-lgmodule-2.0'

%install
%makeinstall_std

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/libnotify.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Notify-%{gimajor}.typelib

%files -n %{devname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/*
%{_datadir}/gir-1.0/Notify-%{gimajor}.gir

