#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIRECTORY}/../../../.." && pwd)"
REMOTE_ARGUMENT_LIST=()
PASSTHROUGH_ARGUMENT_LIST=()

while [[ $# -gt 0 ]]; do
    case "$1" in
        --remote|--remote-host-alias|--remote-repository-path|--remote-conda-environment-name|--dry-run)
            REMOTE_ARGUMENT_LIST+=("$1")
            if [[ "$1" != "--remote" && "$1" != "--dry-run" ]]; then
                REMOTE_ARGUMENT_LIST+=("$2")
                shift 2
            else
                shift
            fi
            ;;
        *)
            PASSTHROUGH_ARGUMENT_LIST+=("$1")
            if [[ $# -gt 1 && "$2" != --* ]]; then
                PASSTHROUGH_ARGUMENT_LIST+=("$2")
                shift 2
            else
                shift
            fi
            ;;
    esac
done

echo "[INFO] Aggregate Launcher | run_track1_remaining_family_full_matrix_campaigns.ps1"
echo "[INFO] Aggregate Launcher Count | 9"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_mlp_full_matrix_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_mlp_full_matrix_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_rf_full_matrix_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_rf_full_matrix_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_dt_full_matrix_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_dt_full_matrix_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_et_full_matrix_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_et_full_matrix_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_ert_full_matrix_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_ert_full_matrix_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_gbm_full_matrix_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_gbm_full_matrix_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_hgbm_full_matrix_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_hgbm_full_matrix_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_xgbm_full_matrix_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_xgbm_full_matrix_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_lgbm_full_matrix_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_lgbm_full_matrix_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo "[DONE] Aggregate exact-paper campaign sequence completed successfully"
