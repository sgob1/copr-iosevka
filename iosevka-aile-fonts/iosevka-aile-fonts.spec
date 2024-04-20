%global         source_name Iosevka
%global         debug_package %{nil}
%global         name_base IosevkaAile

Name:           iosevka-aile-fonts
Version:        29.2.1
Release:        1%{?dist}
Summary:        Slender typeface for code, from code (Quasi-proportional, Sans-serif)

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/releases/download/v%{version}/SuperTTC-%{name_base}-%{version}.zip
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
%autosetup -cT
for s in %{_sourcedir}/*.zip; do
	unzip -qq $s '*.ttc'
done
cp %{SOURCE10} %{SOURCE11} %{SOURCE12} .


%build
# Nothing here


%install
%{__install} -D -m 0644 %{name_base}.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name_base}.ttc


%files
%license LICENSE.md
%doc {README,CHANGELOG}.md
%{_datadir}/fonts/%{name}


%changelog
%autochangelog
