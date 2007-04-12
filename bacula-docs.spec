# compatability macros
%{?!mkrel:%define mkrel(c:) %{-c:0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*)(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

%{?!_with_unstable: %{error:%(echo -e "\n\n\nYou are building package for a stable release, please see \nhttp://qa.mandrakesoft.com/twiki/bin/view/Main/DistroSpecificReleaseTag\nif you think this is incorrect\n\n\n ")}%(sleep 2)}


%define blurb Bacula - It comes by night and sucks the vital essence from your computers.

# fixes passwords in configuration files
# removing "SubSys Directory" is needed if upgrading from 1.30a or lower
%define post_fix_config() umask 0037; if [ -s %{_sysconfdir}/%{name}/.pw.sed ]; then for i in %{_sysconfdir}/%{name}/%{1}.conf %{_sysconfdir}/%{name}/%{1}.conf.rpmnew; do if [ -s $i ]; then sed -f %{_sysconfdir}/%{name}/.pw.sed $i > $i.tmp; sed -e '/SubSys[[:space:]]*Directory/I d' $i.tmp > $i; rm -f $i.tmp; fi; done; fi;

Summary:	Bacula Documentation
Name:		bacula-docs
Version:	1.38.11
Release:	%mkrel 3
Epoch:		1
Group:		Archiving/Backup
License:	GPL
URL:		http://www.bacula.org/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		bacula-docs-1.38.11-languages_fix.diff
BuildRequires:  ghostscript-dvipdf
BuildRequires:  tetex-latex
BuildRequires:  latex2html
BuildRequires:  tetex-dvipdfm
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

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
Summary:	Bacula English Documentation
Group:		Archiving/Backup

%description -n	bacula-doc-en
%{blurb}
Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computercontains
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.

Contains the english manual.

%package -n	bacula-doc-de
Summary:	Bacula Deutsch Documentation
Group:		Archiving/Backup

%description -n	bacula-doc-de
%{blurb}
Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.

Contains the deutsch manual.

%package -n	bacula-doc-fr
Summary:	Bacula French Documentation
Group:		Archiving/Backup

%description -n	bacula-doc-fr
%{blurb}
Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.

Contains the french manual.

%package -n	bacula-doc-web
Summary:	Bacula Web Documentation
Group:		Archiving/Backup

%description -n	bacula-doc-web
%{blurb}
Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.

Contains the bacula-web documentation

%package -n	bacula-doc-dev
Summary:	Bacula Developer Documentation
Group:		Archiving/Backup

%description -n	bacula-doc-dev
%{blurb}
Bacula is a set of computer programs that permit you (or the system
administrator) to manage backup, recovery, and verification of computer
data across a network of computers of different kinds. In technical terms,
it is a network client/server based backup program. Bacula is relatively
easy to use and efficient, while offering many advanced storage management
features that make it easy to find and recover lost or damaged files.

Contains the developer documentation

%prep

%setup -q
%patch0 -p0 -b .makedoc

mkdir src
cat > src/version.h << EOF
#undef  VERSION
#define VERSION "%{version}"
#define BDATE   "28 June 2006"
#define LSMDATE "28Jun06"
EOF

%build

%configure2_5x \
    --with-bacula=.
cp manual/bacula/imagename_translations manual-fr/imagename_translations
cp manual/bacula/imagename_translations manual-de/imagename_translations
%make 

%install
rm -rf %{buildroot}

%makeinstall
# sysconfdir=%{buildroot}%{_sysconfdir}/%{name} scriptdir=%{buildroot}%{_libexecdir}/%{name} working_dir=%{buildroot}%{_localstatedir}/%{name}


install -d -m 0755 %{buildroot}/%_defaultdocdir/bacula-%{version}/developers
cp developers/*.{pdf,html,png} %{buildroot}/%_defaultdocdir/bacula-%{version}/developers/

# bacula-web doc install 
install -d -m 0755 %{buildroot}/%_defaultdocdir/bacula-%{version}/bacula-web
cp bacula-web/*.{pdf,html,png} %{buildroot}/%_defaultdocdir/bacula-%{version}/bacula-web/

# manual-fr doc install 
install -d -m 0755 %{buildroot}/%_defaultdocdir/bacula-%{version}/manual-fr
cp manual-fr/*.{pdf,html,png} %{buildroot}/%_defaultdocdir/bacula-%{version}/manual-fr/

# manual-de doc install 
install -d -m 0755 %{buildroot}/%_defaultdocdir/bacula-%{version}/manual-de
cp manual-de/*.{pdf,html,png} %{buildroot}/%_defaultdocdir/bacula-%{version}/manual-de/

# manual doc install 
install -d -m 0755 %{buildroot}/%_defaultdocdir/bacula-%{version}/manual-en
cp manual/*.{pdf,html,png} %{buildroot}/%_defaultdocdir/bacula-%{version}/manual-en/

%clean
rm -rf %{buildroot}

%files -n bacula-doc-web
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/bacula-web/*.png
%{_defaultdocdir}/bacula-%{version}/bacula-web/*.html
%{_defaultdocdir}/bacula-%{version}/bacula-web/*.pdf

%files -n bacula-doc-dev
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/developers/*.png
%{_defaultdocdir}/bacula-%{version}/developers/*.html
%{_defaultdocdir}/bacula-%{version}/developers/*.pdf

%files -n bacula-doc-fr
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/manual-fr/*.png
%{_defaultdocdir}/bacula-%{version}/manual-fr/*.html
%{_defaultdocdir}/bacula-%{version}/manual-fr/*.pdf

%files -n bacula-doc-de
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/manual-de/*.png
%{_defaultdocdir}/bacula-%{version}/manual-de/*.html
%{_defaultdocdir}/bacula-%{version}/manual-de/*.pdf

%files -n bacula-doc-en
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/manual-en/*.png
%{_defaultdocdir}/bacula-%{version}/manual-en/*.html
%{_defaultdocdir}/bacula-%{version}/manual-en/*.pdf


