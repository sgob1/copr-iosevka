%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss05
Version:        27.3.3
Release:        2%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Fira Mono Style).

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  nodejs-npm
BuildRequires:  ttfautohint


%description
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.


%prep
%autosetup -n %{source_name}-%{version}


%build
npm install

npm run build -- ttf::iosevka-ss05
npm run build -- ttf::iosevka-term-ss05
npm run build -- ttf::iosevka-fixed-ss05


%clean
%{__rm} -rf %{buildroot}


%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss05/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss05/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss05-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss05/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss05-fonts


# Iosevka SS05 — Monospace, Fira Mono Style
%files -n iosevka-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss05-fonts/*


%files -n iosevka-term-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss05-fonts/*


%files -n iosevka-fixed-ss05-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss05-fonts/*


%changelog
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed description
* Wed Nov 01 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- First version
