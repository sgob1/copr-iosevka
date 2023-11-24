%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-aile
Version:        27.3.5
Release:        1%{?dist}
Summary:        Slender typeface for code, from code (Quasi-proportional, Sans-serif)

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/releases/download/v%{version}/super-ttc-sgr-%{name}-%{version}.zip
Source10:      https://github.com/be5invis/Iosevka/raw/v%{version}/LICENSE.md
Source11:      https://github.com/be5invis/Iosevka/raw/v%{version}/README.md
Source12:      https://github.com/be5invis/Iosevka/raw/v%{version}/CHANGELOG.md

BuildArch:      noarch

BuildRequires:  unzip


%description
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n %{name}-fonts
Summary:        Slender typeface for code, from code (Quasi-proportional, Sans-serif)
%description -n %{name}-fonts
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
%{__install} -D -m 0644 sgr-%{name}.ttc %{buildroot}%{_datadir}/fonts/%{name}-fonts/%{name}.ttc


# Iosevka Aile - Quasi-proportional, Sans-serif
%files -n %{name}-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}-fonts


%changelog
%autochangelog
