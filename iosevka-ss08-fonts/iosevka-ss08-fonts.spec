%global         source_name Iosevka
%global         debug_package %{nil}
%global         name_base IosevkaSS08
%global         name_term IosevkaTermSS08
%global         name_fixed IosevkaFixedSS08

Name:           iosevka-ss08-fonts
Version:        30.2.0
Release:        1%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Pragmata Pro Style)

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/releases/download/v%{version}/SuperTTC-SGr-%{name_base}-%{version}.zip
Source1:        %{url}/releases/download/v%{version}/SuperTTC-SGr-%{name_term}-%{version}.zip
Source2:        %{url}/releases/download/v%{version}/SuperTTC-SGr-%{name_fixed}-%{version}.zip
Source10:       %{url}/raw/v%{version}/LICENSE.md
Source11:       %{url}/raw/v%{version}/README.md
Source12:       %{url}/raw/v%{version}/CHANGELOG.md

BuildArch:      noarch

BuildRequires:  unzip


%description
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%prep
for s in %{_sourcedir}/*.zip; do
	unzip -qq $s '*.ttc'
done
cp %{SOURCE10} %{SOURCE11} %{SOURCE12} .


%build
# Nothing here


%install
%{__install} -D -m 0644 SGr-%{name_base}.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name_base}.ttc
%{__install} -D -m 0644 SGr-%{name_term}.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name_term}.ttc
%{__install} -D -m 0644 SGr-%{name_fixed}.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name_fixed}.ttc


%files
%license LICENSE.md
%doc {README,CHANGELOG}.md
%{_datadir}/fonts/%{name}


%changelog
%autochangelog
