#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"
ACTIVE_CAMPAIGN_PATH="${PROJECT_ROOT}/doc/running/active_training_campaign.yaml"
RUNNER_PATH="${PROJECT_ROOT}/scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py"

cd "${PROJECT_ROOT}"

DIRECTION="Both"
FAMILY="All"
FAMILIES=""
STAGE="Search"
BEST_PARAMETER_SUMMARY_PATH=""
GRID_SEARCH_VERBOSE_OVERRIDE="-1"
HISTORICAL_CROSS_VALIDATE_VERBOSE_OVERRIDE="-1"
NO_EVAL="0"
NO_EXPORT="0"
CONDA_ENVIRONMENT_NAME="standard_ml_codex_env"
PYTHON_EXECUTABLE="python"
REPOSITORY_PATH_PLATFORM="linux"
DRY_RUN="0"

print_usage() {
    cat <<'USAGE'
Usage:
  bash scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh [options]

Options:
  --direction Forward|Backward|Both
  --family All|SVR|MLP|RF|DT|ET|ERT|GBM|HGBM|XGBM|LGBM|ELM
  --families "SVR,MLP,RF"
  --stage Search|Eval|Export|LoadBest
  --best-parameter-summary-path PATH
  --grid-search-verbose-override INT
  --historical-cross-validate-verbose-override INT
  --no-eval
  --no-export
  --conda-environment-name NAME
  --python-executable COMMAND
  --linux
  --windows
  --dry-run
  --help
USAGE
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --direction)
            DIRECTION="$2"
            shift 2
            ;;
        --family)
            FAMILY="$2"
            shift 2
            ;;
        --families)
            FAMILIES="$2"
            shift 2
            ;;
        --stage)
            STAGE="$2"
            shift 2
            ;;
        --best-parameter-summary-path)
            BEST_PARAMETER_SUMMARY_PATH="$2"
            shift 2
            ;;
        --grid-search-verbose-override)
            GRID_SEARCH_VERBOSE_OVERRIDE="$2"
            shift 2
            ;;
        --historical-cross-validate-verbose-override)
            HISTORICAL_CROSS_VALIDATE_VERBOSE_OVERRIDE="$2"
            shift 2
            ;;
        --no-eval)
            NO_EVAL="1"
            shift
            ;;
        --no-export)
            NO_EXPORT="1"
            shift
            ;;
        --conda-environment-name)
            CONDA_ENVIRONMENT_NAME="$2"
            shift 2
            ;;
        --python-executable)
            PYTHON_EXECUTABLE="$2"
            shift 2
            ;;
        --linux)
            REPOSITORY_PATH_PLATFORM="linux"
            shift
            ;;
        --windows)
            REPOSITORY_PATH_PLATFORM="windows"
            shift
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

case "$DIRECTION" in
    Forward|Backward|Both) ;;
    *)
        echo "[ERROR] Unsupported direction | ${DIRECTION}" >&2
        exit 2
        ;;
esac

case "$STAGE" in
    Search|Eval|Export|LoadBest) ;;
    *)
        echo "[ERROR] Unsupported stage | ${STAGE}" >&2
        exit 2
        ;;
esac

CONDA_COMMAND=()
if command -v conda >/dev/null 2>&1; then
    CONDA_COMMAND=(conda)
elif [[ -n "${CONDA_EXE:-}" ]]; then
    CONDA_COMMAND=("${CONDA_EXE}")
elif command -v conda.exe >/dev/null 2>&1; then
    CONDA_COMMAND=(conda.exe)
else
    echo "[ERROR] Unable to resolve conda on PATH." >&2
    exit 127
fi

QUEUE_BUNDLE_JSON="$(
    "${CONDA_COMMAND[@]}" run -n "${CONDA_ENVIRONMENT_NAME}" "${PYTHON_EXECUTABLE}" - <<PYTHON
from pathlib import Path
import json
import yaml

from scripts.tooling import repository_path_support

project_root = Path(r'''${PROJECT_ROOT}''')
campaign_path = Path(r'''${ACTIVE_CAMPAIGN_PATH}''')
direction_name = '''${DIRECTION}'''
family_name = '''${FAMILY}'''
families_text = '''${FAMILIES}'''
stage_name = '''${STAGE}'''
exact_family_order = ["SVR", "MLP", "RF", "DT", "ET", "ERT", "GBM", "HGBM", "XGBM", "LGBM", "ELM"]

campaign_payload = yaml.safe_load(campaign_path.read_text(encoding="utf-8"))
queue_path_list = campaign_payload.get("queue_config_path_list", [])

requested_token_list = []
if families_text.strip():
    requested_token_list = [token.strip().upper() for token in families_text.split(",") if token.strip()]
elif family_name.strip():
    requested_token_list = [family_name.strip().upper()]
if not requested_token_list:
    requested_token_list = ["ALL"]

requested_family_list = []
for requested_token in requested_token_list:
    if requested_token == "ALL":
        requested_family_list = ["All"]
        break
    if requested_token not in exact_family_order:
        raise ValueError(f"Unsupported exact-paper family selector | {requested_token}")
    if requested_token not in requested_family_list:
        requested_family_list.append(requested_token)

