#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../.." && pwd)"

# shellcheck source=../infrastructure/shared_streaming_campaign_launcher.sh
source "${PROJECT_ROOT}/scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh"

CONDA_ENVIRONMENT_NAME="standard_ml_codex_env"
PYTHON_EXECUTABLE="python"
GPU_ID="0"
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
        --gpu-id)
            GPU_ID="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN="1"
            shift
            ;;
        --help|-h)
            echo "Usage: bash scripts/campaigns/wave1/run_wave1_directional_optuna_recovery_micro_campaign.sh [--conda-environment-name NAME] [--python-executable COMMAND] [--gpu-id ID] [--dry-run]"
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            exit 2
            ;;
    esac
done

cd "${PROJECT_ROOT}"

CONDA_COMMAND="$(campaign_launcher_resolve_conda_command)"
STUDY_CONFIG_PATH="config/training/wave1_directional_optuna_recovery_micro/campaigns/2026-05-12_wave1_directional_optuna_recovery_micro_campaign/optuna_studies/feedforward_recovery_micro.yaml"
COMMAND_LIST=(
    "${CONDA_COMMAND}"
    run
    --no-capture-output
    -n
    "${CONDA_ENVIRONMENT_NAME}"
    "${PYTHON_EXECUTABLE}"
    scripts/training/run_optuna_neural_hpo_study.py
    --study-config-path
    "${STUDY_CONFIG_PATH}"
    --gpu-id
    "${GPU_ID}"
    --linux
)

echo "[INFO] Study Config | ${STUDY_CONFIG_PATH}"
echo "[INFO] GPU ID | ${GPU_ID}"
echo "[INFO] Command | $(campaign_launcher_join_command "${COMMAND_LIST[@]}")"

if [[ "${DRY_RUN}" == "1" ]]; then
    echo "DRY_RUN_STUDY_CONFIG::${STUDY_CONFIG_PATH}"
    exit 0
fi

CUDA_VISIBLE_DEVICES="${GPU_ID}" "${COMMAND_LIST[@]}"
exit $?
