#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

bash "${SCRIPT_DIRECTORY}/run_original_dataset_active_campaign.sh" \
    --launcher-relative-path "scripts/campaigns/track1/exact_paper/run_track1_forward_open_cell_repair_campaign.sh" \
    --validation-output-root "output/validation_checks/paper_reimplementation_rcim_original_dataset_exact_model_bank_forward_open_cell_repair" \
    --validation-report-root "doc/reports/analysis/validation_checks" \
    "$@"
