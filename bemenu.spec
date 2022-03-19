Summary:	Dynamic menu library and client program inspired by dmenu
Name:		bemenu
Version:	0.6.7
Release:	1
License:	LGPL v3+, GPL v3+
Group:		Applications
Source0:	https://github.com/Cloudef/bemenu/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0192901b294b8d1b159a33961ce87f71
URL:		https://github.com/Cloudef/bemenu
BuildRequires:	cairo-devel
BuildRequires:	ncurses-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	scdoc
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
Requires:	bemenu-renderer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dynamic menu library and client program inspired by dmenu.

%package renderer-curses
Summary:	Curses renderer for bemenu
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Provides:	bemenu-renderer

%description renderer-curses
Curses renderer for bemenu.

%package renderer-wayland
Summary:	Wayland renderer for bemenu
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Provides:	bemenu-renderer

%description renderer-wayland
Wayland renderer for bemenu.

%package renderer-x11
Summary:	X11 renderer for bemenu
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Provides:	bemenu-renderer

%description renderer-x11
X11 renderer for bemenu.

%package devel
Summary:	Header files for bemenu
Group:		Development/Libraries

%description devel
Header files for bemenu.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	CPPFLAGS="%{rpmcppflags}" \
	LDFLAGS="%{rpmldflags}" \
	PREFIX=%{_prefix} \
	libdir=/%{_lib}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	PREFIX=%{_prefix} \
	libdir=/%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/bemenu
%attr(755,root,root) %{_bindir}/bemenu-run
%attr(755,root,root) %{_libdir}/libbemenu.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libbemenu.so.0
%dir %{_libdir}/bemenu
%{_mandir}/man1/bemenu.1*

%files renderer-curses
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bemenu/bemenu-renderer-curses.so

%files renderer-wayland
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bemenu/bemenu-renderer-wayland.so

%files renderer-x11
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bemenu/bemenu-renderer-x11.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libbemenu.so
%{_includedir}/bemenu.h
%{_pkgconfigdir}/bemenu.pc
