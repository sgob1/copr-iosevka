%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss08
Version:        27.3.3
Release:        1%{?dist}
Summary:        Slender typeface for code, from code.

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

# Iosevka SS08 — Monospace, Pragmata Pro Style
%package -n iosevka-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n iosevka-ss08-fonts
Iosevka Monospace, Monaco Style

%package -n iosevka-term-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n iosevka-term-ss08-fonts
Iosevka Monospace, Monaco Style

%package -n iosevka-fixed-ss08-fonts
Summary:        Monospace, Pragmata Pro Style
%description -n iosevka-fixed-ss08-fonts
Iosevka Monospace, Monaco Style

%build
npm install

npm run build -- ttf::iosevka-ss08
npm run build -- ttf::iosevka-term-ss08
npm run build -- ttf::iosevka-fixed-ss08

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss08/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss08-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss08/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss08-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss08/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss08-fonts

# Iosevka SS08 — Monospace, Pragmata Pro Style
%files -n iosevka-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss08-fonts/*

%files -n iosevka-term-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss08-fonts/*

%files -n iosevka-fixed-ss08-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss08-fonts/*

%changelog
