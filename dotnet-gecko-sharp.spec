Summary:	Gecko# - A Gtk# Mozilla binding
Summary(pl):	Gecko# - wi±zanie Gtk# dla Mozilli
Name:		dotnet-gecko-sharp
Version:	0.5
Release:	2
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://www.go-mono.com/archive/1.0/gecko-sharp-%{version}.tar.gz
# Source0-md5:	71e75186b2ee5c644d5dd1560ce27357
Patch0:		%{name}-mint.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp-devel >= 0.98
BuildRequires:	mono-devel >= 0.96
BuildRequires:	mono-csharp >= 0.96
BuildRequires:	pkgconfig
BuildConflicts:	gecko-sharp < 0.2
Requires:	mozilla-embedded
Requires:	dotnet-gtk-sharp >= 0.98
Provides:	dotnet-gecko
Provides:	gecko-sharp = %{version}
Obsoletes:	dotnet-gecko
Obsoletes:	gecko-sharp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gecko# - A Gtk# Mozilla binding.

%description -l pl
Gecko# - wi±zanie Gtk# dla Mozilli.

%package devel
Summary:	Gecko# development files
Summary(pl):	Pliki programistyczne Gecko#
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	mozilla-embedded-devel
Provides:	dotnet-gecko-devel
Provides:	gecko-sharp-devel
Obsoletes:	dotnet-gecko-devel
Obsoletes:	gecko-sharp-devel

%description devel
Gecko# development files.

%description devel -l pl
Pliki programistyczne Gecko#.

%prep
%setup -q -n gecko-sharp-%{version}
%patch0 -p1

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
%{_libdir}/gecko-sharp
%{_libdir}/mono/gac/gecko-sharp

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*
%{_libdir}/mono/gecko-sharp
