#!/usr/bin/env bash

# Launch a repository-owned training campaign on a Linux remote host and sync
# the completed campaign artifacts back to the local repository.

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../.." && pwd)"

REMOTE_HOST_ALIAS="${PINNS_REMOTE_TRAINING_HOST:-xilab-remote}"
REMOTE_REPOSITORY_PATH="${PINNS_REMOTE_TRAINING_REPO_PATH:-}"
REMOTE_CONDA_ENVIRONMENT_NAME="${PINNS_REMOTE_TRAINING_CONDA_ENV:-pinns_env}"
CAMPAIGN_NAME=""
PLANNING_REPORT_PATH=""
DRY_RUN="0"
CAMPAIGN_CONFIG_PATH_LIST=()
SOURCE_SYNC_PATH_LIST=("scripts" "config" "doc" "requirements.txt")

print_usage() {
    cat <<'USAGE'
Usage:
  bash scripts/campaigns/infrastructure/run_remote_training_campaign.sh \
    --campaign-name NAME \
    --planning-report-path PATH \
    --campaign-config-path PATH [--campaign-config-path PATH ...] \
    --remote-repository-path PATH

Options:
  --campaign-config-path PATH       Repository-relative campaign YAML path. Repeatable.
  --campaign-name NAME              Campaign name passed to run_training_campaign.py.
  --planning-report-path PATH       Repository-relative planning report path.
  --remote-host-alias HOST          SSH host alias. Defaults to PINNS_REMOTE_TRAINING_HOST or xilab-remote.
  --remote-repository-path PATH     Repository root on the Linux remote host.
  --remote-conda-environment NAME   Conda environment on the Linux remote host.
  --source-sync-path PATH           Repository-relative path to sync. Repeatable; overrides defaults.
  --dry-run                         Print resolved actions without SSH or training execution.
  --help                            Show this help text.
USAGE
}

normalize_repository_relative_path() {
    local raw_path="$1"
    raw_path="${raw_path//\\//}"
    raw_path="${raw_path#./}"
    raw_path="${raw_path#/}"
    printf '%s\n' "${raw_path}"
}

join_shell_command() {
    local command_text=""
    local argument_text

    for argument_text in "$@"; do
        if [[ -z "${command_text}" ]]; then
            printf -v command_text "%q" "${argument_text}"
        else
            printf -v command_text "%s %q" "${command_text}" "${argument_text}"
        fi
    done

    echo "${command_text}"
}

join_quoted_argument_list() {
    local command_text=""
    local argument_text

    for argument_text in "$@"; do
        if [[ -z "${command_text}" ]]; then
            printf -v command_text "%q" "${argument_text}"
        else
            printf -v command_text "%s %q" "${command_text}" "${argument_text}"
        fi
    done

    echo "${command_text}"
}

parse_arguments() {
    local source_sync_overridden="0"

    while [[ $# -gt 0 ]]; do
        case "$1" in
            --campaign-config-path)
                CAMPAIGN_CONFIG_PATH_LIST+=("$(normalize_repository_relative_path "$2")")
                shift 2
                ;;
            --campaign-name)
                CAMPAIGN_NAME="$2"
                shift 2
                ;;
            --planning-report-path)
                PLANNING_REPORT_PATH="$(normalize_repository_relative_path "$2")"
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
            --remote-conda-environment)
                REMOTE_CONDA_ENVIRONMENT_NAME="$2"
                shift 2
                ;;
            --source-sync-path)
                if [[ "${source_sync_overridden}" == "0" ]]; then
                    SOURCE_SYNC_PATH_LIST=()
                    source_sync_overridden="1"
                fi
                SOURCE_SYNC_PATH_LIST+=("$(normalize_repository_relative_path "$2")")
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
}

validate_inputs() {
    if [[ "${#CAMPAIGN_CONFIG_PATH_LIST[@]}" -eq 0 ]]; then
        echo "[ERROR] At least one --campaign-config-path is required." >&2
        exit 2
    fi
    if [[ -z "${CAMPAIGN_NAME}" ]]; then
        echo "[ERROR] --campaign-name is required." >&2
        exit 2
    fi
    if [[ -z "${PLANNING_REPORT_PATH}" ]]; then
        echo "[ERROR] --planning-report-path is required." >&2
        exit 2
    fi
    if [[ -z "${REMOTE_REPOSITORY_PATH}" ]]; then
        echo "[ERROR] --remote-repository-path is required or set PINNS_REMOTE_TRAINING_REPO_PATH." >&2
        exit 2
    fi

    local relative_path
    for relative_path in "${CAMPAIGN_CONFIG_PATH_LIST[@]}" "${PLANNING_REPORT_PATH}" "${SOURCE_SYNC_PATH_LIST[@]}"; do
        if [[ ! -e "${PROJECT_ROOT}/${relative_path}" ]]; then
            echo "[ERROR] Repository-relative path does not exist | ${relative_path}" >&2
            exit 2
        fi
    done
}

