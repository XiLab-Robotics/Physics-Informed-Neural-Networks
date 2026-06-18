# Track 1 SVM Micro-Closure Campaign Plan Report

## Overview

This report prepares the next `Track 1` campaign as a very narrow `SVR`
micro-closure package focused only on the last residual yellow `SVM` cells in
the canonical paper-facing benchmark.

The previous `SVM` final-closure campaign already closed harmonic `156` on the
two amplitude surfaces. What remains is now a true micro-pass.

## Current Canonical SVM Status

Current `SVM` cell status in the canonical benchmark:

- Table `2` amplitude `MAE`
  - `green`: `0, 1, 3, 39, 78, 81, 156, 162, 240`
  - `yellow`: `40`
  - `red`: none
- Table `3` amplitude `RMSE`
  - `green`: `0, 1, 3, 39, 78, 81, 156, 162`
  - `yellow`: `40, 240`
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

1. amplitude `40`
2. amplitude `240`
3. phase `162`

## Campaign Principle

The exact-paper runner already supports harmonic filtering through
`target_scope.harmonic_order_filter`, so the campaign can remain very clean:

- keep `SVR` as the only enabled family;
- isolate amplitudes and phases;
- target only `40` and `240` on the amplitude side;
- target only `162` on the phase side;
- vary only seed and split in a very small set of runs.

Campaign success should be evaluated through:

1. whether amplitude `40` becomes green in both `MAE` and `RMSE`;
2. whether amplitude `240` becomes green in `RMSE`;
3. whether phase `162` becomes green in both `MAE` and `RMSE`;
4. whether the `SVM` row reaches full closure across Tables `2-5`.

## Candidate Run Matrix

| Config ID | Planned Name | Scope | Harmonic Filter | Random Seed | Test Size | Role |
| --- | --- | --- | --- | ---: | ---: | --- |
| `M1` | `track1_svm_amplitude_micro_closure_baseline` | amplitudes | `40, 240` | `0` | `0.20` | Canonical amplitude micro-closure baseline on the two residual amplitude harmonics. |
| `M2` | `track1_svm_amplitude_micro_closure_seed23` | amplitudes | `40, 240` | `23` | `0.20` | Best-seed replay on the residual amplitude pair. |
| `M3` | `track1_svm_amplitude_micro_closure_split15` | amplitudes | `40, 240` | `0` | `0.15` | Lighter test split on the residual amplitude pair. |
| `M4` | `track1_svm_amplitude_40_only` | amplitudes | `40` | `23` | `0.20` | Isolate the last residual low-order amplitude cell. |
| `M5` | `track1_svm_amplitude_240_only` | amplitudes | `240` | `23` | `0.20` | Isolate the last residual late-order amplitude RMSE cell. |
| `M6` | `track1_svm_phase_micro_closure_baseline` | phases | `162` | `0` | `0.20` | Canonical phase micro-closure baseline on the last remaining phase harmonic. |
| `M7` | `track1_svm_phase_micro_closure_split15` | phases | `162` | `0` | `0.15` | Best current split replay for phase `162`. |
| `M8` | `track1_svm_phase_micro_closure_seed23` | phases | `162` | `23` | `0.20` | Seed perturbation for the final phase harmonic. |

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

That is enough for a final micro-pass while keeping interpretation tight.

### Export Policy

All runs may stay on:

- `enable_onnx_export: true`
- `export_failure_mode: continue`

Even in a micro-pass, the deployment-facing path should stay visible.

## Planned Campaign Size

Recommended package:

- `8` explicit runs
  - `5` amplitude-side runs
  - `3` phase-side runs

This is intentionally the smallest `SVM` package so far while still probing
multiple closure routes.

## Operator Deliverables

After approval, preparation must generate:

1. the campaign YAML package;
2. the dedicated PowerShell launcher;
3. the matching launcher note;
4. updated `doc/running/active_training_campaign.yaml`;
5. the exact PowerShell launch command.

## Next Step

After approval of this technical document and planning report, generate the
`SVR` micro-closure campaign package and prepare it for operator launch.
