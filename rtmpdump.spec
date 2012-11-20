%define		gitrev	19d36368f6c1ec6fa55df319173ca93048309f9a

Summary:	A utility for getting files from RTMP servers
Name:		rtmpdump
Version:	2.4
Release:	0.%{gitrev}.1
License:	GPL v2
Group:		Applications/Networking
#Source0:	http://rtmpdump.mplayerhq.hu/download/%{name}-%{version}.tgz
Source0:	%{name}-%{version}-%{gitrev}.tar.xz
# Source0-md5:	72421f7b1fbf3f9ddd0bf4ccc758741c
URL:		http://rtmpdump.mplayerhq.hu/
BuildRequires:	gnutls-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rtmpdump is a toolkit for RTMP streams. All forms of RTMP are
supported, including rtmp://, rtmpt://, rtmpe://, rtmpte:// and
rtmps://.

%package libs
Summary:	RTMP library - RTMPDump Real-Time Messaging Protocol API
License:	LGPL v2.1+
Group:		Libraries

%description libs
RTMP library - RTMPDump Real-Time Messaging Protocol API.

%package devel
Summary:	Header files for RTMP library
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gnutls-devel
Requires:	zlib-devel

%description devel
Header files for RTMP library.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}"		\
	CRYPTO=GNUTLS		\
	LDFLAGS="%{rpmldflags}"	\
	OPT="%{rpmcppflags} %{rpmcflags}"	\
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT	\
	libdir=%{_libdir}	\
	mandir=%{_mandir}	\
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/rtmpdump
%attr(755,root,root) %{_sbindir}/rtmpgw
%attr(755,root,root) %{_sbindir}/rtmpsrv
%attr(755,root,root) %{_sbindir}/rtmpsuck
%{_mandir}/man1/rtmpdump.1*
%{_mandir}/man8/rtmpgw.8*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librtmp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librtmp.so
%{_includedir}/librtmp
%{_pkgconfigdir}/librtmp.pc
%{_mandir}/man3/librtmp.3*

