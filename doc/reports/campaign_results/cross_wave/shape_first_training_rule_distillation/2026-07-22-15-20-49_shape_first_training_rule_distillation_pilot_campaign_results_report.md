# Shape-First Training-Rule Distillation Pilot Campaign Results

## Overview

The `shape_first_training_rule_distillation_pilot_2026_07_22` campaign tested
whether stable checks from the `TE Curve Verification Pipeline` shape-first
screen could be used as auxiliary training terms instead of only post-training
acceptance criteria.

The pilot deliberately kept both modeling roads alive:

- one time-windowed `periodic_gru_sequence` candidate;
- one non-windowed `periodic_mlp` harmonic candidate.

The campaign ran remotely on `xilab-remote` against `polished_dataset`,
setpoint inputs, and forward-only `Fw` curves. Both runs completed
successfully. The local terminal remained active after remote completion
because the shared remote launcher used a blocking SSH stream polling path.
That infrastructure issue was fixed in
`scripts/campaigns/infrastructure/run_remote_training_campaign.ps1` by moving
remote stdout/stderr handling to asynchronous stream events.

## Execution Summary

| Item | Value |
| --- | --- |
| Campaign | `shape_first_training_rule_distillation_pilot_2026_07_22` |
| Remote host | `xilab-remote` |
| Dataset | `polished_dataset` |
| Input mode | `setpoints` |
| Surface | `Fw` |
| Started | `2026-07-22T14:38:51+02:00` |
| Completed | `2026-07-22T14:48:11+02:00` |
| Completed runs | `2` |
| Failed runs | `0` |
| Campaign output | `output/training_campaigns/2026-07-22-14-38-51_shape_first_training_rule_distillation_pilot_2026_07_22` |

## Candidate Ranking

| Rank | Family | Model Type | Windowed | Validation MAE | Test MAE | Test RMSE | Params |
| ---: | --- | --- | --- | ---: | ---: | ---: | ---: |
| 1 | `shape_first_distilled_periodic_mlp_harmonic_fw` | `periodic_mlp` | no | `0.001573` | `0.001420` | `0.001866` | `28,545` |
| 2 | `shape_first_distilled_periodic_gru_sequence_fw` | `periodic_gru_sequence` | yes | `0.002004` | `0.001523` | `0.001920` | `157,953` |

Scalar campaign selection therefore picks the non-windowed harmonic MLP. This
is not a promotion decision: the repository selection policy requires
curve-first evidence before accepting a compensation-relevant forward model.

## Metric Breakdown

| Metric | Time-Windowed GRU | Non-Windowed Harmonic MLP |
| --- | ---: | ---: |
| Validation pointwise loss | `0.017261` | `0.009553` |
| Validation centered shape loss | `0.014137` | `0.007614` |
| Validation offset loss | `0.003124` | `0.003152` |
| Validation amplitude loss | `0.046970` | `0.102087` |
| Validation sparse harmonic loss | `0.000339` | `0.000131` |
| Test pointwise loss | `0.009925` | `0.007084` |
| Test centered shape loss | `0.007235` | `0.005375` |
| Test offset loss | `0.002689` | `0.003210` |
| Test amplitude loss | `0.018799` | `0.075478` |
| Test sparse harmonic loss | `0.000150` | `0.000090` |

The non-windowed harmonic MLP improved scalar MAE, pointwise loss,
mean-centered shape loss, and sparse harmonic loss. The time-windowed GRU kept
better test offset and amplitude losses. That split is exactly why the result
needs a bounded `TE Curve Verification Pipeline` screen before any expansion:
the scalar and shape-component signals do not collapse to a single clear
deployment answer.

## Interpretation

This pilot gives useful evidence for the training-rule distillation idea. The
non-windowed harmonic road was not dead: once the shape-first rules were added
as training terms, it became the scalar winner and slightly beat the recent
shape-gate loss v2 checkpoint-selection pilot on test MAE.

The result does not overturn the current forward recommendation. A prior
non-windowed shape-objective scalar winner failed the bounded curve-first
screen, so scalar improvement alone is not enough. The correct reading is:
continue testing both the time-windowed and non-windowed roads, but force the
new scalar winner through the same bounded curve-first gate before any larger
campaign.

## Decision

The campaign is accepted as a completed pilot. The scalar winner is
`shape_first_distilled_periodic_mlp_harmonic_fw`.

Do not promote it yet. The next required step is a bounded
`TE Curve Verification Pipeline` screen on `polished_dataset`, setpoint inputs,
and `Fw`, comparing:

- `polished_setpoints_periodic_gru_sequence_Fw`;
- `polished_setpoints_periodic_mlp_harmonic_Fw`;
- `shape_first_distilled_periodic_gru_sequence_fw`;
- `shape_first_distilled_periodic_mlp_harmonic_fw`.

That screen should report raw error, centered shape fidelity, offset behavior,
harmonic retention, derivative/phase behavior, visual measured-vs-predicted
curves, and the curve-first recommendation.

## Artifacts

- Campaign execution report:
  `output/training_campaigns/2026-07-22-14-38-51_shape_first_training_rule_distillation_pilot_2026_07_22/campaign_execution_report.md`
- Campaign leaderboard:
  `output/training_campaigns/2026-07-22-14-38-51_shape_first_training_rule_distillation_pilot_2026_07_22/campaign_leaderboard.yaml`
- Campaign best run:
  `output/training_campaigns/2026-07-22-14-38-51_shape_first_training_rule_distillation_pilot_2026_07_22/campaign_best_run.yaml`
- Time-windowed GRU run:
  `output/training_runs/shape_first_training_rule_distillation/2026-07-22-14-38-51__te_shape_first_distilled_periodic_gru_sequence_fw__polished_setpoints`
- Non-windowed harmonic MLP run:
  `output/training_runs/shape_first_training_rule_distillation/2026-07-22-14-43-06__te_shape_first_distilled_periodic_mlp_harmonic_fw__polished_setpoints`
