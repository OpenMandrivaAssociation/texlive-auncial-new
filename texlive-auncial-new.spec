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
BuildSystem:	texlive
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

