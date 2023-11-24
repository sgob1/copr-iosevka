%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-curly
Version:        27.3.5
Release:        1%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Curly Style)

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/releases/download/v%{version}/super-ttc-sgr-%{name}-%{version}.zip
Source1:        %{url}/releases/download/v%{version}/super-ttc-sgr-iosevka-term-curly-%{version}.zip
Source2:        %{url}/releases/download/v%{version}/super-ttc-sgr-iosevka-fixed-curly-%{version}.zip
Source10:      https://github.com/be5invis/Iosevka/raw/v%{version}/LICENSE.md
Source11:      https://github.com/be5invis/Iosevka/raw/v%{version}/README.md
Source12:      https://github.com/be5invis/Iosevka/raw/v%{version}/CHANGELOG.md

BuildArch:      noarch

BuildRequires:  unzip


%description
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-curly-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style)
%description -n iosevka-curly-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-term-curly-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style)
%description -n iosevka-term-curly-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fixed-curly-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style)
%description -n iosevka-fixed-curly-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%prep
%autosetup -cT
for s in %{_sourcedir}/*.zip; do
	unzip -qq $s '*.ttc'
done
cp %{SOURCE10} %{SOURCE11} %{SOURCE12} .


%build
# Nothing here


%install
%{__install} -D -m 0644 sgr-%{name}.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name}.ttc
%{__install} -D -m 0644 sgr-iosevka-term-curly.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name}-term.ttc
%{__install} -D -m 0644 sgr-iosevka-fixed-curly.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name}-fixed.ttc

# Iosevka Curly — Monospace, Curly Style
%files -n iosevka-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}/%{name}.ttc


%files -n iosevka-term-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}/%{name}-term.ttc


%files -n iosevka-fixed-curly-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}/%{name}-fixed.ttc


%changelog
%autochangelog
