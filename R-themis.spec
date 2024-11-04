#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
#
Name     : R-themis
Version  : 1.0.2
Release  : 19
URL      : https://cran.r-project.org/src/contrib/themis_1.0.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/themis_1.0.2.tar.gz
Summary  : Extra Recipes Steps for Dealing with Unbalanced Data
Group    : Development/Tools
License  : MIT
Requires: R-RANN
Requires: R-ROSE
Requires: R-dplyr
Requires: R-generics
Requires: R-glue
Requires: R-gower
Requires: R-hardhat
Requires: R-lifecycle
Requires: R-purrr
Requires: R-recipes
Requires: R-rlang
Requires: R-tibble
Requires: R-vctrs
Requires: R-withr
BuildRequires : R-RANN
BuildRequires : R-ROSE
BuildRequires : R-dplyr
BuildRequires : R-generics
BuildRequires : R-glue
BuildRequires : R-gower
BuildRequires : R-hardhat
BuildRequires : R-lifecycle
BuildRequires : R-modeldata
BuildRequires : R-purrr
BuildRequires : R-recipes
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-vctrs
BuildRequires : R-withr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
said to be unbalanced. Many models produce a subpar performance on
    unbalanced datasets. A dataset can be balanced by increasing the

%prep
%setup -q -n themis
pushd ..
cp -a themis buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692061161

%install
export SOURCE_DATE_EPOCH=1692061161
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
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/themis/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/themis/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/themis/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/themis/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/themis/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/themis/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/themis/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/themis/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/themis/help/figures/logo.png
/usr/lib64/R/library/themis/help/paths.rds
/usr/lib64/R/library/themis/help/themis.rdb
/usr/lib64/R/library/themis/help/themis.rdx
/usr/lib64/R/library/themis/html/00Index.html
/usr/lib64/R/library/themis/html/R.css
/usr/lib64/R/library/themis/tests/testthat.R
/usr/lib64/R/library/themis/tests/testthat/_snaps/adasyn.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/adasyn_impl.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/bsmote.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/bsmote_impl.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/downsample.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/extension_check.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/nearmiss.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/rose.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/smote.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/smote_impl.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/smotenc.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/tomek.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/tomek_impl.md
/usr/lib64/R/library/themis/tests/testthat/_snaps/upsample.md
/usr/lib64/R/library/themis/tests/testthat/test-S3-methods.R
/usr/lib64/R/library/themis/tests/testthat/test-adasyn.R
/usr/lib64/R/library/themis/tests/testthat/test-adasyn_impl.R
/usr/lib64/R/library/themis/tests/testthat/test-bsmote.R
/usr/lib64/R/library/themis/tests/testthat/test-bsmote_impl.R
/usr/lib64/R/library/themis/tests/testthat/test-downsample.R
/usr/lib64/R/library/themis/tests/testthat/test-extension_check.R
/usr/lib64/R/library/themis/tests/testthat/test-nearmiss.R
/usr/lib64/R/library/themis/tests/testthat/test-rose.R
/usr/lib64/R/library/themis/tests/testthat/test-smote.R
/usr/lib64/R/library/themis/tests/testthat/test-smote_impl.R
/usr/lib64/R/library/themis/tests/testthat/test-smotenc.R
/usr/lib64/R/library/themis/tests/testthat/test-tomek.R
/usr/lib64/R/library/themis/tests/testthat/test-tomek_impl.R
/usr/lib64/R/library/themis/tests/testthat/test-upsample.R
/usr/lib64/R/library/themis/tests/testthat/testthat-problems.rds
