#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "${SCRIPT_DIRECTORY}/run_track1_svm_campaign_bundle.sh" \
  --campaign-config-root "config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/svm_targeted_closure/svm/2026-04-14_track1_svm_micro_closure_campaign" \
  --planning-report-path "doc/reports/campaign_plans/track_1/svm/2026-04-14-21-42-47_track1_svm_micro_closure_campaign_plan_report.md" \
  --campaign-name "track1_svm_micro_closure_campaign_2026_04_14_21_42_47" \
  "$@"
