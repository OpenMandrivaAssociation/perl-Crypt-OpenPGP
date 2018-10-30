%define	modname	Crypt-OpenPGP
%define modver 1.08

Summary:	Pure-Perl OpenPGP implementation
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Crypt/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Compress::Zlib)
BuildRequires:	perl(Crypt::Blowfish)
BuildRequires:	perl(Crypt::CAST5_PP)
BuildRequires:	perl(Crypt::DES_EDE3)
BuildRequires:	perl(Crypt::DSA)
BuildRequires:	perl(Crypt::IDEA)
BuildRequires:	perl(Crypt::Rijndael)
BuildRequires:	perl(Crypt::RIPEMD160)
BuildRequires:	perl(Crypt::RSA)
BuildRequires:	perl(Crypt::Twofish) >= 2.00
BuildRequires:	perl(Data::Buffer) >= 0.04
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Math::Pari)
BuildRequires:	perl(MIME::Base64) >= 3.07
BuildRequires:	perl(URI::Escape)
BuildRequires:	perl(Data::Random)

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
%setup -qn %{modname}-%{modver}
rm -f t/07-digest.t

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
rm -f t/07-digest.t
#make test

%install
%makeinstall_std

%files
%doc README
%{_bindir}/*
%{perl_vendorlib}/Crypt/*
%{_mandir}/man3/*
