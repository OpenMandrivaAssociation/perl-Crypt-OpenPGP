%define	upstream_name	 Crypt-OpenPGP
%define upstream_version 1.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Pure-Perl OpenPGP implementation
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(Crypt::Blowfish)
BuildRequires: perl(Crypt::CAST5_PP)
BuildRequires: perl(Crypt::DES_EDE3)
BuildRequires: perl(Crypt::DSA)
BuildRequires: perl(Crypt::IDEA)
BuildRequires: perl(Crypt::Rijndael)
BuildRequires: perl(Crypt::RIPEMD160)
BuildRequires: perl(Crypt::RSA)
BuildRequires: perl(Crypt::Twofish) >= 2.00
BuildRequires: perl(Data::Buffer) >= 0.04
BuildRequires: perl(File::HomeDir)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(Math::Pari)
BuildRequires: perl(MIME::Base64) >= 3.07
BuildRequires: perl(URI::Escape)

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Crypt::OpenPGP is a pure-Perl implementation of the OpenPGP stan- dard[1]. In
addition to support for the standard itself, Crypt::OpenPGP claims
compatibility with many other PGP implementations, both those that support the
standard and those that preceded it.

Crypt::OpenPGP provides signing/verification, encryption/decryption, keyring
management, and key-pair generation; in short it should provide you with
everything you need to PGP-enable yourself. Alternatively it can be used as
part of a larger system; for example, perhaps you have a web-form-to-email
generator written in Perl, and you'd like to encrypt outgoing messages, because
they contain sensitive information.  Crypt::OpenPGP can be plugged into such a
scenario, given your public key, and told to encrypt all messages; they will
then be readable only by you.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm -f t/07-digest.t

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# this test works under iurt as user, but not under build system
rm -f t/07-digest.t
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Crypt/*
%{_mandir}/*/*
