#
# Conditional build:
%bcond_with	tests	# perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Exception
%define		pnam	Class-DBI
Summary:	Exception::Class::DBI - DBI exception objects
Summary(pl):	Exception::Class::DBI - obiekty wyj±tków DBI
Name:		perl-Exception-Class-DBI
Version:	0.91
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4bc75e487b141180961feb12d41bc9d6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Module-Build >= 0.20
%if %{with tests}
BuildRequires:	perl-DBI >= 1.28
BuildRequires:	perl-Exception-Class >= 1.02
BuildRequires:	perl-Test-Simple >= 0.40
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module offers a set of DBI-specific exception classes. They
inherit from Exception::Class::Base, the base class for all exception
objects created by the Exception::Class module from the CPAN.
Exception::Class::DBI itself offers a single class method, handler(),
that returns a code reference appropriate for passing the DBI
HandleError attribute.

%description -l pl
Ten modu³ oferuje zestaw specyficznych dla DBI klas wyj±tków.
Dziedzicz± one z Exception::Class::Base, czyli bazowej klasy dla
wszystkich obiektów wyj±tków tworzonych przez modu³ Exception::Class.
Sam Exception::Class::DBI oferuje pojedyncz± metodê klasy - handler(),
zwracaj±c± referencjê do kodu w³a¶ciw± do przekazywania atrybutu DBI
HandleError.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%{__perl} -pi -e 's/^(use 5.005)(00;)$/$1_$2/' ./lib/Exception/Class/DBI.pm

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorlib}/Exception/Class
%{perl_vendorlib}/Exception/Class/*.pm
%{_mandir}/man3/*
