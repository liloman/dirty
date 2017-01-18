%define repo https://github.com/liloman

Name:		dirty
Version:	0.6
Release:	1%{?dist}
Summary:	nothing special just a dirty repo

License:	MIT
URL:	%{repo}/dirty
Source0:	%{url}/archive/v%{version}-1.tar.gz	

BuildRequires:	wget

%description

so it will do n000thing

%prep
wget	%{url}/archive/v%{version}-1.tar.gz	
tar zxvf v%{version}-1.tar.gz


# %build

%install
mkdir -p %{buildroot}/tmp
cp -av %{name}-%{version}-1/ %{buildroot}/tmp

%files
/tmp/*
%doc


