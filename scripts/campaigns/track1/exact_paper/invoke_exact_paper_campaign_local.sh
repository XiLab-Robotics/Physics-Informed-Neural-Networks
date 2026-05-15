#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"

# shellcheck source=../../infrastructure/shared_streaming_campaign_launcher.sh
source "${PROJECT_ROOT}/scripts/campaigns/infrastructure/shared_streaming_campaign_launcher.sh"

invoke_exact_paper_campaign_local_usage() {
    cat <<'USAGE'
Usage:
  bash scripts/campaigns/track1/exact_paper/invoke_exact_paper_campaign_local.sh [options] -- [runner arguments]

Options:
  --campaign-name NAME
  --planning-report-path PATH
  --campaign-config-root PATH
  --campaign-config-file NAME            Repeat for multiple configs.
  --campaign-config-file-list "A.yaml,B.yaml"
  --campaign-output-root-override PATH
  --runner-script-path PATH
  --output-suffix TEXT
  --conda-environment-name NAME
  --python-executable COMMAND
  --dry-run
  --help
USAGE
}

invoke_exact_paper_campaign_local() {
    local campaign_name=""
    local planning_report_path=""
    local campaign_config_root=""
    local campaign_output_root_override=""
    local runner_script_path="scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py"
    local output_suffix="campaign_run"
    local conda_environment_name="standard_ml_codex_env"
    local python_executable="python"
    local dry_run="0"
    local campaign_config_file_name_list=()
    local runner_argument_list=()

    while [[ $# -gt 0 ]]; do
        case "$1" in
            --campaign-name)
                campaign_name="$2"
                shift 2
                ;;
            --planning-report-path)
                planning_report_path="$2"
                shift 2
                ;;
            --campaign-config-root)
                campaign_config_root="$2"
                shift 2
                ;;
            --campaign-config-file)
                campaign_config_file_name_list+=("$2")
                shift 2
                ;;
            --campaign-config-file-list)
                IFS=',' read -r -a campaign_config_file_name_list <<< "$2"
                shift 2
                ;;
            --campaign-output-root-override)
                campaign_output_root_override="$2"
                shift 2
                ;;
            --runner-script-path)
                runner_script_path="$2"
                shift 2
                ;;
            --output-suffix)
                output_suffix="$2"
                shift 2
                ;;
            --conda-environment-name)
                conda_environment_name="$2"
                shift 2
                ;;
            --python-executable)
                python_executable="$2"
                shift 2
                ;;
            --dry-run)
                dry_run="1"
                shift
                ;;
            --help|-h)
                invoke_exact_paper_campaign_local_usage
                return 0
                ;;
            --)
                shift
                runner_argument_list+=("$@")
                break
                ;;
            *)
                echo "[ERROR] Unsupported argument | $1" >&2
                invoke_exact_paper_campaign_local_usage >&2
                return 2
                ;;
        esac
    done

    if [[ -z "${campaign_name}" || -z "${planning_report_path}" || -z "${campaign_config_root}" ]]; then
        echo "[ERROR] Campaign name, planning report path, and config root are required." >&2
        return 2
    fi
    if [[ "${#campaign_config_file_name_list[@]}" -eq 0 ]]; then
        echo "[ERROR] At least one campaign config file is required." >&2
        return 2
    fi

    local campaign_output_root
    if [[ -z "${campaign_output_root_override}" ]]; then
        campaign_output_root="output/training_campaigns/track1/exact_paper/${campaign_name}"
    else
        campaign_output_root="${campaign_output_root_override}"
    fi
    local campaign_log_root="${PROJECT_ROOT}/${campaign_output_root}/logs"
    mkdir -p "${campaign_log_root}"

    echo "[INFO] Campaign Name | ${campaign_name}"
    echo "[INFO] Planning Report | ${planning_report_path}"
    echo "[INFO] Campaign Output Root | ${campaign_output_root}"
    echo "[INFO] Exact-Paper Run Count | ${#campaign_config_file_name_list[@]}"

    local config_index=0
    local config_count="${#campaign_config_file_name_list[@]}"
    local config_file_name
    for config_file_name in "${campaign_config_file_name_list[@]}"; do
        config_index=$((config_index + 1))
        config_file_name="${config_file_name#"${config_file_name%%[![:space:]]*}"}"
        config_file_name="${config_file_name%"${config_file_name##*[![:space:]]}"}"
        local config_path="${campaign_config_root}/${config_file_name}"
        local config_file_stem
        config_file_stem="$(basename "${config_file_name}")"
        config_file_stem="${config_file_stem%.yaml}"
        local run_log_path="${campaign_log_root}/${config_file_stem}.log"

        echo "REMOTE_ACTIVE_CONFIG::${config_index}::${config_count}::${config_path}"
        echo "REMOTE_ACTIVE_LOG::${run_log_path}"
        echo "REMOTE_ACTIVE_STAGE::Preparing exact-paper validation subprocess"
        echo "[INFO] Exact-Paper Campaign Progress ${config_index}/${config_count} | ${config_path}"

        campaign_launcher_run_with_streaming_log \
            --environment-name "${conda_environment_name}" \
            --python-executable "${python_executable}" \
            --runner-script-path "${runner_script_path}" \
            --config-path "${config_path}" \
            --output-suffix "${output_suffix}" \
            --log-path "${run_log_path}" \
            $([[ "${dry_run}" == "1" ]] && echo "--dry-run") \
            -- "${runner_argument_list[@]}"

        local native_exit_code="$?"
        if [[ "${native_exit_code}" -ne 0 ]]; then
            echo "[ERROR] Exact-paper campaign run failed | ${config_path}" >&2
            echo "[ERROR] Failing log file | ${run_log_path}" >&2
            return "${native_exit_code}"
        fi

        echo "REMOTE_COMPLETED_CONFIG::${config_index}::${config_count}::${config_path}"
        echo "REMOTE_ACTIVE_STAGE::Completed exact-paper validation subprocess"
        echo "[DONE] Exact-paper config complete | ${config_path}"
    done

    echo "[DONE] Exact-paper campaign completed successfully"
    echo "[DONE] Campaign logs available under | ${campaign_log_root}"
    return 0
}

if [[ "${BASH_SOURCE[0]}" == "$0" ]]; then
    invoke_exact_paper_campaign_local "$@"
fi
