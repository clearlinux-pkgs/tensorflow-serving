Name     : tensorflow-serving
Version  : 2.3.0
Release  : 15
URL      : https://github.com/tensorflow/serving/archive/2.3.0/tensorflow-serving-2.3.0.tar.gz
Source0  : https://github.com/tensorflow/serving/archive/2.3.0/tensorflow-serving-2.3.0.tar.gz
Summary  : Serving system for machine learning models
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : bazel
BuildRequires : buildreq-distutils3
BuildRequires : curl
BuildRequires : gcc9
BuildRequires : gcc9-dev
BuildRequires : git
BuildRequires : numpy
BuildRequires : patch
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : unzip
BuildRequires : virtualenv
BuildRequires : wget
BuildRequires : wheel
BuildRequires : which

# SOURCES BEGIN
Source10: https://github.com/bazelbuild/rules_pkg/releases/download/0.2.5/rules_pkg-0.2.5.tar.gz
Source11: https://github.com/tensorflow/tensorflow/archive/b36436b087bd8e8701ef51718179037cccdfc26e.tar.gz
Source12: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/bazel-toolchains/archive/92dd8a7a518a2fb7ba992d47c8b38299fe0be825.tar.gz
Source13: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_closure/archive/308b05b2419edb5c8ee0471b67a40403df940149.tar.gz
Source14: https://storage.googleapis.com/mirror.tensorflow.org/github.com/grpc/grpc/archive/b54a5b338637f92bfcf4b0bc05e0f57a5fd8fadd.tar.gz
Source15: https://github.com/protocolbuffers/upb/archive/9effcbcb27f0a665f9f345030188c0b291e32482.tar.gz
Source16: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_cc/archive/01d4a48911d5e7591ecb1c06d3b8af47fe872371.zip
Source17: https://mirror.bazel.build/github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip
Source18: https://github.com/bazelbuild/rules_docker/releases/download/v0.14.4/rules_docker-v0.14.4.tar.gz
Source19: https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.21.1/bazel-gazelle-v0.21.1.tar.gz
Source20: https://github.com/bazelbuild/bazel-skylib/archive/1.0.2/bazel-skylib-archive-1.0.2.tar.gz
Source21: https://github.com/bazelbuild/rules_python/archive/dd7f9c5f01bafbfea08c44092b6b0c8fc8fcb77f.tar.gz
Source22: https://storage.googleapis.com/bazel-mirror/github.com/bazelbuild/rules_go/releases/download/v0.23.3/rules_go-v0.23.3.tar.gz
Source23: https://github.com/bazelbuild/rules_pkg/releases/download/0.2.6-1/rules_pkg-0.2.6.tar.gz
Source24: https://github.com/protocolbuffers/protobuf/archive/v3.9.2/protobuf-3.9.2.zip
Source25: https://github.com/tensorflow/text/archive/v2.2.0/text-2.2.0.zip
Source26: https://storage.googleapis.com/mirror.tensorflow.org/github.com/abseil/abseil-cpp/archive/df3ea785d8c30a9503321a3d35ee7d35808f190d.tar.gz
Source27: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_apple/archive/5131f3d46794bf227d296c82f30c2499c9de3c5b.tar.gz
Source28: https://github.com/bazelbuild/bazel-skylib/releases/download/1.0.2/bazel-skylib-1.0.2.tar.gz
Source29: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/re2/archive/506cfa4bffd060c06ec338ce50ea3468daa6c814.tar.gz
Source30: https://github.com/open-source-parsers/jsoncpp/archive/1.9.2/jsoncpp-1.9.2.tar.gz
Source31: https://github.com/libevent/libevent/archive/release-2.1.8-stable/libevent-2.1.8.zip
Source32: https://storage.googleapis.com/mirror.tensorflow.org/zlib.net/zlib-1.2.11.tar.gz
Source33: https://storage.googleapis.com/mirror.tensorflow.org/curl.haxx.se/download/curl-7.69.1.tar.gz
Source34: https://mirror.bazel.build/github.com/bazelbuild/rules_proto/archive/97d8af4dc474595af3900dd85cb3a29ad28cc313.tar.gz
Source35: https://github.com/aws/aws-sdk-cpp/archive/1.7.336/aws-sdk-cpp-1.7.336.tar.gz
Source36: https://github.com/google/nsync/archive/1.22.0/nsync-1.22.0.tar.gz
Source37: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/double-conversion/archive/3992066a95b823efc8ccc1baf82a1cfc73f6e9b8.zip
Source38: https://storage.googleapis.com/mirror.tensorflow.org/gitlab.com/libeigen/eigen/-/archive/386d809bde475c65b7940f290efe80e6a05878c4/eigen-386d809bde475c65b7940f290efe80e6a05878c4.tar.gz
Source39: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/rules_swift/archive/3eeeb53cebda55b349d64c9fc144e18c5f7c0eb8.tar.gz
Source40: https://storage.googleapis.com/mirror.tensorflow.org/github.com/bazelbuild/apple_support/archive/501b4afb27745c4813a88ffa28acd901408014e4.tar.gz
Source41: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/boringssl/archive/80ca9f9f6ece29ab132cce4cf807a9465a18cfac.tar.gz
Source42: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/farmhash/archive/816a4ae622e964763ca0862d9dbd19324a1eaf45.tar.gz
Source43: https://github.com/petewarden/OouraFFT/archive/v1.0/OouraFFT-1.0.tar.gz
Source44: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/highwayhash/archive/fd3d9af80465e4383162e4a7c5e2f406e82dd968.tar.gz
Source45: https://github.com/google/snappy/archive/1.1.8/snappy-1.1.8.tar.gz
Source46: https://github.com/Tencent/rapidjson/archive/v1.1.0/rapidjson-1.1.0.zip
Source47: https://github.com/google/sentencepiece/archive/1.0.0/sentencepiece-1.0.0.zip
Source48: https://storage.googleapis.com/mirror.tensorflow.org/github.com/joe-kuo/sobol_data/archive/835a7d7b1ee3bc83e575e302a985c66ec4b65249.tar.gz
Source49: https://github.com/libjpeg-turbo/libjpeg-turbo/archive/2.0.5/libjpeg-turbo-2.0.5.tar.gz
Source50: https://storage.googleapis.com/mirror.tensorflow.org/pilotfiber.dl.sourceforge.net/project/giflib/giflib-5.2.1.tar.gz
Source51: https://github.com/google/flatbuffers/archive/v1.12.0/flatbuffers-1.12.0.tar.gz
Source52: https://github.com/LMDB/lmdb/archive/LMDB_0.9.22/lmdb-0.9.22.tar.gz
Source53: https://github.com/oneapi-src/oneDNN/archive/v0.21.3/openDNN-0.21.3.tar.gz
Source54: https://github.com/bazelbuild/rules_android/archive/v0.1.1/rules_android-0.1.1.zip
Source55: https://github.com/glennrp/libpng/archive/v1.6.37/libpng-1.6.37.tar.gz
Source56: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/gemmlowp/archive/fda83bdc38b118cc6b56753bd540caa49e570745.zip
Source57: https://storage.googleapis.com/mirror.tensorflow.org/www.sqlite.org/2020/sqlite-amalgamation-3320300.zip
Source58: https://github.com/awslabs/aws-c-common/archive/v0.4.29/aws-c-common-0.4.29.tar.gz
Source59: https://github.com/awslabs/aws-c-event-stream/archive/v0.1.4/aws-c-event-stream-0.1.4.tar.gz
Source60: https://github.com/awslabs/aws-checksums/archive/v0.1.5/aws-checksums-0.1.5.tar.gz
Source61: https://github.com/gflags/gflags/archive/v2.2.1/gflags-2.2.1.tar.gz
Source62: https://mirror.bazel.build/github.com/google/glog/archive/028d37889a1e80e8a07da1b8945ac706259e5fd8.tar.gz
Source63: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/googletest/archive/b6cd405286ed8635ece71c72f118e659f4ade3fb.zip
Source64: https://storage.googleapis.com/mirror.tensorflow.org/github.com/google/ruy/archive/34ea9f4993955fa1ff4eb58e504421806b7f2e8f.zip
Source65: https://storage.googleapis.com/mirror.tensorflow.org/github.com/intel/ARM_NEON_2_x86_SSE/archive/1200fe90bb174a6224a525ee60148671a786a71f.tar.gz
Source66: https://github.com/llvm/llvm-project/archive/7e825abd5704ce28b166f9463d4bd304348fd2a9.tar.gz
Source67: https://storage.googleapis.com/mirror.tensorflow.org/github.com/unicode-org/icu/archive/release-64-2.zip
Source68: https://storage.googleapis.com/mirror.tensorflow.org/www.nasm.us/pub/nasm/releasebuilds/2.13.03/nasm-2.13.03.tar.bz2
Source69: https://storage.googleapis.com/mirror.tensorflow.org/github.com/pytorch/cpuinfo/archive/6cecd15784fcb6c5c0aa7311c6248879ce2cb8b2.zip
Source70: https://storage.googleapis.com/mirror.tensorflow.org/github.com/pytorch/cpuinfo/archive/d5e37adf1406cf899d7d9ec1d317c47506ccb970.tar.gz
# SOURCES END

