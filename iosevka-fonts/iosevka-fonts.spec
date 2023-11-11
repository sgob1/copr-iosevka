%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka
Version:        27.3.4
Release:        2%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Default)

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


%package -n iosevka-fonts
Summary:        Slender typeface for code, from code (Monospace, Default)
%description -n iosevka-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-term-fonts
Summary:        Slender typeface for code, from code (Monospace, Default)
%description -n iosevka-term-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fixed-fonts
Summary:        Slender typeface for code, from code (Monospace, Default)
%description -n iosevka-fixed-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%prep
%autosetup -n %{source_name}-%{version}


%build
npm install
npm run build -- ttf::iosevka
npm run build -- ttf::iosevka-term
npm run build -- ttf::iosevka-fixed


%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-fonts


# Iosevka — Monospace, Default
%files -n iosevka-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fonts


%files -n iosevka-term-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-fonts


%files -n iosevka-fixed-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-fonts


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
