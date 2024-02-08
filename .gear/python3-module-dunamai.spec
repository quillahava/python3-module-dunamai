%define pypi_name dunamai

Name:           python3-module-%pypi_name
Version:        1.19.1
Release:        alt1
Summary:        Dynamic version generation
Group:          Development/Python3

License:        MIT
URL:            https://github.com/mtkennerly/dunamai
Source0:        %{name}-%{version}.tar

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-dev
BuildRequires:  python3(setuptools)
BuildRequires:  python3(wheel)
BuildRequires:  python3-module-poetry
Requires: python3-module-packaging

%py3_provides %pypi_name

BuildArch:      noarch

%description
Dunamai is a Python 3.5+ library and command line tool for producing dynamic, standards-compliant version strings, derived from tags in your version control system. This facilitates uniquely identifying nightly or per-commit builds in continuous integration and releasing new versions of your software simply by creating a tag.

%prep
%setup -v

%build
%pyproject_build

%install
%pyproject_install
install -Dm644 LICENSE %{buildroot}%{_licensedir}/%{name}/LICENSE


%files
%doc README.md CHANGELOG.md CONTRIBUTING.md
%_licensedir/%name/LICENSE
%python3_sitelibdir/*

%changelog
* Thu Feb 8 2024 Aleksandr A. Voyt <vojtaa@basealt.ru> 1.19.1-alt1
- First package version

