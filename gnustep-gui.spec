%define version		0.12.0
%define name		gnustep-gui
%define release		%mkrel 3

%define major	0.12

%define libname %mklibname %name %major
%define libnamedev %mklibname %name -d

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source: 	%{name}-%{version}.tar.bz2
License: 	GPL
Group:		Development/Other
Summary: 	GNUstep GUI package
URL:		http://www.gnustep.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	gnustep-base
BuildRequires:	gcc-objc
BuildRequires:	gnustep-base-devel >= 0.14.0
BuildRequires:	gnustep-make
BuildRequires:	cups-devel
BuildRequires:	aspell-devel
BuildRequires:	portaudio-devel
BuildRequires:	libaudiofile-devel
BuildRequires:	X11-devel	
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
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix}
make

%install
%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%doc ANNOUNCE COPYING.LIB BUGS NEWS README NOTES
%{_bindir}/*
%{_prefix}/lib/GNUstep/*

%files -n %{libname}
%defattr(-,root,root)
%{_prefix}/lib/*.so.*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_includedir}/*
%{_prefix}/lib/*.so
%{_datadir}/GNUstep/Makefiles/Additional/*
