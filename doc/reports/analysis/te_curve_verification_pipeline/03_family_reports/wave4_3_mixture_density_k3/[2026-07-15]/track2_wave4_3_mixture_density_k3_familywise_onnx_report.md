# TE Curve Verification Pipeline Familywise ONNX Report - wave4_3_mixture_density_k3

## Overview

This report evaluates exported ONNX models from the dataset input-mode
retraining program. Each dataset/input-mode section uses dataset-matched
held-out test curves and lists the exact model artifacts loaded from
`models/`.

Rank-3 temporal ONNX exports are evaluated on the sequence-window test
contract stored in each `training_config.snapshot.yaml`, including
`sequence_length`, `sequence_stride`, `sequence_target_position`, and
`maximum_sequences_per_curve`.
The collage pages keep the measured TE trace at the original full-curve
resolution; temporal ONNX predictions are overlaid at the evaluated
sequence-target angles.

The report is diagnostic and family-specific. It does not replace an
official multi-index model-promotion decision.

## Output Artifacts

- output directory: `output/validation_checks/track2_familywise_onnx_report/wave4_3_mixture_density_k3/2026-07-15-17-24-28__track2_wave4_3_mixture_density_k3_familywise_onnx_report`;
- summary YAML: `output/validation_checks/track2_familywise_onnx_report/wave4_3_mixture_density_k3/2026-07-15-17-24-28__track2_wave4_3_mixture_density_k3_familywise_onnx_report/track2_familywise_onnx_report_summary.yaml`;
- model inventory CSV: `output/validation_checks/track2_familywise_onnx_report/wave4_3_mixture_density_k3/2026-07-15-17-24-28__track2_wave4_3_mixture_density_k3_familywise_onnx_report/model_inventory.csv`;
- per-curve metrics CSV: `output/validation_checks/track2_familywise_onnx_report/wave4_3_mixture_density_k3/2026-07-15-17-24-28__track2_wave4_3_mixture_density_k3_familywise_onnx_report/per_curve_metrics.csv`.

## Simplified Dataset + Setpoints

- dataset: `simplified_dataset`;
- input mode: `setpoints`;
- evaluated family: `wave4_3_mixture_density_k3`;
- dataset root: `data/simplified_dataset`.

### Models Used

| Surface | Run Name | Run Instance | Dataset Schema |
| --- | --- | --- | --- |
| forward | `te_wave4_3_mixture_density_k3_fw__simplified_setpoints` | `2026-07-15-10-35-14__te_wave4_3_mixture_density_k3_fw__simplified_setpoints` | `simplified_curve_v1` |
| backward | `te_wave4_3_mixture_density_k3_bw__simplified_setpoints` | `2026-07-15-10-57-54__te_wave4_3_mixture_density_k3_bw__simplified_setpoints` | `simplified_curve_v1` |
| global | `te_wave4_3_mixture_density_k3_global__simplified_setpoints` | `2026-07-15-10-10-10__te_wave4_3_mixture_density_k3_global__simplified_setpoints` | `simplified_curve_v1` |

Exact model paths:

| Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- |
| forward | `models/simplified_dataset/setpoints/wave4_3_mixture_density_k3/forward/onnx/model.onnx` | `models/simplified_dataset/setpoints/wave4_3_mixture_density_k3/forward/python/curve_aware_harmonic_residual_offset_probe-epoch=077-val_mae=0.00357399.ckpt` |
| backward | `models/simplified_dataset/setpoints/wave4_3_mixture_density_k3/backward/onnx/model.onnx` | `models/simplified_dataset/setpoints/wave4_3_mixture_density_k3/backward/python/curve_aware_harmonic_residual_offset_probe-epoch=083-val_mae=0.00361315.ckpt` |
| global | `models/simplified_dataset/setpoints/wave4_3_mixture_density_k3/global/onnx/model.onnx` | `models/simplified_dataset/setpoints/wave4_3_mixture_density_k3/global/python/curve_aware_harmonic_residual_offset_probe-epoch=103-val_mae=0.00358189.ckpt` |

### Aggregate Metrics

