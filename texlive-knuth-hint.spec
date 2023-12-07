Name:		texlive-knuth-hint
Version:	67373
Release:	1
Summary:	HINT collection of typeset C/WEB sources in TeX Live
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/knuth-hint
License:	pd knuth
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth-hint.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth-hint.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The knuth-hint package contains the large collection of HINT
documents for many of the CWEB amd WEB sources of programs in
the TeX Live distribution (and, for technical reasons, PDF
documents for CTWILL and XeTeX). Each program is presented in
its original form as written by the respective authors, and in
the "changed" form as used in TeX Live. Care has been taken to
keep the section numbering intact, so that you can study the
codes and the changes in parallel. Also included are the
"errata" for Donald Knuth's "Computers & Typesetting". HINT is
the dynamic document format created by Martin Ruckert's HiTeX
engine that was added to TeX Live 2022. The HINT files can be
viewed on Linux, Windows, and Android with the hintview
application. The knuth-hint package is a showcase of HiTeX's
capabilities.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/doc/generic/knuth-hint

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
