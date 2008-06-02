%define blurb Bacula - It comes by night and sucks the vital essence from your computers.

Summary:	Bacula Documentation
Name:		bacula-docs
Version:	2.2.8
Release:	%mkrel 1
Epoch:		1
Group:		Books/Other
License:	GPL
URL:		http://www.bacula.org/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		bacula-docs-languages_fix.diff
BuildRequires:  ghostscript-dvipdf
BuildRequires:  tetex-latex
BuildRequires:  latex2html
BuildRequires:  tetex-dvipdfm
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Summary:	Bacula English Documentation in the HTML format
Group:		Books/Other

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
Summary:	Bacula Deutsch Documentation in the HTML format
Group:		Books/Other

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
Summary:	Bacula French Documentation in the HTML format
Group:		Books/Other

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
Summary:	Bacula Web Documentation in the HTML format
Group:		Books/Other

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
Summary:	Bacula Developer Documentation in the HTML format
Group:		Books/Other

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
#define BDATE   "26 January 2008"
#define LSMDATE "26Jan08"
EOF
ln -s ../src manual/src

%build

%configure2_5x \
    --with-bacula=.
cp manual/bacula/imagename_translations manual-fr/imagename_translations
cp manual/bacula/imagename_translations manual-de/imagename_translations

make

%install
rm -rf %{buildroot}

%makeinstall
# sysconfdir=%{buildroot}%{_sysconfdir}/%{name} scriptdir=%{buildroot}%{_libexecdir}/%{name} working_dir=%{buildroot}%{_localstatedir}/lib/%{name}

install -d -m 0755 %{buildroot}/%{_defaultdocdir}/bacula-%{version}/developers
cp developers/*.{html,png} %{buildroot}/%{_defaultdocdir}/bacula-%{version}/developers/

# bacula-web doc install 
install -d -m 0755 %{buildroot}/%{_defaultdocdir}/bacula-%{version}/bacula-web
cp bacula-web/*.{html,png} %{buildroot}/%{_defaultdocdir}/bacula-%{version}/bacula-web/

# manual-fr doc install 
install -d -m 0755 %{buildroot}/%{_defaultdocdir}/bacula-%{version}/manual-fr
cp manual-fr/*.{html,png} %{buildroot}/%{_defaultdocdir}/bacula-%{version}/manual-fr/

# manual-de doc install 
install -d -m 0755 %{buildroot}/%{_defaultdocdir}/bacula-%{version}/manual-de
cp manual-de/*.{html,png} %{buildroot}/%{_defaultdocdir}/bacula-%{version}/manual-de/

# manual doc install 
install -d -m 0755 %{buildroot}/%{_defaultdocdir}/bacula-%{version}/manual-en
cp manual/*.{html,png} %{buildroot}/%{_defaultdocdir}/bacula-%{version}/manual-en/

%clean
rm -rf %{buildroot}

%files -n bacula-doc-web
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/bacula-web/*.png
%{_defaultdocdir}/bacula-%{version}/bacula-web/*.html

%files -n bacula-doc-dev
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/developers/*.png
%{_defaultdocdir}/bacula-%{version}/developers/*.html

%files -n bacula-doc-fr
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/manual-fr/*.png
%{_defaultdocdir}/bacula-%{version}/manual-fr/*.html

%files -n bacula-doc-de
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/manual-de/*.png
%{_defaultdocdir}/bacula-%{version}/manual-de/*.html

%files -n bacula-doc-en
%defattr(-, root, root)
%{_defaultdocdir}/bacula-%{version}/manual-en/*.png
%{_defaultdocdir}/bacula-%{version}/manual-en/*.html
