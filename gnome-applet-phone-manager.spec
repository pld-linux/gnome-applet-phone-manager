%define applet phone-manager
Summary:	Phone Manager
Summary(pl):	Zarz±dca telefonu
Name:		gnome-applet-%{applet}
Version:	0.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.usefulinc.com/gnome-phone-manager/gnome-%{applet}-0.4.tar.gz
# Source0-md5:	48856faffb8fc3d50c910c163b8e89d1
URL:		http://usefulinc.com/software/phonemgr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gob2 >= 2.0.6
BuildRequires:	gsmlib-devel >= 1.10-2
BuildRequires:	gnome-bluetooth-devel >= 0.5.1
Requires:	bluez-utils
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This applet will connect to your mobile phone over a serial port,
either via a cable, infra-red or Bluetooth connection.

It listens for text messages, and when they arrive, displays them on
the desktop.

%description -l pl
Ten aplet ³±czy siê z telefonem komórkowym przez port szeregowy przy
pomoc± kabelka, podczerwieni lub po³±czenia Bluetooth.

Oczekuje wiadomo¶ci tekstowych, a kiedy nadejd±, wy¶wietla je na
pulpicie.

%prep
%setup -q -n gnome-%{applet}-%{version}

%build
rm -f missing
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1 \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{applet} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files -f %{applet}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/gnome-%{applet}/*
%{_desktopdir}/*
