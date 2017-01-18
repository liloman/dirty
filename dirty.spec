Name:	dirty
Version:	0.8
Release:	1%{?dist}
Summary:	nothing special just a dirty repo
License:	MIT
%define repo https://github.com/liloman
URL:	%{repo}/dirty

%define tgz %{name}-%{version}-1.tar.gz	
Source0:	%{url}/archive/%{tgz}


BuildRequires:	wget

%description

so it will do n000thing

%prep
wget	%{SOURCE0}
tar zxvf ${tgz}


%build

%install
mkdir -p %{buildroot}/tmp
cp -av %{name}-%{version}-1/ %{buildroot}/tmp

%files
/tmp/*
%doc


