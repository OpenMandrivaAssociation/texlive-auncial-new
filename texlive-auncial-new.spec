# revision 15878
# category Package
# catalog-ctan /fonts/auncial-new
# catalog-date 2008-08-16 20:32:59 +0200
# catalog-license lppl
# catalog-version 2.0
Name:		texlive-auncial-new
Version:	2.0
Release:	4
Summary:	Artificial Uncial font and LaTeX support macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/auncial-new
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auncial-new.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auncial-new.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/auncial-new.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The auncial-new bundle provides packages and fonts for a script
based on the Artificial Uncial manuscript book-hand used
between the 6th & 10th century AD. The script consists of
minuscules and digits, with some appropriate period punctuation
marks. Both normal and bold versions are provided, and the font
is distributed in Adobe Type 1 format. This is an experimental
new version of the auncial bundle, which is one of a series of
bookhand fonts. The font follows the B1 encoding developed for
bookhands. Access to the encoding is essential. The encoding
mainly follows the standard T1 encoding.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/auncial-new/auncl10.afm
%{_texmfdistdir}/fonts/afm/public/auncial-new/aunclb10.afm
%{_texmfdistdir}/fonts/map/dvips/auncial-new/auncial.map
%{_texmfdistdir}/fonts/tfm/public/auncial-new/auncl10.tfm
%{_texmfdistdir}/fonts/tfm/public/auncial-new/aunclb10.tfm
%{_texmfdistdir}/fonts/type1/public/auncial-new/auncl10.pfb
%{_texmfdistdir}/fonts/type1/public/auncial-new/aunclb10.pfb
%{_texmfdistdir}/tex/latex/auncial-new/allauncl.sty
%{_texmfdistdir}/tex/latex/auncial-new/auncial.sty
%{_texmfdistdir}/tex/latex/auncial-new/b1auncl.fd
%doc %{_texmfdistdir}/doc/fonts/auncial-new/README
%doc %{_texmfdistdir}/doc/fonts/auncial-new/auncial.pdf
%doc %{_texmfdistdir}/doc/fonts/auncial-new/tryauncial.pdf
%doc %{_texmfdistdir}/doc/fonts/auncial-new/tryauncial.tex
#- source
%doc %{_texmfdistdir}/source/fonts/auncial-new/auncial.dtx
%doc %{_texmfdistdir}/source/fonts/auncial-new/auncial.ins
%doc %{_texmfdistdir}/source/fonts/auncial-new/aunclmfb.dtx
%doc %{_texmfdistdir}/source/fonts/auncial-new/aunclmfc.dtx
%doc %{_texmfdistdir}/source/fonts/auncial-new/aunclmft.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.0-2
+ Revision: 749422
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.0-1
+ Revision: 717868
- texlive-auncial-new
- texlive-auncial-new
- texlive-auncial-new
- texlive-auncial-new
- texlive-auncial-new

