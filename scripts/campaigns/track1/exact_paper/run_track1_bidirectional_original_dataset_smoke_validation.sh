#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"

source "${PROJECT_ROOT}/scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh"

CONDA_ENVIRONMENT_NAME="standard_ml_codex_env"
PYTHON_EXECUTABLE="python"
DRY_RUN="0"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --conda-environment-name)
            CONDA_ENVIRONMENT_NAME="$2"
            shift 2
            ;;
        --python-executable)
            PYTHON_EXECUTABLE="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN="1"
            shift
            ;;
        --help|-h)
            echo "Usage: bash ${0} [--conda-environment-name NAME] [--python-executable COMMAND] [--dry-run]"
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            exit 2
            ;;
    esac
done

CONFIG_ROOT="config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/smoke"
RUNNER_SCRIPT_PATH="scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py"
LOG_ROOT="${PROJECT_ROOT}/output/training_campaigns/track1/exact_paper/original_dataset_smoke_validation/logs"
mkdir -p "${LOG_ROOT}"

mapfile -t CONFIG_PATH_LIST < <(find "${PROJECT_ROOT}/${CONFIG_ROOT}" -type f -name "*.yaml" | sort)
if [[ "${#CONFIG_PATH_LIST[@]}" -eq 0 ]]; then
    echo "[ERROR] No smoke configs found under ${CONFIG_ROOT}" >&2
    exit 2
fi

for config_path in "${CONFIG_PATH_LIST[@]}"; do
    config_relative_path="$(realpath --relative-to="${PROJECT_ROOT}" "${config_path}")"
    config_file_stem="$(basename "${config_relative_path}" .yaml)"
    echo "[INFO] Running smoke validation | ${config_relative_path}"
    launcher_arguments=(
        --environment-name "${CONDA_ENVIRONMENT_NAME}"
        --python-executable "${PYTHON_EXECUTABLE}"
        --runner-script-path "${RUNNER_SCRIPT_PATH}"
        --config-path "${config_relative_path}"
        --output-suffix "smoke_validation"
        --log-path "${LOG_ROOT}/${config_file_stem}.log"
    )
    if [[ "${DRY_RUN}" == "1" ]]; then
        launcher_arguments+=(--dry-run)
    fi
    campaign_launcher_run_with_streaming_log "${launcher_arguments[@]}"
done

echo "[DONE] Track 1 bidirectional original-dataset smoke validation completed"
