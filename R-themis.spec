#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-themis
Version  : 0.1.4
Release  : 3
URL      : https://cran.r-project.org/src/contrib/themis_0.1.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/themis_0.1.4.tar.gz
Summary  : Extra Recipes Steps for Dealing with Unbalanced Data
Group    : Development/Tools
License  : MIT
Requires: R-RANN
Requires: R-ROSE
Requires: R-dplyr
Requires: R-generics
Requires: R-purrr
Requires: R-recipes
Requires: R-rlang
Requires: R-tibble
Requires: R-unbalanced
Requires: R-withr
BuildRequires : R-RANN
BuildRequires : R-ROSE
BuildRequires : R-dplyr
BuildRequires : R-generics
BuildRequires : R-modeldata
BuildRequires : R-purrr
BuildRequires : R-recipes
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-unbalanced
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
class is said to be unbalanced. Many models produce a subpar
    performance on unbalanced datasets. A dataset can be balanced by
    increasing the number of minority cases using SMOTE 2011

%prep
%setup -q -c -n themis
cd %{_builddir}/themis

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641137748

%install
export SOURCE_DATE_EPOCH=1641137748
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library themis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library themis
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library themis
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc themis || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/themis/DESCRIPTION
/usr/lib64/R/library/themis/INDEX
/usr/lib64/R/library/themis/LICENSE
/usr/lib64/R/library/themis/Meta/Rd.rds
/usr/lib64/R/library/themis/Meta/data.rds
/usr/lib64/R/library/themis/Meta/features.rds
/usr/lib64/R/library/themis/Meta/hsearch.rds
/usr/lib64/R/library/themis/Meta/links.rds
/usr/lib64/R/library/themis/Meta/nsInfo.rds
/usr/lib64/R/library/themis/Meta/package.rds
/usr/lib64/R/library/themis/NAMESPACE
/usr/lib64/R/library/themis/NEWS.md
/usr/lib64/R/library/themis/R/themis
/usr/lib64/R/library/themis/R/themis.rdb
/usr/lib64/R/library/themis/R/themis.rdx
/usr/lib64/R/library/themis/data/Rdata.rdb
/usr/lib64/R/library/themis/data/Rdata.rds
/usr/lib64/R/library/themis/data/Rdata.rdx
/usr/lib64/R/library/themis/help/AnIndex
/usr/lib64/R/library/themis/help/aliases.rds
/usr/lib64/R/library/themis/help/figures/README-unnamed-chunk-2-1.png
/usr/lib64/R/library/themis/help/figures/README-unnamed-chunk-3-1.png
/usr/lib64/R/library/themis/help/figures/README-unnamed-chunk-4-1.png
/usr/lib64/R/library/themis/help/figures/README-unnamed-chunk-5-1.png
/usr/lib64/R/library/themis/help/figures/README-unnamed-chunk-6-1.png
/usr/lib64/R/library/themis/help/paths.rds
/usr/lib64/R/library/themis/help/themis.rdb
/usr/lib64/R/library/themis/help/themis.rdx
/usr/lib64/R/library/themis/html/00Index.html
/usr/lib64/R/library/themis/html/R.css
/usr/lib64/R/library/themis/tests/testthat.R
/usr/lib64/R/library/themis/tests/testthat/helper-test-functions.R
/usr/lib64/R/library/themis/tests/testthat/test-S3-methods.R
/usr/lib64/R/library/themis/tests/testthat/test-adasyn.R
/usr/lib64/R/library/themis/tests/testthat/test-adasyn_impl.R
/usr/lib64/R/library/themis/tests/testthat/test-bsmote.R
/usr/lib64/R/library/themis/tests/testthat/test-bsmote_impl.R
/usr/lib64/R/library/themis/tests/testthat/test-downsample.R
/usr/lib64/R/library/themis/tests/testthat/test-nearmiss.R
/usr/lib64/R/library/themis/tests/testthat/test-rose.R
/usr/lib64/R/library/themis/tests/testthat/test-smote.R
/usr/lib64/R/library/themis/tests/testthat/test-smote_impl.R
/usr/lib64/R/library/themis/tests/testthat/test-tomek.R
/usr/lib64/R/library/themis/tests/testthat/test-upsample.R
