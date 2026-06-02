# Track 2 Mean-Centered Collage Diagnostics

## Overview

This document plans a `Track 2` diagnostic report that tests the observed
persistent vertical offset between measured and predicted `TE` curves in the
existing best-model collage report.

The task is analysis-only. It does not train models, change datasets, update
promotion registries, or alter the runtime input contract. The diagnostic
compares the original absolute-error metrics with a mean-centered metric view
where each measured curve and each predicted curve is centered by its own
curve mean before `MAE` and `RMSE` are recomputed.

## Technical Approach

Build a companion report analogous to the existing best-model collage report:

- source report:
  `doc/reports/analysis/track2/best_model_collage_report/[2026-05-28]/track2_best_model_collage_report.md`;
- source run:
  `output/validation_checks/track2_best_model_collage_report/2026-05-28-13-37-39__track2_best_model_collage_report`;
- new output root:
  `output/validation_checks/track2_mean_centered_collage_report/`;
- new report root:
  `doc/reports/analysis/track2/mean_centered_collage_report/[2026-06-02]/`.

For each candidate and selected collage curve:

1. run the same causal prediction path used by the existing `Track 2` collage
   workflow;
2. compute raw curve `MAE` and `RMSE`;
3. compute `truth_mean_deg` and `prediction_mean_deg`;
4. subtract `truth_mean_deg` from the measured curve and
   `prediction_mean_deg` from the predicted curve;
5. recompute mean-centered `MAE` and `RMSE`;
6. report absolute and percentage improvement for every candidate and
   direction-valid surface.

The visual output should include collages where each subplot overlays
mean-centered truth and prediction curves. The report should include summary
tables over the same deterministic four-curve selections used by the source
collage report. A later full-matrix mean-centered pass can be opened if this
first diagnostic confirms that offset removal materially changes the ranking.

## Involved Components

- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- new companion script under `scripts/reports/analysis/`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `output/validation_checks/track2_best_model_collage_report/2026-05-28-13-37-39__track2_best_model_collage_report/`
- `doc/reports/analysis/track2/best_model_collage_report/[2026-05-28]/`
- `doc/reports/analysis/track2/mean_centered_collage_report/[2026-06-02]/`

## Implementation Steps

1. Reuse the existing `Track 2` collage candidate inventory and deterministic
   selected-curve policy.
2. Add a companion analysis script that writes:
   - per-selected-curve raw and mean-centered metrics CSV;
   - per-candidate aggregate raw and mean-centered metrics CSV;
   - mean-centered collage images;
   - summary YAML;
   - Markdown report.
3. Keep `Fw`, `Bw`, and `global` surfaces separated in all tables.
4. Clearly label mean-centering as a diagnostic post-processing view, not as a
   deployable correction unless a later causal offset-calibration strategy is
   explicitly approved.
5. Run scoped Python checks, Markdown QA, PDF export if requested after the
   Markdown report is accepted, and Sphinx when the report script enters the
   documented API surface.
