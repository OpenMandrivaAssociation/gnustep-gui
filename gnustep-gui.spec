%define major	%(echo %version |cut -d. -f1-2)

%define libname %mklibname %name %major
%define libnamedev %mklibname %name -d

Name: 		gnustep-gui
Version: 	0.23.1
Release: 	1
Source0: 	ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz
Patch1:		gnustep-gui-0.23.1-giflib5.patch
License: 	GPLv2+
Group:		Development/Other
Summary: 	GNUstep GUI package
URL:		http://www.gnustep.org/
Requires:	gnustep-base >= 1.24.0-3
BuildRequires:	gcc-objc
BuildRequires:	gnustep-base-devel >= 1.24.0-2
BuildRequires:	gnustep-make >= 2.6.2-3
BuildRequires:	cups-devel
BuildRequires:	aspell-devel
BuildRequires:	pkgconfig(ao)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(libpng) >= 1.5
BuildRequires:	ungif-devel
Buildrequires:	pkgconfig(libtiff-4)

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
%patch1 -p1

%build
%configure2_5x --with-installation-domain=SYSTEM
%make GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%install
rm -fr %buildroot
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files
%defattr (-, root, root)
%doc ANNOUNCE COPYING.LIB BUGS NEWS README
%{_bindir}/*
%{_libdir}/GNUstep/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/GNUstep/Makefiles/Additional/*


%changelog
* Sat May 12 2012 Bernhard Rosenkraenzer <bero@bero.eu> 0.22.0-3
+ Revision: 798521
- Fix BuildRequirement on 32bit libraries on x86_64
- Rebuild for current gnustep-core

  + Lev Givon <lev@mandriva.org>
    - Bump release to force rebuild.
    - Update to 0.22.0.

* Tue Aug 03 2010 Funda Wang <fwang@mandriva.org> 0.18.0-1mdv2011.0
+ Revision: 565346
- new version 0.18.0

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 0.16.0-1mdv2010.0
+ Revision: 436524
- adjust file list

  + Funda Wang <fwang@mandriva.org>
    - protect major

* Wed Jan 07 2009 Funda Wang <fwang@mandriva.org> 0.16.0-1mdv2009.1
+ Revision: 326911
- New version 0.16.0

* Thu Aug 21 2008 Funda Wang <fwang@mandriva.org> 0.14.0-2mdv2009.0
+ Revision: 274529
- fix underlink
- New version 0.14.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jun 03 2008 Franck Villaume <fvill@mandriva.com> 0.13.2-1mdv2009.0
+ Revision: 214482
- new version 0.13.2

* Tue Jan 22 2008 Funda Wang <fwang@mandriva.org> 0.12.1-1mdv2008.1
+ Revision: 156246
- New version 0.12.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.12.0-4mdv2008.0
+ Revision: 67910
- rebuilt against new portaudio libs

* Mon Jul 23 2007 Austin Acton <austin@mandriva.org> 0.12.0-3mdv2008.0
+ Revision: 54501
- fix lib64 requires
- re-libify
- new directory structure
- drop hacky provides

* Sun Jun 03 2007 Austin Acton <austin@mandriva.org> 0.12.0-2mdv2008.0
+ Revision: 34948
- increment release
- explicit provides

* Sun Jun 03 2007 Austin Acton <austin@mandriva.org> 0.12.0-1mdv2008.0
+ Revision: 34793
- buildrequires gcc-objc
- simplify, simplify, simplify

  + Adam Williamson <awilliamson@mandriva.org>
    - Import gnustep-gui



* Mon Apr 04 2005 Charles A Edwards <eslrahc@mandrake.org> 0.9.5-1mdk
- 0.9.5
- quiet setup
- buildrequires

* Thu Oct  7 2004 Nicolas Planel <nplanel@n3.mandrakesoft.com> 0.9.4-2mdk
- move lib to libgnustep-gui.

* Thu Oct  7 2004 Nicolas Planel <nplanel@mandrakesoft.com> 0.9.4-1mdk
- 0.9.4.
