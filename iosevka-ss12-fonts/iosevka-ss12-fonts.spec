%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-ss12
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

# Iosevka SS12 — Monospace, Ubuntu Mono Style
%package -n iosevka-ss12-fonts
Summary:        Monospace, Ubuntu Mono Style
%description -n iosevka-ss12-fonts
Iosevka Monospace, Ubuntu Mono Style

%package -n iosevka-term-ss12-fonts
Summary:        Monospace, Ubuntu Mono Style
%description -n iosevka-term-ss12-fonts
Iosevka Monospace, Ubuntu Mono Style

%package -n iosevka-fixed-ss12-fonts
Summary:        Monospace, Ubuntu Mono Style
%description -n iosevka-fixed-ss12-fonts
Iosevka Monospace, Ubuntu Mono Style

%build
npm install

npm run build -- ttf::iosevka-ss12
npm run build -- ttf::iosevka-term-ss12
npm run build -- ttf::iosevka-fixed-ss12

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-ss12/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-ss12-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-ss12/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-ss12-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-ss12/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-ss12-fonts

# Iosevka SS12 — Monospace, Ubuntu Mono Style
%files -n iosevka-ss12-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-ss12-fonts/*

%files -n iosevka-term-ss12-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-ss12-fonts/*

%files -n iosevka-fixed-ss12-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-ss12-fonts/*

%changelog
