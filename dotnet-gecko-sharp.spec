Summary:	Gecko# - A Gtk# Mozilla binding
Summary(pl):	Gecko# - wi�zanie Gtk# dla Mozilli
Name:		dotnet-gecko-sharp
Version:	0.6
Release:	1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://www.go-mono.com/archive/1.0.3/gecko-sharp-%{version}.tar.gz
# Source0-md5:	9ce9bb08125f7c7eecf8bd696a3345bd
Patch0:		%{name}-mint.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp-devel >= 0.98
BuildRequires:	mono-csharp >= 0.96
BuildRequires:	pkgconfig
BuildConflicts:	gecko-sharp < 0.2
Requires:	mozilla-embedded
Requires:	dotnet-gtk-sharp >= 0.98
Provides:	dotnet-gecko
Provides:	gecko-sharp = %{version}
Obsoletes:	dotnet-gecko
Obsoletes:	gecko-sharp
ExcludeArch:	alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gecko# - A Gtk# Mozilla binding.

%description -l pl
Gecko# - wi�zanie Gtk# dla Mozilli.

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
