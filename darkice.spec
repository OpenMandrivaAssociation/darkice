Summary:	Live IceCast / ShoutCast streamer
Name:		darkice
Version:	1.6
Release:	1
License:	GPLv3+
Group:	Sound
Url:		http://www.darkice.org/
# The devel tree really is here: https://github.com/rafael2k/darkice, but it contains much more
# than darkice only.
Source0:	https://github.com/rafael2k/darkice/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	make
BuildRequires:	slibtool
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(fdk-aac)
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
%license %{name}/trunk/COPYING
%doc %{name}/trunk/AUTHORS %{name}/trunk/ChangeLog %{name}/trunk/FAQ
%doc %{name}/trunk/README %{name}/trunk/TODO
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.cfg.5*

#----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
pushd %{name}/trunk
	./autogen.sh
	%configure \
		--with-fdkaac \
		--with-flac \
	    --with-lame \
	    --with-opus \
	    --with-twolame \
	    --with-vorbis

	%make_build
popd


%install
pushd %{name}/trunk
	%make_install
popd
