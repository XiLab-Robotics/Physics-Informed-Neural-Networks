#!/usr/bin/env bash

# Launch the targeted remote follow-up campaign on a Linux remote host.

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

REMOTE_HOST_ALIAS="${STANDARDML_REMOTE_TRAINING_HOST:-xilab-remote}"
REMOTE_REPOSITORY_PATH="${STANDARDML_REMOTE_TRAINING_REPO_PATH:-}"
REMOTE_CONDA_ENVIRONMENT_NAME="${STANDARDML_REMOTE_TRAINING_CONDA_ENV:-standard_ml_lan_node}"
DRY_RUN_ARGUMENT_LIST=()

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
        --remote-conda-environment)
            REMOTE_CONDA_ENVIRONMENT_NAME="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN_ARGUMENT_LIST+=(--dry-run)
            shift
            ;;
        --help)
            bash "${SCRIPT_DIRECTORY}/run_remote_training_campaign.sh" --help
            exit 0
            ;;
        *)
            echo "[ERROR] Unsupported argument | $1" >&2
            exit 2
            ;;
    esac
done

bash "${SCRIPT_DIRECTORY}/run_remote_training_campaign.sh" \
    --campaign-name "targeted_remote_followup_campaign_2026_04_04_11_21_09" \
    --planning-report-path "doc/reports/campaign_plans/infrastructure/2026-04-04-11-21-09_targeted_remote_followup_campaign_plan_report.md" \
    --campaign-config-path "config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/01_residual_h12_deep_long_remote.yaml" \
    --campaign-config-path "config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/02_residual_h12_deep_dense_remote.yaml" \
    --campaign-config-path "config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/03_feedforward_high_compute_long_remote.yaml" \
    --campaign-config-path "config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/04_feedforward_stride1_high_compute_long_remote.yaml" \
    --campaign-config-path "config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/05_hist_gbr_remote_refined.yaml" \
    --source-sync-path "scripts" \
    --source-sync-path "config" \
    --source-sync-path "requirements.txt" \
    --remote-host-alias "${REMOTE_HOST_ALIAS}" \
    --remote-repository-path "${REMOTE_REPOSITORY_PATH}" \
    --remote-conda-environment "${REMOTE_CONDA_ENVIRONMENT_NAME}" \
    "${DRY_RUN_ARGUMENT_LIST[@]}"
