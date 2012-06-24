#
# Conditional build:
# _with_tests - perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	Exception
%define	pnam	Class-DBI
Summary:	Exception::Class::DBI - DBI Exception objects
#Summary(pl):	
Name:		perl-Exception-Class-DBI
Version:	0.01
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_with_tests:1}%{!?_with_tests:0}
BuildRequires:	perl-DBI >= 1.28
BuildRequires:	perl-Exception-Class >= 1.02
BuildRequires:	perl-Test-Simple >= 0.40
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module offers a set of DBI-specific exception classes.  They inherit from
Exception::Class::Base, the base class for all exception objects created by the
Exception::Class module from the CPAN.  Exception::Class::DBI itself offers a
single class method, handler(), that returns a code reference appropriate for
passing the DBI HandleError attribute.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/Exception/Class/*.pm
%{_mandir}/man3/*
