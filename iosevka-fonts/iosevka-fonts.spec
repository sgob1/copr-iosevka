%global         source_name Iosevka
%global         debug_package %{nil}
%global         name_term iosevka-term
%global         name_fixed iosevka-fixed

Name:           iosevka
Version:        27.3.5
Release:        1%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Default)

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/releases/download/v%{version}/super-ttc-sgr-%{name}-%{version}.zip
Source1:        %{url}/releases/download/v%{version}/super-ttc-sgr-%{name_term}-%{version}.zip
Source2:        %{url}/releases/download/v%{version}/super-ttc-sgr-%{name_fixed}-%{version}.zip
Source10:      https://github.com/be5invis/Iosevka/raw/v%{version}/LICENSE.md
Source11:      https://github.com/be5invis/Iosevka/raw/v%{version}/README.md
Source12:      https://github.com/be5invis/Iosevka/raw/v%{version}/CHANGELOG.md

BuildArch:      noarch

BuildRequires:  unzip


%description
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fonts
Summary:        Slender typeface for code, from code (Monospace, Default)
%description -n iosevka-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-term-fonts
Summary:        Slender typeface for code, from code (Monospace, Default)
%description -n iosevka-term-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fixed-fonts
Summary:        Slender typeface for code, from code (Monospace, Default)
%description -n iosevka-fixed-fonts
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
%{__install} -D -m 0644 sgr-%{name_term}.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name_term}.ttc
%{__install} -D -m 0644 sgr-%{name_fixed}.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name_fixed}.ttc


# Iosevka — Monospace, Default
%files -n %{name}-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}/%{name}.ttc


%files -n %{name_term}-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}/%{name_term}.ttc


%files -n %{name_fixed}-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}/%{name_fixed}.ttc


%changelog
%autochangelog
