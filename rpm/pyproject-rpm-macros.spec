Name:           pyproject-rpm-macros
Summary:        RPM macros for PEP 517 Python packages
License:        MIT
Version:        1.14.0
Release:        1
URL:            https://github.com/sailfishos/pyproject-rpm-macros
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

# We build on top of those:
BuildRequires:  python-rpm-macros
BuildRequires:  python-srpm-macros
BuildRequires:  python3-rpm-macros
Requires:       python-rpm-macros
Requires:       python-srpm-macros
Requires:       python3-rpm-macros
Requires:       (pyproject-srpm-macros = %{version}-%{release} if pyproject-srpm-macros)

# We use the following tools outside of coreutils
Requires:       findutils
Requires:       sed

Requires:       rpm-build
BuildRequires:  rpm-build

%description
These macros allow projects that follow the Python packaging specifications
to be packaged as RPMs.

They work for:

* traditional Setuptools-based projects that use the setup.py file,
* newer Setuptools-based projects that have a setup.cfg file,
* general Python projects that use the PEP 517 pyproject.toml file
  (which allows using any build system, such as setuptools, flit or poetry).

These macros replace %%py3_build and %%py3_install,
which only work with setup.py.

%package -n pyproject-srpm-macros
Summary:        Minimal implementation of %%pyproject_buildrequires
Requires:       (pyproject-rpm-macros = %{version}-%{release} if pyproject-rpm-macros)
Requires:       rpm-build

%description -n pyproject-srpm-macros
This package contains a minimal implementation of %%pyproject_buildrequires.
When used in %%generate_buildrequires, it will generate BuildRequires
for pyproject-rpm-macros. When both packages are installed, the full version
takes precedence.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%generate_buildrequires

%build

%install
mkdir -p %{buildroot}%{_rpmmacrodir}
mkdir -p %{buildroot}%{_rpmconfigdir}/redhat
install -pm 644 macros.pyproject %{buildroot}%{_rpmmacrodir}/
install -pm 644 macros.aaa-pyproject-srpm %{buildroot}%{_rpmmacrodir}/
install -pm 644 pyproject_buildrequires.py %{buildroot}%{_rpmconfigdir}/redhat/
install -pm 644 pyproject_convert.py %{buildroot}%{_rpmconfigdir}/redhat/
install -pm 644 pyproject_save_files.py  %{buildroot}%{_rpmconfigdir}/redhat/
install -pm 644 pyproject_preprocess_record.py %{buildroot}%{_rpmconfigdir}/redhat/
install -pm 644 pyproject_construct_toxenv.py %{buildroot}%{_rpmconfigdir}/redhat/
install -pm 644 pyproject_requirements_txt.py %{buildroot}%{_rpmconfigdir}/redhat/
install -pm 644 pyproject_wheel.py %{buildroot}%{_rpmconfigdir}/redhat/

%files
%license LICENSE
%doc README.md
%{_rpmmacrodir}/macros.pyproject
%{_rpmconfigdir}/redhat/pyproject_buildrequires.py
%{_rpmconfigdir}/redhat/pyproject_convert.py
%{_rpmconfigdir}/redhat/pyproject_save_files.py
%{_rpmconfigdir}/redhat/pyproject_preprocess_record.py
%{_rpmconfigdir}/redhat/pyproject_construct_toxenv.py
%{_rpmconfigdir}/redhat/pyproject_requirements_txt.py
%{_rpmconfigdir}/redhat/pyproject_wheel.py

%files -n pyproject-srpm-macros
%license LICENSE
%{_rpmmacrodir}/macros.aaa-pyproject-srpm
