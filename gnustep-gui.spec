%define major	%(echo %version |cut -d. -f1)
%define libname %mklibname %{name}
%define devname %mklibname %{name} -d
%define underscoredversion %(echo %{version} |sed -e 's,\\.,_,g')

Summary: 	GNUstep GUI package
Name: 		gnustep-gui
Version: 	0.32.0
Release: 	1
License: 	GPLv2+
Group:		Development/Other
Url:		https://www.gnustep.org/
Source0: 	https://github.com/gnustep/libs-gui/releases/download/gui-%{underscoredversion}/gnustep-gui-%{version}.tar.gz
Patch0:		gnustep-gui-icu-69.patch
Patch1:		gnustep-gnu-0.30.0-clang16.patch

BuildRequires:	gnustep-make >= 2.9.1
BuildRequires:	aspell-devel
BuildRequires:	cups-devel
BuildRequires:	gnustep-base-devel >= 1.29.0
BuildRequires:	jpeg-devel
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(krb5-gssapi)
BuildRequires:	pkgconfig(com_err)
BuildRequires:	pkgconfig(libobjc)

BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(libpng) >= 1.5
BuildRequires:	pkgconfig(libtiff-4)
Requires:	gnustep-base >= 1.29.0

%description
This is a library of graphical user interface classes written completely in the
Objective-C language; the classes are based upon the OpenStep specification as
released by NeXT Software, Inc.  The library does not completely conform to the
specification and has been enhanced in a number of ways to take advantage of
the GNU system. These classes include graphical objects such as buttons, text
fields, popup lists, browser lists, and windows; there are also many associated
classes for handling events, colors, fonts, pasteboards and images.

%package -n     %{libname}
Summary:        Dynamic libraries from %{name}
Group:          System/Libraries
%define oldlibname %mklibname %{name} 0.29
Obsoletes:	%{oldlibname} < %{EVRD}

%description -n %{libname}
Dynamic libraries from %{name}.

%package -n     %{devname}
Summary:        Header files and development library from %{name}
Group:          Development/Other
Requires:       %{libname} >= %{version}
Provides:       %{name}-devel = %{version}-%{release} 

%description -n %{devname}
Library and includes files for developing programs based on %{name}.

%prep
%autosetup -p1

%build
export CC=`gnustep-config --variable=CC`
export CXX=`gnustep-config --variable=CXX`

%configure --with-installation-domain=SYSTEM
%make_build GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%install
%make_install GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%doc ANNOUNCE COPYING.LIB BUGS NEWS README
%{_bindir}/*
%{_libdir}/GNUstep/*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/GNUstep/Makefiles/Additional/*
%{_libdir}/pkgconfig/*.pc
