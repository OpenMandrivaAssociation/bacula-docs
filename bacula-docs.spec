%define blurb Bacula - It comes by night and sucks the vital essence from your computers.

Summary:	Bacula Documentation
Name:		bacula-docs
Version:	5.0.2
Release:	3
Epoch:		1
Group:		Books/Other
License:	GPL
URL:		http://www.bacula.org/
Source0:	http://prdownloads.sourceforge.net/bacula/%{name}-%{version}.tar.bz2
Source1:	http://prdownloads.sourceforge.net/bacula/%{name}-%{version}.tar.bz2.sig
BuildRequires:  ghostscript-dvipdf
BuildRequires:  tetex-latex
BuildRequires:  latex2html
BuildRequires:  tetex-dvipdfm
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%bcond_with	fr
%bcond_with	de
%bcond_with	es

%description
%{blurb}
Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.

This package contains the documentation for Bacula.

%package -n	bacula-doc-en
Summary:	Bacula English Documentation in the HTML and PDF format
Group:		Books/Other

%description -n	bacula-doc-en
%{blurb}
Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computercontains
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.

This package contains the English manual.

%if %with de
%package -n	bacula-doc-de
Summary:	Bacula Deutsch Documentation in the HTML and PDF format
Group:		Books/Other

%description -n	bacula-doc-de
%{blurb}
Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.

This package contains the German manual.
%endif

%if %with fr
%package -n	bacula-doc-fr
Summary:	Bacula French Documentation in the HTML and PDF format
Group:		Books/Other

%description -n	bacula-doc-fr
%{blurb}
Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.

This Package contains the french manual.
%endif

%if %with es
%package -n	bacula-doc-es
Summary:	Bacula Spanish Documentation in the HTML and PDF format
Group:		Books/Other

%description -n	bacula-doc-es
%{blurb}
Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.

This package contains the Spanish manual.
%endif

%package -n	bacula-doc-web
Summary:	Bacula-web Documentation in the HTML and PDF format
Group:		Books/Other

%description -n	bacula-doc-web
%{blurb}
Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.

This package ontains the bacula-web documentation

%prep

%setup -q
mkdir src
cat > src/version.h <<EOF
#define VERSION "%{version}"
#define BDATE   "24 February 2010"
#define LSMDATE "24Feb10
EOF

# create dvipdf wrapper to workaround default secure mode
# not including images
mkdir bin
cat > bin/dvipdf <<EOF
#!/bin/sh
exec /usr/bin/dvipdf -R0 "\$@"
EOF
chmod +x bin/dvipdf

%build
%configure2_5x \
    --with-bacula=$PWD

export PATH=$PWD/bin:$PATH
make
make -C bacula-web

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_defaultdocdir}/bacula-%{version}/bacula-web
cp bacula-web/bacula-web.pdf %{buildroot}%{_defaultdocdir}/bacula-%{version}
cp bacula-web/bacula-web/*.{html,css,png} %{buildroot}%{_defaultdocdir}/bacula-%{version}/bacula-web
cd manuals
for i in {de,en,es,fr}/*; do
	lang=${i%%/*}
	module=${i##*/}
	if [ -s $i/$module.pdf ]; then
		mkdir -p %{buildroot}%{_defaultdocdir}/bacula-%{version}/manual-$lang
		cp $i/$module.pdf %{buildroot}%{_defaultdocdir}/bacula-%{version}/manual-$lang
	fi
	if [ -d $i/$module ]; then
		mkdir -p %{buildroot}%{_defaultdocdir}/bacula-%{version}/manual-$lang/$module
		cp $i/$module/*.{html,css,png} %{buildroot}%{_defaultdocdir}/bacula-%{version}/manual-$lang/$module
	fi
done
%clean
rm -rf %{buildroot}

%files -n bacula-doc-web
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/bacula-web
%{_defaultdocdir}/bacula-%{version}/bacula-web.pdf

%if %with %fr
%files -n bacula-doc-fr
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/manual-fr
%endif

%if %with %fr
%files -n bacula-doc-de
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/manual-de
%endif

%files -n bacula-doc-en
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/manual-en

%if %with %fr
%files -n bacula-doc-es
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/manual-es
%endif


%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1:5.0.2-2mdv2011.0
+ Revision: 610025
- rebuild

* Mon Jun 14 2010 Luca Berra <bluca@mandriva.org> 1:5.0.2-1mdv2010.1
+ Revision: 548043
- New version 5.0.2

* Thu Mar 11 2010 Luca Berra <bluca@mandriva.org> 1:5.0.1-1mdv2010.1
+ Revision: 517927
- New version 5.0.1
- build pdf manuals (with a workaround for dvipdf secure mode)
- do not build french, german and spanish since they are not really there yet

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1:2.4.3-2mdv2010.0
+ Revision: 436765
- rebuild

* Mon Oct 13 2008 Oden Eriksson <oeriksson@mandriva.com> 1:2.4.3-1mdv2009.1
+ Revision: 293185
- 2.4.3

* Sun Jul 27 2008 Oden Eriksson <oeriksson@mandriva.com> 1:2.4.2-1mdv2009.0
+ Revision: 250683
- 2.4.2

* Thu Jul 10 2008 Oden Eriksson <oeriksson@mandriva.com> 1:2.4.1-1mdv2009.0
+ Revision: 233357
- 2.4.1

* Sun Jun 08 2008 Oden Eriksson <oeriksson@mandriva.com> 1:2.4.0-1mdv2009.0
+ Revision: 216853
- 2.4.0

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Fri May 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1:2.2.8-1mdv2009.0
+ Revision: 208103
- 2.2.8
- rediffed P0
- fix rpm group

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 1:1.38.11-3mdv2008.1
+ Revision: 135828
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix URL


* Fri Dec 22 2006 Oden Eriksson <oeriksson@mandriva.com> 1.38.11-3mdv2007.0
+ Revision: 101483
- Import bacula-docs

* Sat Jul 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.38.11-3mdv2007.0
- 1.38.11 (broken out from bacula)

