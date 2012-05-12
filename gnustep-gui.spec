%define major	%(echo %version |cut -d. -f1-2)

%define libname %mklibname %name %major
%define libnamedev %mklibname %name -d

Name: 		gnustep-gui
Version: 	0.22.0
Release: 	3
Source0: 	ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
License: 	GPLv2+
Group:		Development/Other
Summary: 	GNUstep GUI package
URL:		http://www.gnustep.org/
Requires:	gnustep-base
BuildRequires:	gcc-objc
BuildRequires:	gnustep-base-devel >= 1.24.0
BuildRequires:	gnustep-make >= 2.6.2
BuildRequires:	cups-devel
BuildRequires:	aspell-devel
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng) >= 1.5
BuildRequires:	ungif-devel
Buildrequires:	pkgconfig(libtiff-4)
Requires:	gnustep-base

%description
This is a library of graphical user interface classes written completely in the
Objective-C language; the classes are based upon the OpenStep specification as
released by NeXT Software, Inc.  The library does not completely conform to the
specification and has been enhanced in a number of ways to take advantage of
the GNU system. These classes include graphical objects such as buttons, text
fields, popup lists, browser lists, and windows; there are also many associated
classes for handling events, colors, fonts, pasteboards and images.

%package -n     %{libname}
Summary:        Dynamic libraries from %name
Group:          System/Libraries

%description -n %{libname}
Dynamic libraries from %name.

%package -n     %{libnamedev}
Summary:        Header files and static libraries from %name
Group:          Development/Other
Requires:       %{libname} >= %{version}
Provides:       lib%{name}-devel = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release} 
Obsoletes:      %name-devel

%description -n %{libnamedev}
Libraries and includes files for developing programs based on %name.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -fr %buildroot
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%doc ANNOUNCE COPYING.LIB BUGS NEWS README
%{_bindir}/*
%{_prefix}/lib/GNUstep/*

%files -n %{libname}
%defattr(-,root,root)
%{_prefix}/lib/lib%{name}.so.%{major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_includedir}/*
%{_prefix}/lib/*.so
%{_datadir}/GNUstep/Makefiles/Additional/*
