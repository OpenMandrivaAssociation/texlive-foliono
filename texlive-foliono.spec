Name:		texlive-foliono
Version:	58877
Release:	1
Summary:	Use folio numbers to replace page numbers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/foliono
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foliono.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foliono.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package adds functionality to create several styles of
folio numbers. Folio numbering preceded the modern page
numbering convention and was in common use until the 18th
century. In folio numbering the numbers are placed only on odd
(right-side) pages and the numbers typically comprise of two
parts: quire and folio numbers. The intended use for this
package is to help creating old-style books.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/foliono
%doc %{_texmfdistdir}/doc/latex/foliono

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
