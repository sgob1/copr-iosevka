%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss17
Version:        27.3.3
Release:        3%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Recursive Mono Style).

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  nodejs-npm
BuildRequires:  ttfautohint


%description
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.


%package -n iosevka-ss17-fonts


%package -n iosevka-term-ss17-fonts


%package -n iosevka-fixed-ss17-fonts


%prep
%autosetup -n %{source_name}-%{version}


%build
npm install

npm run build -- ttf::iosevka-ss17
npm run build -- ttf::iosevka-term-ss17
npm run build -- ttf::iosevka-fixed-ss17


%clean
%{__rm} -rf %{buildroot}


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
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed files specification
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed description
* Wed Nov 01 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- First version