write_status_file() {
    local run_status="$1"
    local stage="$2"
    local log_path="$3"
    local remote_campaign_output_directory="${4:-}"
    local remote_manifest_path="${5:-}"

    mkdir -p "${PROJECT_ROOT}/doc/running"
    cat >"${PROJECT_ROOT}/doc/running/remote_training_campaign_status.json" <<EOF
{
  "run_status": "${run_status}",
  "stage": "${stage}",
  "remote_host_alias": "${REMOTE_HOST_ALIAS}",
  "remote_repository_path": "${REMOTE_REPOSITORY_PATH}",
  "remote_conda_environment_name": "${REMOTE_CONDA_ENVIRONMENT_NAME}",
  "campaign_name": "${CAMPAIGN_NAME}",
  "planning_report_path": "${PLANNING_REPORT_PATH}",
  "local_log_path": "${log_path}",
  "remote_campaign_output_directory": "${remote_campaign_output_directory}",
  "remote_manifest_path": "${remote_manifest_path}",
  "updated_at": "$(date -Iseconds)"
}
EOF
}

sync_sources_to_remote() {
    echo "[STEP] Syncing local source paths to remote repository"
    tar -C "${PROJECT_ROOT}" -cf - "${SOURCE_SYNC_PATH_LIST[@]}" |
        ssh "${REMOTE_HOST_ALIAS}" "mkdir -p $(printf '%q' "${REMOTE_REPOSITORY_PATH}") && tar -C $(printf '%q' "${REMOTE_REPOSITORY_PATH}") -xf -"
}

build_remote_command() {
    local remote_script
    local config_arguments=""
    local config_path

    for config_path in "${CAMPAIGN_CONFIG_PATH_LIST[@]}"; do
        config_arguments+=" $(printf '%q' "${config_path}")"
    done

    remote_script=$(cat <<EOF
set -euo pipefail
cd $(printf '%q' "${REMOTE_REPOSITORY_PATH}")
conda run --no-capture-output -n $(printf '%q' "${REMOTE_CONDA_ENVIRONMENT_NAME}") python -B scripts/training/run_training_campaign.py${config_arguments} --campaign-name $(printf '%q' "${CAMPAIGN_NAME}") --planning-report-path $(printf '%q' "${PLANNING_REPORT_PATH}")
remote_manifest_path="\$(find output/training_campaigns -type f -name campaign_manifest.yaml -path "*${CAMPAIGN_NAME}*" -printf '%T@ %p\n' | sort -n | tail -1 | cut -d' ' -f2-)"
if [[ -z "\${remote_manifest_path}" ]]; then
    echo "REMOTE_RUN_OUTPUT_DIRECTORY_NOT_FOUND"
    exit 3
fi
remote_output_directory="\$(dirname "\${remote_manifest_path}")"
remote_sync_manifest_path=".temp/remote_training_sync_manifest.json"
mkdir -p .temp
conda run --no-capture-output -n $(printf '%q' "${REMOTE_CONDA_ENVIRONMENT_NAME}") python -B scripts/training/build_remote_training_sync_manifest.py --campaign-manifest-path "\${remote_manifest_path}" --output-path "\${remote_sync_manifest_path}"
echo "REMOTE_CAMPAIGN_OUTPUT_DIRECTORY::\${remote_output_directory}"
echo "REMOTE_CAMPAIGN_MANIFEST_PATH::\${remote_manifest_path}"
echo "REMOTE_SYNC_MANIFEST_PATH::\${remote_sync_manifest_path}"
EOF
)

    printf '%s\n' "${remote_script}"
}

