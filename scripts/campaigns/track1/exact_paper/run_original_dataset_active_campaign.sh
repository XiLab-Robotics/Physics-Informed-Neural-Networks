#!/usr/bin/env bash

# Linux launcher for Track 1 original-dataset exact-model-bank campaigns that
# are defined by doc/running/active_training_campaign.yaml.

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"

source "${PROJECT_ROOT}/scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh"

ACTIVE_CAMPAIGN_PATH="doc/running/active_training_campaign.yaml"
CONDA_ENVIRONMENT_NAME="standard_ml_codex_env"
PYTHON_EXECUTABLE="python"
REMOTE_MODE="0"
REMOTE_HOST_ALIAS="${STANDARDML_REMOTE_TRAINING_HOST_ALIAS:-xilab-remote}"
REMOTE_REPOSITORY_PATH="${STANDARDML_REMOTE_TRAINING_REPO_PATH:-}"
REMOTE_CONDA_ENVIRONMENT_NAME="${STANDARDML_REMOTE_TRAINING_CONDA_ENV:-standard_ml_codex_env}"
LAUNCHER_RELATIVE_PATH=""
VALIDATION_OUTPUT_ROOT="output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank"
VALIDATION_REPORT_ROOT="doc/reports/analysis/validation_checks"
OUTPUT_SUFFIX="campaign_run"
SUPPRESS_GRID_SEARCH_CONSOLE_NOISE="0"
DRY_RUN="0"

print_usage() {
    cat <<'USAGE'
Usage:
  bash scripts/campaigns/track1/exact_paper/run_original_dataset_active_campaign.sh [options]

Options:
  --active-campaign-path PATH        Active campaign YAML path.
  --launcher-relative-path PATH      Launcher path recorded for remote launch.
  --validation-output-root PATH      Remote validation output root metadata.
  --validation-report-root PATH      Remote validation report root metadata.
  --output-suffix TEXT               Output suffix for validation runs.
  --suppress-grid-search-console-noise
  --remote
  --remote-host-alias HOST
  --remote-repository-path PATH
  --remote-conda-environment-name NAME
  --conda-environment-name NAME
  --python-executable COMMAND
  --dry-run
  --help
USAGE
}

metadata_python() {
    if command -v python >/dev/null 2>&1; then
        echo "python"
    elif command -v python3 >/dev/null 2>&1; then
        echo "python3"
    else
        echo "[ERROR] Neither python nor python3 is available for YAML parsing." >&2
        return 127
    fi
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
        --active-campaign-path)
            ACTIVE_CAMPAIGN_PATH="$(normalize_repository_relative_path "$2")"
            shift 2
            ;;
        --launcher-relative-path)
            LAUNCHER_RELATIVE_PATH="$(normalize_repository_relative_path "$2")"
            shift 2
            ;;
        --validation-output-root)
            VALIDATION_OUTPUT_ROOT="$(normalize_repository_relative_path "$2")"
            shift 2
            ;;
        --validation-report-root)
            VALIDATION_REPORT_ROOT="$(normalize_repository_relative_path "$2")"
            shift 2
            ;;
        --output-suffix)
            OUTPUT_SUFFIX="$2"
            shift 2
            ;;
        --suppress-grid-search-console-noise)
            SUPPRESS_GRID_SEARCH_CONSOLE_NOISE="1"
            shift
            ;;
        --remote)
            REMOTE_MODE="1"
            shift
            ;;
        --remote-host-alias)
            REMOTE_HOST_ALIAS="$2"
            shift 2
            ;;
        --remote-repository-path)
            REMOTE_REPOSITORY_PATH="$2"
            shift 2
            ;;
        --remote-conda-environment-name)
            REMOTE_CONDA_ENVIRONMENT_NAME="$2"
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
        --help|-h)
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

if [[ -z "${LAUNCHER_RELATIVE_PATH}" ]]; then
    echo "[ERROR] --launcher-relative-path is required." >&2
    exit 2
fi

PYTHON_FOR_METADATA="$(metadata_python)"
CAMPAIGN_METADATA_JSON="$(
    "${PYTHON_FOR_METADATA}" - "${PROJECT_ROOT}" "${ACTIVE_CAMPAIGN_PATH}" <<'PY'
import json
import sys
from pathlib import Path

import yaml

project_root = Path(sys.argv[1]).resolve()
campaign_path = (project_root / sys.argv[2]).resolve()
payload = yaml.safe_load(campaign_path.read_text(encoding="utf-8"))
queue_path_list = [str(path).replace("\\", "/") for path in payload.get("queue_config_path_list", [])]
run_name_list = []
for queue_path in queue_path_list:
    queue_payload = yaml.safe_load((project_root / queue_path).read_text(encoding="utf-8"))
    run_name_list.append(queue_payload["experiment"]["run_name"])
result = {
    "campaign_name": payload.get("campaign_name"),
    "planning_report_path": str(payload.get("planning_report_path", "")).replace("\\", "/"),
    "campaign_output_directory": str(payload.get("campaign_output_directory", "")).replace("\\", "/"),
    "queue_config_path_list": queue_path_list,
    "run_name_list": run_name_list,
}
print(json.dumps(result))
PY
)"

