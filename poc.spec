Summary:	poc - a MP3 and Ogg streamer
Summary(pl):	poc - program do generowania strumieni MP3 i Ogg
Name:		poc
Version:	0.3.7.1
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.bl0rg.net/software/poc/%{name}-%{version}.tar.gz
# Source0-md5:	d96ed857d3a9e075210653c434d655d1
# Source0-size:	102983
URL:		http://www.bl0rg.net/software/poc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	gettext-devel
BuildRequires:	libtool
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

%description -l pl
poc to program do generowania strumieni MP3 i Ogg obs³uguj±cy
nastêpuj±ce protoko³y:
 - HTTP (MP3 i Ogg)
 - RTP (RFC 2250) (tylko MP3)
 - RTP (RFC 3119) (tylko MP3)
 - w³asny protokó³ FEC (tylko MP3)

Program powinien dzia³aæ na dowolnej platformie zgodnej z POSIX i nie
wymaga ¿adnej dodatkowej biblioteki. Do zbudowania potrzebny jest
kompilator zgodny z C99. poc jest nadal w stadium beta, a IPv6 i Ogg
nie by³y zbyt intensywnie testowane. poc zawiera mp3cue - program do
wycinania CUE z MP3.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install {mp3cue,pob-2250,pob-2250-rb,pob-3119,pob-3119-rb,pob-fec,poc-2250,poc-2250-ploss,poc-3119,poc-3119-ploss,poc-fec,poc-fec-ploss,poc-http,pogg-http,radio.sh} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.mp3cue TODO
%attr(755,root,root) %{_bindir}/*
