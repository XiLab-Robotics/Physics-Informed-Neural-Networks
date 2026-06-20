#!/usr/bin/env bash

# Shared Bash launcher for RCIM Model-Bank Reproduction harmonic-wise bundles.

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"

source "${PROJECT_ROOT}/scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh"

CONDA_ENVIRONMENT_NAME="pinns_env"
PYTHON_EXECUTABLE="python"
CAMPAIGN_CONFIG_ROOT=""
PLANNING_REPORT_PATH=""
CAMPAIGN_NAME=""
DRY_RUN="0"
CAMPAIGN_CONFIG_FILE_LIST=()

print_usage() {
    cat <<'USAGE'
Usage:
  bash scripts/campaigns/track_1/harmonic_wise/run_track1_harmonic_wise_campaign_bundle.sh \
    --campaign-config-root PATH \
    --planning-report-path PATH \
    --campaign-name NAME

Options:
  --campaign-config-root PATH      Repository-relative folder containing YAML configs.
  --campaign-config-file NAME      Config file name under the root. Repeatable.
  --planning-report-path PATH      Repository-relative planning report path.
  --campaign-name NAME             Campaign output folder stem.
  --conda-environment-name NAME    Conda environment name.
  --python-executable PATH         Python executable passed through conda run.
  --dry-run                        Print resolved runs without launching training.
  --help                           Show this help text.
USAGE
}

normalize_repository_relative_path() {
    local raw_path="$1"
    raw_path="${raw_path//\\//}"
    raw_path="${raw_path#./}"
    raw_path="${raw_path#/}"
    printf '%s\n' "${raw_path}"
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --campaign-config-root)
            CAMPAIGN_CONFIG_ROOT="$(normalize_repository_relative_path "$2")"
            shift 2
            ;;
        --campaign-config-file)
            CAMPAIGN_CONFIG_FILE_LIST+=("$2")
            shift 2
            ;;
        --planning-report-path)
            PLANNING_REPORT_PATH="$(normalize_repository_relative_path "$2")"
            shift 2
            ;;
        --campaign-name)
            CAMPAIGN_NAME="$2"
            shift 2
            ;;
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
        --help)
            print_usage
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            print_usage >&2
            exit 2
            ;;
    esac
done

if [[ -z "${CAMPAIGN_CONFIG_ROOT}" || -z "${PLANNING_REPORT_PATH}" || -z "${CAMPAIGN_NAME}" ]]; then
    echo "[ERROR] --campaign-config-root, --planning-report-path, and --campaign-name are required." >&2
    exit 2
fi

CAMPAIGN_CONFIG_ROOT="${CAMPAIGN_CONFIG_ROOT%/}"
CAMPAIGN_OUTPUT_ROOT="output/training_campaigns/track1/harmonic_wise/${CAMPAIGN_NAME}"
CAMPAIGN_LOG_ROOT="${PROJECT_ROOT}/${CAMPAIGN_OUTPUT_ROOT}/logs"
RUNNER_SCRIPT_PATH="scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/run_harmonic_wise_comparison_pipeline.py"
mkdir -p "${CAMPAIGN_LOG_ROOT}"

CAMPAIGN_CONFIG_PATH_LIST=()
if [[ "${#CAMPAIGN_CONFIG_FILE_LIST[@]}" -gt 0 ]]; then
    for config_file in "${CAMPAIGN_CONFIG_FILE_LIST[@]}"; do
        CAMPAIGN_CONFIG_PATH_LIST+=("${CAMPAIGN_CONFIG_ROOT}/${config_file}")
    done
else
    while IFS= read -r config_path; do
        CAMPAIGN_CONFIG_PATH_LIST+=("$(realpath --relative-to="${PROJECT_ROOT}" "${config_path}")")
    done < <(find "${PROJECT_ROOT}/${CAMPAIGN_CONFIG_ROOT}" -maxdepth 1 -type f -name "*.yaml" | sort)
fi

echo "[INFO] Campaign Name | ${CAMPAIGN_NAME}"
echo "[INFO] Planning Report | ${PLANNING_REPORT_PATH}"
echo "[INFO] Campaign Output Root | ${CAMPAIGN_OUTPUT_ROOT}"
echo "[INFO] Harmonic-Wise Run Count | ${#CAMPAIGN_CONFIG_PATH_LIST[@]}"

for config_index in "${!CAMPAIGN_CONFIG_PATH_LIST[@]}"; do
    config_path="${CAMPAIGN_CONFIG_PATH_LIST[${config_index}]}"
    config_file_name="$(basename "${config_path}" .yaml)"
    run_log_path="${CAMPAIGN_LOG_ROOT}/${config_file_name}.log"

    echo ""
    printf '=%.0s' {1..96}
    echo ""
    echo "[INFO] Harmonic-Wise Campaign Progress $((config_index + 1))/${#CAMPAIGN_CONFIG_PATH_LIST[@]} | ${config_path}"
    echo "[INFO] Runner Script | ${RUNNER_SCRIPT_PATH}"
    echo "[INFO] Log Path | ${run_log_path}"
    printf '=%.0s' {1..96}
    echo ""

    launcher_arguments=(
        --environment-name "${CONDA_ENVIRONMENT_NAME}"
        --python-executable "${PYTHON_EXECUTABLE}"
        --runner-script-path "${RUNNER_SCRIPT_PATH}"
        --config-path "${config_path}"
        --output-suffix "campaign_run"
        --log-path "${run_log_path}"
    )
    if [[ "${DRY_RUN}" == "1" ]]; then
        launcher_arguments+=(--dry-run)
    fi

    campaign_launcher_run_with_streaming_log "${launcher_arguments[@]}"
done

echo ""
echo "[DONE] Harmonic-wise campaign completed successfully"
echo "[DONE] Campaign logs available under | ${CAMPAIGN_LOG_ROOT}"
