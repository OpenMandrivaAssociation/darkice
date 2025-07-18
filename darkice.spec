Summary:	Live IceCast / ShoutCast streamer
Name:		darkice
Version:	1.5
Release:	1
License:	GPLv3+
Group:	Sound
Url:		http://www.darkice.org/
# The devel tree really is here: https://github.com/rafael2k/darkice, but it contains much more
# than darkice only.
Source0:	https://github.com/rafael2k/darkice/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(lame)
BuildRequires:	pkgconfig(libaacs)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(ogg)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(twolame)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(vorbisenc)

%description
This is an IceCast, IceCast2 and ShoutCast live audio streamer. It takes audio
input from a sound card, encodes it into mp3 and/or Ogg Vorbis, and sends the
mp3 stream to one or more IceCast and/or ShoutCast servers, the Ogg Vorbis
stream to one or more IceCast2 servers.

%files
%license COPYING
%doc AUTHORS ChangeLog FAQ README TODO
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.cfg.5*

#----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
# For aacplus we need libaacplus, but it has legal issues:
# see http://tipok.org.ua/node/17
%configure \
		--with-flac \
	    --with-lame \
	    --with-opus \
	    --with-twolame \
	    --with-vorbis \
	    --without-aacplus

%make_build


%install
%make_install
