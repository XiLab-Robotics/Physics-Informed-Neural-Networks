#!/usr/bin/env bash

# Linux adapter for legacy Track 1 exact-paper PowerShell launch metadata.

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"

SOURCE_POWERSHELL_SCRIPT=""
CONDA_ENVIRONMENT_NAME="pinns_env"
PYTHON_EXECUTABLE="python"
REMOTE_HOST_ALIAS="${PINNS_REMOTE_TRAINING_HOST_ALIAS:-xilab-remote}"
REMOTE_REPOSITORY_PATH="${PINNS_REMOTE_TRAINING_REPO_PATH:-}"
REMOTE_CONDA_ENVIRONMENT_NAME="${PINNS_REMOTE_TRAINING_CONDA_ENV:-pinns_env}"
REMOTE_MODE="0"
DRY_RUN="0"

METADATA_PYTHON_EXECUTABLE=""

print_usage() {
    cat <<'USAGE'
Usage:
  bash scripts/campaigns/track_1/exact_paper/run_exact_paper_campaign_from_powershell_metadata.sh \
    --source-powershell-script PATH [options]

Options:
  --source-powershell-script PATH       PowerShell launcher to read metadata from.
  --remote                             Launch through the Linux remote exact-paper wrapper.
  --remote-host-alias HOST             SSH host alias for remote mode.
  --remote-repository-path PATH        Repository root on the remote Linux host.
  --remote-conda-environment-name NAME Conda environment on the remote Linux host.
  --conda-environment-name NAME        Local Conda environment.
  --python-executable COMMAND          Local Python executable.
  --dry-run                            Print resolved runs without launching training.
  --help                               Show this help text.
USAGE
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --source-powershell-script)
            SOURCE_POWERSHELL_SCRIPT="$2"
            shift 2
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

if [[ -z "${SOURCE_POWERSHELL_SCRIPT}" ]]; then
    echo "[ERROR] --source-powershell-script is required." >&2
    exit 2
fi
if command -v python >/dev/null 2>&1; then
    METADATA_PYTHON_EXECUTABLE="python"
elif command -v python3 >/dev/null 2>&1; then
    METADATA_PYTHON_EXECUTABLE="python3"
else
    echo "[ERROR] Neither python nor python3 is available for launcher metadata parsing." >&2
    exit 127
fi

METADATA_JSON="$(
    "${METADATA_PYTHON_EXECUTABLE}" - "${SOURCE_POWERSHELL_SCRIPT}" "${PROJECT_ROOT}" <<'PY'
import json
import re
import sys
from pathlib import Path

source_path = Path(sys.argv[1]).resolve()
project_root = Path(sys.argv[2]).resolve()
text = source_path.read_text(encoding="utf-8-sig")


def normalize_path(path_text: str) -> str:
    normalized = path_text.replace("\\", "/").strip().strip("/")
    return normalized


def read_scalar(variable_name: str) -> str:
    pattern = re.compile(rf"\${re.escape(variable_name)}\s*=\s*\"([^\"]+)\"", re.IGNORECASE)
    match = pattern.search(text)
    if not match:
        raise SystemExit(f"Missing ${variable_name} in {source_path}")
    return normalize_path(match.group(1))


def read_file_name_list() -> list[str]:
    block_match = re.search(
        r"\$campaignConfigFileNameList\s*=\s*@\((.*?)\)",
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if block_match:
        return re.findall(r"\"([^\"]+\.ya?ml)\"", block_match.group(1), flags=re.IGNORECASE)

    join_path_file_name_list = re.findall(
        r"Join-Path\s+\$campaignConfigRoot\s+\"([^\"]+\.ya?ml)\"",
        text,
        flags=re.IGNORECASE,
    )
    if join_path_file_name_list:
        unique_file_name_list: list[str] = []
        seen_file_name_set: set[str] = set()
        for file_name in join_path_file_name_list:
            if file_name in seen_file_name_set:
                continue
            seen_file_name_set.add(file_name)
            unique_file_name_list.append(file_name)
        return unique_file_name_list

    config_root = read_scalar("campaignConfigRoot")
    config_root_path = project_root / config_root
    return sorted(child.name for child in config_root_path.glob("*.yaml"))


campaign_config_root = read_scalar("campaignConfigRoot")
planning_report_path = read_scalar("planningReportPath")
campaign_name = read_scalar("campaignName")
config_file_name_list = read_file_name_list()

if not config_file_name_list:
    raise SystemExit(f"No YAML configs resolved from {source_path}")

payload = {
    "campaign_config_root": campaign_config_root,
    "planning_report_path": planning_report_path,
    "campaign_name": campaign_name,
    "config_file_name_list": config_file_name_list,
    "launcher_relative_path": normalize_path(str(source_path.relative_to(project_root))).replace(".ps1", ".sh"),
}
print(json.dumps(payload))
PY
)"

