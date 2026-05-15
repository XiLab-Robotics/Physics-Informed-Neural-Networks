#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"

# shellcheck source=../../infrastructure/shared_streaming_campaign_launcher.sh
source "${PROJECT_ROOT}/scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh"

CAMPAIGN_NAME=""
PLANNING_REPORT_PATH=""
LAUNCHER_RELATIVE_PATH=""
CAMPAIGN_OUTPUT_ROOT_OVERRIDE=""
VALIDATION_OUTPUT_ROOT="output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward"
VALIDATION_REPORT_ROOT="doc/reports/analysis/validation_checks/track1/exact_paper/forward"
REMOTE_HOST_ALIAS="${STANDARDML_REMOTE_TRAINING_HOST_ALIAS:-xilab-remote}"
REMOTE_REPOSITORY_PATH="${STANDARDML_REMOTE_TRAINING_REPO_PATH:-}"
REMOTE_CONDA_ENVIRONMENT_NAME="${STANDARDML_REMOTE_TRAINING_CONDA_ENV:-standard_ml_codex_env}"
DRY_RUN="0"
CAMPAIGN_CONFIG_PATH_LIST=()
RUN_NAME_LIST=()
SOURCE_SYNC_PATH_LIST=(scripts config doc requirements.txt)
LAUNCHER_ARGUMENT_LIST=()

print_usage() {
    cat <<'USAGE'
Usage:
  bash scripts/campaigns/track1/exact_paper/run_exact_paper_campaign_remote.sh [options] -- [launcher arguments]

Options:
  --campaign-name NAME
  --planning-report-path PATH
  --launcher-relative-path PATH
  --campaign-config-path PATH             Repeat for multiple configs.
  --run-name NAME                         Repeat for multiple runs.
  --campaign-output-root-override PATH
  --validation-output-root PATH
  --validation-report-root PATH
  --source-sync-path PATH                 Repeat to replace default sync list.
  --remote-host-alias HOST
  --remote-repository-path PATH
  --remote-conda-environment-name NAME
  --dry-run
  --help
USAGE
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --campaign-name)
            CAMPAIGN_NAME="$2"
            shift 2
            ;;
        --planning-report-path)
            PLANNING_REPORT_PATH="$2"
            shift 2
            ;;
        --launcher-relative-path)
            LAUNCHER_RELATIVE_PATH="$2"
            shift 2
            ;;
        --campaign-config-path)
            CAMPAIGN_CONFIG_PATH_LIST+=("$2")
            shift 2
            ;;
        --run-name)
            RUN_NAME_LIST+=("$2")
            shift 2
            ;;
        --campaign-output-root-override)
            CAMPAIGN_OUTPUT_ROOT_OVERRIDE="$2"
            shift 2
            ;;
        --validation-output-root)
            VALIDATION_OUTPUT_ROOT="$2"
            shift 2
            ;;
        --validation-report-root)
            VALIDATION_REPORT_ROOT="$2"
            shift 2
            ;;
        --source-sync-path)
            if [[ "${#SOURCE_SYNC_PATH_LIST[@]}" -eq 4 && "${SOURCE_SYNC_PATH_LIST[*]}" == "scripts config doc requirements.txt" ]]; then
                SOURCE_SYNC_PATH_LIST=()
            fi
            SOURCE_SYNC_PATH_LIST+=("$2")
            shift 2
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
        --dry-run)
            DRY_RUN="1"
            shift
            ;;
        --help|-h)
            print_usage
            exit 0
            ;;
        --)
            shift
            LAUNCHER_ARGUMENT_LIST+=("$@")
            break
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            print_usage >&2
            exit 2
            ;;
    esac
done

if [[ -z "${CAMPAIGN_NAME}" || -z "${PLANNING_REPORT_PATH}" || -z "${LAUNCHER_RELATIVE_PATH}" ]]; then
    echo "[ERROR] Campaign name, planning report path, and launcher relative path are required." >&2
    exit 2
fi
if [[ -z "${REMOTE_REPOSITORY_PATH}" ]]; then
    echo "[ERROR] Remote repository path is required through --remote-repository-path or STANDARDML_REMOTE_TRAINING_REPO_PATH." >&2
    exit 2
fi
if [[ "${#CAMPAIGN_CONFIG_PATH_LIST[@]}" -eq 0 ]]; then
    echo "[ERROR] At least one campaign config path is required." >&2
    exit 2
fi

