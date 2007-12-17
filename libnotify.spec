%define major 1
%define libname %mklibname notify %{major}

Summary:	Desktop notifications library
Name:		libnotify
Version:	0.4.4
Release:	%mkrel 3
License:	GPL
Group:		System/Libraries
URL:		http://www.galago-project.org/
Source:		http://www.galago-project.org/files/releases/source/libnotify/libnotify-%version.tar.bz2
Buildrequires:	dbus-glib-devel
Buildrequires:	popt-devel
Buildrequires:	gtk+2-devel
Buildrequires:	gtk-doc

%description
A library that sends desktop notifications to a notification daemon, as
defined in the Desktop Notifications spec. These notifications can be
used to inform the user about an event or display some form of
information without getting in the user's way.

%package -n %{libname}
Group:		System/Libraries
Summary:	Desktop notifications library - shared library
Requires:	virtual-notification-daemon

%description -n %{libname}
A library that sends desktop notifications to a notification daemon, as
defined in the Desktop Notifications spec. These notifications can be
used to inform the user about an event or display some form of
information without getting in the user's way.

%package -n %{libname}-devel
Group:		Development/C
Summary:	Desktop notifications library - headers
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %libname-devel
A library that sends desktop notifications to a notification daemon, as
defined in the Desktop Notifications spec. These notifications can be
used to inform the user about an event or display some form of
information without getting in the user's way.


%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/lib*.a
%{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*
%{_includedir}/*
%_datadir/gtk-doc/html/*
