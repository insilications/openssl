#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD9C4D26D0E604491 (matt@openssl.org)
#
%define keepstatic 1
Name     : openssl
Version  : 1.1.1g
Release  : 99
URL      : https://www.openssl.org/source/openssl-1.1.1g.tar.gz
Source0  : https://www.openssl.org/source/openssl-1.1.1g.tar.gz
Source1  : https://www.openssl.org/source/openssl-1.1.1g.tar.gz.asc
Summary  : unknown
Group    : Development/Tools
License  : BSD-2-Clause
Requires: openssl-bin = %{version}-%{release}
Requires: openssl-data = %{version}-%{release}
Requires: openssl-lib = %{version}-%{release}
Requires: ca-certs
Requires: ca-certs-static
Requires: p11-kit
BuildRequires : buildreq-configure
BuildRequires : buildreq-cpan
BuildRequires : buildreq-qmake
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : p11-kit
BuildRequires : perl(Test::More)
BuildRequires : pkgconfig(zlib)
BuildRequires : util-linux-bin
BuildRequires : util-linux-extras
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Use-clearlinux-CFLAGS-during-build.patch
Patch2: 0002-Hide-a-symbol-from-Steam.patch
Patch3: 0003-Use-OS-provided-copy-of-openssl.cnf-as-fallback.patch

%description
OpenSSL 1.1.1g 21 Apr 2020
All rights reserved.
DESCRIPTION
-----------
The OpenSSL Project is a collaborative effort to develop a robust,
commercial-grade, fully featured, and Open Source toolkit implementing the
Transport Layer Security (TLS) protocols (including SSLv3) as well as a
full-strength general purpose cryptographic library.

%package bin
Summary: bin components for the openssl package.
Group: Binaries
Requires: openssl-data = %{version}-%{release}

%description bin
bin components for the openssl package.


%package data
Summary: data components for the openssl package.
Group: Data

%description data
data components for the openssl package.


%package dev
Summary: dev components for the openssl package.
Group: Development
Requires: openssl-lib = %{version}-%{release}
Requires: openssl-bin = %{version}-%{release}
Requires: openssl-data = %{version}-%{release}
Provides: openssl-devel = %{version}-%{release}
Requires: openssl = %{version}-%{release}

%description dev
dev components for the openssl package.


%package dev32
Summary: dev32 components for the openssl package.
Group: Default
Requires: openssl-lib32 = %{version}-%{release}
Requires: openssl-bin = %{version}-%{release}
Requires: openssl-data = %{version}-%{release}
Requires: openssl-dev = %{version}-%{release}

%description dev32
dev32 components for the openssl package.


%package lib
Summary: lib components for the openssl package.
Group: Libraries
Requires: openssl-data = %{version}-%{release}

%description lib
lib components for the openssl package.


%package lib32
Summary: lib32 components for the openssl package.
Group: Default
Requires: openssl-data = %{version}-%{release}

%description lib32
lib32 components for the openssl package.


%package staticdev
Summary: staticdev components for the openssl package.
Group: Default
Requires: openssl-dev = %{version}-%{release}

%description staticdev
staticdev components for the openssl package.


%package staticdev32
Summary: staticdev32 components for the openssl package.
Group: Default
Requires: openssl-dev = %{version}-%{release}

%description staticdev32
staticdev32 components for the openssl package.


%prep
%setup -q -n openssl-1.1.1g
cd %{_builddir}/openssl-1.1.1g
%patch1 -p1
%patch2 -p1
%patch3 -p1
pushd ..
cp -a openssl-1.1.1g build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598741598
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fsemantic-interposition -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -pipe -fPIC -ffat-lto-objects -falign-loops=32 -ffunction-sections $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fsemantic-interposition -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -pipe -fPIC -ffat-lto-objects -falign-loops=32 -ffunction-sections $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fsemantic-interposition -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -pipe -fPIC -ffat-lto-objects -falign-loops=32 -ffunction-sections $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fsemantic-interposition -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -pipe -fPIC -ffat-lto-objects -falign-loops=32 -ffunction-sections $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -fsemantic-interposition -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -pipe -fPIC -ffat-lto-objects -falign-loops=32 -ffunction-sections $PGO_GEN"
## pgo use
## -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden  -ffat-lto-objects
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fsemantic-interposition -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wno-error -pipe -fPIC -ffat-lto-objects -falign-loops=32 -ffunction-sections $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fsemantic-interposition -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wno-error -pipe -fPIC -ffat-lto-objects -falign-loops=32 -ffunction-sections $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fsemantic-interposition -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wno-error -pipe -fPIC -ffat-lto-objects -falign-loops=32 -ffunction-sections $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fsemantic-interposition -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wno-error -pipe -fPIC -ffat-lto-objects -falign-loops=32 -ffunction-sections $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fsemantic-interposition -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -mtls-dialect=gnu2 -Wno-error -pipe -fPIC -ffat-lto-objects -falign-loops=32 -ffunction-sections $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#export CCACHE_DISABLE=1
## altflags_pgo end
##
%define _lto_cflags 1
##
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
 ./config no-ssl zlib shared no-rc4 no-ssl2 no-ssl3 --prefix=/usr --openssldir=/etc/ssl --libdir=lib64
