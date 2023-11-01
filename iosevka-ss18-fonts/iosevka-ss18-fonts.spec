%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss18
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

# Iosevka SS18 — Monospace, Input Mono Style
%package -n iosevka-ss18-fonts
Summary:        Monospace, Input Mono Style
%description -n iosevka-ss18-fonts
Iosevka Monospace, Input Mono Style

%package -n iosevka-term-ss18-fonts
Summary:        Monospace, Input Mono Style
%description -n iosevka-term-ss18-fonts
Iosevka Monospace, Input Mono Style

%package -n iosevka-fixed-ss18-fonts
Summary:        Monospace, Input Mono Style
%description -n iosevka-fixed-ss18-fonts
Iosevka Monospace, Input Mono Style

%build
npm install

npm run build -- ttf::iosevka-ss18
npm run build -- ttf::iosevka-term-ss18
npm run build -- ttf::iosevka-fixed-ss18

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss18/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss18-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss18/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss18-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss18/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss18-fonts

# Iosevka SS18 — Monospace, Input Mono Style
%files -n iosevka-ss18-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss18-fonts/*

%files -n iosevka-term-ss18-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss18-fonts/*

%files -n iosevka-fixed-ss18-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss18-fonts/*

%changelog
