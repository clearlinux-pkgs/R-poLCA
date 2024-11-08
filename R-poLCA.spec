#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-poLCA
Version  : 1.6.0.1
Release  : 44
URL      : https://cran.r-project.org/src/contrib/poLCA_1.6.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/poLCA_1.6.0.1.tar.gz
Summary  : Polytomous Variable Latent Class Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-poLCA-lib = %{version}-%{release}
Requires: R-scatterplot3d
BuildRequires : R-scatterplot3d
BuildRequires : buildreq-R

%description
for polytomous outcome variables.  Also known as latent structure analysis.

%package lib
Summary: lib components for the R-poLCA package.
Group: Libraries

%description lib
lib components for the R-poLCA package.


%prep
%setup -q -c -n poLCA
cd %{_builddir}/poLCA

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650901214

%install
export SOURCE_DATE_EPOCH=1650901214
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library poLCA
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library poLCA
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library poLCA
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc poLCA || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/poLCA/CITATION
/usr/lib64/R/library/poLCA/DESCRIPTION
/usr/lib64/R/library/poLCA/INDEX
/usr/lib64/R/library/poLCA/Meta/Rd.rds
/usr/lib64/R/library/poLCA/Meta/data.rds
/usr/lib64/R/library/poLCA/Meta/features.rds
/usr/lib64/R/library/poLCA/Meta/hsearch.rds
/usr/lib64/R/library/poLCA/Meta/links.rds
/usr/lib64/R/library/poLCA/Meta/nsInfo.rds
/usr/lib64/R/library/poLCA/Meta/package.rds
/usr/lib64/R/library/poLCA/NAMESPACE
/usr/lib64/R/library/poLCA/R/poLCA
/usr/lib64/R/library/poLCA/R/poLCA.rdb
/usr/lib64/R/library/poLCA/R/poLCA.rdx
/usr/lib64/R/library/poLCA/data/carcinoma.rda
/usr/lib64/R/library/poLCA/data/cheating.rda
/usr/lib64/R/library/poLCA/data/election.rda
/usr/lib64/R/library/poLCA/data/gss82.rda
/usr/lib64/R/library/poLCA/data/values.rda
/usr/lib64/R/library/poLCA/doc/index.html
/usr/lib64/R/library/poLCA/doc/poLCA-manual-1-4.pdf
/usr/lib64/R/library/poLCA/doc/poLCA-manual-example.R
/usr/lib64/R/library/poLCA/help/AnIndex
/usr/lib64/R/library/poLCA/help/aliases.rds
/usr/lib64/R/library/poLCA/help/paths.rds
/usr/lib64/R/library/poLCA/help/poLCA.rdb
/usr/lib64/R/library/poLCA/help/poLCA.rdx
/usr/lib64/R/library/poLCA/html/00Index.html
/usr/lib64/R/library/poLCA/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/poLCA/libs/poLCA.so
/usr/lib64/R/library/poLCA/libs/poLCA.so.avx2
/usr/lib64/R/library/poLCA/libs/poLCA.so.avx512
