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

echo "[INFO] Aggregate Launcher | run_track1_open_cell_full_matrix_closure_campaigns_resume_after_mlp.ps1"
echo "[INFO] Aggregate Launcher Count | 8"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_rf_open_cell_full_matrix_closure_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_rf_open_cell_full_matrix_closure_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_dt_open_cell_full_matrix_closure_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_dt_open_cell_full_matrix_closure_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_et_open_cell_full_matrix_closure_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_et_open_cell_full_matrix_closure_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_ert_open_cell_full_matrix_closure_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_ert_open_cell_full_matrix_closure_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_gbm_open_cell_full_matrix_closure_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_gbm_open_cell_full_matrix_closure_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_hgbm_open_cell_full_matrix_closure_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_hgbm_open_cell_full_matrix_closure_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_xgbm_open_cell_full_matrix_closure_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_xgbm_open_cell_full_matrix_closure_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo ""
printf "=%.0s" {1..96}; echo
echo "[INFO] Running aggregate child | scripts/campaigns/track_1/exact_paper/run_track1_lgbm_open_cell_full_matrix_closure_campaign.sh"
printf "=%.0s" {1..96}; echo
bash "${PROJECT_ROOT}/scripts/campaigns/track_1/exact_paper/run_track1_lgbm_open_cell_full_matrix_closure_campaign.sh" "${REMOTE_ARGUMENT_LIST[@]}" "${PASSTHROUGH_ARGUMENT_LIST[@]}"

echo "[DONE] Aggregate exact-paper campaign sequence completed successfully"
