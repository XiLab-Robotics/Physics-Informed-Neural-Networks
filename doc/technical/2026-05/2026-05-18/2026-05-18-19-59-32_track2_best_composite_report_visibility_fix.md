# Track 2 Best Composite Report Visibility Fix

## Overview

The canonical `Track 2` report currently includes the composed best-reference
models in the candidate inventory and in their source-group metric tables, but
it does not expose them as a dedicated first-class comparison section.

This makes the new `paper_original_best_Fw`, `paper_retuned_best_Fw`,
`track1_best_Fw`, `paper_retuned_best_Bw`, and `track1_best_Bw` candidates too
easy to miss in
`doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`.

## Technical Approach

Add a dedicated `Best Composite Reference Models` section to the Track 2 report
generator. The section will be generated from `composite_reference_bank`
candidate metadata and the existing direction-level metric dictionaries, so it
stays synchronized with future Track 2 reruns instead of being a manual report
edit.

The canonical report and the timestamped validation-check report will then be
regenerated from the already completed Track 2 validation summary. No training
or model evaluation rerun is required because this is a report-visibility
correction over already available metrics.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
  - report Markdown generator that should emit the new composite summary
    section.
- `output/validation_checks/track2_reference_comparison/2026-05-18-16-35-26__track2_full_directional_family_matrix_composite_best_reference_validation/validation_summary.yaml`
  - existing validation summary used to regenerate the Markdown reports.
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
  - canonical Track 2 report that must show the best composite models
    explicitly.
- `doc/reports/analysis/validation_checks/track2/2026-05-18-17-26-52_track2_full_directional_family_matrix_composite_best_reference_validation_report.md`
  - timestamped validation report that should match the canonical Track 2
    report content.

## Implementation Steps

1. Extend the Track 2 Markdown report generator with a helper that selects
   candidates whose `candidate_kind` is `composite_reference_bank`.
2. Emit a dedicated `Best Composite Reference Models` table with candidate,
   source, surface, evaluated direction, and the existing curve-level metrics.
3. Regenerate the canonical and timestamped Track 2 reports from the completed
   validation summary.
4. Run Python compilation for the touched generator and scoped Markdown QA for
   the touched report files.