## make_prepend content
make depend
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1

LD_PRELOAD="./libcrypto.so ./libssl.so" apps/openssl speed rsa
V=1 VERBOSE=1 make -j16 test || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
./config no-ssl zlib shared no-rc4 no-ssl2 no-ssl3 --prefix=/usr --openssldir=/etc/ssl --libdir=lib64
## make_prepend content
make depend
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1

pushd ../build32/
export CFLAGS="-g -O2 -fuse-linker-plugin -pipe"
export CXXFLAGS="-g -O2 -fuse-linker-plugin -fvisibility-inlines-hidden -pipe"
export LDFLAGS="-g -O2 -fuse-linker-plugin -pipe"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
i386 ./config no-ssl zlib shared no-rc4 no-ssl2 no-ssl3 no-asm --prefix=/usr --openssldir=/etc/ssl --libdir=lib32
## make_prepend content
make depend
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1598741598
rm -rf %{buildroot}
## install_prepend content
export CFLAGS_ORIG="$CFLAGS"
export LDFLAGS_ORIG="$LDFLAGS"
export CXXFLAGS_ORIG="$CXXFLAGS"
## install_prepend end
## install_macro_32 start
pushd ../build32/
export CFLAGS="$CFLAGS_ORIG -m32 -fno-lto -mstackrealign" 
export LDFLAGS="$LDFLAGS_ORIG -m32 -fno-lto -mstackrealign" 
export CXXFLAGS="$CXXFLAGS_ORIG -m32 -fno-lto -mstackrealign" 
V=1 VERBOSE=1 make DESTDIR=%{buildroot} MANDIR=/usr/share/man MANSUFFIX=openssl install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
## install_macro_32 end
## install_macro start
export CFLAGS="$CFLAGS_ORIG -m64 -flto=16" 
export LDFLAGS="$LDFLAGS_ORIG -m64 -flto=16" 
export CXXFLAGS="$CXXFLAGS_ORIG -m64 -flto=16" 
V=1 VERBOSE=1 make DESTDIR=%{buildroot} MANDIR=/usr/share/man MANSUFFIX=openssl install
## install_macro end
## install_append content
install -D -m0644 apps/openssl.cnf %{buildroot}/usr/share/defaults/ssl/openssl.cnf
rm -rf %{buildroot}/etc/ssl
rm -rf %{buildroot}/usr/share/doc/openssl/html
rm -rf %{buildroot}/usr/share/man/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/c_rehash
/usr/bin/openssl

%files data
%defattr(-,root,root,-)
/usr/share/defaults/ssl/openssl.cnf

