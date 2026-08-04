# Wave 5.2 Post-Shape-Loss Decision Gate

> Supersession note, `2026-08-04`: the deferred `Wave 5.2C` item in this
> historical decision is within-machine dirty-to-clean supervision. It is not
> the separately governed Cross-Machine Backbone Adaptation extension.

## Overview

This report closes the post-shape-loss decision gate after the completed
shape-gate, shape-objective, and shape-first distillation pilots.

The purpose is to choose the next implementable branch without launching a
training campaign. The recent evidence says that the `TE Curve Verification
Pipeline` shape limits are useful as selection and diagnostic rules, but they
did not work as direct training pressure in the tested forms.

## Decision

Do not continue the current shape-threshold-loss family.

The next branch should be a narrow causal offset / mean calibration pilot
anchored to the accepted `polished_setpoints_periodic_gru_sequence_Fw`
baseline. It should keep the non-windowed `periodic_mlp_harmonic` path as a
required comparator, but the primary implementation target should be a
time-windowed GRU-compatible calibration path.

The branch should be prepared only after a separate campaign plan is approved.
No model implementation or training is authorized by this report.

## Evidence Summary

### Shape-Gate Loss V2 Screen

The bounded `polished_dataset` setpoint `Fw` screen evaluated the v2 checkpoint
against the reduced active set over `100` held-out forward curves.

| Candidate | Rank | Raw MAE [deg] | Centered MAE [deg] | Offset Error [deg] | Harmonic Amp Error [%] | Shape Pass |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `polished_setpoints_periodic_gru_sequence_Fw` | 1 | 0.001837 | 0.001483 | 0.000932 | 17.554759 | 0.950 |
| `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_Fw` | 5 | 0.001973 | 0.001541 | 0.000959 | 21.523907 | 0.960 |

The v2 checkpoint improved the per-curve pass rate, but it lost on raw error,
centered error, harmonic amplitude, and robustness. This is not a promotion
profile.

### Shape-Objective Screen

The bounded shape-objective screen compared the scalar-winning non-windowed
MLP against the accepted forward baselines.

| Candidate | Rank | Raw MAE [deg] | Centered MAE [deg] | Offset Error [deg] | Harmonic Amp Error [%] | Shape Pass |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `polished_setpoints_periodic_gru_sequence_Fw` | 1 | 0.001837 | 0.001483 | 0.000932 | 17.554759 | 0.950 |
| `shape_objective_periodic_mlp_harmonic_Fw` | 3 | 0.002035 | 0.001578 | 0.001059 | 18.390567 | 0.910 |

The scalar pilot winner did not survive curve-first validation. It worsened
raw error, centered shape, offset, harmonic phase, robustness, and shape pass
rate relative to the accepted GRU baseline.

### Shape-First Distillation Screen

The bounded shape-first distillation screen compared both the windowed GRU and
non-windowed MLP distillation candidates against the accepted forward
baselines.

| Candidate | Rank | Raw MAE [deg] | Centered MAE [deg] | Offset Error [deg] | Harmonic Amp Error [%] | Shape Pass |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `polished_setpoints_periodic_gru_sequence_Fw` | 1 | 0.001837 | 0.001483 | 0.000932 | 17.554759 | 0.950 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | 2 | 0.001938 | 0.001490 | 0.001008 | 15.623668 | 0.920 |
| `shape_first_distilled_periodic_gru_sequence_Fw` | 3 | 0.002032 | 0.001561 | 0.001042 | 31.327127 | 0.920 |
| `shape_first_distilled_periodic_mlp_harmonic_Fw` | 4 | 0.002079 | 0.001637 | 0.001065 | 18.906554 | 0.900 |

The non-windowed MLP won the scalar pilot with test MAE `0.001420 deg`, but it
ranked last in the bounded curve-first screen. The windowed GRU distillation
candidate preserved peak-to-peak behavior best, but still lost on raw error,
centered error, offset, harmonic amplitude, and composite score.

## Cross-Pilot Interpretation

The three recent shape-aware attempts share the same pattern:

| Finding | Interpretation |
| --- | --- |
| Shape diagnostics can improve or stay acceptable while raw error worsens. | Threshold-like shape pressure is not aligned enough with the final objective. |
| Scalar validation can select the wrong branch. | Every future scalar winner needs bounded Track 2 screening before expansion. |
| The accepted GRU baseline remains hard to beat on combined raw, offset, and centered-shape behavior. | The next branch should modify or calibrate this path rather than replace it. |
| Non-windowed MLP candidates remain useful comparators but have not beaten the curve-first GRU baseline. | Keep non-windowed roads visible, but do not make them primary. |
| Offset and harmonic-amplitude regressions repeat across failed candidates. | The next loss or architecture should target offset / mean and harmonic amplitude directly, not only threshold pass/fail shape. |

