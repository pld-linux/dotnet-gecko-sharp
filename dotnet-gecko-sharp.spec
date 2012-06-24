%include	/usr/lib/rpm/macros.mono
Summary:	Gecko# - A Gtk# Mozilla binding
Summary(pl):	Gecko# - wi�zanie Gtk# dla Mozilli
Name:		dotnet-gecko-sharp
Version:	0.11
Release:	0.1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://go-mono.com/sources/gecko-sharp-2.0/gecko-sharp-2.0-%{version}.tar.gz
# Source0-md5:	7362d710b7fe6a8b5f68a614279147de
#Patch0:		%{name}-gtk-compat.patch
URL:		http://www.mono-project.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 1.9.3
BuildRequires:	mono-csharp >= 1.1.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildConflicts:	gecko-sharp < 0.2
Requires:	mozilla-embedded
Provides:	dotnet-gecko
Provides:	gecko-sharp = %{version}
Obsoletes:	dotnet-gecko
Obsoletes:	gecko-sharp
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
Provides:	dotnet-gecko-devel
Provides:	gecko-sharp-devel
Obsoletes:	dotnet-gecko-devel
Obsoletes:	gecko-sharp-devel

%description devel
Gecko# development files.

%description devel -l pl
Pliki programistyczne Gecko#.

%prep
%setup -q -n gecko-sharp-2.0-%{version}
#%patch0 -p1

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

if test -f $RPM_BUILD_ROOT%{_pkgconfigdir} ; then
  :
else
  install -d $RPM_BUILD_ROOT%{_pkgconfigdir}
  if [ "%{_pkgconfigdir}" != "/usr/lib/pkgconfig" ]; then
  	mv $RPM_BUILD_ROOT/usr/lib/pkgconfig/* $RPM_BUILD_ROOT%{_pkgconfigdir}
  fi
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
#%attr(755,root,root)%{_bindir}/webshot
#%{_libdir}/gecko-sharp
/usr/lib/mono/gac/gecko-sharp

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*
%{_libdir}/monodoc/sources/*
/usr/lib/mono/gecko-sharp-2.0
