%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss17
Version:        27.3.5
Release:        1%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Recursive Mono Style)

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


%package -n iosevka-ss17-fonts
Summary:        Slender typeface for code, from code (Monospace, Recursive Mono Style)
%description -n iosevka-ss17-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-term-ss17-fonts
Summary:        Slender typeface for code, from code (Monospace, Recursive Mono Style)
%description -n iosevka-term-ss17-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fixed-ss17-fonts
Summary:        Slender typeface for code, from code (Monospace, Recursive Mono Style)
%description -n iosevka-fixed-ss17-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%prep
%autosetup -n %{source_name}-%{version}


%build
npm install

npm run build -- ttf::iosevka-ss17
npm run build -- ttf::iosevka-term-ss17
npm run build -- ttf::iosevka-fixed-ss17


%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss17/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss17-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss17/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss17-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss17/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss17-fonts


# Iosevka SS17 — Monospace, Recursive Mono Style
%files -n iosevka-ss17-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss17-fonts


%files -n iosevka-term-ss17-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss17-fonts


%files -n iosevka-fixed-ss17-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss17-fonts


%changelog
* Sat Nov 11 18:39:05 CET 2023 Marco Sgobino <marco.sgobino@gmail.com> - v27.3.5-1
- Version 27.3.5
* Sat Nov 11 09:49:18 CET 2023 Marco Sgobino <marco.sgobino@gmail.com> - v27.3.4-2
- Version 27.3.4
- Removed clean section
- Removed period in Summary
* Sat Nov 04 14:08:39 CET 2023 Marco Sgobino <marco.sgobino@gmail.com> - v27.3.4-1
- Version 27.3.4
* Fri Nov 03 15:52:45 CET 2023 Marco Sgobino <marco.sgobino@gmail.com> - v27.3.3-4
- Fixed formatting of descriptions
- Introduced new changelog format
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed files specification
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed description
* Wed Nov 01 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- First version
