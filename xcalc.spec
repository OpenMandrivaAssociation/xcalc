Name: xcalc
Version: 1.0.7
Release: 1
Summary: Scientific calculator for X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: pkgconfig(xt) >= 1.0.0
BuildRequires: xaw-devel >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.0.1

%description
Xcalc is a scientific calculator desktop accessory that can emulate a TI-30
or an HP-10C.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%{_bindir}/xcalc
%{_datadir}/X11/app-defaults/XCalc
%{_datadir}/X11/app-defaults/XCalc-color
%{_mandir}/man1/xcalc.1*
