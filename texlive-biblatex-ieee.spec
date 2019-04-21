Name:		texlive-biblatex-ieee
Version:	1.3
Release:	1
Summary:	Ieee style files for biblatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-ieee
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ieee.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ieee.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a biblatex style that implements the bibliography style
of the IEEE for biblatex. The implementation follows standard
biblatex conventions, and can be used simply by loading
biblatex with the appropriate option:
\usepackage[style=ieee]{biblatex} A demonstration database is
provided to show how to format input for the style.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-ieee
%doc %{_texmfdistdir}/doc/latex/biblatex-ieee

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