CAMPAIGN_OUTPUT_ROOT="${CAMPAIGN_OUTPUT_ROOT_OVERRIDE:-output/training_campaigns/track1/exact_paper/forward/${CAMPAIGN_NAME}}"
RUN_TIMESTAMP="$(date +"%Y-%m-%d-%H-%M-%S")"
REMOTE_TRACKING_ROOT=".temp/remote_training_campaigns/${RUN_TIMESTAMP}_${CAMPAIGN_NAME//[^A-Za-z0-9]/_}"
RUN_LOG_PATH="${PROJECT_ROOT}/${REMOTE_TRACKING_ROOT}/remote_training_campaign.log"
mkdir -p "$(dirname "${RUN_LOG_PATH}")"

echo "[INFO] Campaign Name | ${CAMPAIGN_NAME}"
echo "[INFO] Planning Report | ${PLANNING_REPORT_PATH}"
echo "[INFO] Campaign Output Root | ${CAMPAIGN_OUTPUT_ROOT}"
echo "[INFO] Exact-Paper Run Count | ${#CAMPAIGN_CONFIG_PATH_LIST[@]}"
echo "[INFO] Remote Host Alias | ${REMOTE_HOST_ALIAS}"
echo "[INFO] Remote Repository Path | ${REMOTE_REPOSITORY_PATH}"
echo "[INFO] Remote Conda Environment | ${REMOTE_CONDA_ENVIRONMENT_NAME}"

if [[ "${DRY_RUN}" == "1" ]]; then
    echo "[INFO] Dry run requested; no SSH, sync, or training command will be launched."
    REMOTE_ARGUMENT_TEXT="$(campaign_launcher_join_command "${LAUNCHER_ARGUMENT_LIST[@]}")"
    printf 'DRY_RUN_SOURCE_SYNC::%s\n' "${SOURCE_SYNC_PATH_LIST[@]}"
    printf 'DRY_RUN_CONFIG::%s\n' "${CAMPAIGN_CONFIG_PATH_LIST[@]}"
    printf 'DRY_RUN_RUN_NAME::%s\n' "${RUN_NAME_LIST[@]}"
    printf 'DRY_RUN_REMOTE_COMMAND::cd %q && bash %q %s\n' \
        "${REMOTE_REPOSITORY_PATH}" \
        "${LAUNCHER_RELATIVE_PATH}" \
        "${REMOTE_ARGUMENT_TEXT}"
    exit 0
fi

command -v ssh >/dev/null 2>&1 || { echo "[ERROR] ssh is not available." >&2; exit 127; }
command -v tar >/dev/null 2>&1 || { echo "[ERROR] tar is not available." >&2; exit 127; }

echo "[STEP] Checking remote reachability"
ssh "${REMOTE_HOST_ALIAS}" "mkdir -p '${REMOTE_REPOSITORY_PATH}'"

echo "[STEP] Syncing local repository source paths to remote Linux host"
tar -C "${PROJECT_ROOT}" -cf - "${SOURCE_SYNC_PATH_LIST[@]}" |
    ssh "${REMOTE_HOST_ALIAS}" "tar -C '${REMOTE_REPOSITORY_PATH}' -xf -"

echo "[STEP] Verifying required remote paths"
ssh "${REMOTE_HOST_ALIAS}" "cd '${REMOTE_REPOSITORY_PATH}' && test -f '${LAUNCHER_RELATIVE_PATH}' && test -f '${PLANNING_REPORT_PATH}'"
for config_path in "${CAMPAIGN_CONFIG_PATH_LIST[@]}"; do
    ssh "${REMOTE_HOST_ALIAS}" "cd '${REMOTE_REPOSITORY_PATH}' && test -f '${config_path}'"
done

REMOTE_ARGUMENT_LIST=(
    --conda-environment-name
    "${REMOTE_CONDA_ENVIRONMENT_NAME}"
    "${LAUNCHER_ARGUMENT_LIST[@]}"
)
REMOTE_ARGUMENT_TEXT="$(campaign_launcher_join_command "${REMOTE_ARGUMENT_LIST[@]}")"

echo "[STEP] Launching remote exact-paper campaign"
ssh "${REMOTE_HOST_ALIAS}" "cd '${REMOTE_REPOSITORY_PATH}' && bash '${LAUNCHER_RELATIVE_PATH}' ${REMOTE_ARGUMENT_TEXT}" 2>&1 | tee "${RUN_LOG_PATH}"
NATIVE_EXIT_CODE="${PIPESTATUS[0]}"
if [[ "${NATIVE_EXIT_CODE}" -ne 0 ]]; then
    echo "[ERROR] Remote exact-paper campaign failed | campaign=${CAMPAIGN_NAME} | log=${RUN_LOG_PATH}" >&2
    exit "${NATIVE_EXIT_CODE}"
fi

echo "[DONE] Remote exact-paper campaign completed successfully"
echo "[DONE] Remote wrapper log available under | ${RUN_LOG_PATH}"
