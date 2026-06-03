# Track 2E Offset Predictability Feasibility

## Overview

This document plans the next analysis step after the completed `Track 2D`
mean-offset full-matrix audit.

The goal is to determine whether the persistent curve-level vertical offset
identified by the mean-centered diagnostics is predictable from the same
causal information that can be available at runtime: current point-level
state, explicitly supported short causal history, and causal derived
features. The analysis must not use future TE curve samples as model inputs
and must not restructure the dataset into non-deployable full-curve inputs.

This is an analysis-only feasibility step. It must not train production
models, start a campaign, change registries, promote a new best model, or
alter the `Fw`, `Bw`, and `global` parallel-branch policy.

## Technical Approach

Implement a `Track 2E` diagnostic report that consumes the completed
`Track 2D` machine-readable artifacts and evaluates whether the curve mean
offset can be explained or approximated from causal metadata and candidate
prediction diagnostics.

The analysis should keep three surfaces in parallel:

- `Fw`;
- `Bw`;
- `global`.

For each surface and candidate group, the report should answer:

- whether the candidate is mainly offset-limited, shape-limited, or mixed;
- whether offset magnitude changes with speed, torque, oil temperature,
  direction, or valid-window identifiers;
- whether a simple causal offset calibration would reduce raw curve error;
- whether the calibration signal is stable enough to justify a future
  sequential residual-offset model;
- whether a future multi-head model should explicitly separate centered
  waveform shape from curve offset;
- whether a loss-function change should prioritize raw error, centered-shape
  error, offset error, amplitude error, or a weighted combination.

The first implementation should prefer conservative, inspectable diagnostics
over a new learned production path. Candidate feasibility methods should
include:

- per-surface offset distribution summaries;
- condition-stratified offset medians and dispersion;
- simple causal baseline correction using training-safe condition aggregates
  when the required split information is available;
- leakage checks that distinguish post-inference full-curve diagnostics from
  deployable causal inputs;
- decision labels that map candidates to the next likely intervention:
  `loss_reweighting`, `multi_head_shape_offset`, `sequential_offset_model`,
  `posthoc_offset_baseline`, or `not_offset_first`.

If a learned offset-predictability probe is added, it must remain explicitly
diagnostic and must use only causal features available before or at the
current TE prediction point. It must not be treated as a production model or
campaign result without a later training-gate document and campaign plan.

## Involved Components

Expected implementation surfaces:

- new script:
  `scripts/reports/analysis/build_track2e_offset_predictability_feasibility.py`;
- script documentation:
  `doc/scripts/reports/analysis/build_track2e_offset_predictability_feasibility.md`;
- analysis output root:
  `output/validation_checks/track2e_offset_predictability_feasibility/`;
- report bundle:
  `doc/reports/analysis/track2/offset_predictability_feasibility/[2026-06-03]/`;
- report index:
  `doc/README.md`;
- status updates:
  `doc/running/te_model_live_backlog.md` and
  `doc/reports/analysis/Training Results Master Summary.md`.

Reference inputs:

- `doc/reports/analysis/track2/mean_offset_full_matrix_audit/[2026-06-03]/track2d_mean_offset_full_matrix_audit.md`;
- `output/validation_checks/track2d_mean_offset_full_matrix_audit/2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit/track2d_per_curve_metrics.csv`;
- `output/validation_checks/track2d_mean_offset_full_matrix_audit/2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit/track2d_candidate_summary.csv`;
- `output/validation_checks/track2d_mean_offset_full_matrix_audit/2026-06-03-10-54-10__track2d_mean_offset_full_matrix_audit/track2d_condition_stratified_summary.csv`;
- `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`;
- `doc/reports/analysis/Training Results Master Summary.md`;
- `doc/running/te_model_live_backlog.md`.

## Implementation Steps

1. Inspect the `Track 2D` CSV and YAML artifacts to identify available
   per-curve, per-candidate, and condition-level fields.
2. Implement the `Track 2E` diagnostic builder with deterministic output paths
   and CLI arguments for report date, source `Track 2D` output directory, and
   optional candidate filtering.
3. Compute offset-predictability summaries for `Fw`, `Bw`, and `global`
   separately, preserving the parallel-best policy.
4. Add conservative causal correction baselines only when the required
   grouping variables are available without future-curve leakage.
5. Export machine-readable artifacts:
   - per-candidate feasibility summary CSV;
   - per-surface intervention recommendation CSV;
   - condition-level offset stability CSV;
   - YAML summary with recommended next intervention per surface.
6. Generate a Markdown report that explains whether the next step should be
   loss reweighting, multi-head shape/offset modeling, sequential offset
   modeling, post-hoc offset calibration, or a non-offset-first branch.
7. Generate and validate a styled PDF companion if the report is stable enough
   for decision review.
8. Update the TE live backlog and Training Results Master Summary with the
   resulting decision labels and the recommended next training gate.
9. Add script-level documentation under `doc/scripts/reports/analysis/` and
   register the new report and script documentation from `doc/README.md`.
10. Run scoped Python checks for the new script and scoped Markdown QA for all
    touched authored Markdown files.
