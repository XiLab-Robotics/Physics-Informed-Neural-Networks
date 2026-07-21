# Shape Gate Loss V2 Checkpoint Selection Pilot

## Overview

The first `shape_gate_loss_pilot_periodic_gru_sequence_Fw` run proved that a
shape-aware training pressure can produce a viable forward candidate, but the
patched polished-setpoint Fw/Bw expansion did not promote it. The pilot passed
the forward shape gate yet ranked fifth behind the existing polished-setpoint
active candidates. Launching the full three-dataset, three-surface Aries
campaign from that exact loss profile is therefore not justified.

The next step is a stricter second pilot on the primary surface:
`polished_dataset` setpoints `Fw`. The pilot should test whether shape-gate
metrics are more useful as checkpoint-selection monitors and light auxiliary
pressures than as a broad composite loss that competes with scalar MAE.

## Technical Approach

The pilot will remain intentionally small and non-promotional:

- train only `polished_dataset` setpoints `Fw` first;
- keep `periodic_gru_sequence` as the base temporal family;
- preserve the existing scalar training objective as the anchor;
- add a narrow ripple/derivative-aware auxiliary pressure only if it is
  already supported by the current training loss infrastructure or can be added
  cleanly;
- compute validation-side shape-gate monitor metrics after checkpoints or at
  bounded validation intervals, focusing on normalized derivative RMSE,
  derivative sign agreement, smoothed derivative correlation, FFT amplitude
  similarity, harmonic amplitude error, harmonic phase error, offset error, and
  per-curve shape pass rate;
- select the candidate checkpoint by a strict ordered policy rather than by
  `val_mae` alone.

The proposed checkpoint ordering is:

1. pass the configured shape gate;
2. improve or match derivative/ripple metrics against the first pilot;
3. avoid worse raw MAE than the first pilot by more than a small tolerance;
4. avoid worse harmonic amplitude and phase metrics;
5. use scalar validation MAE only as the final tie-breaker.

This is not a full campaign acceptance rule. Full promotion still requires
`simplified_setpoints`, `polished_setpoints`, and `polished_actual_values`, each
across `global`, `Fw`, and `Bw`.

## Involved Components

- `scripts/training/transmission_error_regression_module.py`
- `scripts/training/train_feedforward_network.py`
- existing loss/profile configuration under `config/training/`
- new campaign package under `config/training/shape_gate_loss_v2_pilot/`
- new campaign plan under `doc/reports/campaign_plans/cross_wave/`
- new launcher under `scripts/campaigns/cross_wave/`
- new launcher note under `doc/scripts/campaigns/cross_wave/`
- `scripts/reports/analysis/build_shape_gated_te_curve_reranker.py`
- `scripts/reports/analysis/build_track2_candidate_curve_plots.py`
- `doc/running/active_training_campaign.yaml`

No subagent is planned for this task.

## Implementation Steps

1. Inspect the current composite-loss and checkpointing code to determine
   whether the v2 pilot can be implemented as configuration only or requires a
   small training-code extension.
2. Create the campaign planning report in
   `doc/reports/campaign_plans/cross_wave/shape_gate_loss_v2/`.
3. Create a one-run queue YAML for `polished_dataset` setpoints `Fw`.
4. Create a dedicated launcher with local and `-Remote` execution paths.
5. Create the matching launcher note and register the new user-facing command.
6. Store the prepared campaign state in
   `doc/running/active_training_campaign.yaml` after explicit approval.
7. Run preflight and one-batch validation, but do not start training until the
   technical document and campaign plan are both explicitly approved.
8. After pilot completion, evaluate the checkpoint with the shape-gated
   `TE Curve Verification Pipeline` before deciding whether any full Aries
   matrix is justified.
