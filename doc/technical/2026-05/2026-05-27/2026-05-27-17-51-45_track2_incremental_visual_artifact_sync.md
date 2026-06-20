# TE Curve Verification Pipeline Incremental Visual Artifact Sync

## Overview

This technical note plans the cleanup of the `TE Curve Verification Pipeline` refresh launcher and
visual artifact generation after the `Wave 2.2` harmonic-temporal refresh showed
that remote runs can recreate or resynchronize broad historical `Wave 1` PNG
sets. The matrix evaluation is already incremental through the configured
baseline summary, but the report-facing PNG and remote artifact sync paths still
cover more history than the current refresh needs.

## Technical Approach

Keep the default `TE Curve Verification Pipeline` refresh focused on new candidate artifacts:

- preserve the incremental matrix behavior driven by `baseline_summary_path`;
- generate grouped report PNGs only for candidates evaluated in the current
  incremental run;
- keep an explicit opt-in path for full baseline visual regeneration;
- narrow remote artifact synchronization so it downloads the current refresh
  outputs and the new candidate plot source instead of the entire historical
  `doc/reports/campaign_results/track_2/verification_plots` tree;
- document the default so future operator-launched `TE Curve Verification Pipeline` runs do not
  unexpectedly churn closed `Wave 1` visual assets.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `scripts/campaigns/track_2/run_wave2b_track2_verification_refresh.ps1`
- `doc/scripts/campaigns/track_2/run_wave2b_track2_verification_refresh.md`
- `doc/README.md`

## Implementation Steps

1. Add a configuration switch that defaults grouped report plots to the current
   incremental candidate set and requires an explicit flag for full baseline
   plot regeneration.
2. Update the `TE Curve Verification Pipeline` comparison runner so merged baseline summaries retain
   existing metrics while only the current run contributes new grouped plot
   paths by default.
3. Update the Wave 2.2 operator launcher so remote artifact sync pulls the
   current run output directories and the `wave2_temporal_entry_registry`
   report-plot source, not the complete historical report-plot root.
4. Document the new default and the explicit full-refresh option in the launcher
   note.
5. Run scoped Python compile, PowerShell parser, Markdown checks, and a
   lightweight local dry-run path when feasible without starting another heavy
   `TE Curve Verification Pipeline` matrix.
