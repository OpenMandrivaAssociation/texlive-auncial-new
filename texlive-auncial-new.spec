%global tl_name auncial-new
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Artificial Uncial font and LaTeX support macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/auncial-new
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auncial-new.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auncial-new.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auncial-new.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The auncial-new bundle provides packages and fonts for a script based on
the Artificial Uncial manuscript book-hand used between the 6th & 10th
century AD. The script consists of minuscules and digits, with some
appropriate period punctuation marks. Both normal and bold versions are
provided, and the font is distributed in Adobe Type 1 format. This is an
experimental new version of the auncial bundle, which is one of a series
of bookhand fonts. The font follows the B1 encoding developed for
bookhands. Access to the encoding is essential. The encoding mainly
follows the standard T1 encoding.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/source/fonts
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/auncial-new
%dir %{_datadir}/texmf-dist/fonts/afm/public
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/source/fonts/auncial-new
%dir %{_datadir}/texmf-dist/tex/latex/auncial-new
%dir %{_datadir}/texmf-dist/fonts/afm/public/auncial-new
%dir %{_datadir}/texmf-dist/fonts/map/dvips/auncial-new
%dir %{_datadir}/texmf-dist/fonts/tfm/public/auncial-new
%dir %{_datadir}/texmf-dist/fonts/type1/public/auncial-new
%doc %{_datadir}/texmf-dist/doc/fonts/auncial-new/README
%doc %{_datadir}/texmf-dist/doc/fonts/auncial-new/auncial.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/auncial-new/tryauncial.pdf
%doc %{_datadir}/texmf-dist/doc/fonts/auncial-new/tryauncial.tex
%{_datadir}/texmf-dist/fonts/afm/public/auncial-new/auncl10.afm
%{_datadir}/texmf-dist/fonts/afm/public/auncial-new/aunclb10.afm
%{_datadir}/texmf-dist/fonts/map/dvips/auncial-new/auncial.map
%{_datadir}/texmf-dist/fonts/tfm/public/auncial-new/auncl10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/auncial-new/aunclb10.tfm
%{_datadir}/texmf-dist/fonts/type1/public/auncial-new/auncl10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/auncial-new/aunclb10.pfb
%doc %{_datadir}/texmf-dist/source/fonts/auncial-new/auncial.dtx
%doc %{_datadir}/texmf-dist/source/fonts/auncial-new/auncial.ins
%doc %{_datadir}/texmf-dist/source/fonts/auncial-new/aunclmfb.dtx
%doc %{_datadir}/texmf-dist/source/fonts/auncial-new/aunclmfc.dtx
%doc %{_datadir}/texmf-dist/source/fonts/auncial-new/aunclmft.dtx
%{_datadir}/texmf-dist/tex/latex/auncial-new/allauncl.sty
%{_datadir}/texmf-dist/tex/latex/auncial-new/auncial.sty
%{_datadir}/texmf-dist/tex/latex/auncial-new/b1auncl.fd
