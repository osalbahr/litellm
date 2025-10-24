Name:           python-litellm
Version:        1.78.7
Release:        %autorelease
Summary:        Library to easily interface with LLM API providers

License:        MIT
URL:            https://litellm.ai
Source:         %{pypi_source litellm}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'litellm' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-litellm
Summary:        %{summary}

%description -n python3-litellm %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-litellm caching,extra-proxy,mlflow,proxy,semantic-router,utils


%prep
%autosetup -p1 -n litellm-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x caching,extra-proxy,mlflow,proxy,semantic-router,utils


%build
%pyproject_wheel


%install
%pyproject_install
# Add top-level Python module names here as arguments, you can use globs
%pyproject_save_files ...


%check
%pyproject_check_import


%files -n python3-litellm -f %{pyproject_files}


%changelog
%autochangelog