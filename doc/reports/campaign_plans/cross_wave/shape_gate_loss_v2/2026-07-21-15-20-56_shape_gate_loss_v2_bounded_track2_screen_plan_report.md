# Shape-Gate Loss V2 Bounded TE Curve Verification Screen Plan

## Overview

This plan prepares a bounded `TE Curve Verification Pipeline` screen for the
completed shape-gate loss v2 checkpoint. It is not a full promotion matrix and
must not be interpreted as an official model promotion by itself.

## Scope

| Item | Planned Value |
| --- | --- |
| Screen name | `shape_gate_loss_v2_bounded_track2_screen_2026_07_21` |
| Dataset | `polished_dataset` |
| Input mode | `setpoints` |
| Surface | `Fw` |
| Candidate under review | `shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw` |
| Checkpoint | `periodic_gru_sequence-epoch=008-val_mae=0.00198279.ckpt` |
| Output suffix | `shape_gate_loss_v2_bounded_track2_screen_polished_setpoints_fw` |
| Launch mode | Operator-run local or `-Remote` |

## Candidate Set

The screen should include:

- the v2 shape-gate loss checkpoint from
  `output/registries/families/shape_gate_loss_v2_checkpoint_selection_periodic_gru_sequence_fw/latest_family_best.yaml`;
- the first shape-gate loss pilot checkpoint as the direct predecessor;
- the `periodic_gru_sequence` forward baseline;
- the `periodic_mlp_harmonic` forward and/or global reference candidate when
  already available in the current compact matrix;
- active shape-first forward candidates already used by the reduced
  shape-gated reranker.

## Acceptance Rule

The candidate is allowed to advance only if the screen shows that the scalar
test-MAE gain does not come with unacceptable curve-shape, offset, harmonic, or
phase degradation.

The decision must use the repository multi-index curve-first policy:

- raw error;
- mean-centered shape fidelity;
- offset and continuity behavior;
- harmonic and phase fidelity;
- robustness and per-curve pass-rate behavior;
- visual evidence and deployment readiness.

Scalar campaign `MAE` alone is not a promotion criterion.

## Implementation Steps

1. Reuse the existing compact shape-gate pilot `TE Curve Verification Pipeline`
   machinery where possible.
2. Add the v2 registry-backed candidate to a dedicated bounded matrix config.
3. Prepare a launcher under `scripts/campaigns/track_2/` with local and
   `-Remote` support.
4. Add a matching launcher note under `doc/scripts/campaigns/track_2/`.
5. Run package/preflight checks only.
6. Provide the exact local and `-Remote` launch commands.
7. Wait for the operator run to complete before inspecting artifacts or writing
   an official decision.

## Planned Commands

Local:

```powershell
.\scripts\campaigns\track_2\run_shape_gate_loss_v2_bounded_track2_screen.ps1
```

Remote:

```powershell
.\scripts\campaigns\track_2\run_shape_gate_loss_v2_bounded_track2_screen.ps1 -Remote
```

Preflight only:

```powershell
.\scripts\campaigns\track_2\run_shape_gate_loss_v2_bounded_track2_screen.ps1 -PreflightOnly
```

## Stop Condition

After package preparation, Codex must stop and wait for the operator to run the
launcher. Full matrix execution, visual report inspection, and official
promotion or rejection belong to the post-run review step.
