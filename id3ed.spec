%define	name	id3ed
%define	version	1.3
%define	release	2mdk

Summary:	id3ed - edit id3 description tags in mpeg3 files.
Name:		%{name}
Version:	%{version}
Release:	%{release}
Copyright:	GPL
Group:		Sound
URL:		http://www.azstarnet.com/~donut/programs.html
Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}-%{version}-extern_rl.patch.bz2
Patch1:		%{name}-%{version}-makefile.patch.bz2
Packager:	Ryan Weaver <ryanw@infohwy.com>
BuildRoot:	/var/tmp/%{name}-buildroot

%description
id3ed edits the "id3" tag for mpeg layer3 files. The mpeg3
specification does not provide any method for storing song
information, however the id3 tag has become a standard method
for doing this, and most mp3 players can read the tag. It will
not cause any errors in players that do not support it.
The tag is 128 bytes long and is located at the end of the file.

%prep

%setup -q -n %{name}
%patch -p1
%patch1 -p1

%build
CFLAGS=$RPM_OPT_FLAGS
make

%install
if [ -e $RPM_BUILD_ROOT ]; then rm -rf $RPM_BUILD_ROOT; fi

install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/man/man1

install -s -m 755 id3ed $RPM_BUILD_ROOT/usr/bin
install -m 755 id3ed.1 $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING Changelog README
/usr/bin/*
/usr/man/man1/*

%changelog
* Fri Apr 28 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.3-2mdk
- fix group
- fix files section

* Thu Feb 24 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build

* Fri Mar 26 1999 Ryan Weaver <ryanw@infohwy.com>
  [id3ed-1.3-1]
- Initial RPM Build.
- 03/23/1999 - 1.3
- Removed a debug printf that sneaked into the release.
- Added -l to show known genres.
- Added support to set genre by name as well as number.

- 03/22/1999 - 1.2
- Added -SNAYCG selection of which tags you want to edit.
- Added optional use of readline library for input.
  (Tested with Readline 4.0)  Comment the appropriate
  lines in the Makefile if you don't want it.

- 12/03/1998 - 1.1
- Added command line default value patch from Peter Karlsson <pk@abc.se>
- Added -q(uiet) command line param.

- 02/24/1998 - 1.0 - initial release
