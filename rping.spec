%include	/usr/lib/rpm/macros.perl
Summary:	A script for remote pinging from a Cisco router using SNMP
Name:		rping
Version:	0.2
Release:	0.2
License:	Unknown
Group:		Networking
Source0:	http://www.marmoset.net/~knail1/scripts/rping/%{name}-%{version}.tar.gz
# Source0-md5:	fdd6ca4cbd7d528db7f5ff0d89e45f14
URL:		http://www.marmoset.net/~knail1/scripts/rping/rping.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RemotePing is a Perl script which, using SNMP, remotely pings
single/multiple hosts from a (Cisco) router (X) while sitting on a
Unix box (A). This is particularly helpful if you want to ping
multiple Access Routers from a single Backbone Router, or if you want
to ping a machine which is accessible from X but not from A (because
of security or route censoring).

%prep
%setup -q -c %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}/snmp}

install rping $RPM_BUILD_ROOT%{_bindir}
install hostseed $RPM_BUILD_ROOT%{_sysconfdir}/snmp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/snmp/hostseed
%attr(755,root,root) %{_bindir}/*
