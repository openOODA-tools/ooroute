Name:           ooroute
Version:        0.1.0
Release:        1%{?dist}
Summary:        Reads and manages kernel IP routing tables and default gateways.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooroute
Source0:        ooroute-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooroute is a sovereign, capability-bounded ROUTING TABLE written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooroute
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooroute-uninstall

%files
/usr/bin/ooroute
/usr/bin/ooroute-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
