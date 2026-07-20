# Shape-Gate Loss Pilot Campaign Results Report

## Executive Summary

The `shape_gate_loss_pilot_2026_07_20` campaign completed the approved
one-run pilot on `polished_dataset` setpoints for the `Fw` surface.

The accepted campaign output directory is
`output/training_campaigns/2026-07-20-19-59-14_shape_gate_loss_pilot_2026_07_20`.

The run completed without queue failures and produced the required campaign
leaderboard, best-run YAML, best-run Markdown, metrics summary, training report,
and checkpoint. It is accepted as a completed pilot, but it is not promoted to a
full three-target, three-surface training campaign on scalar evidence alone.

Pilot result:

- run: `te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints`;
- dataset: `polished_dataset`;
- input mode: `setpoints`;
- surface: `fw` / `forward_only`;
- validation MAE: `0.002297 deg`;
- validation RMSE: `0.002750 deg`;
- test MAE: `0.002522 deg`;
- test RMSE: `0.003133 deg`;
- trainable parameters: `157,953`.

The scalar result is worse than the existing polished-setpoint `Fw` baselines in
the reduced active set. The next decision should therefore be a strict
`TE Curve Verification Pipeline` shape-gated evaluation of this checkpoint
against the reduced selected-model set, not immediate expansion to the full
matrix.

## Campaign Scope

The pilot intentionally used the narrowest approved scope:

| Field | Value |
| --- | --- |
| Campaign | `shape_gate_loss_pilot_2026_07_20` |
| Dataset | `polished_dataset` |
| Input mode | `setpoints` |
| Dataset schema | `polished_setpoint_curve_v1` |
| Surface | `Fw` |
| Base model | `periodic_gru_sequence` |
| Loss profile | `shape_gate_centered_offset_amplitude_harmonic` |
| Expected run count | `1` |
| Completed run count | `1` |
| Failed run count | `0` |

The full promotion rule remains unchanged: any new model family that survives a
pilot must later be trained across `simplified_setpoints`,
`polished_setpoints`, and `polished_actual_values`, with separate `global`,
`Fw`, and `Bw` surfaces.

## Remote Execution

The first remote invocation failed during repository-root mapping because the
default remote path pointed to the local Windows checkout path. The successful
operator-equivalent command used the remote repository path on `xilab-remote`:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_pilot_campaign.ps1 -Remote -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" -RemoteCondaEnvironmentName pinns_env
```

The local wrapper timed out before its final sync step, after the remote
training had already launched. The completed queue entry and campaign artifacts
were recovered manually from `xilab-remote` and synchronized into the local
repository.

## Artifact Audit

| Artifact | Path |
| --- | --- |
| Campaign leaderboard | `output/training_campaigns/2026-07-20-19-59-14_shape_gate_loss_pilot_2026_07_20/campaign_leaderboard.yaml` |
| Campaign best run | `output/training_campaigns/2026-07-20-19-59-14_shape_gate_loss_pilot_2026_07_20/campaign_best_run.yaml` |
| Campaign best-run report | `output/training_campaigns/2026-07-20-19-59-14_shape_gate_loss_pilot_2026_07_20/campaign_best_run.md` |
| Training metrics | `output/training_runs/shape_gate_loss_pilot_periodic_gru_sequence/2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints/metrics_summary.yaml` |
| Training report | `output/training_runs/shape_gate_loss_pilot_periodic_gru_sequence/2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints/training_test_report.md` |
| Best checkpoint | `output/training_runs/shape_gate_loss_pilot_periodic_gru_sequence/2026-07-20-19-59-14__te_shape_gate_loss_periodic_gru_sequence_fw__polished_setpoints/checkpoints/periodic_gru_sequence-epoch=007-val_mae=0.00229675.ckpt` |
| Completed queue entry | `config/training/queue/shape_gate_loss_pilot/completed/2026-07-20-19-59-14_001_001_shape_gate_loss_periodic_gru_sequence_fw.yaml` |

## Metric Breakdown

| Metric | Validation | Test |
| --- | ---: | ---: |
| Total loss | `0.008242` | `0.011919` |
| MAE | `0.002297` | `0.002522` |
| RMSE | `0.002750` | `0.003133` |
| Pointwise loss | `0.005697` | `0.008580` |
| Centered curve-shape loss | `0.004500` | `0.005242` |
| Curve-offset loss | `0.001197` | `0.003338` |
| Curve-amplitude loss | `0.015342` | `0.018935` |
| Sparse harmonic-shape loss | `0.000108` | `0.000113` |

## Comparable Polished-Setpoint Baselines

The table compares the pilot only against local training runs that used
`polished_setpoints`. These are scalar training metrics, not official
curve-first verification results.

| Family | Surface | Validation MAE | Test MAE | Decision |
| --- | --- | ---: | ---: | --- |
| `periodic_mlp_harmonic` | `global` | `0.001137` | `0.001270` | Stronger scalar baseline |
| `periodic_mlp_harmonic` | `Fw` | `0.001208` | `0.001442` | Stronger scalar baseline |
| `wave4_1_mae_robust_loss` | `Fw` | `0.001792` | `0.002109` | Stronger scalar baseline |
| `periodic_gru_sequence` | `Fw` | `0.001832` | `0.002108` | Stronger same-backbone baseline |
| `wave4_2_quantile_p10_p50_p90` | `Fw` | `0.001801` | `0.002141` | Stronger scalar baseline |
| `shape_gate_loss_pilot_periodic_gru_sequence` | `Fw` | `0.002297` | `0.002522` | Completed pilot, not promoted |

## Acceptance Decision

The campaign is accepted as a completed pilot because:

- the one approved queue entry completed;
- the completed run uses `polished_dataset` setpoints and `Fw` as requested;
- the campaign leaderboard and best-run artifacts exist;
- the metrics summary, training report, checkpoint, and completed queue entry
  exist locally after manual remote sync;
- the active campaign state records the remote-path recovery and final result.

The model is not accepted as a new active leader because:

- test MAE is worse than the same-backbone `periodic_gru_sequence` `Fw`
  polished-setpoint baseline;
- test MAE is worse than the current reduced-set polished-setpoint `Fw`
  robust and quantile candidates;
- the run has not yet passed the calibrated shape-gated reranker;
- the pilot covers only one surface and one target, while promotion requires
  three targets and three surfaces.

## Recommended Next Step

Do not launch the full Aries campaign yet.

The next step should be a checkpoint-level `TE Curve Verification Pipeline`
adapter for this pilot run, followed by a calibrated shape-gated reranker pass
on `polished_dataset` setpoints `Fw`. If the pilot shows a material shape,
harmonic, or phase improvement despite weaker scalar MAE, then prepare a second
pilot with softened weights or a two-run weight ablation. If it fails the shape
gate as well, stop this branch and keep the shape metrics as validation and
selection tools rather than as a training objective.

## Closeout Boundary

This closeout does not change the official `TE Curve Verification Pipeline`
leaders and does not promote the shape-gate loss pilot to program baseline. The
official selection boundary remains curve-first and per-surface.