def normalize_path(path_text):
    return repository_path_support.normalize_repository_relative_path_text(path_text)

def config_direction_name(config_relative_path):
    normalized_path = f"/{normalize_path(config_relative_path).lower()}/"
    if "/forward/" in normalized_path:
        return "Forward"
    if "/backward/" in normalized_path:
        return "Backward"
    raise ValueError(f"Unable to resolve direction from config path | {config_relative_path}")

def config_family_name(config_relative_path):
    normalized_path = f"/{normalize_path(config_relative_path).lower()}/"
    for family in exact_family_order:
        if f"/{family.lower()}/" in normalized_path:
            return family
    raise ValueError(f"Unable to resolve family from config path | {config_relative_path}")

selected_config_path_list = []
selected_run_name_list = []
for config_relative_path in queue_path_list:
    normalized_config_path = normalize_path(config_relative_path)
    config_path = project_root / normalized_config_path
    run_name = yaml.safe_load(config_path.read_text(encoding="utf-8"))["experiment"]["run_name"]
    direction_matches = direction_name == "Both" or config_direction_name(config_relative_path) == direction_name
    family_matches = "All" in requested_family_list or config_family_name(config_relative_path) in requested_family_list
    if direction_matches and family_matches:
        selected_config_path_list.append(normalized_config_path)
        selected_run_name_list.append(run_name)

if not selected_config_path_list:
    raise ValueError(
        "No prepared exact-paper configs matched the requested launcher scope | "
        f"direction={direction_name} | families={','.join(requested_family_list)}"
    )

direction_slug = direction_name.lower()
family_slug = "all" if "All" in requested_family_list else "_".join(family.lower() for family in requested_family_list)
stage_slug = stage_name.lower()
scope_slug = f"{direction_slug}_{family_slug}_{stage_slug}"
base_output_directory = normalize_path(campaign_payload.get("campaign_output_directory"))
payload = {
    "campaign_name": f"{campaign_payload.get('campaign_name')}__{scope_slug}",
    "planning_report_path": normalize_path(campaign_payload.get("planning_report_path")),
    "campaign_output_directory": f"{base_output_directory}__{scope_slug}",
    "queue_config_path_list": selected_config_path_list,
    "run_name_list": selected_run_name_list,
    "requested_family_list": requested_family_list,
}
print(json.dumps(payload))
PYTHON
)"
QUEUE_BUNDLE_PATH="$(mktemp)"
trap 'rm -f "${QUEUE_BUNDLE_PATH}"' EXIT
printf '%s\n' "${QUEUE_BUNDLE_JSON}" > "${QUEUE_BUNDLE_PATH}"

CAMPAIGN_NAME="$(
    "${CONDA_COMMAND[@]}" run -n "${CONDA_ENVIRONMENT_NAME}" "${PYTHON_EXECUTABLE}" -c 'import json, sys; print(json.loads(open(sys.argv[1], encoding="utf-8").read())["campaign_name"])' "${QUEUE_BUNDLE_PATH}"
)"
PLANNING_REPORT_PATH="$(
    "${CONDA_COMMAND[@]}" run -n "${CONDA_ENVIRONMENT_NAME}" "${PYTHON_EXECUTABLE}" -c 'import json, sys; print(json.loads(open(sys.argv[1], encoding="utf-8").read())["planning_report_path"])' "${QUEUE_BUNDLE_PATH}"
)"
CAMPAIGN_OUTPUT_DIRECTORY="$(
    "${CONDA_COMMAND[@]}" run -n "${CONDA_ENVIRONMENT_NAME}" "${PYTHON_EXECUTABLE}" -c 'import json, sys; print(json.loads(open(sys.argv[1], encoding="utf-8").read())["campaign_output_directory"])' "${QUEUE_BUNDLE_PATH}"
)"
REQUESTED_FAMILIES="$(
    "${CONDA_COMMAND[@]}" run -n "${CONDA_ENVIRONMENT_NAME}" "${PYTHON_EXECUTABLE}" -c 'import json, sys; print(",".join(json.loads(open(sys.argv[1], encoding="utf-8").read())["requested_family_list"]))' "${QUEUE_BUNDLE_PATH}"
)"

mapfile -t QUEUE_CONFIG_PATH_LIST < <(
    "${CONDA_COMMAND[@]}" run -n "${CONDA_ENVIRONMENT_NAME}" "${PYTHON_EXECUTABLE}" -c 'import json, sys; [print(value) for value in json.loads(open(sys.argv[1], encoding="utf-8").read())["queue_config_path_list"]]' "${QUEUE_BUNDLE_PATH}"
)

CAMPAIGN_LOG_ROOT="${PROJECT_ROOT}/${CAMPAIGN_OUTPUT_DIRECTORY}/logs"
mkdir -p "${CAMPAIGN_LOG_ROOT}"

RUNNER_ARGUMENT_LIST=(--stage "${STAGE,,}")
if [[ -n "${BEST_PARAMETER_SUMMARY_PATH}" ]]; then
    RUNNER_ARGUMENT_LIST+=(--best-parameter-summary-path "${BEST_PARAMETER_SUMMARY_PATH}")
