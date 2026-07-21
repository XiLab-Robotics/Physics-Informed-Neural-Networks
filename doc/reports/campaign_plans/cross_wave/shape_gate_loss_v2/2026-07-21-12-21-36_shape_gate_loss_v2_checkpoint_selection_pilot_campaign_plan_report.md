# Shape-Gate Loss V2 Checkpoint Selection Pilot Campaign Plan

## Campaign Status

Prepared package only. No training run, registry update, campaign closeout, or
official `TE Curve Verification Pipeline` promotion has started.

The approved technical document is:

- `doc/technical/2026-07/2026-07-21/2026-07-21-12-18-54_shape_gate_loss_v2_checkpoint_selection_pilot.md`

## Objective

Run a stricter second pilot on the primary surface,
`polished_dataset` setpoints `Fw`, to test whether shape-gate evidence is more
useful as checkpoint-selection evidence plus light auxiliary training pressure
than as the broader composite loss used by the first pilot.

The first pilot is not promoted. It passed the corrected forward shape gate but
ranked fifth in the patched polished-setpoint Fw/Bw expansion. This v2 pilot is
therefore a falsification step, not a full campaign opening.

## Evidence Base

The plan is based on:

- first shape-gate loss pilot closeout:
  `doc/reports/campaign_results/cross_wave/shape_gate_loss/2026-07-20-20-12-45_shape_gate_loss_pilot_campaign_results_report.md`;
- corrected pilot-only Track 2 playback report:
  `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/2026-07-21-00-19-31_shape_gate_loss_pilot_only_track2_polished_setpoints_fw_matrix_shape_gate_loss_pilot_only_track2_polished_setpoints_fw_input_mode_fixed_report.md`;
- patched polished-setpoint Fw/Bw expansion report:
  `doc/reports/analysis/validation_checks/te_curve_verification_pipeline/2026-07-21-00-49-22_shape_gate_pilot_expansion_polished_setpoints_fw_bw_matrix_shape_gate_pilot_expansion_polished_setpoints_fw_bw_report.md`;
- patched expansion shape-gated reranker:
  `doc/reports/analysis/te_curve_verification_pipeline/03_cvp_diagnostics/shape_gated_reranker/[2026-07-21]/shape_gate_pilot_expansion_polished_setpoints_fw_bw_matrix_shape_gated_te_curve_reranker_report.md`;
- existing curve-aware loss implementation in
  `scripts/training/transmission_error_regression_module.py`.

## Pilot Scope

| Field | Value |
| --- | --- |
| Dataset | `polished_dataset` |
| Input mode | `setpoints` |
| Surface | `Fw` |
| Base model | `periodic_gru_sequence` |
| Run count | `1` |
| Execution mode | operator launched, local or `-Remote` |
| Promotion status | not promotable by itself |

## V2 Loss Profile

The v2 run keeps the scalar pointwise objective as the anchor and reduces
shape pressure relative to v1:

| Term | Weight |
| --- | ---: |
| pointwise MSE | `1.00` |
| centered curve shape | `0.10` |
| curve offset | `0.08` |
| curve amplitude | `0.04` |
| sparse harmonic shape | `0.06` |

Derivative/ripple metrics are not inserted directly into the training loss in
this package. They remain validation and Track 2 selection evidence because the
current training module does not expose a native derivative loss term. Adding
that term should be a separate code change only if this v2 checkpoint-selection
pilot leaves a credible gap.

## Checkpoint And Acceptance Policy

The training checkpoint callback remains compatible with the existing training
stack. The post-run decision must not use scalar `val_mae` alone.

The pilot is worth expanding only if the final accepted checkpoint:

- passes the corrected polished-setpoint forward shape gate;
- ranks above the first shape-gate loss pilot in the patched forward reduced
  set;
- improves or preserves normalized derivative RMSE, derivative sign agreement,
  smoothed derivative correlation, FFT amplitude similarity, harmonic amplitude
  error, harmonic phase error, offset error, and per-curve shape pass rate;
- avoids material raw MAE degradation against the active
  `polished_setpoints_periodic_gru_sequence_Fw` baseline;
- shows no visual ripple loss or phase drift in sorted-angle Track 2 plots.

## Full Campaign Gate

If and only if this pilot beats the current forward evidence bar, a later Aries
campaign may reuse the exact v2 profile across:

| Target | Surfaces |
| --- | --- |
| `simplified_setpoints` | `global`, `Fw`, `Bw` |
| `polished_setpoints` | `global`, `Fw`, `Bw` |
| `polished_actual_values` | `global`, `Fw`, `Bw` |

That later campaign must be prepared as a separate full-matrix package and
must not inherit promotion from this pilot.

## Launch Commands

Preflight only:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.ps1 `
  -PreflightOnly
```

One-batch validation:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.ps1 `
  -PreflightOnly `
  -RunOneBatchValidation
```

Local launch:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.ps1
```

Remote launch:

```powershell
.\scripts\campaigns\cross_wave\run_shape_gate_loss_v2_checkpoint_selection_pilot_campaign.ps1 `
  -Remote
```

## Closeout Requirements

Normal closeout must produce campaign leaderboard, best-run YAML, best-run
Markdown, campaign-results report, PDF export, and status synchronization.

After closeout, run the corrected shape-gated `TE Curve Verification Pipeline`
screen and regenerate sorted-angle Track 2 plots before any discussion of a
larger Aries matrix.
