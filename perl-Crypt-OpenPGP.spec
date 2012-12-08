%define	upstream_name	 Crypt-OpenPGP
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Pure-Perl OpenPGP implementation
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz
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

BuildRequires:	perl-devel
BuildArch:	noarch

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
#make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Crypt/*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.60.0-3mdv2012.0
+ Revision: 765528
- fix deps
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.60.0-1
+ Revision: 676768
- 1.06
- rebuild
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Jérôme Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.1
+ Revision: 477636
- adding missing buildrequires:
- update to 1.04

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2010.0
+ Revision: 408950
- rebuild using %%perl_convert_version

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.03-1mdv2009.0
+ Revision: 136699
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jun 26 2007 Buchan Milne <bgmilne@mandriva.org> 1.03-1mdv2008.0
+ Revision: 44555
- Drop test 7 (which doesnt work under the build system)
- Buildrequire Crypt::Blowfish
- Import perl-Crypt-OpenPGP



* Thu Jun 21 2007 Buchan Milne <bgmilne@mandriva.org> 1.03-1mdv2007.1
- initial package
