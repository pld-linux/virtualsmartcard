Summary:	Virtual Smart Card - smart card emulator written in Python
Summary(pl.UTF-8):	Virtual Smart Card - emulator kart procesorowych napisany w Pythonie
Name:		virtualsmartcard
Version:	0.7
Release:	3
License:	GPL v3+
Group:		Applications/Emulators
#Source0Download: https://github.com/frankmorgner/vsmartcard/releases
Source0:	https://github.com/frankmorgner/vsmartcard/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	917119fbe74c0b0e331d3a84557c618a
Patch0:		%{name}-prefix.patch
URL:		https://frankmorgner.github.io/vsmartcard/
BuildRequires:	autoconf >= 2.64
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	help2man
BuildRequires:	libtool
BuildRequires:	pcsc-lite-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 2
BuildRequires:	qrencode-devel
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# uses log_msg symbol from pcscd
%define		skip_post_check_so	libifdvpcd.so.*

%description
Virtual Smart Card - smart card emulator written in Python.

%description -l pl.UTF-8
Virtual Smart Card - emulator kart procesorowych napisany w Pythonie.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-serialdropdir=$(pkg-config --variable=usbdropdir libpcsclite) \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/vicc
%attr(755,root,root) %{_bindir}/vpcd-config
%attr(755,root,root) %{_libdir}/pcsc/drivers/libifdvpcd.so*
%config(noreplace) %verify(not md5 mtime size) /etc/reader.conf.d/vpcd
%{py_sitescriptdir}/virtualsmartcard
%{_mandir}/man1/vicc.1*
