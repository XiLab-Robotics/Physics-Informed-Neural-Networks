#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../.." && pwd)"

# shellcheck source=../infrastructure/shared_streaming_campaign_launcher.sh
source "${PROJECT_ROOT}/scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh"

CONDA_ENVIRONMENT_NAME="pinns_env"
PYTHON_EXECUTABLE="python"
GPU_ID_LIST_TEXT="0"
SKIP_GRID_PHASE="0"
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
        --gpu-id-list)
            GPU_ID_LIST_TEXT="$2"
            shift 2
            ;;
        --skip-grid-phase)
            SKIP_GRID_PHASE="1"
            shift
            ;;
        --dry-run)
            DRY_RUN="1"
            shift
            ;;
        --help|-h)
            echo "Usage: bash scripts/campaigns/wave_1/run_wave1_directional_best_hyperparameter_search_campaign.sh [--conda-environment-name NAME] [--python-executable COMMAND] [--gpu-id-list 0,1] [--skip-grid-phase] [--dry-run]"
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
CAMPAIGN_ROOT="config/training/wave1_directional_best_hyperparameter_search/campaigns/2026-05-11_wave1_directional_best_hyperparameter_search_campaign"
GRID_QUEUE_ROOT="${CAMPAIGN_ROOT}/grid_queue"
OPTUNA_STUDY_ROOT="${CAMPAIGN_ROOT}/optuna_studies"
PLANNING_REPORT_PATH="doc/reports/campaign_plans/wave_1/2026-05-11-19-41-11_wave1_directional_best_hyperparameter_search_campaign_plan_report.md"
CAMPAIGN_NAME="wave1_directional_best_hyperparameter_search_campaign_2026_05_11_19_41_11"
CAMPAIGN_OUTPUT_ROOT="output/training_campaigns/wave1/directional_best_hyperparameter_search/${CAMPAIGN_NAME}"
LAUNCHER_LOG_ROOT="${CAMPAIGN_OUTPUT_ROOT}/launcher_logs"
mkdir -p "${LAUNCHER_LOG_ROOT}"

mapfile -t GRID_QUEUE_CONFIG_PATH_LIST < <(find "${GRID_QUEUE_ROOT}" -maxdepth 1 -type f -name '*.yaml' | sort)
mapfile -t OPTUNA_STUDY_CONFIG_PATH_LIST < <(find "${OPTUNA_STUDY_ROOT}" -maxdepth 1 -type f -name '*.yaml' | sort)
IFS=',' read -r -a GPU_ID_LIST <<< "${GPU_ID_LIST_TEXT}"

echo "[INFO] Campaign Name | ${CAMPAIGN_NAME}"
echo "[INFO] Planning Report | ${PLANNING_REPORT_PATH}"
echo "[INFO] Grid Config Count | ${#GRID_QUEUE_CONFIG_PATH_LIST[@]}"
echo "[INFO] Optuna Study Count | ${#OPTUNA_STUDY_CONFIG_PATH_LIST[@]}"
echo "[INFO] GPU IDs | ${GPU_ID_LIST_TEXT}"

if [[ "${SKIP_GRID_PHASE}" != "1" && "${#GRID_QUEUE_CONFIG_PATH_LIST[@]}" -gt 0 ]]; then
    GRID_COMMAND_LIST=(
        "${PYTHON_EXECUTABLE}"
        scripts/training/run_training_campaign.py
        "${GRID_QUEUE_CONFIG_PATH_LIST[@]}"
        --campaign-name
        "${CAMPAIGN_NAME}"
        --planning-report-path
        "${PLANNING_REPORT_PATH}"
        --linux
    )
    echo "[INFO] Grid Command | $(campaign_launcher_join_command "${GRID_COMMAND_LIST[@]}")"
    if [[ "${DRY_RUN}" != "1" ]]; then
        "${GRID_COMMAND_LIST[@]}"
    fi
else
    echo "[INFO] Grid phase skipped"
fi

if [[ "${#OPTUNA_STUDY_CONFIG_PATH_LIST[@]}" -eq 0 ]]; then
    echo "[INFO] No Optuna study configs found | neural HPO phase skipped"
    exit 0
fi

if [[ "${#GPU_ID_LIST[@]}" -eq 0 ]]; then
    echo "[ERROR] --gpu-id-list must contain at least one GPU id." >&2
    exit 2
fi

study_index=0
for study_config_path in "${OPTUNA_STUDY_CONFIG_PATH_LIST[@]}"; do
    gpu_id="${GPU_ID_LIST[$((study_index % ${#GPU_ID_LIST[@]}))]}"
    study_file_name="$(basename "${study_config_path}")"
    study_stem="${study_file_name%.yaml}"
    stdout_path="${LAUNCHER_LOG_ROOT}/${study_stem}.stdout.log"
    command_list=(
        "${CONDA_COMMAND}"
        run
        --no-capture-output
        -n
        "${CONDA_ENVIRONMENT_NAME}"
        "${PYTHON_EXECUTABLE}"
        scripts/training/run_optuna_neural_hpo_study.py
        --study-config-path
        "${study_config_path}"
        --gpu-id
        "${gpu_id}"
        --linux
    )
    echo "[INFO] Optuna Command | $(campaign_launcher_join_command "${command_list[@]}")"
    if [[ "${DRY_RUN}" == "1" ]]; then
        echo "DRY_RUN_STUDY_CONFIG::${study_config_path}"
    else
        CUDA_VISIBLE_DEVICES="${gpu_id}" "${command_list[@]}" 2>&1 | tee "${stdout_path}"
        native_exit_code="${PIPESTATUS[0]}"
        if [[ "${native_exit_code}" -ne 0 ]]; then
            exit "${native_exit_code}"
        fi
    fi
    study_index=$((study_index + 1))
done

echo "[DONE] Wave 1 directional best-hyperparameter search launcher completed"
