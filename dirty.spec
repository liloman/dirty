Name:	dirty
Version:	0.14
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
#download it to sourcedir
wget	%{url}/archive/%{tgz} -P %{_sourcedir}/
%setup -n 


%build
exit 0

%install
mkdir -p %{buildroot}/tmp
cp -av %{name}-%{name}-%{version}-1/ %{buildroot}/tmp

%files
/tmp/*
%doc


