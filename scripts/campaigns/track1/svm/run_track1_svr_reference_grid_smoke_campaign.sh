#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "${SCRIPT_DIRECTORY}/run_track1_svm_campaign_bundle.sh" \
  --campaign-config-root "config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/svm_targeted_closure/svm/2026-04-16_track1_svr_reference_grid_smoke_campaign" \
  --planning-report-path "doc/reports/campaign_plans/track1/svm/2026-04-16-12-45-00_track1_svr_reference_grid_smoke_campaign_plan_report.md" \
  --campaign-name "track1_svr_reference_grid_smoke_campaign_2026_04_16_12_45_00" \
  --campaign-config-file "01_track1_svr_reference_grid_amplitude_40_smoke_singlecore.yaml" \
  "$@"
