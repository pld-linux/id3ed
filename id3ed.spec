Summary:	id3ed - edit id3 description tags in mp3 files
Summary(pl):	Edytor opis�w plik�w mp3
Name:		id3ed
Version:	1.10.3
Release:	1
License:	GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D�wi�k
Source0:	http://www.azstarnet.com/~donut/programs/id3ed/%{name}-%{version}.tar.gz
Patch0:		%{name}-ncurses.patch
Patch1:		%{name}-DESTDIR.patch
URL:		http://www.azstarnet.com/~donut/programs/id3ed.html
BuildRequires:	autoconf
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
id3ed edits the "id3" tag for mpeg layer3 files. The mp3 specification
does not provide any method for storing song information, however the
id3 tag has become a standard method for doing this, and most mp3
players can read the tag. It will not cause any errors in players that
do not support it. The tag is 128 bytes long and is located at the end
of the file.

%description -l pl
id3ed umo�liwia edycj� znacznik�w "id3" umieszczanych w plikach mpeg
warstwy 3 (mp3). Znaczniki id3 sta�y si� standardem jesli chodzi o
umieszczanie informacji o piosence w plikach mp3 i wiekszo��
odtwarzaczy potrafi je odczyta�. Jednocze�nie ich obecno�� nie
powoduje �adnych problem�w w odtwarzaczach nie obs�uguj�cych tych
znacznik�w. Znacznik "id3" zajmuje 128 bajt�w i jest zlokalizowany na
ko�cu pliku d�wi�kowego.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
CXX="%{__cc}"; export CXX
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changelog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
