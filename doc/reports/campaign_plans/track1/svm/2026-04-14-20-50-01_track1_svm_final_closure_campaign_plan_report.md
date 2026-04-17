# Track 1 SVM Final Closure Campaign Plan Report

## Overview

This report prepares the next `Track 1` campaign as a narrow `SVR` final
closure package focused only on the remaining yellow `SVM` cells in the
canonical paper-facing benchmark.

The previous `SVM` repair campaign successfully removed all red cells from the
`SVM` row. The remaining task is to turn the few residual yellow cells into
green ones without reopening already closed surfaces.

## Current Canonical SVM Status

Current `SVM` cell status in the canonical benchmark:

- Table `2` amplitude `MAE`
  - `green`: `0, 1, 3, 39, 78, 81, 162, 240`
  - `yellow`: `40, 156`
  - `red`: none
- Table `3` amplitude `RMSE`
  - `green`: `0, 1, 3, 39, 78, 81, 162`
  - `yellow`: `40, 156, 240`
  - `red`: none
- Table `4` phase `MAE`
  - `green`: `1, 3, 39, 40, 78, 81, 156, 240`
  - `yellow`: `162`
  - `red`: none
- Table `5` phase `RMSE`
  - `green`: `1, 3, 39, 40, 78, 81, 156, 240`
  - `yellow`: `162`
  - `red`: none

This reduces the true closure queue to:

1. amplitude `156`
2. amplitude `240`
3. phase `162`
4. amplitude `40`

## Campaign Principle

The exact-paper runner already supports harmonic filtering through
`target_scope.harmonic_order_filter`, so the campaign can remain clean and
inspectable:

- keep `SVR` as the only enabled family;
- isolate amplitudes and phases;
- target only `40`, `156`, `240` on the amplitude side;
- target only `162` on the phase side;
- vary seed and split in a controlled way to probe whether the remaining gap
  is split-sensitive rather than architecture-limited.

Campaign success should be evaluated through:

1. cell-state changes in Tables `2-5`;
2. whether the remaining yellow amplitude cells become green;
3. whether phase `162` becomes green in both `MAE` and `RMSE`;
4. whether the `SVM` row reaches full closure across Tables `2-5`.

## Candidate Run Matrix

| Config ID | Planned Name | Scope | Harmonic Filter | Random Seed | Test Size | Role |
| --- | --- | --- | --- | ---: | ---: | --- |
| `F1` | `track1_svm_amplitude_final_closure_baseline` | amplitudes | `40, 156, 240` | `0` | `0.20` | Canonical amplitude closure baseline on all residual amplitude harmonics. |
| `F2` | `track1_svm_amplitude_final_closure_seed11` | amplitudes | `40, 156, 240` | `11` | `0.20` | First seed perturbation on the full amplitude closure set. |
| `F3` | `track1_svm_amplitude_final_closure_seed23` | amplitudes | `40, 156, 240` | `23` | `0.20` | Second seed perturbation on the full amplitude closure set. |
| `F4` | `track1_svm_amplitude_hard_tail_focus` | amplitudes | `156, 240` | `0` | `0.20` | Pure late-order amplitude focus on the two hardest residual cells. |
| `F5` | `track1_svm_amplitude_hard_tail_seed11` | amplitudes | `156, 240` | `11` | `0.20` | Seed perturbation for the hardest amplitude pair. |
| `F6` | `track1_svm_amplitude_40_bridge` | amplitudes | `40` | `23` | `0.20` | Isolate the lower-order residual amplitude bridge cell. |
| `F7` | `track1_svm_amplitude_full_closure_split15` | amplitudes | `40, 156, 240` | `0` | `0.15` | Check whether lighter test pressure improves residual amplitude closure. |
| `F8` | `track1_svm_phase_final_closure_baseline` | phases | `162` | `0` | `0.20` | Canonical phase closure baseline on the last remaining phase harmonic. |
| `F9` | `track1_svm_phase_final_closure_seed11` | phases | `162` | `11` | `0.20` | First seed perturbation on phase `162`. |
| `F10` | `track1_svm_phase_final_closure_seed23` | phases | `162` | `23` | `0.20` | Second seed perturbation on phase `162`. |
| `F11` | `track1_svm_phase_final_closure_split15` | phases | `162` | `0` | `0.15` | Check whether lighter test pressure closes both phase metrics together. |
| `F12` | `track1_svm_phase_final_closure_split25` | phases | `162` | `11` | `0.25` | Deliberate split stress test for phase `162` stability. |

## Parameter Notes

### Family Restriction

All runs should keep:

- `training.enabled_families: [SVR]`

This preserves strict `SVM` row closure instead of drifting into a new
cross-family search.

### Harmonic Targeting

All runs should use:

- `target_scope.mode: amplitudes_only` or `phases_only`
- `target_scope.include_phase_zero: false`
- `target_scope.harmonic_order_filter: [...]`

### Controlled Variability

This package should vary only:

- `random_seed`
- `test_size`

That is enough to explore split sensitivity while keeping the interpretation
clean and the results attributable.

### Export Policy

All runs may stay on:

- `enable_onnx_export: true`
- `export_failure_mode: continue`

Even though this is a closure campaign, the deployment-facing path should stay
visible and protected against silent regressions.

## Planned Campaign Size

Recommended package:

- `12` explicit runs
  - `7` amplitude-side runs
  - `5` phase-side runs

This remains narrow relative to the earlier broad `SVM` repair batch, but it
is still large enough to test multiple closure routes concurrently.

## Operator Deliverables

After approval, preparation must generate:

1. the campaign YAML package;
2. the dedicated PowerShell launcher;
3. the matching launcher note;
4. updated `doc/running/active_training_campaign.yaml`;
5. the exact PowerShell launch command.

## Next Step

After approval of this technical document and planning report, generate the
`SVR` final-closure campaign package and prepare it for operator launch.
