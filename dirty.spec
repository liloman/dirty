%define repo https://github.com/liloman

Name:		dirty
Version:	0.1
Release:	1%{?dist}
Summary:	nothing special just a dirty repo

License:	MIT
URL:	%{repo}/dirty/
Source0:	%{url}/archive/v%{version}.tar.gz	

BuildRequires:	wget

%description

so it will do n000thing

%prep
wget %{url}/archive/v%{version}.tar.gz	
tar zxvf v%{version}.tar.gz


# %build

%install
mkdir -p %{buildroot}/tmp
cp -av %{name}-%{version}/ %{buildroot}/tmp

%files
/tmp/*
%doc



%changelog
* Wed Jan 18 2017 liloman <eselilo@gmail.com> 0.1-1
- new package built with tito


