# RCIM Paper Reference Archive Parity Report

## Overview

This document plans a repository-local parity analysis across the three saved
RCIM paper-reference archives under `models/paper_reference`:
`rcim_original`, `rcim_retuned`, and `rcim_track1`.

The requested output is a canonical interpretation report under
`doc/reports/analysis`, analogous in structure and intent to
`doc/reports/analysis/RCIM Original ONNX Release Parity Interpretation.md`,
but focused on repository model archives rather than the recovered external
ONNX release.

The comparison must answer whether the saved repository archives behave
consistently on the same evaluation surfaces and where the expected differences
come from:

- `rcim_original`: recovered original-pipeline reference archive, forward-only
  as the paper-original baseline.
- `rcim_retuned`: repository retuned archive, forward and backward.
- `rcim_track1`: final Track 1 faithful full-dataset archive, forward and
  backward.

## Technical Approach

The implementation will be non-training and read-only with respect to model
archives. It will load existing saved model files from `models/paper_reference`
and compare them on the same evaluation protocol already used by the current
Track 2 and paper-reference validation tooling.

The comparison will use two complementary surfaces:

1. **Target-level parity surface**: evaluate each available family-direction
   archive on the paper harmonic targets used for `Tables 2-5` style checks.
   This gives per-family and per-target MAE/RMSE/MAPE snapshots and direct
   deltas between `original`, `retuned`, and `track1` where the same family and
   direction exist.
2. **Track 2 curve surface**: reconstruct TE curves from each available saved
   archive using the current direction-aware Track 2 protocol. Forward archives
   are evaluated on forward curves, backward archives on backward curves, and
   no mixed-direction historical comparison is reintroduced.

The canonical report will summarize:

- archive inventory and direction coverage;
- forward comparison between `rcim_original`, `rcim_retuned`, and
  `rcim_track1`;
- backward comparison between `rcim_retuned` and `rcim_track1`;
- family-level verdicts grouped by strong agreement, expected retune/Track 1
  improvement, discrepancy, and unavailable surface;
- final interpretation suitable for citing in later Track 2 and benchmark
  documentation.

No subagent is planned for this task. If a subagent later becomes useful, its
scope and approval requirement will be documented before launch.

## Involved Components

| Component | Role |
| --- | --- |
| `models/paper_reference/rcim_original` | Repository original-pipeline baseline archive. |
| `models/paper_reference/rcim_retuned` | Repository retuned paper-reference archive. |
| `models/paper_reference/rcim_track1` | Final Track 1 faithful reference archive. |
| `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/run_reference_family_vs_feedforward_comparison.py` | Existing Track 2 directional comparison path to reuse or extend. |
| `scripts/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/reference_family_vs_feedforward_support.py` | Shared candidate loading, prediction, and report support utilities. |
| `doc/reports/analysis/RCIM Original ONNX Release Parity Interpretation.md` | Report structure and interpretation style reference. |
| `doc/reports/analysis/Track 2 Directional Model Comparison.md` | Current canonical Track 2 matrix context. |
| `output/validation_checks` | Destination for generated comparison summaries and tabular artifacts. |
| `doc/reports/analysis` | Destination for the new canonical interpretation report. |

## Implementation Steps

1. Inspect the current archive inventories for `rcim_original`,
   `rcim_retuned`, and `rcim_track1`, including family and direction coverage.
2. Reuse the existing model-loading and Track 2 evaluation paths where possible
   so the comparison uses the same seed, split, curve reconstruction, and
   direction filters as the current canonical Track 2 report.
3. Add a focused comparison entry point if the existing Track 2 runner cannot
   emit the archive-to-archive parity tables directly.
4. Generate machine-readable validation artifacts under
   `output/validation_checks`, including at least a summary YAML and one or
   more CSV tables for family-direction comparisons.
5. Create the canonical report
   `doc/reports/analysis/RCIM Paper Reference Archive Parity Interpretation.md`
   with sections mirroring the ONNX parity interpretation report:
   executive verdict, source artifacts, test context, forward parity,
   backward parity, family-group interpretation, and final conclusion.
6. Register the canonical report in `doc/README.md`.
7. If a new runnable entry point is added, update the relevant user-facing guide
   and Sphinx API index, then rebuild Sphinx warning-free.
8. Run scoped Markdown QA on every touched Markdown file and Python compile QA
   on any new or modified Python script.
