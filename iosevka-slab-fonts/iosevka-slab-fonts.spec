%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-slab
Version:        27.3.4
Release:        1%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Slab-serif).

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


%package -n iosevka-slab-fonts
Summary:        Slender typeface for code, from code (Monospace, Slab-serif).
%description -n iosevka-slab-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-term-slab-fonts
Summary:        Slender typeface for code, from code (Monospace, Slab-serif).
%description -n iosevka-term-slab-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fixed-slab-fonts
Summary:        Slender typeface for code, from code (Monospace, Slab-serif).
%description -n iosevka-fixed-slab-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%prep
%autosetup -n %{source_name}-%{version}


%build
npm install

npm run build -- ttf::iosevka-slab
npm run build -- ttf::iosevka-term-slab
npm run build -- ttf::iosevka-fixed-slab


%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-slab/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-slab/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-slab/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-slab-fonts


# Iosevka Slab — Monospace, Slab-serif
%files -n iosevka-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-slab-fonts


%files -n iosevka-term-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-slab-fonts


%files -n iosevka-fixed-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-slab-fonts


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
