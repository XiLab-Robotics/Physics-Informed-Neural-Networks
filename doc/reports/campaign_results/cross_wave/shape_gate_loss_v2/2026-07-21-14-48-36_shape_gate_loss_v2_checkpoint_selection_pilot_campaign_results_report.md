# Shape-Gate Loss V2 Checkpoint Selection Pilot Campaign Results Report

## Executive Summary

The `shape_gate_loss_v2_checkpoint_selection_pilot_2026_07_21` campaign
completed the approved one-run pilot on `polished_dataset` setpoints for the
`Fw` surface.

The accepted campaign output directory is
`output/training_campaigns/2026-07-21-13-03-55_shape_gate_loss_v2_checkpoint_selection_pilot_2026_07_21`.

The run completed without queue failures and produced the required campaign
leaderboard, best-run YAML, best-run Markdown, metrics summary, training
report, and checkpoint. It is accepted as a completed pilot, but it is not
promoted to a full three-target, three-surface campaign on scalar evidence
alone.

Pilot result:

- run: `te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints`;
- dataset: `polished_dataset`;
- input mode: `setpoints`;
- surface: `fw` / `forward_only`;
- validation MAE: `0.001983 deg`;
- validation RMSE: `0.002445 deg`;
- test MAE: `0.001463 deg`;
- test RMSE: `0.001831 deg`;
- trainable parameters: `157,953`.

The scalar result improves materially over the first shape-gate loss pilot and
beats the older same-backbone polished-setpoint `periodic_gru_sequence` `Fw`
scalar baseline listed in the first pilot closeout. It remains a pilot-only
checkpoint-selection result, because promotion still requires corrected
shape-gated curve evidence and later full-matrix coverage.

## Campaign Scope

The pilot intentionally used the narrowest approved scope:

| Field | Value |
| --- | --- |
| Campaign | `shape_gate_loss_v2_checkpoint_selection_pilot_2026_07_21` |
| Dataset | `polished_dataset` |
| Input mode | `setpoints` |
| Dataset schema | `polished_setpoint_curve_v1` |
| Surface | `Fw` |
| Base model | `periodic_gru_sequence` |
| Loss profile | `shape_gate_v2_light_centered_offset_amplitude_harmonic` |
| Expected run count | `1` |
| Completed run count | `1` |
| Failed run count | `0` |

The full promotion rule remains unchanged: any model family that survives a
pilot must later be trained across `simplified_setpoints`,
`polished_setpoints`, and `polished_actual_values`, with separate `global`,
`Fw`, and `Bw` surfaces.

## Remote Execution

The operator launched the campaign through the dedicated remote wrapper:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.ps1 `
  -Remote
```

The remote training itself completed successfully on `xilab-remote`. The
original local SSH transport remained open before final marker capture, so the
automatic sync-down stage did not complete. The completed remote artifacts were
then recovered from
`C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks`
and synchronized into this local repository.

## Artifact Audit

| Artifact | Path |
| --- | --- |
| Campaign leaderboard | `output/training_campaigns/2026-07-21-13-03-55_shape_gate_loss_v2_checkpoint_selection_pilot_2026_07_21/campaign_leaderboard.yaml` |
| Campaign best run | `output/training_campaigns/2026-07-21-13-03-55_shape_gate_loss_v2_checkpoint_selection_pilot_2026_07_21/campaign_best_run.yaml` |
| Campaign best-run report | `output/training_campaigns/2026-07-21-13-03-55_shape_gate_loss_v2_checkpoint_selection_pilot_2026_07_21/campaign_best_run.md` |
| Training metrics | `output/training_runs/shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence/2026-07-21-13-03-55__te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints/metrics_summary.yaml` |
| Training report | `output/training_runs/shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence/2026-07-21-13-03-55__te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints/training_test_report.md` |
| Best checkpoint | `output/training_runs/shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence/2026-07-21-13-03-55__te_shape_gate_loss_v2_periodic_gru_sequence_fw__polished_setpoints/checkpoints/periodic_gru_sequence-epoch=008-val_mae=0.00198279.ckpt` |
| Completed queue entry | `config/training/queue/shape_gate_loss_v2_pilot/completed/2026-07-21-13-03-55_001_001_shape_gate_loss_v2_periodic_gru_sequence_fw.yaml` |
| Family registry | `output/registries/families/shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw/latest_family_best.yaml` |

