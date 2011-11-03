# revision 22384
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-ieee
# catalog-date 2011-05-09 16:52:20 +0200
# catalog-license lppl1.3
# catalog-version 1.0b
Name:		texlive-biblatex-ieee
Version:	1.0b
Release:	1
Summary:	Ieee style files for biblatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-ieee
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ieee.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-ieee.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This is a biblatex style that implements the bibliography style
of the IEEE for biblatex. The implementation follows standard
biblatex conventions, and can be used simply by loading
biblatex with the appropriate option:
\usepackage[style=ieee]{biblatex} A demonstration database is
provided to show how to format input for the style. The present
release is believed to be usable, but work is needed to confirm
that it is of production quality. (In particular, the release
does not yet exploit the facilities of biblatex version 1.2 to
the full.).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/biblatex-ieee/biblatex-ieee.bib
%{_texmfdistdir}/tex/latex/biblatex-ieee/ieee.bbx
%{_texmfdistdir}/tex/latex/biblatex-ieee/ieee.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-ieee/README
%doc %{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
