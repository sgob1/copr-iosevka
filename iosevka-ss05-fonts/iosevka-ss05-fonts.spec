%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss05
Version:        27.3.4
Release:        1%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Fira Mono Style)

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


%package -n iosevka-ss05-fonts
Summary:        Slender typeface for code, from code (Monospace, Fira Mono Style)
%description -n iosevka-ss05-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-term-ss05-fonts
Summary:        Slender typeface for code, from code (Monospace, Fira Mono Style)
%description -n iosevka-term-ss05-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fixed-ss05-fonts
Summary:        Slender typeface for code, from code (Monospace, Fira Mono Style)
%description -n iosevka-fixed-ss05-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%prep
%autosetup -n %{source_name}-%{version}


%build
npm install

npm run build -- ttf::iosevka-ss05
npm run build -- ttf::iosevka-term-ss05
npm run build -- ttf::iosevka-fixed-ss05


%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss05/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss05/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss05/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss05-fonts


# Iosevka SS05 — Monospace, Fira Mono Style
%files -n iosevka-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss05-fonts


%files -n iosevka-term-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss05-fonts


%files -n iosevka-fixed-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss05-fonts


%changelog
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
