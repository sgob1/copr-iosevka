%global         source_name Iosevka
%global         debug_package %{nil}

Name:           iosevka-curly-slab
Version:        27.3.5
Release:        1%{?dist}
Summary:        Slender typeface for code, from code (Monospace, Curly Style, Slab-serif)

License:        SIL Open Font License Version 1.1
URL:            https://github.com/be5invis/Iosevka
Source0:        %{url}/releases/download/v%{version}/super-ttc-sgr-%{name}-%{version}.zip
Source1:        %{url}/releases/download/v%{version}/super-ttc-sgr-iosevka-term-curly-slab-%{version}.zip
Source2:        %{url}/releases/download/v%{version}/super-ttc-sgr-iosevka-fixed-curly-slab-%{version}.zip
Source10:      https://github.com/be5invis/Iosevka/raw/v%{version}/LICENSE.md
Source11:      https://github.com/be5invis/Iosevka/raw/v%{version}/README.md
Source12:      https://github.com/be5invis/Iosevka/raw/v%{version}/CHANGELOG.md

BuildArch:      noarch

BuildRequires:  unzip


%description
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-curly-slab-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style, Slab-serif)
%description -n iosevka-curly-slab-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-term-curly-slab-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style, Slab-serif)
%description -n iosevka-term-curly-slab-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace +
quasi‑proportional typeface family, designed for writing code, using in
terminals, and preparing technical documents.


%package -n iosevka-fixed-curly-slab-fonts
Summary:        Slender typeface for code, from code (Monospace, Curly Style, Slab-serif)
%description -n iosevka-fixed-curly-slab-fonts
Iosevka is an open-source, sans-serif + slab-serif, monospace + quasi‑proportional typeface family, designed for writing code, using in terminals, and preparing technical documents.


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
%{__install} -D -m 0644 sgr-iosevka-term-curly-slab.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name}-term.ttc
%{__install} -D -m 0644 sgr-iosevka-fixed-curly-slab.ttc %{buildroot}%{_datadir}/fonts/%{name}/%{name}-fixed.ttc

# Iosevka Curly Slab — Monospace, Curly Style, Slab-serif
%files -n iosevka-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}/%{name}.ttc


%files -n iosevka-term-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}/%{name}-term.ttc


%files -n iosevka-fixed-curly-slab-fonts
%license LICENSE.md
%doc README.md
%{_datadir}/fonts/%{name}/%{name}-fixed.ttc


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
