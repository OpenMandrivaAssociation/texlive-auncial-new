%global tl_name auncial-new
%global tl_revision 79618
%global tl_version 2.0

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Artificial Uncial font and LaTeX support macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/auncial-new
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auncial-new.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auncial-new.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/auncial-new.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

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


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from auncial-new:
Map auncial.map
TL_DROPIN_EOF
