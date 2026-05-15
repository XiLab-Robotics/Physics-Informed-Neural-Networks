#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIRECTORY="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

bash "${SCRIPT_DIRECTORY}/run_track1_harmonic_wise_campaign_bundle.sh" \
    --campaign-config-root "config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/campaigns/2026-04-13_track1_extended_overnight_campaign" \
    --planning-report-path "doc/reports/campaign_plans/track1/harmonic_wise/2026-04-13-13-27-37_track1_extended_overnight_campaign_plan_report.md" \
    --campaign-name "track1_extended_overnight_campaign_2026_04_13_13_31_57" \
    "$@"
