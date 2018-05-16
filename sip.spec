#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sip
Version  : 4.19.6
Release  : 5
URL      : https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.6/sip-4.19.6.tar.gz
Source0  : https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.6/sip-4.19.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
BuildRequires : python3
BuildRequires : python3-dev
Patch1: build.patch

%description
SIP - C/C++ Bindings Generator for Python v2 and v3
===================================================

%prep
%setup -q -n sip-4.19.6
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515339488
python3 configure.py
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1515339488
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/bin/sip
/usr/include/python3.6m/sip.h
/usr/lib/python3.6/site-packages/sip.pyi
/usr/lib/python3.6/site-packages/sip.so
/usr/lib/python3.6/site-packages/sipconfig.py
/usr/lib/python3.6/site-packages/sipdistutils.py
%exclude /usr/lib/python3.6/site-packages/__pycache__/sipconfig.cpython-36.pyc
%exclude /usr/lib/python3.6/site-packages/__pycache__/sipdistutils.cpython-36.pyc
