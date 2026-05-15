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
            echo "Usage: bash scripts/campaigns/wave1/run_wave1_residual_harmonic_family_campaign.sh [--python-executable COMMAND] [--dry-run]"
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            exit 2
            ;;
    esac
done

cd "${PROJECT_ROOT}"

CAMPAIGN_CONFIG_ROOT="config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign"
PLANNING_REPORT_PATH="doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md"
CAMPAIGN_NAME="wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00"
QUEUE_ROOT="config/training/queue"
CAMPAIGN_CONFIG_FILE_NAME_LIST=(
    "01_residual_h08_small_frozen.yaml"
    "02_residual_h08_small_joint.yaml"
    "03_residual_h12_small_frozen.yaml"
    "04_residual_h12_small_joint_anchor.yaml"
    "05_residual_h16_small_joint.yaml"
    "06_residual_h12_medium_joint.yaml"
    "07_residual_h12_wide_joint.yaml"
    "08_residual_h12_deep_joint.yaml"
    "09_residual_h12_small_joint_low_dropout.yaml"
    "10_residual_h12_small_joint_high_dropout.yaml"
    "11_residual_h12_small_joint_no_layer_norm.yaml"
    "12_residual_h12_small_joint_low_lr_long.yaml"
    "13_residual_h12_wide_joint_low_lr_long.yaml"
    "14_residual_h12_small_joint_dense.yaml"
    "15_residual_h12_small_joint_medium_dense_large_batch.yaml"
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
