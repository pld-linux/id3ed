Summary:	id3ed - edit id3 description tags in mpeg3 files
Name:		id3ed
Version:	1.10.2
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	http://www.azstarnet.com/~donut/programs/id3ed/%{name}-%{version}.tar.gz
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-config_h-fix.patch
Patch2:		%{name}-DESTDIR.patch
URL:		http://www.azstarnet.com/~donut/programs/id3ed.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
id3ed edits the "id3" tag for mpeg layer3 files. The mpeg3
specification does not provide any method for storing song
information, however the id3 tag has become a standard method for
doing this, and most mp3 players can read the tag. It will not cause
any errors in players that do not support it. The tag is 128 bytes
long and is located at the end of the file.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
CXXFLAGS="%{!?debug:$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates}%{?debug:-O0 -g}"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	Changelog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
