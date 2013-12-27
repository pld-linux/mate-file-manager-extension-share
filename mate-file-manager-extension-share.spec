Summary:	Share extension for Caja (MATE file manager)
Summary(pl.UTF-8):	Rozszerzenie share dla zarządcy plików Caja ze środowiska MATE
Name:		mate-file-manager-extension-share
Version:	1.6.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://pub.mate-desktop.org/releases/1.6/mate-file-manager-share-%{version}.tar.xz
# Source0-md5:	70a7a02fee63ae358e7e4d943f9206c5
URL:		http://mate-desktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel >= 0.10.40
BuildRequires:	glib2-devel >= 1:2.4.0
BuildRequires:	intltool >= 0.29
BuildRequires:	libtool >= 1:1.4.3
BuildRequires:	mate-file-manager-devel >= 1.1.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.4.0
Requires:	mate-file-manager >= 1.1.0
Requires:	samba-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mate-file-manager share extension allows you to quickly share a folder
from the MATE Caja file manager without requiring root access. It uses
Samba, so your folders can be accessed by any operating system.

%description -l pl.UTF-8
Rozszerzenie share dla mate-file-managera pozwala szybko udostępnić
folder z poziomu zarządcy plików Caja (ze środowiska MATE) bez dostępu
do uprawnień administratora. Wykorzystuje Sambę, więc foldery są
dostępne z dowolnego systemu operacyjnego.

%prep
%setup -q -n mate-file-manager-share-%{version}

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/caja/extensions-2.0/*.la

%find_lang mate-file-manager-share

%clean
rm -rf $RPM_BUILD_ROOT

%files -f mate-file-manager-share.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog MAINTAINERS README
%attr(755,root,root) %{_libdir}/caja/extensions-2.0/libcaja-share.so
%{_datadir}/mate-file-manager-share
