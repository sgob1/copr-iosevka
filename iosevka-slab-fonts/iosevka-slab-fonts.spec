%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-slab
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

# Iosevka Slab — Monospace, Slab-serif
%package -n iosevka-slab-fonts
Summary:        Monospace, Slab-serif
%description -n iosevka-slab-fonts
Iosevka Monospace, Slab-serif

%package -n iosevka-term-slab-fonts
Summary:        Monospace, Slab-serif
%description -n iosevka-term-slab-fonts
Iosevka Monospace, Slab-serif

%package -n iosevka-fixed-slab-fonts
Summary:        Monospace, Slab-serif
%description -n iosevka-fixed-slab-fonts
Iosevka Monospace, Slab-serif

%build
npm install

npm run build -- ttf::iosevka-slab
npm run build -- ttf::iosevka-term-slab
npm run build -- ttf::iosevka-fixed-slab

%clean
%{__rm} -rf %{buildroot}

%install
%{__rm} -rf %{buildroot}

%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-slab/ttf/*.ttf       -t %{buildroot}%{_datadir}/fonts/iosevka-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-term-slab/ttf/*.ttf  -t %{buildroot}%{_datadir}/fonts/iosevka-term-slab-fonts
%{__install} -D -m 0644 %{_builddir}/%{source_name}-%{version}/dist/iosevka-fixed-slab/ttf/*.ttf -t %{buildroot}%{_datadir}/fonts/iosevka-fixed-slab-fonts

# Iosevka Slab — Monospace, Slab-serif
%files -n iosevka-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-slab-fonts/*

%files -n iosevka-term-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-term-slab-fonts/*

%files -n iosevka-fixed-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/iosevka-fixed-slab-fonts/*

%changelog
