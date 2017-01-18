Name:	dirty
Version:	0.12
Release:	1%{?dist}
Summary:	nothing special just a dirty repo
License:	MIT
URL:  https://github.com/liloman/dirty

%define tgz %{name}-%{version}-1.tar.gz	
Source0:	%{url}/archive/%{tgz}


BuildRequires:	wget

%description

so it will do n000thing

%prep
wget	%{url}/archive/%{tgz}
tar zxvf %{tgz}


%build
exit 0

%install
mkdir -p %{buildroot}/tmp
cp -av %{name}-%{name}-%{version}-1/ %{buildroot}/tmp

%files
/tmp/*
%doc


