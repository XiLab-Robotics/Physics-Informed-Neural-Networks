# Original ONNX TE Curve Verification Pipeline Offset Diagnostic

## Overview

This technical document plans a focused diagnostic pass that loads the recovered
original RCIM paper ONNX models, evaluates them through the repository `TE Curve Verification Pipeline`
forward reconstruction path, and checks whether the mean-offset error pattern
seen in the recent `CVP 1.1` through `Wave 3.1` investigation is present in
the original ONNX release itself.

The repository already contains an ONNX parity runner that evaluates the
recovered original ONNX release against the repository `rcim_original/forward`
archive. The existing historical run proves that ONNX models can be passed
through `TE Curve Verification Pipeline`, but it does not export enough per-curve payload or
mean-centered diagnostics to answer the current offset question directly.

Context7 was requested for ONNX Runtime API details before ONNX-specific work,
but the configured Context7 server returned `Invalid or expired OAuth token`.
The implementation will therefore use local repository code inspection and the
already-working repository-owned ONNX Runtime call path as the fallback.

## Technical Approach

Extend or wrap the existing
`scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_original_onnx_release_parity_validation.py`
workflow without changing the canonical `TE Curve Verification Pipeline` matrix semantics.

The diagnostic should:

- load the recovered original ONNX release from
  `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`;
- use the existing `CPUExecutionProvider` ONNX Runtime path;
- build the canonical `TE Curve Verification Pipeline` forward test curve records from
  `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`;
- reconstruct forward TE curves from ONNX-predicted amplitude and phase targets
  using the same harmonic coefficient convention documented in
  `Track 2 Curve Reconstruction And Collage Pipeline.md`;
- compute raw curve metrics and mean-centered offset diagnostics per family and
  per curve;
- compare ONNX original results against the repository `rcim_original/forward`
  Python archive where available;
- write a machine-readable validation summary plus CSV tables under
  `output/validation_checks/`;
- write a Markdown interpretation report under
  `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/` or a narrower
  `doc/reports/analysis/te_curve_verification_pipeline/` diagnostic topic folder;
- register the final report from `doc/README.md` when created.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_original_onnx_release_parity_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/harmonic_wise_support.py`
- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`
- `models/paper_reference/rcim_original/forward`
- `output/validation_checks/rcim_original_onnx_release_parity/`
- `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/`
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/TE Curve Verification Pipeline Curve Reconstruction And Collage Pipeline.md`
- `doc/README.md`

## Implementation Steps

1. Inspect the existing ONNX parity runner and decide whether to add a narrow
   diagnostic mode or create a small companion script that reuses its helper
   functions.
2. Preserve the existing historical parity behavior and output schema unless a
   backward-compatible field addition is necessary.
3. Add mean-centered per-curve metric computation for ONNX TE Curve Verification Pipeline forward
   reconstructions:
   - raw MAE and RMSE;
   - truth mean;
   - predicted mean;
   - offset error;
   - mean-centered MAE and RMSE;
   - improvement from raw to mean-centered metrics.
4. Run the diagnostic locally with an explicit output suffix that identifies
   the offset investigation.
5. Inspect the resulting YAML and CSV artifacts, focusing on whether ONNX
   original families show the same raw-to-centered improvement pattern.
6. Write a concise interpretation report with family-level conclusions and the
   ONNX Runtime limitations for incomplete families such as `SVR` and `XGBM`.
7. Register the report from `doc/README.md` if the run produces a new canonical
   interpretation artifact.
8. Run scoped Python compilation and Markdown QA on touched source and
   documentation files.
