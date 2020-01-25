Summary:	A script for remote pinging from a Cisco router using SNMP
Summary(pl.UTF-8):	Skrypt do zdalnego pingowania z routerów Cisco przy użyciu SNMP
Name:		rping
Version:	0.2
Release:	0.2
License:	unknown
Group:		Networking
Source0:	http://www.marmoset.net/~knail1/scripts/rping/%{name}-%{version}.tar.gz
# Source0-md5:	fdd6ca4cbd7d528db7f5ff0d89e45f14
URL:		http://www.marmoset.net/~knail1/scripts/rping/rping.html
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RemotePing is a Perl script which, using SNMP, remotely pings
single/multiple hosts from a (Cisco) router (X) while sitting on a
Unix box (A). This is particularly helpful if you want to ping
multiple Access Routers from a single Backbone Router, or if you want
to ping a machine which is accessible from X but not from A (because
of security or route censoring).

%description -l pl.UTF-8
RemotePing to skrypt Perla, który, przy użyciu SNMP, zdalnie pinguje
dany host (lub hosty) z routera Cisco (X), samemu działając na
komputerze z Uniksem (A). Jest to szczególnie pomocne jeśli chcemy
spingować wiele routerów dostępowych z jednego routera szkieletowego,
albo jeśli chcemy spingować maszynę dostępną z X, ale nie z A (ze
względów bezpieczeństwa lub cenzury routingu).

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/snmp}

install rping $RPM_BUILD_ROOT%{_bindir}
install hostseed $RPM_BUILD_ROOT%{_sysconfdir}/snmp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/snmp/hostseed
%attr(755,root,root) %{_bindir}/*
