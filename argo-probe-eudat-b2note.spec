Name:		argo-probe-eudat-b2note
Version:	1.0
Release:	3%{?dist}
Summary:	A list of metrics to check the responsiveness of B2NOTE
License:	GPLv3+
Packager:	Themis Zamani <themiszamani@gmail.com>

Source:		%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}
AutoReqProv: no

%description
Nagios probes to check functionality of B2NOTE service 

%prep
%setup -q

%define _unpackaged_files_terminate_build 0 

%install

install -d %{buildroot}/%{_libexecdir}/argo/probes/eudat-b2note
install -m 755 check_b2note.sh %{buildroot}/%{_libexecdir}/argo/probes/eudat-b2note/check_b2note.sh

%files

%dir /%{_libexecdir}/argo
%dir /%{_libexecdir}/argo/probes/
%dir /%{_libexecdir}/argo/probes/eudat-b2note

%attr(0755,root,root) /%{_libexecdir}/argo/probes/eudat-b2note/check_b2note.sh

%changelog

* Mon Mar 14 2022 Themis Zamani <themiszamani@gmail.com> - 1.0-3
- Update package prerequisites based on argo monitoring. 
* Thu May 16 2019 Themis Zamani <themiszamani@gmail.com> - 1.0-2
- New version
* Tue Jul 2 2018 Themis Zamani <themiszamani@gmail.com> - 1.0-1
- Initial version of the package. 



