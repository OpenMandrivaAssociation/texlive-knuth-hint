%global tl_name knuth-hint
%global tl_revision 78243

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.7
Release:	%{tl_revision}.1
Summary:	HINT collection of typeset C/WEB sources in TeX Live
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/knuth-hint
License:	pd knuth
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth-hint.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/knuth-hint.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The knuth-hint package contains the large collection of HINT documents
for many of the CWEB amd WEB sources of programs in the TeX Live
distribution (and, for technical reasons, a PDF document for XeTeX).
Each program is presented in its original form as written by the
respective authors, and in the "changed" form as used in TeX Live. Care
has been taken to keep the section numbering intact, so that you can
study the codes and the changes in parallel. Also included are the
"errata" for Donald Knuth's "Computers & Typesetting". HINT is the
dynamic document format created by Martin Ruckert's HiTeX engine that
was added to TeX Live 2022. The HINT files can be viewed on Linux,
Windows, and Android with the hintview application. The knuth-hint
package is a showcase of HiTeX's capabilities.

