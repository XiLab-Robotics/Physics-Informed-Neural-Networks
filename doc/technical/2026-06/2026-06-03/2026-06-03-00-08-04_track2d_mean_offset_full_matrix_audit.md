# CVP 1.4 Mean-Offset Full-Matrix Audit

## Overview

This document plans the next analysis step after the `TE Curve Verification Pipeline` mean-centered
collage diagnostic and the mean-offset strategy update.

The goal is to scale the mean-centered finding from the selected collage
curves to the official `TE Curve Verification Pipeline` candidate matrix. The audit must determine
whether each candidate is primarily limited by vertical curve offset, centered
waveform shape, amplitude, harmonic phase, or operating-condition regime.

This is an analysis-only step. It must not train models, alter dataset
structure, change runtime inputs, or promote a new best model by itself.

## Technical Approach

Implement a repository-owned `CVP 1.4` report builder that reuses the
direction-aware `TE Curve Verification Pipeline` candidate matrix and causal inference path.

For every direction-valid candidate and evaluated curve, compute:

- raw per-curve `MAE` and `RMSE`;
- truth mean, prediction mean, and residual curve-bias / `DC` offset;
- centered per-curve `MAE` and `RMSE` after independently subtracting truth
  and prediction means;
- raw-to-centered absolute and percentage improvement;
- truth and prediction peak-to-peak amplitude plus amplitude error;
- selected sparse-`RCIM` harmonic amplitude and phase error when the curve has
  enough angular samples for a stable harmonic fit;
- condition-stratified summaries by direction, speed, torque, temperature, and
  valid-window identifiers available in the `TE Curve Verification Pipeline` payload.

The report should classify each candidate as:

- offset-limited;
- centered-shape-limited;
- amplitude-limited;
- phase-limited;
- mixed-limited;
- condition-regime-limited.

The classification is a diagnostic label for the next training decision, not a
promotion rule. Future retraining should remain blocked until this audit
identifies which failure mode matters for each of the `Fw`, `Bw`, and `global`
surfaces.

## Involved Components

Expected implementation surfaces:

- new script:
  `scripts/reports/analysis/build_track2d_mean_offset_full_matrix_audit.py`;
- script documentation:
  `doc/scripts/reports/analysis/build_track2d_mean_offset_full_matrix_audit.md`;
- analysis output root:
  `output/validation_checks/track2d_mean_offset_full_matrix_audit/`;
- report bundle:
  `doc/reports/analysis/track2/mean_offset_full_matrix_audit/[2026-06-03]/`;
- report index:
  `doc/README.md`;
- status updates:
  `doc/running/te_model_live_backlog.md` and
  `doc/reports/analysis/Training Results Master Summary.md`.

Reference inputs:

- `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`;
- `doc/reports/analysis/track2/mean_centered_collage_report/[2026-06-02]/track2_mean_centered_collage_report.md`;
- `doc/reports/analysis/track2/curve_first_reranking_report/[2026-05-28]/track2_curve_first_reranking_report.md`;
- `doc/reports/analysis/track2/curve_payload_diagnostics_report/[2026-05-28]/track2_curve_payload_diagnostics_report.md`;
- `scripts/reports/analysis/build_track2_mean_centered_collage_report.py`;
- `scripts/reports/analysis/build_track2_curve_payload_diagnostics_report.py`;
- `scripts/reports/analysis/build_track2_curve_first_reranking_report.py`.

## Implementation Steps

1. Inspect the existing `CVP 1.1`, `CVP 1.2`, and mean-centered collage
   builders to reuse candidate loading, prediction payload loading, report
   writing, and plotting conventions.
2. Add the `CVP 1.4` full-matrix audit script with deterministic output
   paths and CLI arguments for report date, source matrix, and optional
   candidate filtering.
3. Export machine-readable artifacts:
   - per-curve metrics CSV;
   - per-candidate summary CSV;
   - per-surface leaderboard CSV;
   - condition-stratified summary CSV;
   - YAML summary with leaders and diagnostic labels.
4. Generate a Markdown report that keeps `Fw`, `Bw`, and `global` branches in
   parallel and separates raw error, offset error, centered-shape error,
   amplitude error, and harmonic phase error.
5. Generate a styled PDF companion using the repository report pipeline and
   validate the real exported PDF.
6. Update the TE live backlog and Training Results Master Summary so the next
   training decision is based on the CVP 1.4 failure-mode classification.
7. Add script-level documentation under `doc/scripts/reports/analysis/` and
   register the new report and script documentation from `doc/README.md`.
8. Run scoped Python checks for the new script and scoped Markdown QA for all
   touched authored Markdown files.