CAMPAIGN_NAME="$("${PYTHON_FOR_METADATA}" -c 'import json,sys; print(json.loads(sys.argv[1])["campaign_name"])' "${CAMPAIGN_METADATA_JSON}")"
PLANNING_REPORT_PATH="$("${PYTHON_FOR_METADATA}" -c 'import json,sys; print(json.loads(sys.argv[1])["planning_report_path"])' "${CAMPAIGN_METADATA_JSON}")"
CAMPAIGN_OUTPUT_DIRECTORY="$("${PYTHON_FOR_METADATA}" -c 'import json,sys; print(json.loads(sys.argv[1])["campaign_output_directory"])' "${CAMPAIGN_METADATA_JSON}")"
mapfile -t QUEUE_CONFIG_PATH_LIST < <("${PYTHON_FOR_METADATA}" -c 'import json,sys; [print(x) for x in json.loads(sys.argv[1])["queue_config_path_list"]]' "${CAMPAIGN_METADATA_JSON}")
mapfile -t RUN_NAME_LIST < <("${PYTHON_FOR_METADATA}" -c 'import json,sys; [print(x) for x in json.loads(sys.argv[1])["run_name_list"]]' "${CAMPAIGN_METADATA_JSON}")

if [[ "${#QUEUE_CONFIG_PATH_LIST[@]}" -eq 0 ]]; then
    echo "[ERROR] Active campaign has no queue_config_path_list entries | ${ACTIVE_CAMPAIGN_PATH}" >&2
    exit 2
fi

if [[ "${REMOTE_MODE}" == "1" ]]; then
    REMOTE_ARGUMENT_LIST=(
        --campaign-name "${CAMPAIGN_NAME}"
        --planning-report-path "${PLANNING_REPORT_PATH}"
        --launcher-relative-path "${LAUNCHER_RELATIVE_PATH}"
        --campaign-output-root-override "${CAMPAIGN_OUTPUT_DIRECTORY}"
        --validation-output-root "${VALIDATION_OUTPUT_ROOT}"
        --validation-report-root "${VALIDATION_REPORT_ROOT}"
        --remote-host-alias "${REMOTE_HOST_ALIAS}"
        --remote-repository-path "${REMOTE_REPOSITORY_PATH}"
        --remote-conda-environment-name "${REMOTE_CONDA_ENVIRONMENT_NAME}"
    )
    for config_path in "${QUEUE_CONFIG_PATH_LIST[@]}"; do
        REMOTE_ARGUMENT_LIST+=(--campaign-config-path "${config_path}")
    done
    for run_name in "${RUN_NAME_LIST[@]}"; do
        REMOTE_ARGUMENT_LIST+=(--run-name "${run_name}")
    done
    if [[ "${DRY_RUN}" == "1" ]]; then
        REMOTE_ARGUMENT_LIST+=(--dry-run)
    fi

    bash "${SCRIPT_DIRECTORY}/run_exact_paper_campaign_remote.sh" "${REMOTE_ARGUMENT_LIST[@]}"
    exit $?
fi

RUNNER_SCRIPT_PATH="scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py"
CAMPAIGN_LOG_ROOT="${PROJECT_ROOT}/${CAMPAIGN_OUTPUT_DIRECTORY}/logs"
mkdir -p "${CAMPAIGN_LOG_ROOT}"

echo "[INFO] Campaign Name | ${CAMPAIGN_NAME}"
echo "[INFO] Planning Report | ${PLANNING_REPORT_PATH}"
echo "[INFO] Campaign Output Root | ${CAMPAIGN_OUTPUT_DIRECTORY}"
echo "[INFO] Exact-Paper Run Count | ${#QUEUE_CONFIG_PATH_LIST[@]}"

for config_index in "${!QUEUE_CONFIG_PATH_LIST[@]}"; do
    config_relative_path="${QUEUE_CONFIG_PATH_LIST[${config_index}]}"
    config_file_stem="$(basename "${config_relative_path}" .yaml)"
    run_log_path="${CAMPAIGN_LOG_ROOT}/${config_file_stem}.log"

    echo "REMOTE_ACTIVE_CONFIG::$((config_index + 1))::${#QUEUE_CONFIG_PATH_LIST[@]}::${config_relative_path}"
    echo "REMOTE_ACTIVE_LOG::${CAMPAIGN_OUTPUT_DIRECTORY}/logs/${config_file_stem}.log"
    echo "REMOTE_ACTIVE_STAGE::Preparing exact-paper validation subprocess"
    echo "[INFO] Exact-Paper Campaign Progress $((config_index + 1))/${#QUEUE_CONFIG_PATH_LIST[@]} | ${config_relative_path}"

    launcher_arguments=(
        --environment-name "${CONDA_ENVIRONMENT_NAME}"
        --python-executable "${PYTHON_EXECUTABLE}"
        --runner-script-path "${RUNNER_SCRIPT_PATH}"
        --config-path "${config_relative_path}"
        --output-suffix "${OUTPUT_SUFFIX}"
        --log-path "${run_log_path}"
    )
    if [[ "${DRY_RUN}" == "1" ]]; then
        launcher_arguments+=(--dry-run)
    fi
    if [[ "${SUPPRESS_GRID_SEARCH_CONSOLE_NOISE}" == "1" ]]; then
        launcher_arguments+=(
            --
            --suppress-grid-search-console-noise
            --grid-search-heartbeat-seconds
            20
            --emit-remote-stage-markers
        )
    fi

    campaign_launcher_run_with_streaming_log "${launcher_arguments[@]}"

    echo "REMOTE_COMPLETED_CONFIG::$((config_index + 1))::${#QUEUE_CONFIG_PATH_LIST[@]}::${config_relative_path}"
    echo "REMOTE_ACTIVE_STAGE::Completed exact-paper validation subprocess"
    echo "[DONE] Exact-paper config complete | ${config_relative_path}"
done

echo "[DONE] Track 1 original-dataset active campaign completed"