%files dev
%defattr(-,root,root,-)
/usr/include/openssl/aes.h
/usr/include/openssl/asn1.h
/usr/include/openssl/asn1_mac.h
/usr/include/openssl/asn1err.h
/usr/include/openssl/asn1t.h
/usr/include/openssl/async.h
/usr/include/openssl/asyncerr.h
/usr/include/openssl/bio.h
/usr/include/openssl/bioerr.h
/usr/include/openssl/blowfish.h
/usr/include/openssl/bn.h
/usr/include/openssl/bnerr.h
/usr/include/openssl/buffer.h
/usr/include/openssl/buffererr.h
/usr/include/openssl/camellia.h
/usr/include/openssl/cast.h
/usr/include/openssl/cmac.h
/usr/include/openssl/cms.h
/usr/include/openssl/cmserr.h
/usr/include/openssl/comp.h
/usr/include/openssl/comperr.h
/usr/include/openssl/conf.h
/usr/include/openssl/conf_api.h
/usr/include/openssl/conferr.h
/usr/include/openssl/crypto.h
/usr/include/openssl/cryptoerr.h
/usr/include/openssl/ct.h
/usr/include/openssl/cterr.h
/usr/include/openssl/des.h
/usr/include/openssl/dh.h
/usr/include/openssl/dherr.h
/usr/include/openssl/dsa.h
/usr/include/openssl/dsaerr.h
/usr/include/openssl/dtls1.h
/usr/include/openssl/e_os2.h
/usr/include/openssl/ebcdic.h
/usr/include/openssl/ec.h
/usr/include/openssl/ecdh.h
/usr/include/openssl/ecdsa.h
/usr/include/openssl/ecerr.h
/usr/include/openssl/engine.h
/usr/include/openssl/engineerr.h
/usr/include/openssl/err.h
/usr/include/openssl/evp.h
/usr/include/openssl/evperr.h
/usr/include/openssl/hmac.h
/usr/include/openssl/idea.h
/usr/include/openssl/kdf.h
/usr/include/openssl/kdferr.h
/usr/include/openssl/lhash.h
/usr/include/openssl/md2.h
/usr/include/openssl/md4.h
/usr/include/openssl/md5.h
/usr/include/openssl/mdc2.h
/usr/include/openssl/modes.h
/usr/include/openssl/obj_mac.h
/usr/include/openssl/objects.h
/usr/include/openssl/objectserr.h
/usr/include/openssl/ocsp.h
/usr/include/openssl/ocsperr.h
/usr/include/openssl/opensslconf.h
/usr/include/openssl/opensslv.h
/usr/include/openssl/ossl_typ.h
/usr/include/openssl/pem.h
/usr/include/openssl/pem2.h
/usr/include/openssl/pemerr.h
/usr/include/openssl/pkcs12.h
/usr/include/openssl/pkcs12err.h
/usr/include/openssl/pkcs7.h
/usr/include/openssl/pkcs7err.h
/usr/include/openssl/rand.h
/usr/include/openssl/rand_drbg.h
/usr/include/openssl/randerr.h
/usr/include/openssl/rc2.h
/usr/include/openssl/rc4.h
/usr/include/openssl/rc5.h
/usr/include/openssl/ripemd.h
/usr/include/openssl/rsa.h
/usr/include/openssl/rsaerr.h
/usr/include/openssl/safestack.h
/usr/include/openssl/seed.h
/usr/include/openssl/sha.h
/usr/include/openssl/srp.h
/usr/include/openssl/srtp.h
/usr/include/openssl/ssl.h
/usr/include/openssl/ssl2.h
/usr/include/openssl/ssl3.h
/usr/include/openssl/sslerr.h
/usr/include/openssl/stack.h
/usr/include/openssl/store.h
/usr/include/openssl/storeerr.h
/usr/include/openssl/symhacks.h
/usr/include/openssl/tls1.h
/usr/include/openssl/ts.h
/usr/include/openssl/tserr.h
/usr/include/openssl/txt_db.h
/usr/include/openssl/ui.h
/usr/include/openssl/uierr.h
/usr/include/openssl/whrlpool.h
/usr/include/openssl/x509.h
/usr/include/openssl/x509_vfy.h
/usr/include/openssl/x509err.h
/usr/include/openssl/x509v3.h
/usr/include/openssl/x509v3err.h
/usr/lib64/libcrypto.so
/usr/lib64/libssl.so
/usr/lib64/pkgconfig/libcrypto.pc
/usr/lib64/pkgconfig/libssl.pc
/usr/lib64/pkgconfig/openssl.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcrypto.so
/usr/lib32/libssl.so
/usr/lib32/pkgconfig/32libcrypto.pc
/usr/lib32/pkgconfig/32libssl.pc
/usr/lib32/pkgconfig/32openssl.pc
/usr/lib32/pkgconfig/libcrypto.pc
/usr/lib32/pkgconfig/libssl.pc
/usr/lib32/pkgconfig/openssl.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/engines-1.1/afalg.so
/usr/lib64/engines-1.1/capi.so
/usr/lib64/engines-1.1/padlock.so
/usr/lib64/libcrypto.so.1.1
/usr/lib64/libssl.so.1.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/engines-1.1/afalg.so
/usr/lib32/engines-1.1/capi.so
/usr/lib32/engines-1.1/padlock.so
/usr/lib32/libcrypto.so.1.1
/usr/lib32/libssl.so.1.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libcrypto.a
/usr/lib64/libssl.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libcrypto.a
/usr/lib32/libssl.a
