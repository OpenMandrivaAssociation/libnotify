%define major 4
%define girmajor	0.7
%define libname %mklibname notify %{major}
%define girname %mklibname notify-gir %{girmajor}
%define develname %mklibname -d notify

Summary:	Desktop notifications library
Name:		libnotify
Version:	0.7.5
Release:	2
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
Obsoletes:	%mklibname -d notify 1

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
find %{buildroot} -name '*.la' -delete

# remove some quite annoying /usr/usr
perl -pi -e "s|/usr/usr/%{_lib}|%{_libdir}|g" %{buildroot}%{_libdir}/*.la

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

