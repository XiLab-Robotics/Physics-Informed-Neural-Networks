#!/usr/bin/env bash

# Sync interrupted RCIM Model-Bank Reproduction artifacts from a Linux remote
# repository back into the local repository.

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"

REMOTE_HOST_ALIAS=""
REMOTE_REPOSITORY_PATH=""
ACTIVE_CAMPAIGN_PATH="doc/running/active_training_campaign.yaml"
LOCAL_STAGING_ROOT=".temp/manual_sync_track1_svm"
SKIP_REMOTE_CLEANUP="0"
DRY_RUN="0"

EXPECTED_CAMPAIGN_NAME="track1_remaining_yellow_cell_campaigns_2026_04_22_01_40_43"
EXPECTED_REMOTE_CAMPAIGN_DIRECTORY="output/training_campaigns/track1/exact_paper/forward/remaining_yellow_cells/svm/track1_svm_remaining_yellow_cell_campaign_2026_04_22_01_40_43"
VALIDATION_ROOT="output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward"
VALIDATION_PATTERN="*__track1_svm_*_yellow_cell_attempt_*_campaign_run"
REPORT_ROOT="doc/reports/analysis/validation_checks"
REPORT_PATTERN="*_track1_svm_*_yellow_cell_attempt_*_campaign_run_exact_paper_model_bank_report.md"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --remote-host-alias)
            REMOTE_HOST_ALIAS="$2"
            shift 2
            ;;
        --remote-repository-path)
            REMOTE_REPOSITORY_PATH="$2"
            shift 2
            ;;
        --active-campaign-path)
            ACTIVE_CAMPAIGN_PATH="${2//\\//}"
            shift 2
            ;;
        --local-staging-root)
            LOCAL_STAGING_ROOT="${2//\\//}"
            shift 2
            ;;
        --skip-remote-cleanup)
            SKIP_REMOTE_CLEANUP="1"
            shift
            ;;
        --dry-run)
            DRY_RUN="1"
            shift
            ;;
        --help|-h)
            echo "Usage: bash ${0} [--remote-host-alias HOST] [--remote-repository-path PATH] [--dry-run]"
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            exit 2
            ;;
    esac
done

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

PYTHON_FOR_METADATA="$(metadata_python)"
ACTIVE_METADATA_JSON="$(
    "${PYTHON_FOR_METADATA}" - "${PROJECT_ROOT}" "${ACTIVE_CAMPAIGN_PATH}" <<'PY'
import json
import sys
from pathlib import Path

import yaml

project_root = Path(sys.argv[1]).resolve()
active_path = (project_root / sys.argv[2]).resolve()
payload = yaml.safe_load(active_path.read_text(encoding="utf-8"))
print(json.dumps({
    "campaign_name": payload.get("campaign_name", ""),
    "status": payload.get("status", ""),
    "remote_host_alias": payload.get("remote_host_alias", ""),
    "remote_repository_path": payload.get("remote_repository_path", ""),
}))
PY
)"

ACTIVE_CAMPAIGN_NAME="$("${PYTHON_FOR_METADATA}" -c 'import json,sys; print(json.loads(sys.argv[1])["campaign_name"])' "${ACTIVE_METADATA_JSON}")"
ACTIVE_STATUS="$("${PYTHON_FOR_METADATA}" -c 'import json,sys; print(json.loads(sys.argv[1])["status"])' "${ACTIVE_METADATA_JSON}")"
if [[ -z "${REMOTE_HOST_ALIAS}" ]]; then
    REMOTE_HOST_ALIAS="$("${PYTHON_FOR_METADATA}" -c 'import json,sys; print(json.loads(sys.argv[1])["remote_host_alias"])' "${ACTIVE_METADATA_JSON}")"
fi
if [[ -z "${REMOTE_REPOSITORY_PATH}" ]]; then
    REMOTE_REPOSITORY_PATH="$("${PYTHON_FOR_METADATA}" -c 'import json,sys; print(json.loads(sys.argv[1])["remote_repository_path"])' "${ACTIVE_METADATA_JSON}")"
fi

if [[ "${ACTIVE_CAMPAIGN_NAME}" != "${EXPECTED_CAMPAIGN_NAME}" ]]; then
    echo "[ERROR] Unexpected active campaign identity | expected=${EXPECTED_CAMPAIGN_NAME} | actual=${ACTIVE_CAMPAIGN_NAME}" >&2
    exit 2
fi
if [[ -z "${REMOTE_HOST_ALIAS}" || -z "${REMOTE_REPOSITORY_PATH}" ]]; then
    echo "[ERROR] Remote host alias and repository path are required." >&2
    exit 2
fi

