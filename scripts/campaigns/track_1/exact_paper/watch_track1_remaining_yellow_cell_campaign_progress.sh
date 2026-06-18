#!/usr/bin/env bash

# Monitor Track 1 remaining-yellow-cell campaign progress on a local or Linux
# remote repository.

set -euo pipefail

REMOTE_HOST_ALIAS="${PINNS_REMOTE_TRAINING_HOST_ALIAS:-xilab-remote}"
REMOTE_REPOSITORY_PATH="${PINNS_REMOTE_TRAINING_REPO_PATH:-}"
DIRECT_ON_REMOTE="0"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --direct-on-remote)
            DIRECT_ON_REMOTE="1"
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
        --help|-h)
            echo "Usage: bash ${0} [--direct-on-remote] [--remote-host-alias HOST] [--remote-repository-path PATH]"
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            exit 2
            ;;
    esac
done

if [[ "${DIRECT_ON_REMOTE}" != "1" && -z "${REMOTE_REPOSITORY_PATH}" ]]; then
    echo "[ERROR] --remote-repository-path is required unless --direct-on-remote is used." >&2
    exit 2
fi

read -r -d '' STATUS_SCRIPT <<'SCRIPT' || true
set -euo pipefail

campaign_name="track1_remaining_yellow_cell_campaigns_2026_04_22_01_40_43"
validation_root="output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward"
training_campaign_root="output/training_campaigns/track1/exact_paper/forward"
families=(
    "SVM:svm:180"
    "MLP:mlp:60"
    "ET:et:60"
    "ERT:ert:180"
    "HGBM:hgbm:60"
    "XGBM:xgbm:120"
)

echo "CAMPAIGN_NAME::${campaign_name}"
echo "REPOSITORY_ROOT::$(pwd)"
echo "REMOTE_NOW::$(date '+%Y-%m-%d %H:%M:%S')"

total_done=0
total_expected=0
for family_record in "${families[@]}"; do
    IFS=':' read -r family_name family_slug expected_count <<< "${family_record}"
    mapfile -t validation_list < <(find "${validation_root}" -type d -name "*__track1_${family_slug}_*_yellow_cell_attempt_*_campaign_run" 2>/dev/null | sort)
    distinct_count="$(printf '%s\n' "${validation_list[@]}" | sed 's#^.*/##' | sed 's/^[0-9-]*__//' | sort -u | sed '/^$/d' | wc -l | tr -d ' ')"
    percent_complete="$(awk -v done="${distinct_count}" -v expected="${expected_count}" 'BEGIN { if (expected > 0) printf "%.1f", 100.0 * done / expected; else printf "0.0" }')"
    echo "FAMILY_PROGRESS::${family_name}::${distinct_count}::${expected_count}::${percent_complete}::0"
    if [[ "${#validation_list[@]}" -gt 0 ]]; then
        latest_validation="${validation_list[-1]}"
        echo "FAMILY_LATEST_VALIDATION::${family_name}::$(basename "${latest_validation}")::$(date -r "${latest_validation}" '+%Y-%m-%d %H:%M:%S')"
    fi
    total_done=$((total_done + distinct_count))
    total_expected=$((total_expected + expected_count))
done

total_percent="$(awk -v done="${total_done}" -v expected="${total_expected}" 'BEGIN { if (expected > 0) printf "%.1f", 100.0 * done / expected; else printf "0.0" }')"
echo "TOTAL_PROGRESS::${total_done}::${total_expected}::${total_percent}"

latest_validation="$(find "${validation_root}" -type d -name '*__track1_*_yellow_cell_attempt_*_campaign_run' -printf '%T@ %p\n' 2>/dev/null | sort -n | tail -1 | cut -d' ' -f2-)"
if [[ -n "${latest_validation}" ]]; then
    echo "LATEST_WAVE_VALIDATION::$(basename "${latest_validation}")::$(date -r "${latest_validation}" '+%Y-%m-%d %H:%M:%S')"
fi

latest_log="$(find "${training_campaign_root}" -type f -path '*/logs/*.log' -printf '%T@ %p\n' 2>/dev/null | sort -n | tail -1 | cut -d' ' -f2-)"
if [[ -n "${latest_log}" ]]; then
    echo "LATEST_CAMPAIGN_LOG::${latest_log}::$(date -r "${latest_log}" '+%Y-%m-%d %H:%M:%S')::$(wc -c < "${latest_log}")"
fi

active_process_count="$(pgrep -af 'run_exact_paper_model_bank_validation|remaining_yellow_cell|track1_svm|track1_mlp|track1_et|track1_ert|track1_hgbm|track1_xgbm' 2>/dev/null | wc -l | tr -d ' ')"
echo "ACTIVE_PROCESS_COUNT::${active_process_count}"
SCRIPT

if [[ "${DIRECT_ON_REMOTE}" == "1" ]]; then
    RAW_LINES="$(bash -s <<< "${STATUS_SCRIPT}")"
else
    RAW_LINES="$(printf '%s\n' "${STATUS_SCRIPT}" | ssh "${REMOTE_HOST_ALIAS}" "cd $(printf '%q' "${REMOTE_REPOSITORY_PATH}") && bash -s")"
fi

echo ""
printf '=%.0s' {1..96}
echo ""
echo "[INFO] Track 1 Remaining Yellow-Cell Campaign Progress Monitor"
printf '=%.0s' {1..96}
echo ""
echo "[INFO] Mode | $([[ "${DIRECT_ON_REMOTE}" == "1" ]] && echo direct_on_remote || echo ssh_remote)"
echo "[INFO] Remote Host Alias | ${REMOTE_HOST_ALIAS}"
printf '%s\n' "${RAW_LINES}" | sed -n 's/^REPOSITORY_ROOT::/[INFO] Repository Root | /p'
printf '%s\n' "${RAW_LINES}" | sed -n 's/^REMOTE_NOW::/[INFO] Remote Time | /p'
printf '%s\n' "${RAW_LINES}" | awk -F'::' '/^TOTAL_PROGRESS::/ { printf "[INFO] Total Progress | %s / %s | %s%%\n", $2, $3, $4 }'
echo ""
echo "Family Progress"
printf '%s\n' "${RAW_LINES}" | awk -F'::' '/^FAMILY_PROGRESS::/ { printf "- %s: %s / %s | %s%% | duplicate groups %s\n", $2, $3, $4, $5, $6 }'
echo ""
echo "Active State"
printf '%s\n' "${RAW_LINES}" | sed -n 's/^ACTIVE_PROCESS_COUNT::/- active matching processes: /p'
printf '%s\n' "${RAW_LINES}" | sed -n 's/^LATEST_WAVE_VALIDATION::/- latest validation: /p'
printf '%s\n' "${RAW_LINES}" | sed -n 's/^LATEST_CAMPAIGN_LOG::/- latest campaign log: /p'
