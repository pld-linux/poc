Summary:	poc is a mp3 and ogg streamer
Name:		poc
Version:	0.3.7
Release:	0.1
License:	GPL
Group:		Applications/Sound
Source0:	http://www.bl0rg.net/software/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	948f337697160d6f510e2320db211031
URL:		http://www.bl0rg.net/software/poc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
poc is a mp3 and ogg streamer supporting following protocols:
    - HTTP (mp3 and ogg)
    - RTP (RFC 2250) (mp3 only)
    - RTP (RFC 3119) (mp3 only)
    - homegrown FEC protocol (mp3 only) It should work under any POSIX
      platform, and does not require any additional library. You need a C99
      compiler though. poc is still beta software, ipv6 and ogg support was
      not tested extensively. poc includes mp3cue, a mp3 CUE cutter.

%prep
%setup -q

%build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}/%{name}
cp {mp3cue,pob-2250,pob-2250-rb,pob-3119,pob-3119-rb,pob-fec,poc-2250,poc-2250-ploss,poc-3119,poc-3119-ploss,poc-fec,poc-fec-ploss,poc-http,pogg-http,radio.sh} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.mp3cue TODO
%attr(755,root,root) %{_bindir}/%{name}/*
