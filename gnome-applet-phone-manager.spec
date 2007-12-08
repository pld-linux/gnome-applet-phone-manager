%define		applet phone-manager
Summary:	GNOME Phone Manager applet
Summary(pl.UTF-8):	Zarządca telefonu - aplet GNOME
Name:		gnome-applet-%{applet}
Version:	0.40
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-phone-manager/%{version}/gnome-%{applet}-%{version}.tar.bz2
# Source0-md5:	38537c212e9b2395cf89187ab2be3b9a
Patch0:		%{name}-desktop.patch
URL:		http://usefulinc.com/software/phonemgr/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.8
BuildRequires:	evolution-devel >= 2.6.1
BuildRequires:	gnome-bluetooth-devel > 0.8.0
BuildRequires:	gstreamer-devel >= 0.10
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	intltool >= 0.18
BuildRequires:	libbtctl-devel >= 0.5.0
BuildRequires:	librsvg-devel >= 1:2.0
BuildRequires:	libgnokii-devel >= 0.6.18
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	openobex-devel >= 1.0.0
BuildRequires:	pkgconfig
Requires:	bluez-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_ld	-Wl,--as-needed

%description
This applet will connect to your mobile phone over a serial port,
either via a cable, infra-red or Bluetooth connection.

It listens for text messages, and when they arrive, displays them on
the desktop.

%description -l pl.UTF-8
Ten aplet łączy się z telefonem komórkowym przez port szeregowy przy
pomocą kabelka, podczerwieni lub połączenia Bluetooth.

Oczekuje wiadomości tekstowych, a kiedy nadejdą, wyświetla je na
pulpicie.

%prep
%setup -q -n gnome-%{applet}-%{version}
%patch0 -p1

%build
%{__glib_gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/scrollkeeper-update
%gconf_schema_install

%postun -p /usr/bin/scrollkeeper-update

%files
# -f %{applet}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_sysconfdir}/gconf/schemas/gnome-phone-manager.schemas
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/gnome-%{applet}
%{_datadir}/gnome-%{applet}/*
%{_desktopdir}/*.desktop
