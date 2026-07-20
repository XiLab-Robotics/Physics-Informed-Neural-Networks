# Shape-Gate Loss Pilot Campaign Plan

## Campaign Status

Planning only. No training, smoke run, campaign package generation, Slurm
submission, registry update, or `TE Curve Verification Pipeline` refresh has
started.

The approved technical document is:

- `doc/technical/2026-07/2026-07-20/2026-07-20-18-10-35_shape_gate_loss_pilot_and_full_surface_campaign.md`

## Objective

Test whether the calibrated shape-gated reranker metrics can improve training
or checkpoint selection without weakening the current shape-first promotion
policy.

The first pilot uses `polished_dataset` `setpoints` `Fw` as the primary
surface. This is deliberately narrow: it should answer whether shape-aware
pressure helps before preparing a full Aries campaign.

Any new model or materially changed loss profile is not promotable from the
pilot alone. Full promotion requires the complete dataset/input-mode and
surface matrix:

| Target | Surfaces |
| --- | --- |
| `simplified_setpoints` | `global`, `Fw`, `Bw` |
| `polished_setpoints` | `global`, `Fw`, `Bw` |
| `polished_actual_values` | `global`, `Fw`, `Bw` |

The full promotion matrix therefore contains at least `9` runs per approved
model/loss profile.

## Evidence Base

The plan is based on:

- calibrated shape-gated reranker:
  `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-20]/selected_active_track2_polished_setpoints_matrix_shape_gated_te_curve_reranker_report.md`;
- actual-values comparison reranker:
  `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-20]/selected_active_track2_polished_actual_values_matrix_shape_gated_te_curve_reranker_report.md`;
- existing curve-aware loss support in
  `scripts/training/transmission_error_regression_module.py`;
- existing dataset/input-mode retraining materialization pattern in
  `scripts/campaigns/cross_wave/prepare_dataset_input_mode_retraining_campaign.py`.

The calibrated reranker found that the raw derivative-correlation gate alone
is too brittle, while normalized derivative RMSE, derivative sign agreement,
FFT amplitude similarity, harmonic amplitude, harmonic phase, offset, and
centered-shape metrics give a stricter but usable screen.

## Stage 1 Pilot Scope

The pilot should be small and directly falsifiable.

| Field | Value |
| --- | --- |
| Dataset | `polished_dataset` |
| Input mode | `setpoints` |
| Primary surface | `Fw` |
| Primary baseline | `periodic_gru_sequence_Fw` |
| Shape comparator | `wave4_1_mae_robust_loss_Fw` |
| Training status | not prepared |
| Execution target | local one-batch validation first, Aries short run only after approval |

The first pilot should start from the temporal `periodic_gru_sequence` family
unless live config inspection proves that another active family can reuse the
shape-aware loss path with less implementation risk.

## Candidate Loss Or Monitor Terms

Reuse the existing loss infrastructure before adding new code. The current
training module already supports:

- pointwise loss;
- centered curve-shape loss;
- curve-offset loss;
- curve-amplitude loss;
- sparse harmonic-shape loss.

The pilot may add or expose only the minimum extra terms needed for calibrated
shape-gate alignment:

- normalized derivative RMSE;
- derivative sign agreement or a differentiable surrogate;
- validation-only shape-gate monitor values for checkpoint selection.

Every enabled term must be:

- normalized against target scale or curve peak-to-peak amplitude;
- logged independently from total loss;
- disabled by default outside the approved pilot profile;
- compatible with causal runtime inference inputs.

Full-curve loss terms are allowed during training when the batch contains full
training curves. They must not become future-looking runtime corrections in
deployed inference.

## Stage 1 Acceptance Screen

The pilot is worth expanding only if it improves shape evidence without hiding
a scalar regression.

Minimum acceptance checks:

- raw `MAE` and `RMSE` do not degrade materially against the active baseline;
- centered-shape error improves or remains equal;
- harmonic amplitude and phase do not regress;
- normalized derivative RMSE or derivative sign agreement improves;
- calibrated shape-gated reranker keeps the pilot above the baseline or marks
  it as a credible `candidate`;
- visual curve overlays do not show lost ripple or phase drift.

A lower scalar `MAE` is not sufficient if the curve-shape diagnostics fail.

## Stage 2 Full Aries Campaign Scope

If Stage 1 passes, prepare a full Aries campaign package with exactly the same
model/loss profile across:

- `simplified_setpoints`;
- `polished_setpoints`;
- `polished_actual_values`.

Each target must include:

- `global`;
- `Fw`;
- `Bw`.

The full campaign must use immutable timestamped `run_instance_id` folders and
write artifacts under the repository-standard roots:

- `output/training_runs/<model_family>/<run_instance_id>/`;
- `output/training_campaigns/<campaign_id>/`;
- `output/validation_checks/<model_family>/<run_instance_id>/`;
- `output/registries/families/<model_family>/`;
- `output/registries/program/`.

## Aries Execution Policy

The campaign package must include:

- campaign YAML files;
- a dedicated PowerShell launcher with local and `-Remote` paths;
- a launcher note under `doc/scripts/campaigns/`;
- `doc/running/active_training_campaign.yaml` state with protected files;
- exact local and remote launch commands.

The first execution should be a bounded smoke or pilot run. The full `9`-run
campaign should run on Aries only after pilot acceptance and explicit operator
approval.

## Closeout And Verification

Normal campaign closeout must produce:

- campaign leaderboard;
- campaign best-run YAML;
- campaign best-run Markdown;
- campaign-results report;
- PDF export and validation if the closeout report is final;
- family and program registry updates where applicable;
- synchronized project-status documents.

The heavy official `TE Curve Verification Pipeline` matrix is not part of
normal training closeout. It remains a separate optional refresh after the
training campaign artifacts are accepted.

## Approval Gate

This report is not launch approval. Before any training or campaign package is
generated, the next approved implementation pass must create the pilot config
and validation path, then run only non-training compile and one-batch checks
unless the user explicitly approves execution.
