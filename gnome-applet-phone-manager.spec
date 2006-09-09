%define		applet phone-manager
Summary:	GNOME Phone Manager applet
Summary(pl):	Zarz±dca telefonu - aplet GNOME
Name:		gnome-applet-%{applet}
Version:	0.7
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-phone-manager/%{version}/gnome-%{applet}-%{version}.tar.bz2
# Source0-md5:	951471bf5d6fe93fe550c60b6bdf58f9
Patch0:		%{name}-desktop.patch
URL:		http://usefulinc.com/software/phonemgr/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.8
BuildRequires:	evolution-devel >= 2.6.1
BuildRequires:	gnome-bluetooth-devel >= 0.7.0
BuildRequires:	gsmlib-devel >= 1.10-2
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	intltool >= 0.18
BuildRequires:	libbtctl-devel >= 0.5.0
BuildRequires:	libgnokii-devel >= 0.6.5
BuildRequires:	libgnomeui-devel >= 2.14.0
BuildRequires:	openobex-devel >= 1.0.0
BuildRequires:	pkgconfig
Requires:	bluez-utils
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
%patch0 -p1

%build
%{__glib_gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install ui/cellphone.png $RPM_BUILD_ROOT%{_pixmapsdir}/gnome-phone-manager.png
install ui/cellphone.png $RPM_BUILD_ROOT%{_datadir}/gnome-%{applet}

rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{applet} --with-gnome --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{applet}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/gnome-%{applet}
%{_datadir}/gnome-%{applet}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
