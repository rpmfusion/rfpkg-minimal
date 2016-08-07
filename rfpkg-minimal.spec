Name:           rfpkg-minimal
Version:        0.2.0
Release:        1%{?dist}
Summary:        Fork of fedpkg-minimal for RPM Fusion

# Licensing is unclear; LICENSE is the GPLv2 but bin/fedpkg (upstream)
# has a comment saying it is under the GPLv3. We're assuming GPLv2 for now.
# See https://fedorahosted.org/fedpkg-minimal/ticket/2
License:        GPLv2

URL:            https://github.com/rpmfusion-infra/rfpkg-minimal
Source0:        https://github.com/rpmfusion-infra/rfpkg-minimal/archive/%{version}.tar.gz#/rfpkg-minimal-%{version}.tar.gz

BuildArch:      noarch

# The script needs curl, just like fedpkg-minimal.
Requires:       curl

%description
rfpkg-minimal contains a script for use in RPM Fusion's Koji instance
to download the sources of a package. It is based on (and is a fork of)
fedpkg-minimal.

%prep
%autosetup

%build
# Nothing to build!

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 755 bin/rfpkg-minimal %{buildroot}%{_bindir}/rfpkg-minimal

%files
%{_bindir}/rfpkg-minimal
%doc README.md AUTHORS.md
%license LICENSE

%changelog
* Sun Aug  7 2016 Ben Rosser <rosser.bjr@gmail.com> 0.2.0-1
- Update to 0.2.0, with support for non-MD5 hashes
- Change upstream URL to point at rpmfusion-infra repo

* Sat Jul  9 2016 Ben Rosser <rosser.bjr@gmail.com> 0.1.1-1
- Rename rfpkg to rfpkg-minimal, remove conflict with fedpkg
- Add comment with link to upstream bug about licensing

* Fri Jul  8 2016 Ben Rosser <rosser.bjr@gmail.com> 0.1.0-1
- Initial package.
