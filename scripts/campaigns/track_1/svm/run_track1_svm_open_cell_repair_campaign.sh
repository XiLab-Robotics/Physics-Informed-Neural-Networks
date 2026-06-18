#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "${SCRIPT_DIRECTORY}/run_track1_svm_campaign_bundle.sh" \
  --campaign-config-root "config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/svm_targeted_closure/svm/2026-04-14_track1_svm_open_cell_repair_campaign" \
  --planning-report-path "doc/reports/campaign_plans/track_1/svm/2026-04-14-17-17-21_track1_svm_open_cell_repair_campaign_plan_report.md" \
  --campaign-name "track1_svm_open_cell_repair_campaign_2026_04_14_17_17_21" \
  "$@"
