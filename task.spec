Name:           dirty
Version:        0.2
Release:        1%{?dist}
Summary:        dirty repo dir specs
License:        MIT
URL:            https://dirty.org
Source0:        %{url}/download/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  make

BuildRequires:  libuuid-devel
BuildRequires:  gnutls-devel

%description
Dirty and dirty and dirty. so clean it!!

%prep
%autosetup
mkdir %{_target_platform}

%build
pushd %{_target_platform}
  %cmake .. -DTASK_RCDIR=%{_datadir}/%{name}
popd
%make_build -C %{_target_platform}

%install
%make_install -C %{_target_platform}

# Move shell completion stuff to the right place
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
install -Dpm0644 scripts/bash/%{name}.sh %{buildroot}%{_datadir}/bash-completion/completions/%{name}

# Fix perms and drop shebangs
# that's only docs and it's written in README about permissings
find scripts/ -type f -exec chmod -x {} ';'
find scripts/ -type f -exec sed -i -e '1{\@^#!.*@d}' {} ';'

rm -vrf %{buildroot}%{_datadir}/doc/%{name}/

%files
%license LICENSE
%doc NEWS doc/ref/%{name}-ref.pdf
%doc scripts/vim/ scripts/hooks/
%{_bindir}/%{name}
# We don't want to have refresh script there
%exclude %{_datadir}/%{name}/refresh
%{_datadir}/%{name}/
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/%{name}

%changelog
* Mon Jan 16 2017 liloman <eselilo@gmail.com> 0.2-1
- new package built with tito

* Mon Jan 16 2017 liloman <eselilo@gmail.com> 2.5.2-1
- new package built with tito

* Wed Aug 10 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.5.1-2
- Modernize spec

* Tue May 19 2009 Federico Hernandez <ultrafredde@gmail.com> - 1.7.0-1
  Initial RPM.
