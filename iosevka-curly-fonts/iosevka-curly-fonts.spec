%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-curly
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

# Iosevka Curly — Monospace, Curly Style
%package -n iosevka-curly-fonts
Summary:        Monospace, Curly Style
%description -n iosevka-curly-fonts
Iosevka Monospace, Curly Style

%package -n iosevka-term-curly-fonts
Summary:        Monospace, Slab-serif
%description -n iosevka-term-curly-fonts
Iosevka Monospace, Curly Style

%package -n iosevka-fixed-curly-fonts
Summary:        Monospace, Slab-serif
%description -n iosevka-fixed-curly-fonts
Iosevka Monospace, Curly Style

%build
npm install

npm run build -- ttf::iosevka-curly
npm run build -- ttf::iosevka-term-curly
npm run build -- ttf::iosevka-fixed-curly

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-curly/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-curly-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-curly/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-curly-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-curly/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-curly-fonts

# Iosevka Curly — Monospace, Curly Style
%files -n iosevka-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-curly-fonts/*

%files -n iosevka-term-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-curly-fonts/*

%files -n iosevka-fixed-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-curly-fonts/*

%changelog
