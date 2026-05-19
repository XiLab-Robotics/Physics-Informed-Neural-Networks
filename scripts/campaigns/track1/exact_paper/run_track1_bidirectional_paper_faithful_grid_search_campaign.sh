#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"
ACTIVE_CAMPAIGN_PATH="${PROJECT_ROOT}/doc/running/active_training_campaign.yaml"
RUNNER_PATH="${PROJECT_ROOT}/scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py"

# shellcheck source=../../infrastructure/shared_streaming_campaign_launcher.sh
source "${PROJECT_ROOT}/scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh"

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
CONDA_ENVIRONMENT_NAME="pinns_env"
PYTHON_EXECUTABLE="python"
REPOSITORY_PATH_PLATFORM="linux"
DRY_RUN="0"
REMOTE="0"
REMOTE_HOST_ALIAS="${PINNS_REMOTE_TRAINING_HOST_ALIAS:-xilab-remote}"
REMOTE_REPOSITORY_PATH="${PINNS_REMOTE_TRAINING_REPO_PATH:-}"
REMOTE_CONDA_ENVIRONMENT_NAME="${PINNS_REMOTE_TRAINING_CONDA_ENV:-pinns_env}"

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
  --remote
  --remote-host-alias HOST
  --remote-repository-path PATH
  --remote-conda-environment-name NAME
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
        --remote)
            REMOTE="1"
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

CONDA_COMMAND="$(campaign_launcher_resolve_conda_command)"

mkdir -p ".temp/linux_portability"
QUEUE_BUNDLE_SCRIPT_PATH=".temp/linux_portability/track1_exact_paper_queue_bundle_$$.py"
cat > "${QUEUE_BUNDLE_SCRIPT_PATH}" <<'PYTHON'
from pathlib import Path
import sys
import yaml

project_root = Path.cwd()
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from scripts.tooling import repository_path_support

campaign_path = project_root / "doc" / "running" / "active_training_campaign.yaml"
direction_name = sys.argv[1]
family_name = sys.argv[2]
families_text = sys.argv[3]
stage_name = sys.argv[4]
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
print(f"CAMPAIGN_NAME\t{payload['campaign_name']}")
print(f"PLANNING_REPORT_PATH\t{payload['planning_report_path']}")
print(f"CAMPAIGN_OUTPUT_DIRECTORY\t{payload['campaign_output_directory']}")
print(f"REQUESTED_FAMILIES\t{','.join(payload['requested_family_list'])}")
for selected_config_path in payload["queue_config_path_list"]:
    print(f"QUEUE_CONFIG\t{selected_config_path}")
for selected_run_name in payload["run_name_list"]:
    print(f"RUN_NAME\t{selected_run_name}")
PYTHON
trap 'rm -f "${QUEUE_BUNDLE_SCRIPT_PATH}"' EXIT
QUEUE_BUNDLE_TEXT="$(
    "${CONDA_COMMAND}" run -n "${CONDA_ENVIRONMENT_NAME}" "${PYTHON_EXECUTABLE}" "${QUEUE_BUNDLE_SCRIPT_PATH}" "${DIRECTION}" "${FAMILY}" "${FAMILIES}" "${STAGE}"
)"
CAMPAIGN_NAME=""
PLANNING_REPORT_PATH=""
CAMPAIGN_OUTPUT_DIRECTORY=""
REQUESTED_FAMILIES=""
QUEUE_CONFIG_PATH_LIST=()
RUN_NAME_LIST=()
while IFS=$'\t' read -r bundle_key bundle_value; do
    bundle_value="${bundle_value%$'\r'}"
    case "${bundle_key}" in
        CAMPAIGN_NAME)
            CAMPAIGN_NAME="${bundle_value}"
            ;;
        PLANNING_REPORT_PATH)
            PLANNING_REPORT_PATH="${bundle_value}"
            ;;
        CAMPAIGN_OUTPUT_DIRECTORY)
            CAMPAIGN_OUTPUT_DIRECTORY="${bundle_value}"
            ;;
        REQUESTED_FAMILIES)
            REQUESTED_FAMILIES="${bundle_value}"
            ;;
        QUEUE_CONFIG)
            QUEUE_CONFIG_PATH_LIST+=("${bundle_value}")
            ;;
        RUN_NAME)
            RUN_NAME_LIST+=("${bundle_value}")
            ;;
    esac
