%define		applet phone-manager
Summary:	GNOME Phone Manager applet
Summary(pl.UTF-8):	Zarządca telefonu - aplet GNOME
Name:		gnome-applet-%{applet}
Version:	0.65
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-phone-manager/%{version}/gnome-%{applet}-%{version}.tar.bz2
# Source0-md5:	afbe02a45062179978860a7b90b837b7
Patch0:		%{name}-desktop.patch
URL:		http://usefulinc.com/software/phonemgr/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	bluez-libs-devel >= 3.12
BuildRequires:	dbus-glib-devel
BuildRequires:	evolution-data-server-devel >= 2.20.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-bluetooth-devel >= 2.28.0
BuildRequires:	gnome-common
BuildRequires:	gnome-icon-theme >= 2.20.0
BuildRequires:	gtk+2-devel >= 2:2.10.0
BuildRequires:	gtkspell-devel >= 2.0
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libglade2-devel
BuildRequires:	libgnokii-devel >= 1:0.6.27
BuildRequires:	libtool
BuildRequires:	telepathy-glib-devel
BuildRequires:	pkgconfig
Requires(post,preun):	GConf2
Requires:	bluez-utils
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%{__intltoolize}
%{__libtoolize}
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

%find_lang gnome-phone-manager

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-phone-manager.schemas

%preun
%gconf_schema_uninstall gnome-phone-manager.schemas

%files -f gnome-phone-manager.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/gnome-phone-manager
%{_datadir}/gnome-phone-manager
%{_mandir}/man1/gnome-phone-manager.1*
%{_desktopdir}/gnome-phone-manager.desktop
%{_libdir}/telepathy-phoney
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.phoney.service
%{_datadir}/telepathy/managers/phoney.manager
%{_sysconfdir}/gconf/schemas/gnome-phone-manager.schemas
