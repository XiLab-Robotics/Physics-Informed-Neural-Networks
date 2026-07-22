# Shape-First Training Rule Distillation Pilot Campaign Plan

## Overview

This campaign plan prepares a two-arm mini-pilot that distills
`TE Curve Verification Pipeline` shape-first screen evidence into conservative
training-time pressure and checkpoint-selection evidence. It is the controlled
follow-up to the failed bounded shape-objective screen: the scalar
shape-objective branch is not promoted, but the screen rules remain useful as
training diagnostics and possible future auxiliary-loss ingredients.

The pilot is scoped to `polished_dataset` setpoints and the `Fw` surface. It is
not a full promotion campaign and must not replace the accepted forward
recommendation without a bounded curve-first screen after training.

## Candidate Arms

| Arm | Runtime Contract | Purpose |
| --- | --- | --- |
| `shape_first_distilled_periodic_gru_sequence_fw` | Time-windowed sequence | Test conservative shape-first pressure on the accepted GRU-style forward path. |
| `shape_first_distilled_periodic_mlp_harmonic_fw` | Non-windowed point model | Keep the harmonic non-windowed path active under the same shape-first evidence policy. |

## Loss And Monitor Policy

Both arms reuse existing curve-aware training hooks. The weighted loss terms
stay intentionally conservative:

- pointwise MSE remains the dominant training objective;
- centered shape, offset, amplitude, and sparse harmonic terms provide bounded
  shape-first pressure;
- derivative behavior is logged as curve-aware evidence but kept at zero loss
  weight in this first distillation pilot;
- frequency-domain similarity, dominant-harmonic phase error, derivative
  agreement, and pass-rate thresholds remain post-training bounded-screen
  evidence.

This keeps the first test aligned with the user's rule that time-windowed and
non-windowed variants should both remain active.

## Acceptance Gates

The first promotion gate is a bounded `Fw` screen, not scalar MAE alone. A
candidate should continue only if it satisfies all of the following:

- beats or materially matches `polished_setpoints_periodic_gru_sequence_Fw`;
- beats or materially matches `polished_setpoints_periodic_mlp_harmonic_Fw`;
- improves over the failed shape-objective candidate on raw MAE and centered
  MAE;
- does not regress shape pass rate, offset behavior, harmonic retention, phase
  behavior, or derivative agreement under the shape-gated reranker.

## Planned Artifacts

- Technical document:
  `doc/technical/2026-07/2026-07-22/2026-07-22-12-54-02_shape_first_training_rule_distillation.md`
- Campaign config root:
  `config/training/shape_first_training_rule_distillation/campaigns/2026-07-22_shape_first_training_rule_distillation_pilot/`
- Launcher:
  `scripts/campaigns/cross_wave/run_shape_first_training_rule_distillation_pilot_campaign.ps1`
- Launcher note:
  `doc/scripts/campaigns/cross_wave/run_shape_first_training_rule_distillation_pilot_campaign.md`
- Training output root:
  `output/training_runs/shape_first_training_rule_distillation/`
- Queue root:
  `config/training/queue/shape_first_training_rule_distillation/shape_first_training_rule_distillation_pilot_2026_07_22`

## Launch Policy

The launcher must support:

- `-PreflightOnly`
- `-RunOneBatchValidation`
- local execution
- `-Remote` execution through the repository-owned remote campaign workflow

The remote launch must sync source/configuration/docs before execution and
sync campaign outputs, per-run artifacts, queue end state, registries, and
status artifacts after completion.

## Decision Policy

This is a bounded exploration. If neither arm improves the curve-first evidence
against the windowed and non-windowed baselines, close the branch without
full-surface expansion. If one arm clears the bounded gate, prepare a separate
full `global` / `Fw` / `Bw` plan before any broader campaign.
