#!/usr/bin/env bash

# Shared Bash utilities for campaign launchers.

campaign_launcher_resolve_project_root() {
    local anchor_directory="$1"
    cd "${anchor_directory}/../../.." && pwd
}

campaign_launcher_resolve_conda_command() {
    if command -v conda >/dev/null 2>&1; then
        echo "conda"
        return 0
    fi

    if [[ -n "${CONDA_EXE:-}" ]]; then
        echo "${CONDA_EXE}"
        return 0
    fi

    if command -v conda.exe >/dev/null 2>&1; then
        echo "conda.exe"
        return 0
    fi

    echo "[ERROR] Unable to resolve conda on PATH." >&2
    return 127
}

campaign_launcher_join_command() {
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

campaign_launcher_run_with_streaming_log() {
    local environment_name=""
    local python_executable="python"
    local runner_script_path=""
    local config_path=""
    local output_suffix="campaign_run"
    local log_path=""
    local dry_run="0"
    local additional_argument_list=()

    while [[ $# -gt 0 ]]; do
        case "$1" in
            --environment-name)
                environment_name="$2"
                shift 2
                ;;
            --python-executable)
                python_executable="$2"
                shift 2
                ;;
            --runner-script-path)
                runner_script_path="$2"
                shift 2
                ;;
            --config-path)
                config_path="$2"
                shift 2
                ;;
            --output-suffix)
                output_suffix="$2"
                shift 2
                ;;
            --log-path)
                log_path="$2"
                shift 2
                ;;
            --dry-run)
                dry_run="1"
                shift
                ;;
            --)
                shift
                additional_argument_list+=("$@")
                break
                ;;
            *)
                echo "[ERROR] Unsupported shared launcher argument | $1" >&2
                return 2
                ;;
        esac
    done

    if [[ -z "${environment_name}" ]]; then
        echo "[ERROR] Missing --environment-name." >&2
        return 2
    fi
    if [[ -z "${runner_script_path}" ]]; then
        echo "[ERROR] Missing --runner-script-path." >&2
        return 2
    fi
    if [[ -z "${config_path}" ]]; then
        echo "[ERROR] Missing --config-path." >&2
        return 2
    fi
    if [[ -z "${log_path}" ]]; then
        echo "[ERROR] Missing --log-path." >&2
        return 2
    fi

    local conda_command
    conda_command="$(campaign_launcher_resolve_conda_command)" || return $?
    local log_directory_path
    log_directory_path="$(dirname "${log_path}")"
    mkdir -p "${log_directory_path}"

    local command_list=(
        "${conda_command}"
        run
        --no-capture-output
        -n
        "${environment_name}"
        "${python_executable}"
        "${runner_script_path}"
        --config-path
        "${config_path}"
        --output-suffix
        "${output_suffix}"
        "${additional_argument_list[@]}"
    )

    echo "[INFO] Command | $(campaign_launcher_join_command "${command_list[@]}")"
    echo "[INFO] Log Path | ${log_path}"

    if [[ "${dry_run}" == "1" ]]; then
        echo "[INFO] Dry run requested; command was not launched."
        return 0
    fi

    "${command_list[@]}" 2>&1 | tee "${log_path}"
    local native_exit_code="${PIPESTATUS[0]}"
    return "${native_exit_code}"
}
