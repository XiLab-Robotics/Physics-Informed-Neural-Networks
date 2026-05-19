#!/usr/bin/env bash

# Run the high-quality video-guide rerun workflow against remote LAN AI and LM
# Studio endpoints from Linux.

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../.." && pwd)"

PYTHON_EXECUTABLE="python"
LAN_AI_BASE_URL="${PINNS_LAN_AI_BASE_URL:-}"
LM_STUDIO_BASE_URL="${LM_STUDIO_BASE_URL:-}"
TRANSCRIPT_MODEL="large-v3"
CLEANUP_MODEL="openai/gpt-oss-20b"
REPORT_MODEL="openai/gpt-oss-20b"
VIDEO_NAME_LIST=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --python-executable)
            PYTHON_EXECUTABLE="$2"
            shift 2
            ;;
        --lan-ai-base-url)
            LAN_AI_BASE_URL="$2"
            shift 2
            ;;
        --lm-studio-base-url)
            LM_STUDIO_BASE_URL="$2"
            shift 2
            ;;
        --transcript-model)
            TRANSCRIPT_MODEL="$2"
            shift 2
            ;;
        --cleanup-model)
            CLEANUP_MODEL="$2"
            shift 2
            ;;
        --report-model)
            REPORT_MODEL="$2"
            shift 2
            ;;
        --video-name)
            VIDEO_NAME_LIST+=("$2")
            shift 2
            ;;
        --help|-h)
            echo "Usage: bash ${0} [--video-name NAME ...] [--python-executable COMMAND]"
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            exit 2
            ;;
    esac
done

cd "${PROJECT_ROOT}"

ANALYSIS_ROOT=".temp/video_guides/_analysis_hq_remote_gptoss_tracked"
REPORT_ROOT=".temp/video_guides/_remote_gptoss_tracked_reports"
LOG_ROOT=".temp/video_guides/_remote_gptoss_tracked_logs"
VIDEO_SOURCE_ROOT="reference/video_guides/source_bundle"
STATUS_FILE="doc/running/remote_high_quality_video_rerun_status.json"
CHECKLIST_FILE="doc/running/remote_high_quality_video_rerun_checklist.md"
WORKFLOW_SCRIPT="scripts/tooling/video_guides/extract_video_guide_knowledge.py"
VALIDATION_SCRIPT="scripts/tooling/markdown/markdown_style_check.py"

mkdir -p "${ANALYSIS_ROOT}" "${REPORT_ROOT}" "${LOG_ROOT}" "$(dirname "${STATUS_FILE}")"

if [[ "${#VIDEO_NAME_LIST[@]}" -eq 0 ]]; then
    while IFS= read -r video_path; do
        VIDEO_NAME_LIST+=("$(basename "${video_path%.*}")")
    done < <(find "${VIDEO_SOURCE_ROOT}" -maxdepth 1 -type f \( -iname "*.mp4" -o -iname "*.mkv" -o -iname "*.mov" -o -iname "*.avi" -o -iname "*.m4v" \) | sort)
fi

if [[ "${#VIDEO_NAME_LIST[@]}" -eq 0 ]]; then
    echo "[ERROR] No supported video files were found under ${VIDEO_SOURCE_ROOT}" >&2
    exit 2
fi

