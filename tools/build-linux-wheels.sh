#!/bin/bash

# -------------------------------------------------------------------------
#  Copyright 2026 Ratha SIV. All rights reserved.
#  Apache-2.0 license
# -------------------------------------------------------------------------

set -euxo pipefail

PLAT=$(cat /etc/manylinux-platform-tag)

repair_wheel () {
  local wheel="$1"
  local outdir="$2"

  echo "Inspecting $wheel"
  auditwheel show "$wheel" || {
    echo "SKIP: Invalid wheel $wheel"
    return
  }

  local EXCL_LIST
  EXCL_LIST=$(echo "$AUDITWHEEL_EXCL_LIBS" | tr -d "[]'," )

  local EXCL_ARGS=""
  for lib in $EXCL_LIST; do
    EXCL_ARGS+=" --exclude $lib"
  done

  echo "Attempting repair for $wheel"
  if auditwheel repair \
      $EXCL_ARGS \
      "$wheel" --plat "$PLAT" -w "$outdir"; then
    echo "Repaired wheel: $wheel"
  else
    echo "FAILED to repair wheel: $wheel"
  fi
}

if [[ "${BUILD_ISOLATION:-0}" == "1" ]]; then
  no_isolation=""
else
  no_isolation="--no-isolation"
fi

mkdir -p /io/tmp /io/dist

VERSIONS=$(echo "$PYTHON_VERSIONS" | tr -d "[]'," )

for pv in $VERSIONS; do

  py_tag="cp${pv/./}"
  PYBIN="/opt/python/${py_tag}-${py_tag}/bin"

  if [ -x "${PYBIN}/pip" ]; then

    "${PYBIN}/pip" install --upgrade pip setuptools wheel
    "${PYBIN}/pip" install nvidia-arch

    if [[ "${INSTALL_TORCH:-0}" == "1" ]]; then
      "${PYBIN}/pip" install torch torchvision --index-url https://download.pytorch.org/whl/cu${CUDA_VERSION}
      echo "PyTorch for cu${CUDA_VERSION} installed."
    fi

    if [ -z "${CUDA_ARCH_LIST}" ]; then
      echo "============================== AUTO DETECT =============================="
      echo "CUDA_ARCH_LIST was not and is now being ..."
      nvcc --version
      "${PYBIN}/python" -c "import nvidia_arch as na; print(na.normalize_arches(na.get_arches(gpu_type='${NVIDIA_ARCH_TYPE}', min_sm=${NVIDIA_ARCH_MIN}, add_ptx=True), exclude='10.1', return_mode='cc_string'))"
      export CUDA_ARCH_LIST=$("${PYBIN}/python" -c "import nvidia_arch as na; print(na.normalize_arches(na.get_arches(gpu_type='${NVIDIA_ARCH_TYPE}', min_sm=${NVIDIA_ARCH_MIN}, add_ptx=True), exclude='10.1', return_mode='cc_string'))")
      echo "CUDA_ARCH_LIST=${CUDA_ARCH_LIST}"
      echo "========================================================================="
    fi

    export TORCH_CUDA_ARCH_LIST=${CUDA_ARCH_LIST}
    echo "TORCH_CUDA_ARCH_LIST=${TORCH_CUDA_ARCH_LIST}"

    export BEVX_CUDA_ARCH_LIST=${CUDA_ARCH_LIST}
    echo "BEVX_CUDA_ARCH_LIST=${BEVX_CUDA_ARCH_LIST}"

    export BEVX_GPU_TYPE=${NVIDIA_ARCH_TYPE}
    echo "BEVX_GPU_TYPE=${BEVX_GPU_TYPE}"

    export BEVX_MIN_SM=${NVIDIA_ARCH_MIN}
    echo "BEVX_MIN_SM=${BEVX_MIN_SM}"

    if [ -n "${INSTALL_EXTRA}" ]; then
      "${PYBIN}/pip" install ${INSTALL_EXTRA}
      echo "Extra packages installed: ${INSTALL_EXTRA}."
    fi

    if [ -n "${INSTALL_TXT}" ]; then
      "${PYBIN}/pip" install -r ${INSTALL_TXT}
      echo "Packages in text file installed: ${INSTALL_TXT}."
    fi

    if [ -n "${BUILD_ADDITIONAL_VARS:-}" ]; then
      echo "Exporting additional build vars: ${BUILD_ADDITIONAL_VARS}"
      export ${BUILD_ADDITIONAL_VARS}
    fi

    "${PYBIN}/python" -m build ${no_isolation} --wheel --outdir /io/tmp /io/${PACKAGE_NAME}

  else
    echo "SKIP: Python version ${py_tag} not found."
  fi

done

for whl in /io/tmp/*.whl; do
  repair_wheel "$whl" /io/dist
done

rm -rf /io/tmp
