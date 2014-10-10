%define upstream_name    DBIx-Class-InflateColumn-FS
%define upstream_version 0.01007

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	FS columns resultset class
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBICx::TestDatabase)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::UUIDColumns)
BuildRequires:	perl-DBIx-Class-UUIDColumns >= 0.20.50-4
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(SQL::Abstract)
BuildArch:	noarch

%description
Provides inflation to a Path::Class::File object allowing file system
storage of BLOBS.

The storage path is specified with 'fs_column_path'. Each file receives a
unique name, so the storage for all FS columns can share the same path.

Within the path specified by 'fs_column_path', files are stored in
sub-directories based on the first 2 characters of the unique file names.
Up to 256 sub-directories will be created, as needed. Override
'_fs_column_dirs' in a derived class to change this behavior.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.10.70-4mdv2011.0
+ Revision: 654286
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.10.70-3mdv2011.0
+ Revision: 625074
- Add a dep on the fixed UUIDColumns
- Add dep on SQL::A
- import perl-DBIx-Class-InflateColumn-FS

