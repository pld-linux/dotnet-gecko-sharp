Summary:	gecko-sharp
Summary(pl):	gecko-sharp
Name:		gecko-sharp
Version:	0.1
Release:	0.1
Epoch:		0
License:	GPL
Group:		Libraries
Source0:	http://www.go-mono.com/archive/%{name}-%{version}.tar.gz
URL:		http://www.go-mono.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mono
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gecko-sharp.

%description -l pl
gecko-sharp.

%package devel
Summary:	gecko-sharp devel
Summary(pl):	gecko-sharp devel
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
gecko-sharp devel.

%description devel -l pl
gecko-sharp devel.

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