| Surface | Curves | MAE [deg] | RMSE [deg] | Mean Error [%] | P95 Error [%] |
| --- | ---: | ---: | ---: | ---: | ---: |
| forward | 97 | 0.024845 | 0.030222 | 58.997 | 82.535 |
| backward | 97 | 0.034812 | 0.043383 | 82.585 | 108.227 |
| global | 194 | 0.021445 | 0.026134 | 50.907 | 76.902 |

Offset And Shape Metrics:

| Surface | Signed Offset [deg] | Absolute Offset [deg] | Centered MAE [deg] | P2P Error [deg] |
| --- | ---: | ---: | ---: | ---: |
| forward | 0.008848 | 0.011949 | 0.021185 | 0.076285 |
| backward | -0.019591 | 0.019631 | 0.030673 | 0.130940 |
| global | -0.000115 | 0.014588 | 0.016652 | 0.080630 |

### Forward 12-Curve Page

![simplified_dataset__setpoints forward 12-curve collage](assets/simplified_dataset__setpoints/forward_12_curve_collage.png)

### Backward 12-Curve Page

![simplified_dataset__setpoints backward 12-curve collage](assets/simplified_dataset__setpoints/backward_12_curve_collage.png)

### Global 12-Curve Page

![simplified_dataset__setpoints global 12-curve collage](assets/simplified_dataset__setpoints/global_12_curve_collage.png)

## Polished Dataset + Setpoints

- dataset: `polished_dataset`;
- input mode: `setpoints`;
- evaluated family: `wave4_3_mixture_density_k3`;
- dataset root: `data/polished_dataset`.

### Models Used

| Surface | Run Name | Run Instance | Dataset Schema |
| --- | --- | --- | --- |
| forward | `te_wave4_3_mixture_density_k3_fw__polished_setpoints` | `2026-07-15-12-21-49__te_wave4_3_mixture_density_k3_fw__polished_setpoints` | `polished_setpoint_curve_v1` |
| backward | `te_wave4_3_mixture_density_k3_bw__polished_setpoints` | `2026-07-15-12-55-40__te_wave4_3_mixture_density_k3_bw__polished_setpoints` | `polished_setpoint_curve_v1` |
| global | `te_wave4_3_mixture_density_k3_global__polished_setpoints` | `2026-07-15-11-41-10__te_wave4_3_mixture_density_k3_global__polished_setpoints` | `polished_setpoint_curve_v1` |

Exact model paths:

| Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- |
| forward | `models/polished_dataset/setpoints/wave4_3_mixture_density_k3/forward/onnx/model.onnx` | `models/polished_dataset/setpoints/wave4_3_mixture_density_k3/forward/python/curve_aware_harmonic_residual_offset_probe-epoch=140-val_mae=0.00184649.ckpt` |
| backward | `models/polished_dataset/setpoints/wave4_3_mixture_density_k3/backward/onnx/model.onnx` | `models/polished_dataset/setpoints/wave4_3_mixture_density_k3/backward/python/curve_aware_harmonic_residual_offset_probe-epoch=166-val_mae=0.00183407.ckpt` |
| global | `models/polished_dataset/setpoints/wave4_3_mixture_density_k3/global/onnx/model.onnx` | `models/polished_dataset/setpoints/wave4_3_mixture_density_k3/global/python/curve_aware_harmonic_residual_offset_probe-epoch=177-val_mae=0.00183826.ckpt` |

### Aggregate Metrics

| Surface | Curves | MAE [deg] | RMSE [deg] | Mean Error [%] | P95 Error [%] |
| --- | ---: | ---: | ---: | ---: | ---: |
| forward | 100 | 0.020326 | 0.025385 | 47.446 | 68.898 |
| backward | 94 | 0.018191 | 0.022434 | 41.698 | 61.031 |
| global | 194 | 0.025600 | 0.031621 | 59.389 | 86.511 |

Offset And Shape Metrics:

| Surface | Signed Offset [deg] | Absolute Offset [deg] | Centered MAE [deg] | P2P Error [deg] |
| --- | ---: | ---: | ---: | ---: |
| forward | 0.004207 | 0.004816 | 0.019724 | 0.099689 |
| backward | -0.009033 | 0.009637 | 0.016173 | 0.074918 |
| global | 0.000349 | 0.012429 | 0.022387 | 0.095416 |

### Forward 12-Curve Page

![polished_dataset__setpoints forward 12-curve collage](assets/polished_dataset__setpoints/forward_12_curve_collage.png)

### Backward 12-Curve Page

![polished_dataset__setpoints backward 12-curve collage](assets/polished_dataset__setpoints/backward_12_curve_collage.png)

### Global 12-Curve Page

![polished_dataset__setpoints global 12-curve collage](assets/polished_dataset__setpoints/global_12_curve_collage.png)

## Polished Dataset + Actual Values

- dataset: `polished_dataset`;
- input mode: `actual_values`;
- evaluated family: `wave4_3_mixture_density_k3`;
- dataset root: `data/polished_dataset`.

### Models Used

| Surface | Run Name | Run Instance | Dataset Schema |
| --- | --- | --- | --- |
| forward | `te_wave4_3_mixture_density_k3_fw__polished_actual_values` | `2026-07-15-14-39-00__te_wave4_3_mixture_density_k3_fw__polished_actual_values` | `polished_point_v1` |
| backward | `te_wave4_3_mixture_density_k3_bw__polished_actual_values` | `2026-07-15-15-39-35__te_wave4_3_mixture_density_k3_bw__polished_actual_values` | `polished_point_v1` |
| global | `te_wave4_3_mixture_density_k3_global__polished_actual_values` | `2026-07-15-13-58-20__te_wave4_3_mixture_density_k3_global__polished_actual_values` | `polished_point_v1` |

Exact model paths:

| Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- |
| forward | `models/polished_dataset/actual_values/wave4_3_mixture_density_k3/forward/onnx/model.onnx` | `models/polished_dataset/actual_values/wave4_3_mixture_density_k3/forward/python/curve_aware_harmonic_residual_offset_probe-epoch=240-val_mae=0.00161545.ckpt` |
| backward | `models/polished_dataset/actual_values/wave4_3_mixture_density_k3/backward/onnx/model.onnx` | `models/polished_dataset/actual_values/wave4_3_mixture_density_k3/backward/python/curve_aware_harmonic_residual_offset_probe-epoch=076-val_mae=0.00181385.ckpt` |
| global | `models/polished_dataset/actual_values/wave4_3_mixture_density_k3/global/onnx/model.onnx` | `models/polished_dataset/actual_values/wave4_3_mixture_density_k3/global/python/curve_aware_harmonic_residual_offset_probe-epoch=164-val_mae=0.00178681.ckpt` |

### Aggregate Metrics

| Surface | Curves | MAE [deg] | RMSE [deg] | Mean Error [%] | P95 Error [%] |
| --- | ---: | ---: | ---: | ---: | ---: |
| forward | 100 | 0.012587 | 0.015597 | 29.635 | 33.472 |
| backward | 94 | 0.031030 | 0.038352 | 71.999 | 85.121 |
| global | 194 | 0.011910 | 0.014642 | 27.766 | 39.988 |

Offset And Shape Metrics:

| Surface | Signed Offset [deg] | Absolute Offset [deg] | Centered MAE [deg] | P2P Error [deg] |
| --- | ---: | ---: | ---: | ---: |
| forward | -0.004018 | 0.004018 | 0.012086 | 0.052961 |
| backward | -0.014403 | 0.014742 | 0.028092 | 0.158233 |
| global | 0.000965 | 0.009109 | 0.009046 | 0.036483 |

### Forward 12-Curve Page

![polished_dataset__actual_values forward 12-curve collage](assets/polished_dataset__actual_values/forward_12_curve_collage.png)

### Backward 12-Curve Page

![polished_dataset__actual_values backward 12-curve collage](assets/polished_dataset__actual_values/backward_12_curve_collage.png)

### Global 12-Curve Page

![polished_dataset__actual_values global 12-curve collage](assets/polished_dataset__actual_values/global_12_curve_collage.png)