## Metric Breakdown

| Metric | Validation | Test |
| --- | ---: | ---: |
| Total loss | `0.021138` | `0.011095` |
| MAE | `0.001983` | `0.001463` |
| RMSE | `0.002445` | `0.001831` |
| Pointwise loss | `0.017484` | `0.009410` |
| Centered curve-shape loss | `0.014076` | `0.007082` |
| Curve-offset loss | `0.003407` | `0.002328` |
| Curve-amplitude loss | `0.048856` | `0.019544` |
| Sparse harmonic-shape loss | `0.000339` | `0.000146` |

## Pilot Comparison

These are scalar training metrics, not official `TE Curve Verification
Pipeline` decisions.

| Family | Surface | Validation MAE | Test MAE | Decision |
| --- | --- | ---: | ---: | --- |
| `periodic_mlp_harmonic` | `global` | `0.001137` | `0.001270` | Stronger scalar baseline |
| `periodic_mlp_harmonic` | `Fw` | `0.001208` | `0.001442` | Slightly stronger scalar baseline |
| `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw` | `Fw` | `0.001983` | `0.001463` | Completed v2 pilot; shape-gated screen required |
| `periodic_gru_sequence` | `Fw` | `0.001832` | `0.002108` | Older same-backbone scalar baseline; worse test MAE |
| `wave4_1_mae_robust_loss` | `Fw` | `0.001792` | `0.002109` | Worse test MAE than v2, still active shape-first road |
| `wave4_2_quantile_p10_p50_p90` | `Fw` | `0.001801` | `0.002141` | Worse test MAE than v2, still active shape-first road |
| `shape_gate_loss_pilot_periodic_gru_sequence` | `Fw` | `0.002297` | `0.002522` | First pilot; superseded by v2 scalar result |

## Acceptance Decision

The campaign is accepted as a completed pilot because:

- the one approved queue entry completed;
- the completed run uses `polished_dataset` setpoints and `Fw` as requested;
- the campaign leaderboard and best-run artifacts exist;
- the metrics summary, training report, checkpoint, and completed queue entry
  exist locally after remote recovery;
- the family registry and program registry were synchronized from the remote
  repository.

The model is not accepted as a new active leader yet because:

- the pilot covers only one surface and one target;
- the corrected calibrated shape-gated reranker has not yet evaluated the
  checkpoint;
- the full promotion rule requires `simplified_setpoints`,
  `polished_setpoints`, and `polished_actual_values`, each across `global`,
  `Fw`, and `Bw`;
- official `TE Curve Verification Pipeline` decisions cannot be made from
  scalar `MAE` alone.

## Recommended Next Step

Do not launch the full Aries matrix yet.

The next step should be a bounded checkpoint-level `TE Curve Verification
Pipeline` screen for this v2 checkpoint on `polished_dataset` setpoints `Fw`,
followed by the calibrated shape-gated reranker. If the v2 checkpoint keeps
its scalar gain while improving shape, harmonic, derivative, and phase evidence
against the first pilot and the reduced active `Fw` set, then prepare a
separate full-matrix campaign package. If it fails the shape gate, stop this
loss-profile branch and keep the shape metrics as validation and selection
evidence rather than expanding the training objective.

## Closeout Boundary

This closeout does not change the official `TE Curve Verification Pipeline`
leaders and does not promote the v2 pilot to program baseline. The official
selection boundary remains curve-first and per-surface.
