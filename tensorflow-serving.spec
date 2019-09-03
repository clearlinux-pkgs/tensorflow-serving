Name     : tensorflow-serving
Version  : 1.14.0
Release  : 1
URL      : https://github.com/tensorflow/serving/archive/1.14.0.tar.gz
Source0  : https://github.com/tensorflow/serving/archive/1.14.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : buildreq-distutils3
BuildRequires : bazel
BuildRequires : curl
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-core
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : virtualenv
BuildRequires : wheel
BuildRequires : unzip
BuildRequires : which
BuildRequires : git
BuildRequires : wget
BuildRequires : patch
BuildRequires : numpy

Source10 : https://github.com/tensorflow/tensorflow/archive/87989f69597d6b2d60de8f112e1e3cea23be7298.tar.gz
Source11 : https://github.com/bazelbuild/rules_closure/archive/316e6133888bfc39fb860a4f1a31cfcbae485aef.tar.gz
Source12 : https://github.com/protocolbuffers/protobuf/archive/5902e759108d14ee8e6b0b07653dac2f4e70ac73.tar.gz
Source13 : https://github.com/bazelbuild/bazel-skylib/archive/0.7.0.tar.gz
Source14 : https://github.com/abseil/abseil-cpp/archive/daf381e8535a1f1f1b8a75966a74e7cca63dee89.tar.gz
Source15 : http://mirror.tensorflow.org/github.com/google/nsync/archive/1.20.2.tar.gz
Source16 : http://mirror.tensorflow.org/download.open-mpi.org/release/hwloc/v2.0/hwloc-2.0.3.tar.gz
Source17 : http://mirror.tensorflow.org/github.com/google/double-conversion/archive/3992066a95b823efc8ccc1baf82a1cfc73f6e9b8.zip
Source18 : https://bitbucket.org/eigen/eigen/get/a0d250e79c79.tar.gz
Source19 : http://mirror.tensorflow.org/github.com/google/farmhash/archive/816a4ae622e964763ca0862d9dbd19324a1eaf45.tar.gz
Source20 : http://pilotfiber.dl.sourceforge.net/project/giflib/giflib-5.1.4.tar.gz
Source21 : https://github.com/libjpeg-turbo/libjpeg-turbo/archive/2.0.0.tar.gz
Source22 : http://www.nasm.us/pub/nasm/releasebuilds/2.13.03/nasm-2.13.03.tar.bz2
Source23 : http://mirror.tensorflow.org/www.kurims.kyoto-u.ac.jp/~ooura/fft.tgz
Source24 : http://mirror.tensorflow.org/curl.haxx.se/download/curl-7.60.0.tar.gz
Source25 : http://mirror.tensorflow.org/github.com/google/boringssl/archive/7f634429a04abc48e2eb041c81c5235816c96514.tar.gz
Source26 : http://mirror.tensorflow.org/github.com/open-source-parsers/jsoncpp/archive/1.8.4.tar.gz
Source27 : https://github.com/intel/mkl-dnn/releases/download/v0.18/mklml_lnx_2019.0.3.20190220.tgz
Source28 : https://github.com/intel/mkl-dnn/releases/download/v0.18/mklml_mac_2019.0.3.20190220.tgz
Source29 : https://github.com/intel/mkl-dnn/releases/download/v0.18/mklml_win_2019.0.3.20190220.zip
Source30 : https://github.com/intel/mkl-dnn/archive/v0.18.tar.gz
Source31 : https://github.com/aws/aws-sdk-cpp/archive/1.5.8.tar.gz
Source32 : https://github.com/llvm-mirror/llvm/archive/558b52b517b8c989dc2d7fffb5c580fa45aece34.tar.gz
Source33 : https://github.com/hfp/libxsmm/archive/1.11.tar.gz
Source34 : https://github.com/grpc/grpc/archive/4566c2a29ebec0835643b972eb99f4306c4234a3.tar.gz
Source35 : http://mirror.tensorflow.org/github.com/edenhill/librdkafka/archive/v0.11.5.tar.gz
Source36 : http://mirror.tensorflow.org/www.sqlite.org/2019/sqlite-amalgamation-3280000.zip
Source37 : http://mirror.tensorflow.org/github.com/unicode-org/icu/archive/release-62-1.tar.gz
Source38 : http://mirror.tensorflow.org/github.com/nanopb/nanopb/archive/f8ac463766281625ad710900479130c7fcb4d63b.tar.gz
Source39 : https://github.com/libevent/libevent/archive/release-2.1.8-stable.zip
Source40 : https://github.com/Tencent/rapidjson/archive/v1.1.0.zip
Source41 : https://zlib.net/zlib-1.2.11.tar.gz
Source42 : http://mirror.tensorflow.org/github.com/google/highwayhash/archive/fd3d9af80465e4383162e4a7c5e2f406e82dd968.tar.gz
Source43 : http://mirror.tensorflow.org/github.com/google/re2/archive/2018-10-01.tar.gz
Source44 : http://mirror.tensorflow.org/github.com/google/snappy/archive/1.1.7.tar.gz
Source45 : http://mirror.tensorflow.org/github.com/google/gemmlowp/archive/12fed0cd7cfcd9e169bf1925bc3a7a58725fdcc3.zip
Source46 : http://mirror.tensorflow.org/github.com/LMDB/lmdb/archive/LMDB_0.9.22.tar.gz
Source47 : http://mirror.tensorflow.org/github.com/glennrp/libpng/archive/v1.6.37.tar.gz

