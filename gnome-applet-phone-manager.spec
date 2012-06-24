%define		applet phone-manager
Summary:	GNOME Phone Manager applet
Summary(pl):	Zarz�dca telefonu - aplet GNOME
Name:		gnome-applet-%{applet}
Version:	0.4
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://downloads.usefulinc.com/gnome-phone-manager/gnome-%{applet}-0.4.tar.gz
# Source0-md5:	48856faffb8fc3d50c910c163b8e89d1
Patch0:		%{name}-sigc++.patch
Patch1:		%{name}-desktop.patch
URL:		http://usefulinc.com/software/phonemgr/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-bluetooth-devel >= 0.5.1
BuildRequires:	gsmlib-devel >= 1.10-2
BuildRequires:	gtk+2-devel
BuildRequires:	libbtctl-devel >= 0.4.1
BuildRequires:	libgnomeui-devel
BuildRequires:	libsigc++-devel >= 2.0.5
BuildRequires:	openobex-devel >= 1.0.0
Requires:	bluez-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This applet will connect to your mobile phone over a serial port,
either via a cable, infra-red or Bluetooth connection.

It listens for text messages, and when they arrive, displays them on
the desktop.

%description -l pl
Ten aplet ��czy si� z telefonem kom�rkowym przez port szeregowy przy
pomoc� kabelka, podczerwieni lub po��czenia Bluetooth.

Oczekuje wiadomo�ci tekstowych, a kiedy nadejd�, wy�wietla je na
pulpicie.

%prep
%setup -q -n gnome-%{applet}-%{version}
%patch0 -p1
%patch1 -p1

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
