Summary:	Gecko# - A Gtk# Mozilla binding
Summary(pl):	Gecko# - wi±zanie Gtk# dla Mozilli
Name:		gecko-sharp
Version:	0.1
Release:	0.1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://www.go-mono.com/archive/%{name}-%{version}.tar.gz
# Source0-md5:	f6994a76d090bc6e7a484f5af42a6745
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mono
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
%setup -q

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
%{_libdir}/gecko-sharp.dll

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/*
