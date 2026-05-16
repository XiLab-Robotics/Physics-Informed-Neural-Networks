#!/usr/bin/env bash

# Configure Linux Conda activate/deactivate hooks for NVIDIA runtime libraries
# installed as Python wheels inside the target environment.

set -euo pipefail

CONDA_PREFIX_PATH="${CONDA_PREFIX:-}"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --conda-prefix)
            CONDA_PREFIX_PATH="$2"
            shift 2
            ;;
        --help|-h)
            echo "Usage: bash ${0} [--conda-prefix PATH]"
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            exit 2
            ;;
    esac
done

if [[ -z "${CONDA_PREFIX_PATH}" ]]; then
    if command -v python >/dev/null 2>&1; then
        CONDA_PREFIX_PATH="$(python -c 'import sys; print(sys.prefix)')"
    elif command -v python3 >/dev/null 2>&1; then
        CONDA_PREFIX_PATH="$(python3 -c 'import sys; print(sys.prefix)')"
    fi
fi

if [[ -z "${CONDA_PREFIX_PATH}" ]]; then
    echo "[ERROR] Could not resolve the target Conda environment prefix. Pass --conda-prefix or activate the environment first." >&2
    exit 2
fi

ACTIVATE_DIRECTORY="${CONDA_PREFIX_PATH}/etc/conda/activate.d"
DEACTIVATE_DIRECTORY="${CONDA_PREFIX_PATH}/etc/conda/deactivate.d"
mkdir -p "${ACTIVATE_DIRECTORY}" "${DEACTIVATE_DIRECTORY}"

CUDA_LIBRARY_PATH_LIST=(
    "${CONDA_PREFIX_PATH}/lib/python"*/site-packages/nvidia/cublas/lib
    "${CONDA_PREFIX_PATH}/lib/python"*/site-packages/nvidia/cuda_runtime/lib
    "${CONDA_PREFIX_PATH}/lib/python"*/site-packages/nvidia/cudnn/lib
)

RESOLVED_CUDA_LIBRARY_PATH_LIST=()
for cuda_library_path in "${CUDA_LIBRARY_PATH_LIST[@]}"; do
    if [[ -d "${cuda_library_path}" ]]; then
        RESOLVED_CUDA_LIBRARY_PATH_LIST+=("${cuda_library_path}")
    fi
done

if [[ "${#RESOLVED_CUDA_LIBRARY_PATH_LIST[@]}" -eq 0 ]]; then
    echo "[ERROR] Missing expected NVIDIA runtime library directories under ${CONDA_PREFIX_PATH}/lib/python*/site-packages/nvidia" >&2
    exit 2
fi

NVIDIA_LIBRARY_PATH="$(IFS=:; echo "${RESOLVED_CUDA_LIBRARY_PATH_LIST[*]}")"
ACTIVATE_SCRIPT_PATH="${ACTIVATE_DIRECTORY}/standardml_lan_ai_node_cuda_path.sh"
DEACTIVATE_SCRIPT_PATH="${DEACTIVATE_DIRECTORY}/standardml_lan_ai_node_cuda_path.sh"

cat >"${ACTIVATE_SCRIPT_PATH}" <<EOF
export STANDARDML_PREPEND_NVIDIA_LD_LIBRARY_PATH="${NVIDIA_LIBRARY_PATH}"
export STANDARDML_PREVIOUS_LD_LIBRARY_PATH="\${LD_LIBRARY_PATH:-}"
if [ -n "\${LD_LIBRARY_PATH:-}" ]; then
    export LD_LIBRARY_PATH="\${STANDARDML_PREPEND_NVIDIA_LD_LIBRARY_PATH}:\${LD_LIBRARY_PATH}"
else
    export LD_LIBRARY_PATH="\${STANDARDML_PREPEND_NVIDIA_LD_LIBRARY_PATH}"
fi
EOF

cat >"${DEACTIVATE_SCRIPT_PATH}" <<'EOF'
if [ -n "${STANDARDML_PREVIOUS_LD_LIBRARY_PATH+x}" ]; then
    export LD_LIBRARY_PATH="${STANDARDML_PREVIOUS_LD_LIBRARY_PATH}"
else
    unset LD_LIBRARY_PATH
fi
unset STANDARDML_PREVIOUS_LD_LIBRARY_PATH
unset STANDARDML_PREPEND_NVIDIA_LD_LIBRARY_PATH
EOF

echo "Resolved Conda prefix: ${CONDA_PREFIX_PATH}"
echo "Configured activate hook: ${ACTIVATE_SCRIPT_PATH}"
echo "Configured deactivate hook: ${DEACTIVATE_SCRIPT_PATH}"
echo "CUDA runtime LD_LIBRARY_PATH entries:"
printf ' - %s\n' "${RESOLVED_CUDA_LIBRARY_PATH_LIST[@]}"
