%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss06
Version:        27.3.4
Release:        1%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Liberation Mono Style)

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


%package -n iosevka-ss06-fonts
Summary:        Slender typeface for code, from code (Monospace, Liberation Mono Style)
%description -n iosevka-ss06-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-term-ss06-fonts
Summary:        Slender typeface for code, from code (Monospace, Liberation Mono Style)
%description -n iosevka-term-ss06-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fixed-ss06-fonts
Summary:        Slender typeface for code, from code (Monospace, Liberation Mono Style)
%description -n iosevka-fixed-ss06-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%prep
%autosetup -n %{source_name}-%{version}


%build
npm install

npm run build -- ttf::iosevka-ss06
npm run build -- ttf::iosevka-term-ss06
npm run build -- ttf::iosevka-fixed-ss06


%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss06/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss06-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss06/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss06-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss06/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss06-fonts


# Iosevka SS06 — Monospace, Liberation Mono Style
%files -n iosevka-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss06-fonts


%files -n iosevka-term-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss06-fonts


%files -n iosevka-fixed-ss06-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss06-fonts


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