CAMPAIGN_CONFIG_ROOT="$("${METADATA_PYTHON_EXECUTABLE}" -c 'import json,sys; print(json.loads(sys.argv[1])["campaign_config_root"])' "${METADATA_JSON}")"
PLANNING_REPORT_PATH="$("${METADATA_PYTHON_EXECUTABLE}" -c 'import json,sys; print(json.loads(sys.argv[1])["planning_report_path"])' "${METADATA_JSON}")"
CAMPAIGN_NAME="$("${METADATA_PYTHON_EXECUTABLE}" -c 'import json,sys; print(json.loads(sys.argv[1])["campaign_name"])' "${METADATA_JSON}")"
LAUNCHER_RELATIVE_PATH="$("${METADATA_PYTHON_EXECUTABLE}" -c 'import json,sys; print(json.loads(sys.argv[1])["launcher_relative_path"])' "${METADATA_JSON}")"
mapfile -t CONFIG_FILE_NAME_LIST < <("${METADATA_PYTHON_EXECUTABLE}" -c 'import json,sys; [print(x) for x in json.loads(sys.argv[1])["config_file_name_list"]]' "${METADATA_JSON}")

if [[ "${REMOTE_MODE}" == "1" ]]; then
    REMOTE_ARGUMENT_LIST=(
        --campaign-name "${CAMPAIGN_NAME}"
        --planning-report-path "${PLANNING_REPORT_PATH}"
        --launcher-relative-path "${LAUNCHER_RELATIVE_PATH}"
        --remote-host-alias "${REMOTE_HOST_ALIAS}"
        --remote-repository-path "${REMOTE_REPOSITORY_PATH}"
        --remote-conda-environment-name "${REMOTE_CONDA_ENVIRONMENT_NAME}"
    )
    for config_file_name in "${CONFIG_FILE_NAME_LIST[@]}"; do
        REMOTE_ARGUMENT_LIST+=(--campaign-config-path "${CAMPAIGN_CONFIG_ROOT}/${config_file_name}")
    done
    if [[ "${DRY_RUN}" == "1" ]]; then
        REMOTE_ARGUMENT_LIST+=(--dry-run)
    fi

    bash "${SCRIPT_DIRECTORY}/run_exact_paper_campaign_remote.sh" "${REMOTE_ARGUMENT_LIST[@]}"
    exit $?
fi

LOCAL_ARGUMENT_LIST=(
    --campaign-name "${CAMPAIGN_NAME}"
    --planning-report-path "${PLANNING_REPORT_PATH}"
    --campaign-config-root "${CAMPAIGN_CONFIG_ROOT}"
    --conda-environment-name "${CONDA_ENVIRONMENT_NAME}"
    --python-executable "${PYTHON_EXECUTABLE}"
)
for config_file_name in "${CONFIG_FILE_NAME_LIST[@]}"; do
    LOCAL_ARGUMENT_LIST+=(--campaign-config-file "${config_file_name}")
done
if [[ "${DRY_RUN}" == "1" ]]; then
    LOCAL_ARGUMENT_LIST+=(--dry-run)
fi

bash "${SCRIPT_DIRECTORY}/invoke_exact_paper_campaign_local.sh" "${LOCAL_ARGUMENT_LIST[@]}"
