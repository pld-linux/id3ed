Summary:	id3ed - edit id3 description tags in MP3 files
Summary(pl.UTF-8):   Edytor opisów plików MP3
Name:		id3ed
Version:	1.10.4
Release:	3
License:	GPL
Group:		Applications/Sound
Source0:	http://www.azstarnet.com/~donut/programs/id3ed/%{name}-%{version}.tar.gz
# Source0-md5:	fc0df31ef4ad90b83ee133929afbcc83
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://www.azstarnet.com/~donut/programs/id3ed.html
BuildRequires:	autoconf
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
id3ed edits the "id3" tag for mpeg layer3 files. The MP3 specification
does not provide any method for storing song information, however the
id3 tag has become a standard method for doing this, and most MP3
players can read the tag. It will not cause any errors in players that
do not support it. The tag is 128 bytes long and is located at the end
of the file.

%description -l pl.UTF-8
id3ed umożliwia edycję znaczników "id3" umieszczanych w plikach mpeg
warstwy 3 (MP3). Znaczniki id3 stały się standardem jeśli chodzi o 
umieszczanie informacji o piosence w plikach MP3 i większość odtwarzaczy 
potrafi je odczytać. Jednocześnie ich obecność nie powoduje żadnych 
problemów w odtwarzaczach nie obsługujących tych znaczników. Znacznik 
"id3" zajmuje 128 bajtów i jest zlokalizowany na końcu pliku dźwiękowego.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure
%{__make} \
	CPPFLAGS="-I."

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
