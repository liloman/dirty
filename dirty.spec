Name:	dirty
Version:	0.24
Release:	1%{?dist}
Summary:	nothing special just a dirty repo
License:	MIT
URL:  https://github.com/liloman/dirty

%define tgz %{name}-%{version}-1.tar.gz	
# Source0:	%{url}/archive/%{tgz}
Source0: %{name}-%{version}.tar.gz

%description

so it will do n000thing

%prep
%setup -q


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/tmp
cp -a * %{buildroot}/tmp

# cd %{_sourcedir}/%{name}*
# mkdir -p %{buildroot}/tmp
# cp -a * %{buildroot}/tmp


#why only for releases with tito??
# cd %{_sourcedir}
# cp /tmp/tito/%{name}-%{version}.tar.gz	%{tgz} 


%files
/tmp/*
%doc


