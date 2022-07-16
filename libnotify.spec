%define major 4
%define gimajor 0.8
%define libname %mklibname notify %{major}
%define girname %mklibname notify-gir %{gimajor}
%define devname %mklibname -d notify

Summary:	Desktop notifications library
Name:		libnotify
Version:	0.8.0
Release:	1
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.galago-project.org/
Source0:	http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	meson
BuildRequires:	ninja
BuildRequires:	xsltproc
BuildRequires:	docbook-xsl-ns
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 2.90
BuildRequires:	pkgconfig(popt)
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
Requires:	typelib(GdkPixbuf)

%description -n %{girname}
GObject Introspection interface library for %{name}.

%package -n %{devname}
Group:		Development/C
Summary:	Desktop notifications library - headers
Requires:	%{name} = %{EVRD}
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Requires:	pkgconfig(gobject-introspection-1.0)

%description -n %{devname}
This package includes the development files for %{name}.

%prep
%autosetup -p1

%build
%meson -Dtests=false -Dgtk_doc=false -Ddocbook_docs=disabled

%meson_build

%install
%meson_install

%files
%{_bindir}/*
%doc %{_mandir}/man1/notify-send.1.*

%files -n %{libname}
%{_libdir}/libnotify.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Notify-%{gimajor}.typelib

%files -n %{devname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gir-1.0/Notify-%{gimajor}.gir
