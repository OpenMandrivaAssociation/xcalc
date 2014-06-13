Name: xcalc
Version: 1.0.5
Release: 6
Summary: Scientific calculator for X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
Xcalc is a scientific calculator desktop accessory that can emulate a TI-30
or an HP-10C.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xcalc
%{_datadir}/X11/app-defaults/XCalc
%{_datadir}/X11/app-defaults/XCalc-color
%{_mandir}/man1/xcalc.1*


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4.1-2mdv2011.0
+ Revision: 671280
- mass rebuild

* Sat Nov 27 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4.1-1mdv2011.0
+ Revision: 602090
- new release

* Thu Nov 25 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 600979
- new release

* Fri Dec 18 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 479889
- New version: 1.0.3

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.2-5mdv2010.0
+ Revision: 366632
- no more autoconf needed

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2009.0
+ Revision: 226017
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-3mdv2008.1
+ Revision: 166450
- Revert to use upstream tarball, build requires and remove non mandatory local patches.
- Updated BuildRequires and resubmit package.
- Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-1mdv2008.0
+ Revision: 68677
- new upstream version: 1.0.2


* Fri Sep 01 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-09-01 19:22:17 (59409)
- rebuild for libXaw

* Thu Jun 01 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-06-01 20:13:15 (31864)
- fill in missing description & summaries

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-30 20:32:41 (31747)
- rebuild against new libXaw package

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

