Name:	dirty
Version:	0.28
Release:	1%{?dist}
Summary:	nothing special just a dirty repo
License:	MIT
URL:  https://github.com/liloman/dirty

# Source0: %{name}-%{version}.tar.gz
Source0:    %{url}/archive/%{name}-%{version}.tar.gz

%description

so it will do n000thing

%prep
%setup -q


%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/tmp
cp -a * %{buildroot}/tmp

%files
/tmp/*
%doc


