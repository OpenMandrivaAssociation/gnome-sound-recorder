%define url_ver %(echo %{version}|cut -d. -f1,2)
%define debug_package %{nil}
%define __noautoreq /usr/bin/gjs

Name:		gnome-sound-recorder
Version:	3.28.1
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
%make

%install
%makeinstall_std

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


%changelog
* Tue Nov 11 2014 ovitters <ovitters> 3.14.2-1.mga5
+ Revision: 796324
- new version 3.14.2

* Sat Nov 01 2014 wally <wally> 3.14.0.1-4.mga5
+ Revision: 795089
- add missing BuildRequires and Requires for gjs (mga#13848)

* Sun Oct 19 2014 wally <wally> 3.14.0.1-3.mga5
+ Revision: 791741
- rebuild with new rpm-mageia-setup

* Wed Oct 15 2014 umeabot <umeabot> 3.14.0.1-2.mga5
+ Revision: 747781
- Second Mageia 5 Mass Rebuild

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0.1-1.mga5
+ Revision: 719189
- new version 3.14.0.1

* Tue Sep 16 2014 umeabot <umeabot> 3.14-2.mga5
+ Revision: 679767
- Mageia 5 Mass Rebuild

  + tv <tv>
    - auto convert _exclude_files_from_autoreq

* Tue Sep 16 2014 ovitters <ovitters> 3.14-1.mga5
+ Revision: 676943
- new version 3.14

* Tue Sep 02 2014 ovitters <ovitters> 3.13.91-1.mga5
+ Revision: 670854
- new version 3.13.91

* Wed Jul 23 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655749
- new version 3.13.4

* Tue May 13 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622420
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614075
- new version 3.12.1

* Tue Mar 25 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 608214
- new version 3.12.0

* Wed Mar 19 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 605808
- new version 3.11.92

* Tue Mar 04 2014 ovitters <ovitters> 3.11.91.1-1.mga5
+ Revision: 599287
- new version 3.11.91.1

* Mon Mar 03 2014 ovitters <ovitters> 3.11.91-1.mga5
+ Revision: 598815
- new version 3.11.91

* Mon Feb 17 2014 dams <dams> 3.11.9-2.mga5
+ Revision: 593906
- Adds an obsoletes on 'gnome-media'

* Mon Feb 17 2014 ovitters <ovitters> 3.11.9-1.mga5
+ Revision: 593877
- imported package gnome-sound-recorder

