Name:	dirty
Version:	0.20
Release:	1%{?dist}
Summary:	nothing special just a dirty repo
License:	MIT
URL:  https://github.com/liloman/dirty

%define tgz %{name}-%{version}-1.tar.gz	
Source0:	%{url}/archive/%{tgz}


BuildRequires:	wget

%description

so it will do n000thing

# #download it to sourcedir
# wget	%{url}/archive/%{tgz} -P %{_sourcedir}/
# tar -zxvf %{_sourcedir}/%{tgz} 

# %prep


%build
exit 0

%install
cd %{_sourcedir}/%{name}*
mkdir -p %{buildroot}/tmp
cp -a * %{buildroot}/tmp


#tito nonsense?
#cd %{_sourcedir}
#cp /tmp/tito/%{name}-%{version}.tar.gz	%{tgz} 


%files
/tmp/*
%doc


