# Shape Gate Calibration And Training Loss Backlog

## Overview

This technical document plans the next refinement pass after the initial
shape-gated `TE Curve Verification Pipeline` reranker.

The current gate is useful because it is strict: it prevents scalar `MAE`
leaders from being promoted when curve shape, harmonic content, phase behavior,
or local derivative behavior are weak. The problem is that the first threshold
set is too absolute. It currently cuts every selected-active candidate,
including the strongest `periodic_gru_sequence` baseline on polished
actual-value forward and backward surfaces.

The goal of this pass is to keep the gate as a strong screening tool while
making it calibrated enough to distinguish:

- candidates that clearly fail shape preservation;
- candidates that are near-pass and should remain active;
- candidates that pass enough curve-first evidence to justify deeper review;
- metrics that are reliable promotion gates versus metrics that should remain
  diagnostic until validated.

This pass also records a future-work item: once the gate metrics are stable as
validation diagnostics, evaluate whether selected shape, harmonic, phase,
offset, or derivative terms should become training losses or auxiliary
objectives. This idea is plausible, but it should not be promoted directly
until the diagnostic gate is calibrated and the training-time formulation is
causal, differentiable or otherwise optimizable, and not based on future-curve
information unavailable at inference.

No subagent is planned.

## Technical Approach

The implementation should extend the existing
`scripts/reports/analysis/build_shape_gated_te_curve_reranker.py` workflow
rather than creating a parallel report family.

The calibration pass should add an explicit threshold-sweep mode over the
already computed metric families:

- FFT amplitude similarity;
- dominant-harmonic amplitude retention;
- dominant-harmonic phase error;
- mean selected-harmonic amplitude error;
- mean selected-harmonic phase error;
- raw and centered curve error;
- offset error;
- derivative agreement.

The derivative term needs special care. The first implementation used raw
derivative correlation and this made the gate too sharp. The calibration pass
should compare several derivative-style screens without making the gate
permissive:

- raw derivative correlation;
- mean-centered derivative correlation;
- smoothed derivative correlation with a small inspectable window;
- derivative sign-agreement rate;
- derivative RMSE normalized by truth peak-to-peak amplitude.

The gate should remain multi-metric. A candidate should not pass merely because
one threshold is relaxed. The intended policy is:

1. retain hard vetoes for missing evidence, invalid direction scope, severe
   raw error, or severe harmonic/phase failure;
2. treat derivative evidence as a strong screen but avoid requiring a single
   brittle derivative metric to eliminate every candidate;
3. produce candidate labels such as `pass`, `near_pass`, `shape_gate_failed`,
   `baseline_anchor_only`, and `insufficient_evidence`;
4. report which metric caused each failure;
5. preserve forward-led, backward-checked selection and keep `global` paused.

The future training-loss idea should be added to the backlog as an evaluation
item, not as an immediate campaign. The backlog wording should make these
constraints explicit:

- validation diagnostics can use full held-out curves;
- deployed inference cannot use future-curve truth or full-curve
  post-processing;
- training losses may use full training curves only if the model input contract
  remains causal at inference;
- FFT/harmonic, derivative, and offset losses need normalization so they do not
  overpower raw TE accuracy;
- the first experiment should be small and benchmarked against
  `periodic_gru_sequence`, not a broad Wave 6 branch.

## Involved Components

Read-only evidence sources:

- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-20]/selected_active_track2_polished_actual_values_matrix_shape_gated_te_curve_reranker_report.md`;
- `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-20]/selected_active_track2_polished_setpoints_matrix_shape_gated_te_curve_reranker_report.md`;
- `output/validation_checks/shape_gated_te_curve_reranker/2026-07-20-16-49-05__shape_gated_te_curve_reranker/`;
- `output/validation_checks/shape_gated_te_curve_reranker/2026-07-20-16-43-45__shape_gated_te_curve_reranker/`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/te_curve_verification_pipeline/00_overview/multi_index_curve_first_selection_policy/[2026-06-16]/track2_multi_index_curve_first_selection_policy.md`.

Likely edited or generated outputs after approval:

- `scripts/reports/analysis/build_shape_gated_te_curve_reranker.py`;
- a new dated calibration report under
  `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-20]/`;
- threshold-sweep CSV/YAML artifacts under
  `output/validation_checks/shape_gated_te_curve_reranker/`;
- `doc/running/te_model_live_backlog.md` to record the future training-loss
  evaluation item;
- `doc/README.md` if a new canonical calibration report is generated;
- `doc/guide/project_usage_guide.md` and `site/` only if the command surface
  changes.

Protected-file check:

- `doc/running/active_training_campaign.yaml` records the latest campaign as
  completed.
- The protected file list belongs to the closed `rcim_track1` polished
  actual-values campaign.
- This work must not modify those protected campaign package files.
- Updating `doc/running/te_model_live_backlog.md` is allowed after approval
  because it is not listed in the protected campaign file list, but it should
  remain narrow and evidence-based.

No training campaign, training experiment, remote launch, campaign YAML, or
PowerShell campaign launcher is part of this pass.

## Implementation Steps

1. Create this technical document and register it from `doc/README.md`.
2. Wait for explicit user approval before modifying the reranker script,
   generated calibration outputs, or backlog.
3. Extend the reranker with derivative-calibration alternatives and
   threshold-sweep output.
4. Regenerate the polished actual-values and polished setpoints calibration
   reports.
5. Inspect whether the strict gate now separates hard failures from near-pass
   candidates without admitting weak scalar-only models.
6. Update `doc/running/te_model_live_backlog.md` with a future-work item for
   shape/harmonic/phase/offset/derivative-aware training losses, clearly marked
   as evaluation-before-campaign.
7. Register any new canonical report from `doc/README.md`.
8. Run Python compile checks for touched scripts.
9. Run Markdown style and Markdownlint checks on touched Markdown files.
10. Run Sphinx only if approved changes affect the portal scope.
11. Stop and report completion. Do not commit until the user explicitly
    approves a commit.
