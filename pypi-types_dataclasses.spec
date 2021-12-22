#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-types_dataclasses
Version  : 0.6.1
Release  : 1
URL      : https://files.pythonhosted.org/packages/aa/f1/ece799093b042b899aa6921081e65e4404894a44d27bf18490ee1065bee7/types-dataclasses-0.6.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/aa/f1/ece799093b042b899aa6921081e65e4404894a44d27bf18490ee1065bee7/types-dataclasses-0.6.1.tar.gz
Summary  : Typing stubs for dataclasses
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-types_dataclasses-python = %{version}-%{release}
Requires: pypi-types_dataclasses-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
No detailed description available

%package python
Summary: python components for the pypi-types_dataclasses package.
Group: Default
Requires: pypi-types_dataclasses-python3 = %{version}-%{release}

%description python
python components for the pypi-types_dataclasses package.


%package python3
Summary: python3 components for the pypi-types_dataclasses package.
Group: Default
Requires: python3-core
Provides: pypi(types_dataclasses)

%description python3
python3 components for the pypi-types_dataclasses package.


%prep
%setup -q -n types-dataclasses-0.6.1
cd %{_builddir}/types-dataclasses-0.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640196578
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*