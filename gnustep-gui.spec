%define version		0.12.0
%define name		gnustep-gui
%define release		%mkrel 1

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
BuildRequires:	gnustep-base >= 0.14.0
BuildRequires:	gnustep-make
BuildRequires:	cups-devel
BuildRequires:	aspell-devel
BuildRequires:	libportaudio-devel
BuildRequires:	libaudiofile-devel
BuildRequires:	X11-devel	

%description
This is a library of graphical user interface classes written completely in the
Objective-C language; the classes are based upon the OpenStep specification as
released by NeXT Software, Inc.  The library does not completely conform to the
specification and has been enhanced in a number of ways to take advantage of
the GNU system. These classes include graphical objects such as buttons, text
fields, popup lists, browser lists, and windows; there are also many associated
classes for handling events, colors, fonts, pasteboards and images.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{_prefix}
make

%install
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%doc ANNOUNCE COPYING.LIB BUGS NEWS README NOTES
%{_prefix}/GNUstep/System/Library/*
%{_prefix}/GNUstep/System/Tools/*
