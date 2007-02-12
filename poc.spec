Summary:	poc - a MP3 and Ogg streamer
Summary(pl.UTF-8):   poc - program do generowania strumieni MP3 i Ogg
Name:		poc
Version:	0.4.1
Release:	1
License:	distributable
Group:		Applications/Sound
Source0:	http://www.bl0rg.net/software/poc/%{name}-%{version}.tar.gz
# Source0-md5:	f62f0fb5ed54796c5d60c11e92bae544
Patch0:		%{name}-radio_script.patch
URL:		http://www.bl0rg.net/software/poc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	libtool
Requires:	buffer
Requires:	nc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
poc is a MP3 and Ogg streamer supporting following protocols:
 - HTTP (MP3 and Ogg)
 - RTP (RFC 2250) (MP3 only)
 - RTP (RFC 3119) (MP3 only)
 - homegrown FEC protocol (MP3 only)

It should work under any POSIX platform, and does not require any
additional library. You need a C99 compiler though. poc is still beta
software, IPv6 and Ogg support was not tested extensively. poc
includes mp3cue, a MP3 CUE cutter.

%description -l pl.UTF-8
poc to program do generowania strumieni MP3 i Ogg obsługujący
następujące protokoły:
 - HTTP (MP3 i Ogg)
 - RTP (RFC 2250) (tylko MP3)
 - RTP (RFC 3119) (tylko MP3)
 - własny protokół FEC (tylko MP3)

Program powinien działać na dowolnej platformie zgodnej z POSIX i nie
wymaga żadnej dodatkowej biblioteki. Do zbudowania potrzebny jest
kompilator zgodny z C99. poc jest nadal w stadium beta, a IPv6 i Ogg
nie były zbyt intensywnie testowane. poc zawiera mp3cue - program do
wycinania CUE z MP3.

%prep
%setup -q
%patch0 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install mp3cue mp3cut mp3length pob-2250 pob-3119 pob-fec poc-2250 \
        poc-2250-ploss poc-3119 poc-3119-ploss poc-fec poc-fec-ploss \
	poc-http pogg-http radio.sh $RPM_BUILD_ROOT%{_bindir}
install man/man1/* $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
