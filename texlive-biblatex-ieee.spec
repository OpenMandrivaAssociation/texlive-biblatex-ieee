# revision 27972
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-ieee
# catalog-date 2012-10-12 11:24:08 +0200
# catalog-license lppl1.3
# catalog-version 1.1d
Name:		texlive-biblatex-ieee
Version:	1.1d
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
%{_texmfdistdir}/tex/latex/biblatex-ieee/ieee-alphabetic.bbx
%{_texmfdistdir}/tex/latex/biblatex-ieee/ieee-alphabetic.cbx
%{_texmfdistdir}/tex/latex/biblatex-ieee/ieee.bbx
%{_texmfdistdir}/tex/latex/biblatex-ieee/ieee.cbx
%doc %{_texmfdistdir}/doc/latex/biblatex-ieee/README
%doc %{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee-alphabetic.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee-alphabetic.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-ieee/biblatex-ieee.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Fri Oct 26 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1d-1
+ Revision: 819879
- Update to latest release.

* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1b-1
+ Revision: 812037
- Update to latest release.

* Mon Jun 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 804495
- Update to latest release.

* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0d-1
+ Revision: 790538
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0b-2
+ Revision: 749639
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0b-1
+ Revision: 717926
- texlive-biblatex-ieee
- texlive-biblatex-ieee
- texlive-biblatex-ieee
- texlive-biblatex-ieee
- texlive-biblatex-ieee