fi
if [[ "${GRID_SEARCH_VERBOSE_OVERRIDE}" -ge 0 ]]; then
    RUNNER_ARGUMENT_LIST+=(--grid-search-verbose-override "${GRID_SEARCH_VERBOSE_OVERRIDE}")
fi
if [[ "${HISTORICAL_CROSS_VALIDATE_VERBOSE_OVERRIDE}" -ge 0 ]]; then
    RUNNER_ARGUMENT_LIST+=(--historical-cross-validate-verbose-override "${HISTORICAL_CROSS_VALIDATE_VERBOSE_OVERRIDE}")
fi
if [[ "${NO_EVAL}" == "1" ]]; then
    RUNNER_ARGUMENT_LIST+=(--no-eval)
fi
if [[ "${NO_EXPORT}" == "1" ]]; then
    RUNNER_ARGUMENT_LIST+=(--no-export)
fi
RUNNER_ARGUMENT_LIST+=(--"${REPOSITORY_PATH_PLATFORM}")

echo "[INFO] Campaign Name | ${CAMPAIGN_NAME}"
echo "[INFO] Planning Report | ${PLANNING_REPORT_PATH}"
echo "[INFO] Campaign Output Root | ${CAMPAIGN_OUTPUT_DIRECTORY}"
echo "[INFO] Requested Direction | ${DIRECTION}"
echo "[INFO] Requested Families | ${REQUESTED_FAMILIES}"
echo "[INFO] Requested Stage | ${STAGE}"
echo "[INFO] Exact-Paper Run Count | ${#QUEUE_CONFIG_PATH_LIST[@]}"

if [[ "${DRY_RUN}" == "1" ]]; then
    echo "[INFO] Dry run requested; no training subprocesses will be launched."
    for CONFIG_RELATIVE_PATH in "${QUEUE_CONFIG_PATH_LIST[@]}"; do
        echo "DRY_RUN_CONFIG::${CONFIG_RELATIVE_PATH}"
    done
    exit 0
fi

CONFIG_INDEX=0
QUEUE_CONFIG_COUNT="${#QUEUE_CONFIG_PATH_LIST[@]}"
for CONFIG_RELATIVE_PATH in "${QUEUE_CONFIG_PATH_LIST[@]}"; do
    CONFIG_INDEX=$((CONFIG_INDEX + 1))
    CONFIG_PATH="${PROJECT_ROOT}/${CONFIG_RELATIVE_PATH}"
    CONFIG_FILE_NAME="$(basename "${CONFIG_RELATIVE_PATH}")"
    CONFIG_FILE_STEM="${CONFIG_FILE_NAME%.yaml}"
    RUN_LOG_PATH="${CAMPAIGN_LOG_ROOT}/${CONFIG_FILE_STEM}.log"
    COMPLETED_COUNT=$((CONFIG_INDEX - 1))
    REMAINING_COUNT=$((QUEUE_CONFIG_COUNT - COMPLETED_COUNT))

    echo "REMOTE_ACTIVE_CONFIG::${CONFIG_INDEX}::${QUEUE_CONFIG_COUNT}::${CONFIG_RELATIVE_PATH}"
    echo "REMOTE_ACTIVE_LOG::${CAMPAIGN_OUTPUT_DIRECTORY}/logs/${CONFIG_FILE_STEM}.log"
    echo "REMOTE_ACTIVE_STAGE::Preparing exact-paper validation subprocess"
    echo "[INFO] Campaign progress | completed=${COMPLETED_COUNT}/${QUEUE_CONFIG_COUNT} | remaining=${REMAINING_COUNT} | active_run=${CONFIG_FILE_STEM}"
    echo "[INFO] Running paper-faithful grid-search validation | ${CONFIG_PATH}"

    "${CONDA_COMMAND[@]}" run --no-capture-output -n "${CONDA_ENVIRONMENT_NAME}" "${PYTHON_EXECUTABLE}" "${RUNNER_PATH}" \
        --config-path "${CONFIG_RELATIVE_PATH}" \
        --output-suffix "campaign_validation" \
        "${RUNNER_ARGUMENT_LIST[@]}" 2>&1 | tee "${RUN_LOG_PATH}"
    NATIVE_EXIT_CODE="${PIPESTATUS[0]}"
    if [[ "${NATIVE_EXIT_CODE}" -ne 0 ]]; then
        echo "[ERROR] Paper-faithful grid-search campaign run failed | ${CONFIG_PATH}" >&2
        echo "[ERROR] Failing log file | ${RUN_LOG_PATH}" >&2
        exit "${NATIVE_EXIT_CODE}"
    fi

    echo "REMOTE_COMPLETED_CONFIG::${CONFIG_INDEX}::${QUEUE_CONFIG_COUNT}::${CONFIG_RELATIVE_PATH}"
    echo "REMOTE_ACTIVE_STAGE::Completed exact-paper validation subprocess"
    echo "[DONE] Exact-paper config complete | ${CONFIG_RELATIVE_PATH}"
done

echo "[DONE] Track 1 bidirectional paper-faithful grid-search campaign completed"
