#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	pytest plugin for test session metadata
Summary(pl.UTF-8):	Wtyczka pytesta do metadanych sesji testowej
Name:		python-pytest-metadata
# keep 1.x here for python2 support
Version:	1.11.0
Release:	3
License:	MPL v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-metadata/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-metadata/pytest-metadata-%{version}.tar.gz
# Source0-md5:	a1609e923a0c838c38cc425575729ea0
URL:		https://pypi.org/project/pytest-metadata/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-pytest >= 2.9.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-pytest >= 2.9.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest-metadata is a plugin for pytest that provides access to test
session metadata.

%description -l pl.UTF-8
pytest-metadata to wtyczka pytesta, zapewniająca dostęp do metadanych
sesji testowej.

%package -n python3-pytest-metadata
Summary:	pytest plugin for test session metadata
Summary(pl.UTF-8):	Wtyczka pytesta do metadanych sesji testowej
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-pytest-metadata
pytest-metadata is a plugin for pytest that provides access to test
session metadata.

%description -n python3-pytest-metadata -l pl.UTF-8
pytest-metadata to wtyczka pytesta, zapewniająca dostęp do metadanych
sesji testowej.

%prep
%setup -q -n pytest-metadata-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_metadata.plugin \
PYTHONPATH=$(pwd) \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=pytest_metadata.plugin \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/pytest_metadata
%{py_sitescriptdir}/pytest_metadata-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-metadata
%defattr(644,root,root,755)
%doc AUTHORS CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/pytest_metadata
%{py3_sitescriptdir}/pytest_metadata-%{version}-py*.egg-info
%endif