sync_remote_paths_to_local() {
    local sync_manifest_path="$1"
    local sync_path_list

    ssh "${REMOTE_HOST_ALIAS}" "cd $(printf '%q' "${REMOTE_REPOSITORY_PATH}") && tar -cf - $(printf '%q' "${sync_manifest_path}")" |
        tar -C "${PROJECT_ROOT}" -xf -

    mapfile -t sync_path_list < <(
        python - <<PY
import json
from pathlib import Path
payload = json.loads(Path("${PROJECT_ROOT}/${sync_manifest_path}").read_text(encoding="utf-8"))
for path in payload.get("sync_path_list", []):
    print(path)
PY
    )

    if [[ "${#sync_path_list[@]}" -eq 0 ]]; then
        echo "[WARN] Remote sync manifest did not contain artifact paths."
        return 0
    fi

    echo "[STEP] Syncing remote campaign artifacts back to local repository"
    ssh "${REMOTE_HOST_ALIAS}" "cd $(printf '%q' "${REMOTE_REPOSITORY_PATH}") && tar -cf - $(join_quoted_argument_list "${sync_path_list[@]}")" |
        tar -C "${PROJECT_ROOT}" -xf -
}

main() {
    parse_arguments "$@"
    validate_inputs

    local run_timestamp
    run_timestamp="$(date +"%Y-%m-%d-%H-%M-%S")"
    local tracking_directory="${PROJECT_ROOT}/.temp/remote_training_campaigns/${run_timestamp}_${CAMPAIGN_NAME}"
    local log_path="${tracking_directory}/remote_training_campaign.log"
    mkdir -p "${tracking_directory}"

    echo "[INFO] Remote Host | ${REMOTE_HOST_ALIAS}"
    echo "[INFO] Remote Repository | ${REMOTE_REPOSITORY_PATH}"
    echo "[INFO] Remote Conda Environment | ${REMOTE_CONDA_ENVIRONMENT_NAME}"
    echo "[INFO] Campaign Name | ${CAMPAIGN_NAME}"
    echo "[INFO] Planning Report | ${PLANNING_REPORT_PATH}"
    printf '[INFO] Campaign Config | %s\n' "${CAMPAIGN_CONFIG_PATH_LIST[@]}"

    if [[ "${DRY_RUN}" == "1" ]]; then
        echo "[INFO] Dry run requested; remote sync and training were not launched."
        echo "DRY_RUN_REMOTE_COMMAND::ssh ${REMOTE_HOST_ALIAS} $(join_shell_command bash -lc "$(build_remote_command)")"
        return 0
    fi

    write_status_file "running" "sync_up" "${log_path}"
    sync_sources_to_remote

    write_status_file "running" "remote_run" "${log_path}"
    local remote_output
    remote_output="$(ssh "${REMOTE_HOST_ALIAS}" "bash -lc $(printf '%q' "$(build_remote_command)")" 2>&1 | tee "${log_path}")"

    local remote_campaign_output_directory
    local remote_manifest_path
    local remote_sync_manifest_path
    remote_campaign_output_directory="$(printf '%s\n' "${remote_output}" | sed -n 's/^REMOTE_CAMPAIGN_OUTPUT_DIRECTORY:://p' | tail -1)"
    remote_manifest_path="$(printf '%s\n' "${remote_output}" | sed -n 's/^REMOTE_CAMPAIGN_MANIFEST_PATH:://p' | tail -1)"
    remote_sync_manifest_path="$(printf '%s\n' "${remote_output}" | sed -n 's/^REMOTE_SYNC_MANIFEST_PATH:://p' | tail -1)"

    if [[ -z "${remote_manifest_path}" || -z "${remote_sync_manifest_path}" ]]; then
        write_status_file "failed" "remote_run" "${log_path}"
        echo "[ERROR] Remote campaign completed without manifest markers." >&2
        return 3
    fi

    write_status_file "running" "sync_down" "${log_path}" "${remote_campaign_output_directory}" "${remote_manifest_path}"
    sync_remote_paths_to_local "${remote_sync_manifest_path}"
    write_status_file "completed" "completed" "${log_path}" "${remote_campaign_output_directory}" "${remote_manifest_path}"

    echo "[STEP] Refreshing local training results master summary"
    python -B "${PROJECT_ROOT}/scripts/reports/analysis/generate_training_results_master_summary.py" || {
        echo "[WARN] Local training results master summary refresh returned a non-zero exit code"
    }
    echo "[DONE] Remote training campaign completed and artifacts synchronized"
}

main "$@"
