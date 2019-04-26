%define url_ver %(echo %{version}|cut -d. -f1,2)
%define debug_package %{nil}
%define __noautoreq /usr/bin/gjs

Name:		gnome-sound-recorder
Version:	3.32.0
Release:	1
Summary:	A simple, modern sound recorder
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
URL:		https://wiki.gnome.org/Apps/Polari
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	gjs
BuildRequires:	gsettings-desktop-schemas
BuildRequires:	desktop-file-utils
BuildRequires:	gstreamer1.0-tools
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	gstreamer1.0-plugins-base
BuildRequires:	gstreamer1.0-plugins-good
BuildRequires:	gstreamer1.0-flac

Obsoletes:	gnome-media
Requires:	gjs
Requires:	gsettings-desktop-schemas
Requires:	gstreamer1.0-plugins-base
Requires:	gstreamer1.0-plugins-good
Requires:	gstreamer1.0-flac

%description
A simple, modern sound recorder for the GNOME desktop.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS
%{_bindir}/%{name}
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/%{name}
%{_datadir}/applications/org.gnome.SoundRecorder.desktop
%{_iconsdir}/*/*/*/*
%{_datadir}/metainfo/org.gnome.SoundRecorder.appdata.xml
