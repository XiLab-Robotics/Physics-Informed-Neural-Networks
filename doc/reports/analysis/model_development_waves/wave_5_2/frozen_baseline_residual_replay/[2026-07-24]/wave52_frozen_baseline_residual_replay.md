# Wave 5.2 Frozen-Baseline Residual Replay

## Overview

This non-training replay evaluated the four frozen accepted
`polished_dataset` setpoint baselines over their canonical training,
validation, and test datasets. It generated the per-curve residual schema
required by the Wave 5.2 MMT residual-explanatory diagnostic.

No checkpoint was changed, no model was trained, no random split was
introduced, and no model or program registry was updated.

## Provenance

- run instance: `2026-07-24-12-33-00__wave52_frozen_baseline_residual_replay`;
- configuration: `config\analysis\wave52_frozen_baseline_residual_replay.yaml`;
- output directory: `output\validation_checks\wave52_frozen_baseline_residual_replay\2026-07-24-12-33-00__wave52_frozen_baseline_residual_replay`;
- total residual rows: `3876`;
- inference provider: `CPUExecutionProvider`;
- replay input mode: `polished_dataset + setpoints`.

## Split And Registry Provenance

The authoritative split is reconstructed separately from each archived
direction-specific training snapshot. Each baseline therefore contributes
678 training, 194 validation, and 97 test curves. These memberships must
not be replaced by the earlier global audit split over the combined
`Fw` and `Bw` file inventory.

The selected July setpoint archives do not share run IDs with the current
family-registry `best_entry` records, which still identify older June
point-schema runs. This mismatch is retained as an explicit provenance
caveat rather than treated as a replay failure: the frozen selected-model
reference inventories and their training snapshots are the authoritative
sources for this replay.

| Candidate | Registry run | Selected archive run | Aligned |
| --- | --- | --- | --- |
| `polished_setpoints_periodic_gru_sequence_Fw` | `2026-06-26-15-05-38__te_periodic_gru_sequence_fw` | `2026-07-08-22-57-44__te_periodic_gru_sequence_fw__polished_setpoints` | `false` |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `2026-06-26-05-02-22__te_periodic_mlp_harmonic_fw` | `2026-07-08-02-15-59__te_periodic_mlp_harmonic_fw__polished_setpoints` | `false` |
| `polished_setpoints_periodic_gru_sequence_Bw` | `2026-06-26-16-26-19__te_periodic_gru_sequence_bw` | `2026-07-08-23-18-30__te_periodic_gru_sequence_bw__polished_setpoints` | `false` |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `2026-06-26-05-40-23__te_periodic_mlp_harmonic_bw` | `2026-07-08-02-29-32__te_periodic_mlp_harmonic_bw__polished_setpoints` | `false` |

## Split Coverage

| Candidate | Surface | Direction | Split | Residual rows | Fit allowed |
| --- | --- | --- | --- | ---: | --- |
| `polished_setpoints_periodic_gru_sequence_Bw` | `Bw` | `backward` | `test` | 97 | `false` |
| `polished_setpoints_periodic_gru_sequence_Bw` | `Bw` | `backward` | `train` | 678 | `true` |
| `polished_setpoints_periodic_gru_sequence_Bw` | `Bw` | `backward` | `validation` | 194 | `false` |
| `polished_setpoints_periodic_gru_sequence_Fw` | `Fw` | `forward` | `test` | 97 | `false` |
| `polished_setpoints_periodic_gru_sequence_Fw` | `Fw` | `forward` | `train` | 678 | `true` |
| `polished_setpoints_periodic_gru_sequence_Fw` | `Fw` | `forward` | `validation` | 194 | `false` |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `Bw` | `backward` | `test` | 97 | `false` |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `Bw` | `backward` | `train` | 678 | `true` |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `Bw` | `backward` | `validation` | 194 | `false` |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `Fw` | `forward` | `test` | 97 | `false` |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `Fw` | `forward` | `train` | 678 | `true` |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `Fw` | `forward` | `validation` | 194 | `false` |

## Residual Summary

| Candidate | Split | Rows | Raw MAE [deg] | Offset [deg] | Centered MAE [deg] |
| --- | --- | ---: | ---: | ---: | ---: |
| `polished_setpoints_periodic_gru_sequence_Bw` | `test` | 97 | 0.001702 | 0.000685 | 0.001463 |
| `polished_setpoints_periodic_gru_sequence_Bw` | `train` | 678 | 0.001984 | 0.000809 | 0.001681 |
| `polished_setpoints_periodic_gru_sequence_Bw` | `validation` | 194 | 0.002291 | 0.000751 | 0.002076 |
| `polished_setpoints_periodic_gru_sequence_Fw` | `test` | 97 | 0.001340 | 0.000654 | 0.001106 |
| `polished_setpoints_periodic_gru_sequence_Fw` | `train` | 678 | 0.001689 | 0.000878 | 0.001310 |
| `polished_setpoints_periodic_gru_sequence_Fw` | `validation` | 194 | 0.001748 | 0.000668 | 0.001541 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `test` | 97 | 0.001702 | 0.000704 | 0.001431 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `train` | 678 | 0.001997 | 0.000839 | 0.001642 |
| `polished_setpoints_periodic_mlp_harmonic_Bw` | `validation` | 194 | 0.002296 | 0.000712 | 0.002064 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `test` | 97 | 0.001507 | 0.000855 | 0.001149 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `train` | 678 | 0.001843 | 0.001033 | 0.001349 |
| `polished_setpoints_periodic_mlp_harmonic_Fw` | `validation` | 194 | 0.001939 | 0.000883 | 0.001616 |

## Validation Decision

The residual replay closes the provenance blocker only when every
configured candidate has non-zero training, validation, and test
coverage and every residual row resolves to its canonical source file.

The resulting per-curve artifact is an inference result, not evidence
that MMT is useful. Its next authorized consumer is the leakage-safe
MMT explanatory comparison, which must fit on training residuals only
and compare held-out value against metadata-only and shuffled controls.

## Machine-Readable Artifacts

- baseline manifest: `output\validation_checks\wave52_frozen_baseline_residual_replay\2026-07-24-12-33-00__wave52_frozen_baseline_residual_replay\resolved_baseline_manifest.yaml`;
- split coverage: `output\validation_checks\wave52_frozen_baseline_residual_replay\2026-07-24-12-33-00__wave52_frozen_baseline_residual_replay\split_coverage_audit.csv`;
- residual metrics: `output\validation_checks\wave52_frozen_baseline_residual_replay\2026-07-24-12-33-00__wave52_frozen_baseline_residual_replay\per_curve_residual_metrics.csv`;
- run configuration: `output\validation_checks\wave52_frozen_baseline_residual_replay\2026-07-24-12-33-00__wave52_frozen_baseline_residual_replay\run_configuration.yaml`;
- validation summary: `output\validation_checks\wave52_frozen_baseline_residual_replay\2026-07-24-12-33-00__wave52_frozen_baseline_residual_replay\validation_summary.yaml`.
