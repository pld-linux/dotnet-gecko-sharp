Summary:	Gecko# - A Gtk# Mozilla binding
Summary(pl):	Gecko# - wi±zanie Gtk# dla Mozilli
Name:		dotnet-gecko-sharp
Version:	0.5
Release:	1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://www.go-mono.com/archive/beta3/gecko-sharp-%{version}.tar.gz
# Source0-md5:	71e75186b2ee5c644d5dd1560ce27357
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mono
BuildConflicts:	gecko-sharp < 0.2
Provides:	gecko-sharp = %{version}
Obsoletes:	gecko-sharp
Provides:	dotnet-gecko
Obsoletes:	dotnet-gecko
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gecko# - A Gtk# Mozilla binding.

%description -l pl
Gecko# - wi±zanie Gtk# dla Mozilli.

%package devel
Summary:	Gecko# development files
Summary(pl):	Pliki programistyczne Gecko#
Group:		Development/Libraries
Provides:	gecko-sharp-devel
Obsoletes:	gecko-sharp-devel
Provides:	dotnet-gecko-devel
Obsoletes:	dotnet-gecko-devel
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Gecko# development files.

%description devel -l pl
Pliki programistyczne Gecko#.

%prep
%setup -q -n gecko-sharp-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root)%{_bindir}/webshot
%{_libdir}/gecko-sharp/WebThumbnailer.exe
%{_libdir}/mono/gac/gecko-sharp

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*
%{_libdir}/mono/gecko-sharp/gecko-sharp.dll
