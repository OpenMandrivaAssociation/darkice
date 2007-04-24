# (misc) TODO write a initscript, but it requires a proper daemonisation of the server
# and i was unable to code it
# also split --with plf in two

%define build_plf 0


%{?_with_plf: %{expand: %%global build_plf 1}}
%if %build_plf
%define distsuffix plf
%endif


Summary : DarkIce live IceCast / ShoutCast streamer
Name: darkice
Version: 0.18
Release: %mkrel 1
License: GPL
Group: Sound
Source: %{name}-%{version}.tar.bz2
URL: http://%{name}.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: libalsa-devel libogg-devel libvorbis-devel
BuildRequires: libjack-devel 
%if %build_plf
# for some reason, it need the static version to detect liblame
BuildRequires: liblame-static-devel
BuildRequires: libfaac-devel
%endif


%description
DarkIce is an IceCast, IceCast2 and ShoutCast live audio streamer. It
takes audio input from a sound card, encodes it into mp3 and/or Ogg Vorbis,
and sends the mp3 stream to one or more IceCast and/or ShoutCast servers,
the Ogg Vorbis stream to one or more IceCast2 servers.

%if %build_plf
This package is in plf as it was linked with Lame, a mp3 encoder, and support
AAC encoding.
%endif

%prep
%setup -q 
%build

%configure
make all

%install
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-, root, root)
%doc COPYING ChangeLog README TODO AUTHORS
%config(noreplace) %{_sysconfdir}/darkice.cfg
%{_bindir}/*
%{_mandir}/man1/darkice.1*
%{_mandir}/man5/darkice.cfg.5*