Patch1 : 0001-Avoid-superfluous-git-clones.patch
Patch2 : 0002-Update-libjpeg-turbo-to-2.0.5.patch

%description
TensorFlow Serving is a flexible, high-performance serving system for machine
learning models, designed for production environments. TensorFlow Serving makes
it easy to deploy new algorithms and experiments, while keeping the same server
architecture and APIs. TensorFlow Serving provides out-of-the-box integration
with TensorFlow models, but can be easily extended to serve other types of
models and data.

%prep
%setup -q -n serving-%{version}
%patch1 -p1
%patch2 -p1

InstallCacheBazel() {
  sha256=$(sha256sum $1 | cut -f1 -d" ")
  mkdir -p /var/tmp/cache/content_addressable/sha256/$sha256
  cp $1 /var/tmp/cache/content_addressable/sha256/$sha256/file
}

# CACHE BAZEL BEGIN
InstallCacheBazel %{SOURCE10}
InstallCacheBazel %{SOURCE11}
InstallCacheBazel %{SOURCE12}
InstallCacheBazel %{SOURCE13}
InstallCacheBazel %{SOURCE14}
InstallCacheBazel %{SOURCE15}
InstallCacheBazel %{SOURCE16}
InstallCacheBazel %{SOURCE17}
InstallCacheBazel %{SOURCE18}
InstallCacheBazel %{SOURCE19}
InstallCacheBazel %{SOURCE20}
InstallCacheBazel %{SOURCE21}
InstallCacheBazel %{SOURCE22}
InstallCacheBazel %{SOURCE23}
InstallCacheBazel %{SOURCE24}
InstallCacheBazel %{SOURCE25}
InstallCacheBazel %{SOURCE26}
InstallCacheBazel %{SOURCE27}
InstallCacheBazel %{SOURCE28}
InstallCacheBazel %{SOURCE29}
InstallCacheBazel %{SOURCE30}
InstallCacheBazel %{SOURCE31}
InstallCacheBazel %{SOURCE32}
InstallCacheBazel %{SOURCE33}
InstallCacheBazel %{SOURCE34}
InstallCacheBazel %{SOURCE35}
InstallCacheBazel %{SOURCE36}
InstallCacheBazel %{SOURCE37}
InstallCacheBazel %{SOURCE38}
InstallCacheBazel %{SOURCE39}
InstallCacheBazel %{SOURCE40}
InstallCacheBazel %{SOURCE41}
InstallCacheBazel %{SOURCE42}
InstallCacheBazel %{SOURCE43}
InstallCacheBazel %{SOURCE44}
InstallCacheBazel %{SOURCE45}
InstallCacheBazel %{SOURCE46}
InstallCacheBazel %{SOURCE47}
InstallCacheBazel %{SOURCE48}
InstallCacheBazel %{SOURCE49}
InstallCacheBazel %{SOURCE50}
InstallCacheBazel %{SOURCE51}
InstallCacheBazel %{SOURCE52}
InstallCacheBazel %{SOURCE53}
InstallCacheBazel %{SOURCE54}
InstallCacheBazel %{SOURCE55}
InstallCacheBazel %{SOURCE56}
InstallCacheBazel %{SOURCE57}
InstallCacheBazel %{SOURCE58}
InstallCacheBazel %{SOURCE59}
InstallCacheBazel %{SOURCE60}
InstallCacheBazel %{SOURCE61}
InstallCacheBazel %{SOURCE62}
InstallCacheBazel %{SOURCE63}
InstallCacheBazel %{SOURCE64}
InstallCacheBazel %{SOURCE65}
InstallCacheBazel %{SOURCE66}
InstallCacheBazel %{SOURCE67}
InstallCacheBazel %{SOURCE68}
InstallCacheBazel %{SOURCE69}
InstallCacheBazel %{SOURCE70}
# CACHE BAZEL END

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566269687
export GCC_IGNORE_WERROR=1

# external/upb fails to build with GCC 10...
# https://github.com/tensorflow/tensorflow/issues/39467
export CC=gcc-9
export CXX=g++-9

bazel clean
bazel build \
  --repository_cache=/var/tmp/cache \
  --config=release \
  --verbose_failures \
  //tensorflow_serving/model_servers:tensorflow_model_server

%install
export SOURCE_DATE_EPOCH=1566269687
mkdir -p %{buildroot}/usr/bin/
cp -a bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server %{buildroot}/usr/bin/

mkdir -p %{buildroot}/usr/share/package-licenses/tensorflow-serving
cp -a LICENSE %{buildroot}/usr/share/package-licenses/tensorflow-serving/LICENSE

%files
%defattr(-,root,root,-)
/usr/bin/tensorflow_model_server
/usr/share/package-licenses/tensorflow-serving/LICENSE
