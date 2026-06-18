#!/usr/bin/env bash
set -euo pipefail
bash scripts/campaigns/track_1/exact_paper/run_exact_paper_campaign_remote.sh \
  --campaign-name "track1_svm_exact_faithful_final_attempt_campaign_2026_04_17_11_44_20" \
  --planning-report-path "doc/reports/campaign_plans/track_1/svm/2026-04-17-11-44-20_track1_svm_exact_faithful_final_attempt_campaign_plan_report.md" \
  --launcher-relative-path "scripts/campaigns/track_1/svm/run_track1_svm_exact_faithful_final_attempt_campaign.sh" \
  --campaign-output-root-override "output/training_campaigns/track1/svm/track1_svm_exact_faithful_final_attempt_campaign_2026_04_17_11_44_20" \
  --campaign-config-path "config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/svm_targeted_closure/svm/2026-04-17_track1_svm_exact_faithful_final_attempt_campaign/01_track1_svr_exact_faithful_amplitude_pair_repeat.yaml" \
  --campaign-config-path "config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/svm_targeted_closure/svm/2026-04-17_track1_svm_exact_faithful_final_attempt_campaign/02_track1_svr_exact_faithful_amplitude_40_repeat.yaml" \
  --campaign-config-path "config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/svm_targeted_closure/svm/2026-04-17_track1_svm_exact_faithful_final_attempt_campaign/03_track1_svr_exact_faithful_amplitude_240_repeat.yaml" \
  --campaign-config-path "config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/svm_targeted_closure/svm/2026-04-17_track1_svm_exact_faithful_final_attempt_campaign/04_track1_svr_exact_faithful_phase_162_repeat.yaml" \
  --run-name "track1_svr_exact_faithful_amplitude_pair_repeat" \
  --run-name "track1_svr_exact_faithful_amplitude_40_repeat" \
  --run-name "track1_svr_exact_faithful_amplitude_240_repeat" \
  --run-name "track1_svr_exact_faithful_phase_162_repeat" \
  "$@"
