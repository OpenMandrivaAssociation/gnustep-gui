%define version		0.9.5
%define name		gnustep-gui
%define prefix 		/usr/GNUstep/System

%define major 0.9

%define libname %mklibname %name %major
%define libnamedev %mklibname %name %major -d

Name: 		%{name}
Version: 	%{version}
Release: 	1mdk
Source: 	%{name}-%{version}.tar.bz2
License: 	GPL
Group:		Development/Other
Summary: 	GNUstep Gui package
URL:		http://www.gnustep.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
Requires:	gnustep-base
BuildRequires:	gnustep-make libgnustep-base-devel cups-devel

%description
It is a library of graphical user interface classes written
completely in the Objective-C language; the classes are based
upon the OpenStep specification as released by NeXT Software, Inc.
The library does not completely conform to the specification 
and has been enhanced in a number of ways to take advantage
of the GNU system. These classes include graphical objects
such as buttons, text fields, popup lists, browser lists,
and windows; there are also many associated classes
for handling events, colors, fonts, pasteboards and images.


%package -n %libname
Summary: GNUstep Gui library package
Group: Development/Other
Requires: %name
Provides: libgnustep-gui libgnustep-gui.so.%{major}

%description -n %libname
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.

%package -n %libnamedev
Summary: GNUstep Gui library package
Group: Development/Other
Requires: %libname = %version
Provides: libgnustep-gui-devel

%description -n %libnamedev
The GNUstep Base Library is a powerful fast library of general-purpose,
non-graphical Objective C classes, inspired by the superb OpenStep API but
implementing Apple and GNU additions to the API as well.  It includes for
example classes for unicode strings, arrays, dictionaries, sets, byte
streams, typed coders, invocations, notifications, notification dispatchers,
scanners, tasks, files, networking, threading, remote object messaging
support (distributed objects), event loops, loadable bundles, attributed
unicode strings, xml, mime, user defaults. This package includes development
headers too.

%prep
%setup -q -n %{name}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%{prefix}
make

%install
make INSTALL_ROOT_DIR=$RPM_BUILD_ROOT GNUSTEP_INSTALLATION_DIR=$RPM_BUILD_ROOT%{prefix} filelist=yes install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%doc ANNOUNCE COPYING.LIB BUGS
%doc INSTALL NEWS README NOTES
# Well - this is the simplest trick you could think of.  We include in
# the package everything which was installed inside /usr/GNUstep/System/
%{prefix}/Library/Bundles
%{prefix}/Library/ColorPickers
%{prefix}/Library/Images
%{prefix}/Library/Libraries/Resources
%{prefix}/Library/KeyBindings
%{prefix}/Library/Makefiles
%{prefix}/Library/PostScript
%{prefix}/Library/Services
%{prefix}/Tools

%files -n %libname
%defattr (-, root, root)
%{prefix}/Library/Libraries/*.so.*

%files -n %libnamedev
%defattr (-, root, root)
%{prefix}/Library/Libraries/*.so
%{prefix}/Library/Headers
