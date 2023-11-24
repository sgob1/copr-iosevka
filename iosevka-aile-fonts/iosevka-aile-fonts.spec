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


%package -n iosevka-aile-fonts
Summary:        Slender typeface for code, from code (Quasi-proportional, Sans-serif)
%description -n iosevka-aile-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%prep
%autosetup -cT
for s in %{_sourcedir}/super-ttc-sgr-%{name}-*.zip; do
	unzip -qq $s '*.ttc'
done
cp %{SOURCE10} %{SOURCE11} %{SOURCE12} .


%build
# Nothing here


%install
%{__install} -D -m 0644 sgr-%{name}.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name}.ttc


# Iosevka Aile - Quasi-proportional, Sans-serif
%files -n iosevka-aile-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}/%{name}.ttc


%changelog
* Sat Nov 11 18:39:05 CET 2023 Marco Sgobino <marco.sgobino@gmail.com> - v27.3.5-1
- Version 27.3.5
* Sat Nov 11 09:49:18 CET 2023 Marco Sgobino <marco.sgobino@gmail.com> - v27.3.4-2
- Version 27.3.4
- Removed clean section
- Removed period in Summary
* Sat Nov 04 14:08:39 CET 2023 Marco Sgobino <marco.sgobino@gmail.com> - v27.3.4-1
- Version 27.3.4
* Fri Nov 03 15:52:45 CET 2023 Marco Sgobino <marco.sgobino@gmail.com> - v27.3.3-4
- Fixed formatting of descriptions
- Introduced new changelog format
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed files specification
* Fri Nov 03 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- Fixed description
* Wed Nov 01 2023 Marco Sgobino <marco.sgobino@gmail.com> - 27.3.3
- First version
