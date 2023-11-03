%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss04
Version:        27.3.3
Release:        4%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Menlo Style).

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  nodejs-npm
BuildRequires:  ttfautohint


%description
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-ss04-fonts
Summary:        Slender typeface for code, from code (Monospace, Menlo Style).
%description -n iosevka-ss04-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-term-ss04-fonts
Summary:        Slender typeface for code, from code (Monospace, Menlo Style).
%description -n iosevka-term-ss04-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fixed-ss04-fonts
Summary:        Slender typeface for code, from code (Monospace, Menlo Style).
%description -n iosevka-fixed-ss04-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%prep
%autosetup -n %{source_name}-%{version}


%build
npm install

npm run build -- ttf::iosevka-ss04
npm run build -- ttf::iosevka-term-ss04
npm run build -- ttf::iosevka-fixed-ss04


%clean
%{__rm} -rf %{buildroot}


%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss04/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss04-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss04/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss04-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss04/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss04-fonts


# Iosevka SS04 — Monospace, Menlo Style
%files -n iosevka-ss04-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss04-fonts


%files -n iosevka-term-ss04-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss04-fonts


%files -n iosevka-fixed-ss04-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss04-fonts


%changelog
* Fri Nov 03 15:52:45 CET 2023 Marco Sgobino <marco.sgobino@gmail.com> - v27.3.3-4
- Fixed formatting of descriptions
- Introduced new changelog format
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed files specification
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed description
* Wed Nov 01 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- First version
