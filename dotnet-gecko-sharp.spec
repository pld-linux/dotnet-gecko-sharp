Summary:	Gecko# - A Gtk# Mozilla binding
Summary(pl):	Gecko# - wi±zanie Gtk# dla Mozilli
Name:		dotnet-gecko-sharp
Version:	0.6
Release:	2
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://www.go-mono.com/archive/1.0.6/gecko-sharp-%{version}.tar.gz
# Source0-md5:	9ce9bb08125f7c7eecf8bd696a3345bd
Patch0:		%{name}-mint.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
# just gtk-sharp
BuildRequires:	dotnet-gtk-sharp-devel >= 0.98
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	mono-csharp >= 0.96
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
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

if ! pkg-config --exists mono; then
	sed -i -e 's/exec mono/exec mint/' $RPM_BUILD_ROOT%{_bindir}/webshot
fi

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
%{_libdir}/mono/gecko-sharp
%{_pkgconfigdir}/gecko-sharp.pc
