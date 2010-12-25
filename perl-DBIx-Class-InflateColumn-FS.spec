%define upstream_name    DBIx-Class-InflateColumn-FS
%define upstream_version 0.01007

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    FS columns resultset class
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBD::SQLite)
BuildRequires: perl(DBICx::TestDatabase)
BuildRequires: perl(DBIx::Class)
BuildRequires: perl(DBIx::Class::UUIDColumns)
BuildRequires: perl-DBIx-Class-UUIDColumns >= 0.20.50-4
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find)
BuildRequires: perl(Path::Class)
BuildRequires: perl(SQL::Abstract)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


