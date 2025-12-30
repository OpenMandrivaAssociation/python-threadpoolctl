Summary:	threadpoolctl
Name:		python-threadpoolctl
Version:	3.5.0
Release:	2
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://pypi.org/project/threadpoolctl/
Source0:	https://pypi.org/packages/source/t/threadpoolctl/threadpoolctl-%{version}.tar.gz
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(flit)
BuildRequires:	python%{pyver}dist(pip)

BuildArch:	noarch

%description
Python helpers to limit the number of threads used in the threadpool-backed
of common native libraries used for scientific computing and data science
(e.g. BLAS and OpenMP).

Fine control of the underlying thread-pool size can be useful in workloads
that involve nested parallelism so as to mitigate oversubscription issues.

%files
%{py_sitedir}/threadpoolctl.py
%{py_sitedir}/threadpoolctl-*.*-info
#{py_sitedir}/__pycache__/threadpoolctl.cpython-.*pyc

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n threadpoolctl-%{version}

%build
%py_build

%install
%py_install

rm -fr %{buildroot}%{py_sitedir}/__pycache__

