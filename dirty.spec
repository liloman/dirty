Name:		dirty
Version:	0.1
Release:	1%{?dist}
Summary:	nothing special just a dirty repo

License:	MIT
URL:	https://github.com/liloman/dirty/
Source0:	https://github.com/liloman/dirty/archive/v0.1.tar.gz	

Requires:	wget

%description

so it will do n000thing

%prep
%setup -q


%build
wget ${source0}
tar zxvf v0.1.tar.gz

%install
mkdir -p %{buildroot}/tmp
cp -a v0.1 %{buildroot}/tmp

%files
/tmp/*
%doc



%changelog
* Wed Jan 18 2017 liloman <eselilo@gmail.com> 0.1-1
- new package built with tito


