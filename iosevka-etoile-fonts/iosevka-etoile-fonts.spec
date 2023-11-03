%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-etoile
Version:        27.3.3
Release:        2%{?dist}
Summary:        Slender typeface for code, from code (Quasi-proportional, Slab-serif).

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

npm run build -- ttf::iosevka-etoile


%clean
%{__rm} -rf %{buildroot}


%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-etoile/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-etoile-fonts


# Iosevka Etoile — Quasi-proportional, Slab-serif
%files -n iosevka-etoile-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-etoile-fonts


%changelog
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed description
* Wed Nov 01 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- First version
