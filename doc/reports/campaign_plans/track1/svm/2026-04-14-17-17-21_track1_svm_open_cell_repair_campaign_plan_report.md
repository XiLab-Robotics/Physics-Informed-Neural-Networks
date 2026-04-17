# Track 1 SVM Open-Cell Repair Campaign Plan Report

## Overview

This report prepares the next `Track 1` campaign as a dedicated `SVR` repair
batch focused on the currently open `SVM` cells in the canonical paper-facing
benchmark.

The campaign is intentionally broader than a single rerun. The goal is to try
multiple repair directions in parallel while staying restricted to the `SVM`
row.

## Current Canonical SVM Status

Current `SVM` cell status in the canonical benchmark:

- Table `2` amplitude `MAE`
  - `green`: `1, 3, 39, 78, 162`
  - `yellow`: `0, 40, 81, 156, 240`
  - `red`: none
- Table `3` amplitude `RMSE`
  - `green`: `1, 3, 39, 78, 162`
  - `yellow`: `0, 40, 81, 240`
  - `red`: `156`
- Table `4` phase `MAE`
  - `green`: `3, 39, 40, 78, 81, 156`
  - `yellow`: `1, 162`
  - `red`: `240`
- Table `5` phase `RMSE`
  - `green`: `3, 40, 78, 81, 156`
  - `yellow`: `1, 39, 162`
  - `red`: `240`

This implies the highest-priority repair queue is:

1. amplitude `156`
2. phase `240`
3. phase `162`
4. amplitude `0, 40, 81, 240`
5. phase `1, 39`

## Campaign Principle

The exact-paper runner now supports harmonic filtering directly through
`target_scope.harmonic_order_filter`.

That enables a proper repair design:

- keep `SVR` as the only enabled family;
- isolate amplitudes and phases;
- target only the open harmonics in each run;
- vary seed and split in a controlled way to probe whether the current gaps are
  budget-limited or split-sensitive.

Campaign success should be evaluated through:

1. cell-state changes in Tables `2-5`;
2. whether any `red` cell becomes `yellow` or `green`;
3. whether any `yellow` cell becomes `green`;
4. whether harmonic `240` and amplitude `156` stop being hard blockers.

## Candidate Run Matrix

| Config ID | Planned Name | Scope | Harmonic Filter | Random Seed | Test Size | Role |
| --- | --- | --- | --- | ---: | ---: | --- |
| `S1` | `track1_svm_amplitude_repair_baseline` | amplitudes | `0, 40, 81, 156, 240` | `0` | `0.20` | Canonical amplitude repair baseline on all currently open amplitude cells. |
| `S2` | `track1_svm_amplitude_repair_seed11` | amplitudes | `0, 40, 81, 156, 240` | `11` | `0.20` | Check whether amplitude repair is split-stable or seed-sensitive. |
| `S3` | `track1_svm_amplitude_repair_seed23` | amplitudes | `0, 40, 81, 156, 240` | `23` | `0.20` | Add a second independent amplitude perturbation. |
| `S4` | `track1_svm_amplitude_156_focus` | amplitudes | `156` | `0` | `0.20` | Pure blocker attack on the only red amplitude `RMSE` cell. |
| `S5` | `track1_svm_amplitude_156_240_focus` | amplitudes | `156, 240` | `11` | `0.20` | Couple the hardest late-order amplitude cells in one repair run. |
| `S6` | `track1_svm_amplitude_low_mid_bridge` | amplitudes | `0, 40, 81` | `23` | `0.20` | Focus the near-closure amplitude yellows without late-order pressure. |
| `S7` | `track1_svm_phase_repair_baseline` | phases | `1, 39, 162, 240` | `0` | `0.20` | Canonical phase repair baseline on all open phase cells. |
| `S8` | `track1_svm_phase_repair_seed11` | phases | `1, 39, 162, 240` | `11` | `0.20` | Check whether phase repair is split-stable or seed-sensitive. |
| `S9` | `track1_svm_phase_repair_seed23` | phases | `1, 39, 162, 240` | `23` | `0.20` | Add a second independent phase perturbation. |
| `S10` | `track1_svm_phase_240_focus` | phases | `240` | `0` | `0.20` | Pure blocker attack on the red phase cell. |
| `S11` | `track1_svm_phase_162_240_focus` | phases | `162, 240` | `11` | `0.20` | Concentrate budget on the two late-order open phase harmonics. |
| `S12` | `track1_svm_phase_1_39_bridge` | phases | `1, 39` | `23` | `0.20` | Isolate the residual lower-order phase yellows. |

## Parameter Notes

### Family Restriction

All runs should keep:

- `training.enabled_families: [SVR]`

This preserves row-faithful `SVM` repair instead of drifting into cross-family
winner search.

### Harmonic Targeting

All runs should use:

- `target_scope.mode: amplitudes_only` or `phases_only`
- `target_scope.include_phase_zero: false`
- `target_scope.harmonic_order_filter: [...]`

### Controlled Variability

The campaign should vary only:

- `random_seed`
- optionally `test_size` in a small subset if later needed

The first prepared package should keep `test_size: 0.20` across all runs so
interpretation remains cleaner. If this campaign underperforms, the next wave
can introduce `test_size` perturbations.

### Export Policy

All runs may stay on:

- `enable_onnx_export: true`
- `export_failure_mode: continue`

The primary objective is numeric repair, but keeping export on preserves the
paper-faithful deployment path and avoids silent regressions.

## Planned Campaign Size

Recommended initial package:

- `12` explicit runs
  - `6` amplitude-side runs
  - `6` phase-side runs

This is wide enough to explore multiple repair routes concurrently without
becoming a blind combinatorial sweep.

## Operator Deliverables

After approval, preparation must generate:

1. the campaign YAML package;
2. the dedicated PowerShell launcher;
3. the matching launcher note;
4. updated `doc/running/active_training_campaign.yaml`;
5. the exact PowerShell launch command.

## Next Step

After approval of this technical document and planning report, generate the
`SVR` repair campaign package and prepare it for operator launch.
