%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-curly
Version:        27.3.4
Release:        2%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Curly Style)

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


%package -n iosevka-curly-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style)
%description -n iosevka-curly-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-term-curly-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style)
%description -n iosevka-term-curly-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fixed-curly-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style)
%description -n iosevka-fixed-curly-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%prep
%autosetup -n %{source_name}-%{version}


%build
npm install

npm run build -- ttf::iosevka-curly
npm run build -- ttf::iosevka-term-curly
npm run build -- ttf::iosevka-fixed-curly


%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-curly/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-curly-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-curly/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-curly-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-curly/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-curly-fonts


# Iosevka Curly — Monospace, Curly Style
%files -n iosevka-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-curly-fonts


%files -n iosevka-term-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-curly-fonts


%files -n iosevka-fixed-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-curly-fonts


%changelog
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
