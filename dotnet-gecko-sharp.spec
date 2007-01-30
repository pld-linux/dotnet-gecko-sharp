%include	/usr/lib/rpm/macros.mono
Summary:	Gecko# - A Gtk# Mozilla binding
Summary(pl):	Gecko# - wi±zanie Gtk# dla Mozilli
Name:		dotnet-gecko-sharp
Version:	0.6
Release:	7
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://www.go-mono.com/archive/1.0.6/gecko-sharp-%{version}.tar.gz
# Source0-md5:	9ce9bb08125f7c7eecf8bd696a3345bd
Patch0:		%{name}-mint.patch
Patch1:		%{name}-monodir.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
# just gtk-sharp
BuildRequires:	dotnet-gtk-sharp-devel >= 0.98
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	mono-csharp >= 1.1.7
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildConflicts:	gecko-sharp < 0.2
Requires:	mono >= 1.1.7
Requires:	dotnet-gtk-sharp >= 0.98
ExcludeArch:	i386 alpha sparc sparc64
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

%description devel
Gecko# development files.

%description devel -l pl
Pliki programistyczne Gecko#.

%prep
%setup -q -n gecko-sharp-%{version}
%patch0 -p1
%patch1 -p1

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
%{_prefix}/lib/mono/gac/gecko-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gecko-sharp
%{_pkgconfigdir}/gecko-sharp.pc
