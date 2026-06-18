#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

bash "${SCRIPT_DIRECTORY}/run_track1_harmonic_wise_campaign_bundle.sh" \
    --campaign-config-root "config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/campaigns/2026-04-13_track1_overnight_gap_closure_campaign" \
    --campaign-config-file "01_track1_hgbm_h01_deeper_low_order.yaml" \
    --campaign-config-file "02_track1_hgbm_h013_deeper_low_order.yaml" \
    --campaign-config-file "03_track1_hgbm_h01_ultradeep_guarded.yaml" \
    --campaign-config-file "04_track1_hgbm_h01_shallow_regularized.yaml" \
    --campaign-config-file "05_track1_hgbm_h0139_low_order_anchor.yaml" \
    --campaign-config-file "06_track1_hgbm_h014078_low_order_anchor.yaml" \
    --campaign-config-file "07_track1_hgbm_h162_h240_repair.yaml" \
    --campaign-config-file "08_track1_hgbm_h081_h162_h240_repair.yaml" \
    --campaign-config-file "09_track1_hgbm_h156_h162_h240_repair.yaml" \
    --campaign-config-file "10_track1_hgbm_h039_h162_h240_bridge.yaml" \
    --campaign-config-file "11_track1_hgbm_h013_h162_h240_joint.yaml" \
    --campaign-config-file "12_track1_hgbm_h240_extreme_focus.yaml" \
    --campaign-config-file "13_track1_rf_full_rcim_reference.yaml" \
    --campaign-config-file "14_track1_rf_h01_focus.yaml" \
    --campaign-config-file "15_track1_rf_h081_focus.yaml" \
    --campaign-config-file "16_track1_rf_h156_h162_h240_focus.yaml" \
    --campaign-config-file "17_track1_hgbm_h01_engineered_recheck.yaml" \
    --campaign-config-file "18_track1_hgbm_h013_engineered_recheck.yaml" \
    --campaign-config-file "19_track1_hgbm_h162_h240_engineered_recheck.yaml" \
    --campaign-config-file "20_track1_rf_h01_h081_engineered_recheck.yaml" \
    --planning-report-path "doc/reports/campaign_plans/track_1/harmonic_wise/2026-04-13-00-55-21_track1_overnight_gap_closure_campaign_plan_report.md" \
    --campaign-name "track1_overnight_gap_closure_campaign_2026_04_13_01_02_23" \
    "$@"
