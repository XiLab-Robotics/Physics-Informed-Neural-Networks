# TE Curve Verification Pipeline Curve Reconstruction Documentation

## Overview

This technical document plans a repository-owned Markdown report that documents
how `TE Curve Verification Pipeline` reconstructs and plots TE curves in the best-model collage report.
The report will focus on the standard collage pipeline, the repository-model
path represented by `harmonic_regression`, the paper-original forward reference
path represented by `paper_original_best_Fw`, and the relationship to the
mean-centered diagnostics introduced by commit
`940a16b934e29ca83fef36da010fdf671bdd52c4`.

## Technical Approach

Create a detailed analysis report under `doc/reports/analysis/track2/` using a
readable title-based filename or a narrow topic-root folder. The report will
cite concrete source files and line ranges from the current repository code,
including the `TE Curve Verification Pipeline` matrix template, shared evaluation support, collage
report builder, mean-centered diagnostics builder, harmonic decomposition
support, and `harmonic_regression` model implementation.

The report will distinguish the two inference paths:

- repository-backed models that predict full TE curves point-by-point;
- paper/reference-bank candidates that predict amplitude and phase targets
  before reconstructing a TE curve from harmonic coefficients.

## Involved Components

- `config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/full_track2_matrix_template.yaml`
- `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/harmonic_wise_support.py`
- `scripts/reports/analysis/build_track2_best_model_collage_report.py`
- `scripts/reports/analysis/build_track2_mean_centered_collage_report.py`
- `scripts/models/harmonic_regression.py`
- `doc/reports/analysis/track2/`
- `doc/README.md`

## Implementation Steps

1. Create the detailed TE Curve Verification Pipeline curve reconstruction Markdown report after this
   technical document is explicitly approved.
2. Include step-by-step sections for dataset/test-curve construction, candidate
   loading, direction filtering, metric calculation, representative-curve
   selection, payload regeneration, and plotting.
3. Include a dedicated `harmonic_regression` section that explains registry
   loading and direct pointwise TE prediction.
4. Include a dedicated `paper_original_best_Fw` section that explains the 10
   amplitude and 9 phase predictions, the amplitude/phase-to-coefficient
   conversion, and final harmonic reconstruction.
5. Include code-reference tables and short code excerpts with original file
   paths and line numbers.
6. Register the finished report from `doc/README.md`.
7. Run Markdown QA on the touched Markdown scope and fix any warnings before
   reporting completion.
