#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "${SCRIPT_DIRECTORY}/run_track1_svr_reference_grid_search_repair_campaign.sh" --dry-run >/dev/null
bash scripts/campaigns/track_1/exact_paper/run_exact_paper_campaign_remote.sh \
  --campaign-name "track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48" \
  --planning-report-path "doc/reports/campaign_plans/track_1/svm/2026-04-14-22-53-48_track1_svr_reference_grid_search_repair_campaign_plan_report.md" \
  --launcher-relative-path "scripts/campaigns/track_1/svm/run_track1_svr_reference_grid_search_repair_campaign.sh" \
  --campaign-output-root-override "output/training_campaigns/track1/svm/track1_svr_reference_grid_search_repair_campaign_2026_04_14_22_53_48" \
  --campaign-config-path "config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/svm_targeted_closure/svm/2026-04-14_track1_svr_reference_grid_search_repair_campaign/01_track1_svr_reference_grid_amplitude_pair.yaml" \
  --campaign-config-path "config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/svm_targeted_closure/svm/2026-04-14_track1_svr_reference_grid_search_repair_campaign/02_track1_svr_reference_grid_amplitude_40_only.yaml" \
  --campaign-config-path "config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/svm_targeted_closure/svm/2026-04-14_track1_svr_reference_grid_search_repair_campaign/03_track1_svr_reference_grid_amplitude_240_only.yaml" \
  --campaign-config-path "config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/svm_targeted_closure/svm/2026-04-14_track1_svr_reference_grid_search_repair_campaign/04_track1_svr_reference_grid_phase_162_only.yaml" \
  --run-name "track1_svr_reference_grid_amplitude_pair" \
  --run-name "track1_svr_reference_grid_amplitude_40_only" \
  --run-name "track1_svr_reference_grid_amplitude_240_only" \
  --run-name "track1_svr_reference_grid_phase_162_only" \
  "$@"
