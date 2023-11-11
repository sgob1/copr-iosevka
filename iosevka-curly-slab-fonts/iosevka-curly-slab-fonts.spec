%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-curly-slab
Version:        27.3.5
Release:        1%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Curly Style, Slab-serif)

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


%package -n iosevka-curly-slab-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style, Slab-serif)
%description -n iosevka-curly-slab-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-term-curly-slab-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style, Slab-serif)
%description -n iosevka-term-curly-slab-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fixed-curly-slab-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style, Slab-serif)
%description -n iosevka-fixed-curly-slab-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.


%prep
%autosetup -n %{source_name}-%{version}


%build
npm install

npm run build -- ttf::iosevka-curly-slab
npm run build -- ttf::iosevka-term-curly-slab
npm run build -- ttf::iosevka-fixed-curly-slab


%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-curly-slab/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-curly-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-curly-slab/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-curly-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-curly-slab/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-curly-slab-fonts


# Iosevka Curly Slab — Monospace, Curly Style, Slab-serif
%files -n iosevka-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-curly-slab-fonts


%files -n iosevka-term-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-curly-slab-fonts


%files -n iosevka-fixed-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-curly-slab-fonts


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
