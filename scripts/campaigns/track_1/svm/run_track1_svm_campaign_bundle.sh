#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"

# shellcheck source=../../infrastructure/shared_streaming_campaign_launcher.sh
source "${PROJECT_ROOT}/scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh"

CAMPAIGN_CONFIG_ROOT=""
PLANNING_REPORT_PATH=""
CAMPAIGN_NAME=""
CONDA_ENVIRONMENT_NAME="pinns_env"
PYTHON_EXECUTABLE="python"
DRY_RUN="0"
CAMPAIGN_CONFIG_FILE_LIST=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --campaign-config-root)
            CAMPAIGN_CONFIG_ROOT="$2"
            shift 2
            ;;
        --planning-report-path)
            PLANNING_REPORT_PATH="$2"
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
        --campaign-config-file)
            CAMPAIGN_CONFIG_FILE_LIST+=("$2")
            shift 2
            ;;
        --help|-h)
            echo "Usage: bash scripts/campaigns/track_1/svm/run_track1_svm_campaign_bundle.sh --campaign-config-root PATH --planning-report-path PATH --campaign-name NAME [--dry-run]"
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            exit 2
            ;;
    esac
done

if [[ -z "${CAMPAIGN_CONFIG_ROOT}" || -z "${PLANNING_REPORT_PATH}" || -z "${CAMPAIGN_NAME}" ]]; then
    echo "[ERROR] Campaign config root, planning report path, and campaign name are required." >&2
    exit 2
fi

cd "${PROJECT_ROOT}"

if [[ "${#CAMPAIGN_CONFIG_FILE_LIST[@]}" -gt 0 ]]; then
    CAMPAIGN_CONFIG_PATH_LIST=()
    for config_file_name in "${CAMPAIGN_CONFIG_FILE_LIST[@]}"; do
        CAMPAIGN_CONFIG_PATH_LIST+=("${CAMPAIGN_CONFIG_ROOT}/${config_file_name}")
    done
else
    mapfile -t CAMPAIGN_CONFIG_PATH_LIST < <(find "${CAMPAIGN_CONFIG_ROOT}" -maxdepth 1 -type f -name '*.yaml' | sort)
fi
CAMPAIGN_OUTPUT_ROOT="output/training_campaigns/track1/svm/${CAMPAIGN_NAME}"
CAMPAIGN_LOG_ROOT="${CAMPAIGN_OUTPUT_ROOT}/logs"
RUNNER_PATH="scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py"

mkdir -p "${CAMPAIGN_LOG_ROOT}"

echo "[INFO] Campaign Name | ${CAMPAIGN_NAME}"
echo "[INFO] Planning Report | ${PLANNING_REPORT_PATH}"
echo "[INFO] Campaign Output Root | ${CAMPAIGN_OUTPUT_ROOT}"
echo "[INFO] Exact-Paper Run Count | ${#CAMPAIGN_CONFIG_PATH_LIST[@]}"

if [[ "${#CAMPAIGN_CONFIG_PATH_LIST[@]}" -eq 0 ]]; then
    echo "[ERROR] No YAML configs found | ${CAMPAIGN_CONFIG_ROOT}" >&2
    exit 2
fi

for config_path in "${CAMPAIGN_CONFIG_PATH_LIST[@]}"; do
    config_file_name="$(basename "${config_path}")"
    config_file_stem="${config_file_name%.yaml}"
    run_log_path="${CAMPAIGN_LOG_ROOT}/${config_file_stem}.log"

    if [[ "${DRY_RUN}" == "1" ]]; then
        echo "DRY_RUN_CONFIG::${config_path}"
        continue
    fi

    campaign_launcher_run_with_streaming_log \
        --environment-name "${CONDA_ENVIRONMENT_NAME}" \
        --python-executable "${PYTHON_EXECUTABLE}" \
        --runner-script-path "${RUNNER_PATH}" \
        --config-path "${config_path}" \
        --output-suffix "campaign_run" \
        --log-path "${run_log_path}" \
        -- --linux
done

echo "[DONE] Track 1 SVM campaign completed successfully"
