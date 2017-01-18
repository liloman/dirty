Name:	dirty
Version:	0.18
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
if %{release} != 1.git*
#download it to sourcedir
wget	%{url}/archive/%{tgz} -P %{_sourcedir}/
tar -zxvf %{_sourcedir}/%{tgz} 
%else
echo "hola"
%endif

%build
exit 0

%install
cd %{name}-%{name}-%{version}-1/
mkdir -p %{buildroot}/tmp

cp -av * %{buildroot}/tmp

%files
/tmp/*
%doc