RUN_TIMESTAMP="$(date +"%Y-%m-%d-%H-%M-%S")"
LOCAL_RUN_STAGE_DIRECTORY="${PROJECT_ROOT}/${LOCAL_STAGING_ROOT}/${RUN_TIMESTAMP}"
mkdir -p "${LOCAL_RUN_STAGE_DIRECTORY}"

REMOTE_TEMP_ROOT=".temp/track1_interrupted_manual_sync"
REMOTE_CAMPAIGN_ARCHIVE="${REMOTE_TEMP_ROOT}/track1_svm_campaign_output.tar"
REMOTE_VALIDATION_ARCHIVE="${REMOTE_TEMP_ROOT}/track1_svm_validation_dirs.tar"
REMOTE_REPORT_ARCHIVE="${REMOTE_TEMP_ROOT}/track1_svm_validation_reports.tar"

echo "[INFO] RCIM Model-Bank Reproduction interrupted SVM manual sync starting"
echo "[INFO] Campaign | ${ACTIVE_CAMPAIGN_NAME}"
echo "[INFO] Canonical local campaign status | ${ACTIVE_STATUS}"
echo "[INFO] Remote host alias | ${REMOTE_HOST_ALIAS}"
echo "[INFO] Remote repository path | ${REMOTE_REPOSITORY_PATH}"
echo "[INFO] Local staging directory | ${LOCAL_RUN_STAGE_DIRECTORY}"

if [[ "${DRY_RUN}" == "1" ]]; then
    echo "[INFO] Dry run requested; remote archives were not created or downloaded."
    echo "DRY_RUN_REMOTE_CAMPAIGN_DIRECTORY::${EXPECTED_REMOTE_CAMPAIGN_DIRECTORY}"
    echo "DRY_RUN_VALIDATION_PATTERN::${VALIDATION_ROOT}/${VALIDATION_PATTERN}"
    echo "DRY_RUN_REPORT_PATTERN::${REPORT_ROOT}/${REPORT_PATTERN}"
    exit 0
fi

command -v ssh >/dev/null 2>&1 || { echo "[ERROR] ssh is not available." >&2; exit 127; }
command -v tar >/dev/null 2>&1 || { echo "[ERROR] tar is not available." >&2; exit 127; }

ssh "${REMOTE_HOST_ALIAS}" "cd $(printf '%q' "${REMOTE_REPOSITORY_PATH}") && mkdir -p ${REMOTE_TEMP_ROOT} && test -d $(printf '%q' "${EXPECTED_REMOTE_CAMPAIGN_DIRECTORY}")"

ssh "${REMOTE_HOST_ALIAS}" "cd $(printf '%q' "${REMOTE_REPOSITORY_PATH}") && tar -cf ${REMOTE_CAMPAIGN_ARCHIVE} $(printf '%q' "${EXPECTED_REMOTE_CAMPAIGN_DIRECTORY}")"
ssh "${REMOTE_HOST_ALIAS}" "cd $(printf '%q' "${REMOTE_REPOSITORY_PATH}") && find $(printf '%q' "${VALIDATION_ROOT}") -type d -name $(printf '%q' "${VALIDATION_PATTERN}") -print0 | tar --null -T - -cf ${REMOTE_VALIDATION_ARCHIVE}"
ssh "${REMOTE_HOST_ALIAS}" "cd $(printf '%q' "${REMOTE_REPOSITORY_PATH}") && find $(printf '%q' "${REPORT_ROOT}") -type f -name $(printf '%q' "${REPORT_PATTERN}") -print0 | tar --null -T - -cf ${REMOTE_REPORT_ARCHIVE}"

for archive_path in "${REMOTE_CAMPAIGN_ARCHIVE}" "${REMOTE_VALIDATION_ARCHIVE}" "${REMOTE_REPORT_ARCHIVE}"; do
    archive_name="$(basename "${archive_path}")"
    echo "[STEP] Downloading remote archive | ${archive_path}"
    ssh "${REMOTE_HOST_ALIAS}" "cat $(printf '%q' "${REMOTE_REPOSITORY_PATH}/${archive_path}")" >"${LOCAL_RUN_STAGE_DIRECTORY}/${archive_name}"
    tar -xf "${LOCAL_RUN_STAGE_DIRECTORY}/${archive_name}" -C "${PROJECT_ROOT}"
done

if [[ "${SKIP_REMOTE_CLEANUP}" != "1" ]]; then
    ssh "${REMOTE_HOST_ALIAS}" "cd $(printf '%q' "${REMOTE_REPOSITORY_PATH}") && rm -f ${REMOTE_CAMPAIGN_ARCHIVE} ${REMOTE_VALIDATION_ARCHIVE} ${REMOTE_REPORT_ARCHIVE}"
fi

echo "[DONE] Interrupted SVM manual artifact sync completed"
