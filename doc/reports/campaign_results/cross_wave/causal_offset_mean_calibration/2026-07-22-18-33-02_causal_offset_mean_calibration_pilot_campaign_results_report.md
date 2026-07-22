# Causal Offset Mean Calibration Pilot Campaign Results

## Overview

This report closes the
`causal_offset_mean_calibration_pilot_2026_07_22` campaign. The campaign tested
whether direct offset / curve-mean pressure gives a better next branch than
continuing direct shape-threshold loss escalation.

The campaign used `polished_dataset` setpoint `Fw` data only and preserved both
development roads requested for this stage:

- a time-windowed residual-offset GRU candidate;
- a non-windowed periodic MLP harmonic candidate.

The campaign completed remotely through manual recovery after the repository
remote launcher and the user's terminal exited around transport handling. The
remote runner produced `Completed 2` and `Failed 0`; the generated artifacts
were synchronized back from the remote workstation.

## Execution Summary

| Item | Value |
| --- | --- |
| Campaign | `causal_offset_mean_calibration_pilot_2026_07_22` |
| Dataset | `polished_dataset` |
| Input mode | `setpoints` |
| Surface | `Fw` |
| Completed runs | `2` |
| Failed runs | `0` |
| Scalar winner | `causal_offset_mean_periodic_mlp_harmonic_fw` |
| Promotion | Not promoted |
| Required next gate | bounded `TE Curve Verification Pipeline` screen |

## Candidate Ranking

| Rank | Family | Runtime Road | Validation MAE | Test MAE | Test RMSE | Params |
| ---: | --- | --- | ---: | ---: | ---: | ---: |
| 1 | `causal_offset_mean_periodic_mlp_harmonic_fw` | non-windowed harmonic MLP | 0.001469 | 0.001277 | 0.001739 | 28,545 |
| 2 | `causal_offset_mean_gru_sequence_fw` | time-windowed residual-offset GRU | 0.002428 | 0.002100 | 0.002610 | 92,802 |

## Metric Breakdown

| Metric | Validation | Test |
| --- | ---: | ---: |
| MLP pointwise loss | 0.008758 | 0.006205 |
| MLP centered curve shape loss | 0.007616 | 0.005440 |
| MLP curve offset loss | 0.002398 | 0.002524 |
| MLP curve amplitude loss | 0.098801 | 0.070889 |
| MLP sparse harmonic shape loss | 0.000134 | 0.000094 |
| GRU pointwise loss | 0.021806 | 0.014675 |
| GRU centered curve shape loss | 0.019289 | 0.011694 |
| GRU curve offset loss | 0.002517 | 0.002981 |
| GRU curve amplitude loss | 0.106397 | 0.053888 |
| GRU sparse harmonic shape loss | 0.000443 | 0.000250 |
| GRU base MAE | 0.013305 | 0.013640 |
| GRU residual offset mean abs | 0.013476 | 0.014143 |

## Pilot Comparison

| Family | Surface | Validation MAE | Test MAE | Decision |
| --- | --- | ---: | ---: | --- |
| `periodic_gru_sequence_fw` | `Fw` | 0.001099 | 0.001101 | Accepted model-development forward baseline remains stronger on scalar error. |
| `shape_objective_periodic_mlp_harmonic_fw` | `Fw` | 0.001429 | 0.001236 | Stronger scalar MLP reference, but failed bounded curve-first promotion. |
| `causal_offset_mean_periodic_mlp_harmonic_fw` | `Fw` | 0.001469 | 0.001277 | Campaign scalar winner; useful non-windowed result, not promoted. |
| `periodic_mlp_harmonic_fw` | `Fw` | 0.001144 | 0.001326 | Original non-windowed comparator; new MLP improves test MAE against this scalar baseline. |
| `shape_first_distilled_periodic_mlp_harmonic_fw` | `Fw` | 0.001573 | 0.001420 | New MLP improves scalar error against the prior distillation MLP. |
| `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw` | `Fw` | 0.001983 | 0.001463 | New MLP is stronger on scalar test MAE. |
| `causal_offset_mean_gru_sequence_fw` | `Fw` | 0.002428 | 0.002100 | Completed control, but not worth expanding in this exact profile. |

## Interpretation

The non-windowed harmonic MLP is the only useful result from this pilot. It
improves the scalar test MAE against the original non-windowed
`periodic_mlp_harmonic_fw` comparator and against the prior
shape-first-distilled MLP, but it does not beat the strongest scalar
shape-objective MLP reference and does not beat the accepted forward
model-development GRU baseline.

The time-windowed residual-offset GRU did not work as a next road in this
configuration. Its final test MAE is `0.002100 deg`, and the logged base MAE
plus residual-offset magnitude show that the residual branch is making a large
correction without becoming competitive. This branch should stay as completed
evidence, not as the immediate expansion path.

The MLP result is not enough for promotion. The recent shape-objective pilot
already showed that a strong scalar MLP can fail the bounded curve-first screen.
This new winner therefore needs the same bounded `TE Curve Verification
Pipeline` treatment before it can affect accepted model status.

## Decision

Close the campaign as completed and do not promote either candidate.

The next repository step is a bounded `TE Curve Verification Pipeline` screen
on `polished_dataset` setpoint `Fw` that compares:

- `causal_offset_mean_periodic_mlp_harmonic_fw`;
- `causal_offset_mean_gru_sequence_fw`;
- `polished_setpoints_periodic_gru_sequence_Fw`;
- `polished_setpoints_periodic_mlp_harmonic_Fw`.

The screen may include `shape_objective_periodic_mlp_harmonic_Fw` as a scalar
high-water reference, but promotion must still follow the multi-index
curve-first policy rather than scalar `MAE` alone.

## Operational Note

The campaign result is valid, but remote execution tooling needs follow-up
before the next heavy campaign. The repository launcher and the user's terminal
both exited during remote transport handling, and direct remote `conda run`
returned a nonzero post-completion process code after writing successful
campaign outputs. The campaign leaderboard is the canonical ranking surface for
this closeout because the aggregate
`output/registries/families/causal_offset_mean_calibration/leaderboard.yaml`
artifact was not generated.

## Primary Artifacts

- `output/training_campaigns/2026-07-22-18-09-27_causal_offset_mean_calibration_pilot_2026_07_22/campaign_leaderboard.yaml`
- `output/training_campaigns/2026-07-22-18-09-27_causal_offset_mean_calibration_pilot_2026_07_22/campaign_best_run.yaml`
- `output/training_campaigns/2026-07-22-18-09-27_causal_offset_mean_calibration_pilot_2026_07_22/campaign_best_run.md`
- `output/training_runs/causal_offset_mean_calibration/2026-07-22-18-15-50__te_causal_offset_mean_periodic_mlp_harmonic_fw__polished_setpoints/`
- `output/training_runs/causal_offset_mean_calibration/2026-07-22-18-09-27__te_causal_offset_mean_gru_sequence_fw__polished_setpoints/`
- `doc/reports/campaign_plans/cross_wave/causal_offset_mean_calibration/2026-07-22-17-42-11_causal_offset_mean_calibration_pilot_plan_report.md`
- `doc/reports/analysis/model_development_waves/wave_5_2/causal_offset_mean_calibration/[2026-07-22]/causal_offset_mean_calibration_pilot_model_report.md`
