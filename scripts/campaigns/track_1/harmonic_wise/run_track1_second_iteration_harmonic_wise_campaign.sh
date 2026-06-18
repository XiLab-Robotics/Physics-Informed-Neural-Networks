#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

bash "${SCRIPT_DIRECTORY}/run_track1_harmonic_wise_campaign_bundle.sh" \
    --campaign-config-root "config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/campaigns/2026-04-09_track1_second_iteration_harmonic_wise_campaign" \
    --campaign-config-file "01_full_rcim_baseline_reference.yaml" \
    --campaign-config-file "02_h013_engineered_stage1.yaml" \
    --campaign-config-file "03_h013_random_forest_diagnostic.yaml" \
    --campaign-config-file "04_h01340_engineered_stage2.yaml" \
    --campaign-config-file "05_h0134078_engineered_stage3.yaml" \
    --campaign-config-file "06_full_rcim_no_engineering_reference.yaml" \
    --campaign-config-file "07_full_rcim_engineered_balanced.yaml" \
    --campaign-config-file "08_full_rcim_engineered_deeper.yaml" \
    --planning-report-path "doc/reports/campaign_plans/track_1/harmonic_wise/2026-04-09-18-56-03_track1_second_iteration_harmonic_wise_campaign_plan_report.md" \
    --campaign-name "track1_second_iteration_harmonic_wise_campaign_2026_04_09_18_56_03" \
    "$@"
