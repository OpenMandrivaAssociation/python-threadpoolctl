%define module threadpoolctl
%bcond tests 1

Name:		python-threadpoolctl
Version:	3.6.0
Release:	1
Summary:	Python helpers to limit the number of threads used in libraries
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://github.com/joblib/threadpoolctl
Source0:	https://github.com/joblib/threadpoolctl/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(flit-core)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-cov)
BuildRequires:	python%{pyver}dist(scipy)
BuildRequires:	python%{pyver}dist(setuptools)
%endif

%description
Python helpers to limit the number of threads used in native libraries that
handle their own internal threadpool (BLAS and OpenMP implementations)

Fine control of the underlying thread-pool size can be useful in workloads
that involve nested parallelism so as to mitigate oversubscription issues.

%install -a
rm -rf %{buildroot}%{python_sitelib}/__pycache__/%{module}.*.py*

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}"
# test_architecture has a hardcoded list of architectures,
# instead of playing Whac-A-Mole by adding new and new, we skip it
pytest --no-cov -ra tests/ -k 'not test_architecture and not test_command_line'\
	--deselect "tests/test_threadpoolctl.py::test_controller_info_actualized"
%endif

%files
%doc README.md multiple_openmp.md
%{python_sitelib}/%{module}.py
%{python_sitelib}/%{module}-%{version}.dist-info
