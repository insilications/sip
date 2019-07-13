#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sip
Version  : 4.19.13
Release  : 11
URL      : https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.13/sip-4.19.13.tar.gz
Source0  : https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.13/sip-4.19.13.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: sip-bin = %{version}-%{release}
Requires: sip-license = %{version}-%{release}
Requires: sip-python = %{version}-%{release}
Requires: sip-python3 = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : python3
BuildRequires : python3-dev
BuildRequires : qscintilla-dev
Patch1: 0001-Add-configure-to-generate-Makefile.patch

%description
SIP - C/C++ Bindings Generator for Python v2 and v3
===================================================

%package bin
Summary: bin components for the sip package.
Group: Binaries
Requires: sip-license = %{version}-%{release}

%description bin
bin components for the sip package.


%package dev
Summary: dev components for the sip package.
Group: Development
Requires: sip-bin = %{version}-%{release}
Provides: sip-devel = %{version}-%{release}

%description dev
dev components for the sip package.


%package license
Summary: license components for the sip package.
Group: Default

%description license
license components for the sip package.


%package python
Summary: python components for the sip package.
Group: Default
Requires: sip-python3 = %{version}-%{release}

%description python
python components for the sip package.


%package python3
Summary: python3 components for the sip package.
Group: Default
Requires: python3-core

%description python3
python3 components for the sip package.


%prep
%setup -q -n sip-4.19.13
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542081849
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1542081849
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sip
cp LICENSE-GPL2 %{buildroot}/usr/share/package-licenses/sip/LICENSE-GPL2
cp LICENSE-GPL3 %{buildroot}/usr/share/package-licenses/sip/LICENSE-GPL3
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sip

%files dev
%defattr(-,root,root,-)
/usr/include/python3.7m/sip.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sip/LICENSE-GPL2
/usr/share/package-licenses/sip/LICENSE-GPL3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
