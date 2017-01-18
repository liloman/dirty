%define repo https://github.com/liloman

Name:		dirty
Version:	0.4
Release:	1%{?dist}
Summary:	nothing special just a dirty repo

License:	MIT
URL:	%{repo}/dirty/
Source0:	%{url}/archive/v%{version}-%{release}.tar.gz	

BuildRequires:	wget

%description

so it will do n000thing

%prep
wget	%{url}/archive/v%{version}-%{release}.tar.gz	
tar zxvf v%{version}.tar.gz


# %build

%install
mkdir -p %{buildroot}/tmp
cp -av %{name}-%{version}/ %{buildroot}/tmp

%files
/tmp/*
%doc