done <<< "${QUEUE_BUNDLE_TEXT}"

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

if [[ "${REMOTE}" == "1" ]]; then
    REMOTE_WRAPPER_ARGUMENT_LIST=(
        --campaign-name "${CAMPAIGN_NAME}"
        --planning-report-path "${PLANNING_REPORT_PATH}"
        --launcher-relative-path "scripts/campaigns/track1/exact_paper/run_track1_bidirectional_paper_faithful_grid_search_campaign.sh"
        --campaign-output-root-override "${CAMPAIGN_OUTPUT_DIRECTORY}"
        --validation-output-root "output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank"
        --validation-report-root "doc/reports/analysis/validation_checks"
        --remote-host-alias "${REMOTE_HOST_ALIAS}"
        --remote-repository-path "${REMOTE_REPOSITORY_PATH}"
        --remote-conda-environment-name "${REMOTE_CONDA_ENVIRONMENT_NAME}"
    )
    if [[ "${DRY_RUN}" == "1" ]]; then
        REMOTE_WRAPPER_ARGUMENT_LIST+=(--dry-run)
    fi
    for config_relative_path in "${QUEUE_CONFIG_PATH_LIST[@]}"; do
        REMOTE_WRAPPER_ARGUMENT_LIST+=(--campaign-config-path "${config_relative_path}")
    done
    for run_name in "${RUN_NAME_LIST[@]}"; do
        REMOTE_WRAPPER_ARGUMENT_LIST+=(--run-name "${run_name}")
    done

    REMOTE_LAUNCHER_ARGUMENT_LIST=(
        --direction "${DIRECTION}"
        --families "${REQUESTED_FAMILIES}"
        --stage "${STAGE}"
    )
    if [[ -n "${BEST_PARAMETER_SUMMARY_PATH}" ]]; then
        REMOTE_LAUNCHER_ARGUMENT_LIST+=(--best-parameter-summary-path "${BEST_PARAMETER_SUMMARY_PATH}")
    fi
    if [[ "${GRID_SEARCH_VERBOSE_OVERRIDE}" -ge 0 ]]; then
        REMOTE_LAUNCHER_ARGUMENT_LIST+=(--grid-search-verbose-override "${GRID_SEARCH_VERBOSE_OVERRIDE}")
    fi
    if [[ "${HISTORICAL_CROSS_VALIDATE_VERBOSE_OVERRIDE}" -ge 0 ]]; then
        REMOTE_LAUNCHER_ARGUMENT_LIST+=(--historical-cross-validate-verbose-override "${HISTORICAL_CROSS_VALIDATE_VERBOSE_OVERRIDE}")
    fi
    if [[ "${NO_EVAL}" == "1" ]]; then
        REMOTE_LAUNCHER_ARGUMENT_LIST+=(--no-eval)
    fi
    if [[ "${NO_EXPORT}" == "1" ]]; then
        REMOTE_LAUNCHER_ARGUMENT_LIST+=(--no-export)
    fi
    REMOTE_LAUNCHER_ARGUMENT_LIST+=(--"${REPOSITORY_PATH_PLATFORM}")

    bash scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.sh \
        "${REMOTE_WRAPPER_ARGUMENT_LIST[@]}" \
        -- "${REMOTE_LAUNCHER_ARGUMENT_LIST[@]}"
    exit $?
fi

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

    campaign_launcher_run_with_streaming_log \
        --environment-name "${CONDA_ENVIRONMENT_NAME}" \
        --python-executable "${PYTHON_EXECUTABLE}" \
        --runner-script-path "${RUNNER_PATH}" \
        --config-path "${CONFIG_RELATIVE_PATH}" \
        --output-suffix "campaign_validation" \
        --log-path "${RUN_LOG_PATH}" \
        -- "${RUNNER_ARGUMENT_LIST[@]}"
    NATIVE_EXIT_CODE="$?"
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
