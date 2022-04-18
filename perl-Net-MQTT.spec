#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Net
%define		pnam	MQTT
Summary:	Net::MQTT - Perl modules for MQTT Protocol (http://mqtt.org/)
Summary(pl.UTF-8):	Net::MQTT - moduły perlowe do obsułgi protokołu sieciowego MQTT
Name:		perl-Net-MQTT
Version:	1.163170
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6c3eac1a3e6c402ddbfdfebb3e3fa1cb
URL:		http://search.cpan.org/dist/Net-MQTT/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test::More)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Low level API for the MQTT protocol described at http://mqtt.org.

IMPORTANT: This is an early release and the API is still subject to
change.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Net/MQTT/Message
%{perl_vendorlib}/Net/MQTT/Constants.pm
%{perl_vendorlib}/Net/MQTT/Message.pm
%{perl_vendorlib}/Net/MQTT/Message/ConnAck.pm
%{perl_vendorlib}/Net/MQTT/Message/Connect.pm
%{perl_vendorlib}/Net/MQTT/Message/Disconnect.pm
%{perl_vendorlib}/Net/MQTT/Message/JustMessageId.pm
%{perl_vendorlib}/Net/MQTT/Message/PingReq.pm
%{perl_vendorlib}/Net/MQTT/Message/PingResp.pm
%{perl_vendorlib}/Net/MQTT/Message/PubAck.pm
%{perl_vendorlib}/Net/MQTT/Message/PubComp.pm
%{perl_vendorlib}/Net/MQTT/Message/PubRec.pm
%{perl_vendorlib}/Net/MQTT/Message/PubRel.pm
%{perl_vendorlib}/Net/MQTT/Message/Publish.pm
%{perl_vendorlib}/Net/MQTT/Message/SubAck.pm
%{perl_vendorlib}/Net/MQTT/Message/Subscribe.pm
%{perl_vendorlib}/Net/MQTT/Message/UnsubAck.pm
%{perl_vendorlib}/Net/MQTT/Message/Unsubscribe.pm
%{perl_vendorlib}/Net/MQTT/TopicStore.pm
%attr(755,root,root) %{_bindir}/net-mqtt-pub
%attr(755,root,root) %{_bindir}/net-mqtt-sub
%attr(755,root,root) %{_bindir}/net-mqtt-trace
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
