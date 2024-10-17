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
Version: 1.1
Release: 3
License: GPLv3+
Group: Sound
Source: http://darkice.googlecode.com/files/%{name}-%{version}.tar.gz
Patch: darkice-0.19-fix-missing-limits_h.diff
URL: https://code.google.com/p/darkice/  
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(ogg)
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(jack)
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
%patch -p0

%build

%configure
%make all

%install
%makeinstall

%files
%defattr (-, root, root)
%doc COPYING ChangeLog README TODO AUTHORS
%config(noreplace) %{_sysconfdir}/darkice.cfg
%{_bindir}/*
%{_mandir}/man1/darkice.1*
%{_mandir}/man5/darkice.cfg.5*


%changelog
* Wed Dec 14 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.1-1
+ Revision: 741043
- version update 1.1

* Wed Sep 01 2010 Michael Scherer <misc@mandriva.org> 1.0-1mdv2011.0
+ Revision: 574986
- update to 1.0
- fix download url and License

* Thu Feb 04 2010 Michael Scherer <misc@mandriva.org> 0.20.1-1mdv2010.1
+ Revision: 500616
- new version
- new url

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Jul 09 2008 Michael Scherer <misc@mandriva.org> 0.19-1mdv2009.0
+ Revision: 232919
- new version 0.19
- new url
- add patch to fix build

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.18.1-1mdv2008.1
+ Revision: 136360
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 01 2007 Michael Scherer <misc@mandriva.org> 0.18.1-1mdv2008.0
+ Revision: 19937
- upgrade to 0.18.1

* Tue Apr 24 2007 Michael Scherer <misc@mandriva.org> 0.18-1mdv2008.0
+ Revision: 17885
- ermove lib64 hack, as this is not correctly detected
- upgrade to 0.18
- patch1 is now included upstream
- Import darkice