Patch1: 0001-Rename-gettid-in-grpc-included-by-tensorflow.patch

%description
# TensorFlow Serving: A flexible, high-performance serving system for machine learning models
[![Ubuntu Build Status](https://storage.googleapis.com/tensorflow-serving-kokoro-build-badges/ubuntu.svg)](https://storage.googleapis.com/tensorflow-serving-kokoro-build-badges/ubuntu.html)
[![Ubuntu Build Status at TF HEAD](https://storage.googleapis.com/tensorflow-serving-kokoro-build-badges/ubuntu-tf-head.svg)](https://storage.googleapis.com/tensorflow-serving-kokoro-build-badges/ubuntu-tf-head.html)
![Docker CPU Nightly Build Status](https://storage.googleapis.com/tensorflow-serving-kokoro-build-badges/docker-cpu-nightly.svg)
![Docker GPU Nightly Build Status](https://storage.googleapis.com/tensorflow-serving-kokoro-build-badges/docker-gpu-nightly.svg)

%prep
%setup -q -n serving-1.14.0

%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1566269687

InstallCache() {
        sha256=`sha256sum $1 | cut -f1 -d" "`
        mkdir -p /tmp/cache/content_addressable/sha256/$sha256/
        cp $1 /tmp/cache/content_addressable/sha256/$sha256/file
        cp $1 /tmp/cache/
}

InstallCache %{SOURCE10}
InstallCache %{SOURCE11}
InstallCache %{SOURCE12}
InstallCache %{SOURCE13}
InstallCache %{SOURCE14}
InstallCache %{SOURCE15}
InstallCache %{SOURCE16}
InstallCache %{SOURCE17}
InstallCache %{SOURCE18}
InstallCache %{SOURCE19}
InstallCache %{SOURCE20}
InstallCache %{SOURCE21}
InstallCache %{SOURCE22}
InstallCache %{SOURCE23}
InstallCache %{SOURCE24}
InstallCache %{SOURCE25}
InstallCache %{SOURCE26}
InstallCache %{SOURCE27}
InstallCache %{SOURCE28}
InstallCache %{SOURCE29}
InstallCache %{SOURCE30}
InstallCache %{SOURCE31}
InstallCache %{SOURCE32}
InstallCache %{SOURCE33}
InstallCache %{SOURCE34}
InstallCache %{SOURCE35}
InstallCache %{SOURCE35}
InstallCache %{SOURCE36}
InstallCache %{SOURCE37}
InstallCache %{SOURCE38}
InstallCache %{SOURCE39}
InstallCache %{SOURCE40}
InstallCache %{SOURCE41}
InstallCache %{SOURCE42}
InstallCache %{SOURCE43}
InstallCache %{SOURCE44}
InstallCache %{SOURCE45}
InstallCache %{SOURCE46}
InstallCache %{SOURCE47}

bazel clean
bazel build --logging=0 --repository_cache=/tmp/cache --color=yes --curses=yes --config=nativeopt --local_ram_resources=2048 --verbose_failures --output_filter=DONT_MATCH_ANYTHING --incompatible_no_support_tools_in_action_inputs=false tensorflow_serving/model_servers:tensorflow_model_server

%install
export SOURCE_DATE_EPOCH=1566269687
mkdir -p %{buildroot}/usr/bin/
cp bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server %{buildroot}/usr/bin/

mkdir -p %{buildroot}/usr/share/package-licenses/tensorflow-serving
cp LICENSE %{buildroot}/usr/share/package-licenses/tensorflow-serving/LICENSE

%files
%defattr(-,root,root,-)
/usr/bin/tensorflow_model_server
/usr/share/package-licenses/tensorflow-serving/LICENSE