write_state() {
    local run_status="$1"
    local current_video_name="$2"
    local current_video_index="$3"
    local last_failure_message="${4:-}"

    "${PYTHON_EXECUTABLE}" - "${STATUS_FILE}" "${CHECKLIST_FILE}" "${run_status}" "${current_video_name}" "${current_video_index}" "${last_failure_message}" "${LAN_AI_BASE_URL}" "${LM_STUDIO_BASE_URL}" "${TRANSCRIPT_MODEL}" "${CLEANUP_MODEL}" "${REPORT_MODEL}" "${ANALYSIS_ROOT}" "${REPORT_ROOT}" "${LOG_ROOT}" "${VIDEO_NAME_LIST[@]}" <<'PY'
import json
import sys
from datetime import datetime
from pathlib import Path

status_path = Path(sys.argv[1])
checklist_path = Path(sys.argv[2])
run_status, current_video_name, current_video_index, last_failure_message = sys.argv[3:7]
lan_ai_base_url, lm_studio_base_url, transcript_model, cleanup_model, report_model = sys.argv[7:12]
analysis_root, report_root, log_root = sys.argv[12:15]
video_name_list = sys.argv[15:]

payload = {
    "run_status": run_status,
    "current_video_name": current_video_name,
    "current_video_index": int(current_video_index),
    "lan_ai_base_url": lan_ai_base_url,
    "lm_studio_base_url": lm_studio_base_url,
    "transcript_model": transcript_model,
    "cleanup_model": cleanup_model,
    "report_model": report_model,
    "analysis_root": analysis_root,
    "report_root": report_root,
    "log_root": log_root,
    "last_failure_message": last_failure_message,
    "updated_at": datetime.now().isoformat(),
    "video_name_list": video_name_list,
}
status_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

lines = [
    "# Remote High-Quality Video Rerun Checklist",
    "",
    f"- Run status: {run_status}",
    f"- Current video: {current_video_name}",
    f"- Current index: {current_video_index}",
    f"- LAN AI base URL: {lan_ai_base_url}",
    f"- LM Studio base URL: {lm_studio_base_url}",
    f"- Transcript model: {transcript_model}",
    f"- Cleanup model: {cleanup_model}",
    f"- Report model: {report_model}",
    f"- Updated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    "",
    "## Video Set",
    "",
]
lines.extend(f"- {video_name}" for video_name in video_name_list)
if last_failure_message:
    lines.extend(["", "## Last Failure", "", last_failure_message])
checklist_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
PY
}

echo "[INFO] Tracked video set | ${VIDEO_NAME_LIST[*]}"
write_state "running" "" 0

for video_index in "${!VIDEO_NAME_LIST[@]}"; do
    video_name="${VIDEO_NAME_LIST[${video_index}]}"
    video_slug="$(printf '%s' "${video_name}" | tr -c '[:alnum:]' '_' | tr '[:upper:]' '[:lower:]' | sed 's/^_*//; s/_*$//')"
    video_log_path="${LOG_ROOT}/${video_slug}.log"
    mkdir -p "$(dirname "${video_log_path}")"

    echo "[STEP] Processing video $((video_index + 1))/${#VIDEO_NAME_LIST[@]} | ${video_name}"
    write_state "running" "${video_name}" "$((video_index + 1))"

    "${PYTHON_EXECUTABLE}" -B "${WORKFLOW_SCRIPT}" \
        --video-filter "${video_name}" \
        --limit-videos 1 \
        --analysis-root "${ANALYSIS_ROOT}" \
        --report-root "${REPORT_ROOT}" \
        --transcript-provider lan \
        --cleanup-provider lmstudio \
        --report-provider lmstudio \
        --ocr-provider local \
        --transcript-model "${TRANSCRIPT_MODEL}" \
        --cleanup-model "${CLEANUP_MODEL}" \
        --report-model "${REPORT_MODEL}" \
        --lan-ai-base-url "${LAN_AI_BASE_URL}" \
        --lm-studio-base-url "${LM_STUDIO_BASE_URL}" \
        --lmstudio-max-report-chunk-characters 220 2>&1 | tee "${video_log_path}"
    native_exit_code="${PIPESTATUS[0]}"

    if [[ "${native_exit_code}" -ne 0 ]]; then
        failure_message="Video failed | name=${video_name} | exit_code=${native_exit_code} | log=${video_log_path}"
        write_state "failed" "${video_name}" "$((video_index + 1))" "${failure_message}"
        echo "[FAIL] ${failure_message}" >&2
        exit "${native_exit_code}"
    fi

    transcript_path="${REPORT_ROOT}/${video_slug}/${video_slug}_transcript.md"
    report_path="${REPORT_ROOT}/${video_slug}/${video_slug}_report.md"
    "${PYTHON_EXECUTABLE}" -B "${VALIDATION_SCRIPT}" "${transcript_path}" "${report_path}"
    echo "[DONE] Completed video | ${video_name}"
done

write_state "completed" "" "${#VIDEO_NAME_LIST[@]}"
echo "[DONE] Remote high-quality video rerun completed"