## Wave 5.2 Evidence

The prior `Wave 5.2A` paired-dataset diagnostic evaluated `1938` paired
directional records across `simplified_dataset` and `polished_dataset`.

| Signal | Value |
| --- | ---: |
| Paired directional records | 1938 |
| Mean absolute offset delta [deg] | 0.003216838 |
| Mean absolute peak-to-peak delta [deg] | 0.000000134 |
| Mean absolute smoothness delta [deg] | 0.000000003 |
| Mean max harmonic delta [deg] | 0.001749405 |
| Offset-shifted pairs | 901 |
| Nonzero-harmonic changed pairs | 944 |
| Sampling anomalies | 27 |

This evidence points to offset / mean and harmonic-amplitude effects as the
most defensible physical next target. It does not justify a heavy full PINN,
because the current MMT parameter inventory still treats several equivalent
error groups as train-only calibratable rather than known runtime inputs.

The prior `Wave 5.2B` offset and harmonic guided campaign produced a strong
forward scalar run:

| Run | Test MAE [deg] | Validation MAE [deg] | Params |
| --- | ---: | ---: | ---: |
| `te_wave52b_offset_harmonic_guided_offset_centered_shape_harmonic_fw` | 0.001392 | 0.001809 | 22593 |

That result is useful architecture evidence, but it is not enough to rerun
`Wave 5.2B` unchanged. The current accepted baseline and recent Track 2 screens
show that the next branch needs checkpoint and acceptance gates tied to raw
error, offset error, centered shape, harmonic amplitude, and robustness from
the start.

## Recommended Next Branch

Prepare a narrow causal offset / mean calibration pilot.

### Scope

| Item | Decision |
| --- | --- |
| Primary anchor | `polished_setpoints_periodic_gru_sequence_Fw` |
| Required comparator | `polished_setpoints_periodic_mlp_harmonic_Fw` |
| Dataset | `polished_dataset` |
| Input mode | `setpoints` |
| First surface | `Fw` |
| Windowed road | Primary |
| Non-windowed road | Comparator, not dropped |
| Training status | Not prepared |
| Campaign status | Not prepared |

### Candidate Mechanism

The pilot should test a small causal calibration layer or auxiliary head that
predicts curve offset / mean behavior from allowed inputs and causal history.
It must not use target curve means, future samples, or offline polishing
statistics at inference.

The minimum useful variant set is:

| Arm | Purpose |
| --- | --- |
| Baseline replay | Re-evaluate the accepted GRU baseline through the same screen. |
| Offset-head GRU | Add a train-time offset / mean auxiliary head while preserving pointwise TE loss. |
| Offset-residual calibrator | Learn a second small causal residual over the frozen or warm-started GRU output. |
| Non-windowed harmonic comparator | Keep the `periodic_mlp_harmonic` road visible under the same gate. |

### Acceptance Gate

The pilot should not be expanded unless it beats the accepted GRU baseline on:

- raw MAE;
- mean absolute offset error;
- centered MAE;
- harmonic amplitude error or a clearly justified harmonic composite;
- P95 mean percentage error;
- shape-gated composite score;
- measured-versus-predicted Track 2 visual evidence.

It is not enough to improve scalar test MAE or shape pass rate alone.

## Rejected Or Deferred Alternatives

| Alternative | Decision | Reason |
| --- | --- | --- |
| Continue shape-threshold loss directly | Reject for now | Three bounded screens failed to promote the candidates. |
| Rerun `Wave 5.2B` unchanged | Reject for now | It is useful evidence, but the next branch needs a stricter baseline-anchored offset gate. |
| Start `Wave 5.2C` within-machine dirty-to-clean supervision | Defer | Paired evidence is useful, but the immediate repeated failure mode is offset / mean plus harmonic amplitude, not noisy simplified-to-polished supervision. |
| Full PINN / MMT soft loss | Defer | Several MMT equivalent-error groups remain train-only calibratable and not safe runtime inputs. |
| Wave 6 integrated multi-head model | Defer | Integration should wait until one narrow offset/harmonic mechanism beats the baseline. |

## Next Action

Prepare a separate technical document and campaign plan for a
`polished_dataset` setpoint `Fw` causal offset / mean calibration pilot.

That future package must include:

- model explanation report for the chosen offset / mean mechanism;
- training YAML files;
- local and `-Remote` PowerShell launcher;
- launcher note;
- active campaign state;
- one-batch validation;
- exact local and remote launch commands;
- bounded Track 2 screen plan after normal campaign closeout.

No training should run from this decision report alone.
