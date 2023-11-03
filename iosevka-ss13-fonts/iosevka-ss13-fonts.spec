%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss13
Version:        27.3.3
Release:        3%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Lucida Style).

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  nodejs-npm
BuildRequires:  ttfautohint


%description
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.


%package -n iosevka-ss13-fonts
Summary:        Slender typeface for code, from code (Monospace, Lucida Style)
%description -n iosevka-ss13-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.


%package -n iosevka-term-ss13-fonts
Summary:        Slender typeface for code, from code (Monospace, Lucida Style).
%description -n iosevka-term-ss13-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.


%package -n iosevka-fixed-ss13-fonts
Summary:        Slender typeface for code, from code (Monospace, Lucida Style).
%description -n iosevka-fixed-ss13-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.


%prep
%autosetup -n %{source_name}-%{version}


%build
npm install

npm run build -- ttf::iosevka-ss13
npm run build -- ttf::iosevka-term-ss13
npm run build -- ttf::iosevka-fixed-ss13


%clean
%{__rm} -rf %{buildroot}


%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss13/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss13-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss13/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss13-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss13/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss13-fonts


# Iosevka SS13 — Monospace, Lucida Style
%files -n iosevka-ss13-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss13-fonts


%files -n iosevka-term-ss13-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss13-fonts


%files -n iosevka-fixed-ss13-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss13-fonts


%changelog
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed files specification
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed description
* Wed Nov 01 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- First version
