# Track 2 Directional Comparison Report

## Overview

This report evaluates `Track 1` paper-reference banks and `Wave 1`
repository models on direction-valid held-out TE curves. Directional
candidates are evaluated only on their matching direction, while global
candidates are evaluated on both directions and reported separately.

## Scope

- dataset config: `config/datasets/transmission_error_dataset.yaml`;
- dataset root: `data\simplified_dataset`;
- comparison mode: `directional_candidate_matrix`;
- candidate count: `5`;
- held-out curve count before candidate filtering: `194`;
- percentage-error denominator: `peak_to_peak_truth`;

## Candidate Inventory

| Candidate | Family | Kind | Surface | Valid Directions | Source |
| --- | --- | --- | --- | --- | --- |
| `LGBM19_Fw` | `LGBM` | `track1_reference_bank` | `Fw` | `forward` | `models\paper_reference\rcim_track1\forward\lgbm_reference_models\reference_inventory.yaml` |
| `LGBM19_Bw` | `LGBM` | `track1_reference_bank` | `Bw` | `backward` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\reference_inventory.yaml` |
| `feedforward_global` | `feedforward` | `wave1_registry_model` | `global` | `forward, backward` | `output\registries\families\feedforward\latest_family_best.yaml` |
| `feedforward_Fw` | `feedforward` | `wave1_registry_model` | `Fw` | `forward` | `output\registries\families\feedforward_fw\latest_family_best.yaml` |
| `feedforward_Bw` | `feedforward` | `wave1_registry_model` | `Bw` | `backward` | `output\registries\families\feedforward_bw\latest_family_best.yaml` |

## Aggregate Comparison

| Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | ---: | ---: | ---: | ---: |
| `LGBM19_Fw` | 0.116164 | 0.116179 | 259.051 | 356.154 |
| `LGBM19_Bw` | 0.005037 | 0.005231 | 11.880 | 48.106 |
| `feedforward_global` | 0.003465 | 0.003897 | 7.636 | 14.203 |
| `feedforward_Fw` | 0.003404 | 0.003855 | 7.551 | 13.029 |
| `feedforward_Bw` | 0.003586 | 0.004023 | 7.832 | 14.856 |

## Direction Breakdown

| Direction | Candidate | Curve MAE [deg] | Curve RMSE [deg] | Mean Percentage Error [%] |
| --- | --- | ---: | ---: | ---: |
| `forward` | `LGBM19_Fw` | 0.116164 | 0.116179 | 259.051 |
| `forward` | `feedforward_global` | 0.003316 | 0.003746 | 7.361 |
| `forward` | `feedforward_Fw` | 0.003404 | 0.003855 | 7.551 |
| `backward` | `LGBM19_Bw` | 0.005037 | 0.005231 | 11.880 |
| `backward` | `feedforward_global` | 0.003613 | 0.004048 | 7.910 |
| `backward` | `feedforward_Bw` | 0.003586 | 0.004023 | 7.832 |

## Sample Preview

- `LGBM19_Fw` | `forward` | `data\simplified_dataset\Test_25degree\1000rpm\1000.0rpm1200.0Nm25.0deg.csv` | `1000 rpm` | `1200 Nm` | `25 C` | `MPE=280.591%`
- `LGBM19_Fw` | `forward` | `data\simplified_dataset\Test_25degree\1000rpm\1000.0rpm1300.0Nm25.0deg.csv` | `1000 rpm` | `1300 Nm` | `25 C` | `MPE=296.082%`
- `LGBM19_Fw` | `forward` | `data\simplified_dataset\Test_25degree\1000rpm\1000.0rpm1800.0Nm25.0deg.csv` | `1000 rpm` | `1800 Nm` | `25 C` | `MPE=342.378%`
- `LGBM19_Fw` | `forward` | `data\simplified_dataset\Test_25degree\1000rpm\1000.0rpm400.0Nm25.0deg.csv` | `1000 rpm` | `400 Nm` | `25 C` | `MPE=190.608%`
- `LGBM19_Fw` | `forward` | `data\simplified_dataset\Test_25degree\1000rpm\1000.0rpm800.0Nm25.0deg.csv` | `1000 rpm` | `800 Nm` | `25 C` | `MPE=249.530%`

## Output Artifacts

- summary YAML: `output\validation_checks\track2_reference_comparison\2026-05-17-22-19-27__track2_directional_lgbm19_vs_feedforward_directional_validation/validation_summary.yaml`;
- per-condition CSV: `output\validation_checks\track2_reference_comparison\2026-05-17-22-19-27__track2_directional_lgbm19_vs_feedforward_directional_validation\per_condition_metrics.csv`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-17-22-19-27__track2_directional_lgbm19_vs_feedforward_directional_validation\preview_curves\preview_01.png`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-17-22-19-27__track2_directional_lgbm19_vs_feedforward_directional_validation\preview_curves\preview_02.png`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-17-22-19-27__track2_directional_lgbm19_vs_feedforward_directional_validation\preview_curves\preview_03.png`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-17-22-19-27__track2_directional_lgbm19_vs_feedforward_directional_validation\preview_curves\preview_04.png`;
- preview plot: `output\validation_checks\track2_reference_comparison\2026-05-17-22-19-27__track2_directional_lgbm19_vs_feedforward_directional_validation\preview_curves\preview_05.png`;
