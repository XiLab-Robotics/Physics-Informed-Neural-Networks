#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../.." && pwd)"

# shellcheck source=../infrastructure/shared_streaming_campaign_launcher.sh
source "${PROJECT_ROOT}/scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh"

PYTHON_EXECUTABLE="python"
DRY_RUN="0"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --python-executable)
            PYTHON_EXECUTABLE="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN="1"
            shift
            ;;
        --help|-h)
            echo "Usage: bash scripts/campaigns/wave_1/run_wave1_directional_retraining_campaign.sh [--python-executable COMMAND] [--dry-run]"
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            exit 2
            ;;
    esac
done

cd "${PROJECT_ROOT}"

CAMPAIGN_CONFIG_ROOT="config/training/wave1_directional_retraining/campaigns/2026-05-06_wave1_directional_retraining_campaign/queue"
PLANNING_REPORT_PATH="doc/reports/campaign_plans/wave_1/2026-05-06-16-07-16_wave1_directional_retraining_campaign_plan_report.md"
CAMPAIGN_NAME="wave1_directional_retraining_campaign_2026_05_06_16_07_16"
QUEUE_ROOT="config/training/queue"
CAMPAIGN_CONFIG_FILE_NAME_LIST=(
    "01_tree_global.yaml"
    "02_tree_fw.yaml"
    "03_tree_bw.yaml"
    "04_residual_harmonic_mlp_global.yaml"
    "05_residual_harmonic_mlp_fw.yaml"
    "06_residual_harmonic_mlp_bw.yaml"
    "07_feedforward_global.yaml"
    "08_feedforward_fw.yaml"
    "09_feedforward_bw.yaml"
    "10_periodic_mlp_global.yaml"
    "11_periodic_mlp_fw.yaml"
    "12_periodic_mlp_bw.yaml"
    "13_harmonic_regression_global.yaml"
    "14_harmonic_regression_fw.yaml"
    "15_harmonic_regression_bw.yaml"
)

CAMPAIGN_CONFIG_PATH_LIST=()
for config_file_name in "${CAMPAIGN_CONFIG_FILE_NAME_LIST[@]}"; do
    CAMPAIGN_CONFIG_PATH_LIST+=("${CAMPAIGN_CONFIG_ROOT}/${config_file_name}")
done

COMMAND_LIST=(
    "${PYTHON_EXECUTABLE}"
    scripts/training/run_training_campaign.py
    "${CAMPAIGN_CONFIG_PATH_LIST[@]}"
    --campaign-name
    "${CAMPAIGN_NAME}"
    --planning-report-path
    "${PLANNING_REPORT_PATH}"
    --linux
)

echo "[INFO] Campaign Name | ${CAMPAIGN_NAME}"
echo "[INFO] Planning Report | ${PLANNING_REPORT_PATH}"
echo "[INFO] Config Count | ${#CAMPAIGN_CONFIG_PATH_LIST[@]}"
echo "[INFO] Command | $(campaign_launcher_join_command "${COMMAND_LIST[@]}")"

if [[ "${DRY_RUN}" == "1" ]]; then
    printf 'DRY_RUN_CONFIG::%s\n' "${CAMPAIGN_CONFIG_PATH_LIST[@]}"
    exit 0
fi

for queue_subdirectory_name in pending running; do
    queue_subdirectory_path="${QUEUE_ROOT}/${queue_subdirectory_name}"
    [[ -d "${queue_subdirectory_path}" ]] || continue
    for config_file_name in "${CAMPAIGN_CONFIG_FILE_NAME_LIST[@]}"; do
        find "${queue_subdirectory_path}" -maxdepth 1 -type f -name "*${config_file_name}" -delete
    done
done

"${COMMAND_LIST[@]}"
exit $?
