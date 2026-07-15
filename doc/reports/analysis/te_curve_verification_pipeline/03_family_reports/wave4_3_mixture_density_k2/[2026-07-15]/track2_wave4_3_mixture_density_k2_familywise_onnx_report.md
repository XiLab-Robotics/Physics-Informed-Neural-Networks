# TE Curve Verification Pipeline Familywise ONNX Report - wave4_3_mixture_density_k2

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

- output directory: `output/validation_checks/track2_familywise_onnx_report/wave4_3_mixture_density_k2/2026-07-15-09-53-26__track2_wave4_3_mixture_density_k2_familywise_onnx_report`;
- summary YAML: `output/validation_checks/track2_familywise_onnx_report/wave4_3_mixture_density_k2/2026-07-15-09-53-26__track2_wave4_3_mixture_density_k2_familywise_onnx_report/track2_familywise_onnx_report_summary.yaml`;
- model inventory CSV: `output/validation_checks/track2_familywise_onnx_report/wave4_3_mixture_density_k2/2026-07-15-09-53-26__track2_wave4_3_mixture_density_k2_familywise_onnx_report/model_inventory.csv`;
- per-curve metrics CSV: `output/validation_checks/track2_familywise_onnx_report/wave4_3_mixture_density_k2/2026-07-15-09-53-26__track2_wave4_3_mixture_density_k2_familywise_onnx_report/per_curve_metrics.csv`.

## Simplified Dataset + Setpoints

- dataset: `simplified_dataset`;
- input mode: `setpoints`;
- evaluated family: `wave4_3_mixture_density_k2`;
- dataset root: `data/simplified_dataset`.

### Models Used

| Surface | Run Name | Run Instance | Dataset Schema |
| --- | --- | --- | --- |
| forward | `te_wave4_3_mixture_density_k2_fw__simplified_setpoints` | `2026-07-14-23-46-20__te_wave4_3_mixture_density_k2_fw__simplified_setpoints` | `simplified_curve_v1` |
| backward | `te_wave4_3_mixture_density_k2_bw__simplified_setpoints` | `2026-07-15-00-37-24__te_wave4_3_mixture_density_k2_bw__simplified_setpoints` | `simplified_curve_v1` |
| global | `te_wave4_3_mixture_density_k2_global__simplified_setpoints` | `2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints` | `simplified_curve_v1` |

Exact model paths:

| Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- |
| forward | `models/simplified_dataset/setpoints/exported/wave4_3_mixture_density_k2/forward/2026-07-14-23-46-20__te_wave4_3_mixture_density_k2_fw__simplified_setpoints/onnx/model.onnx` | `models/simplified_dataset/setpoints/exported/wave4_3_mixture_density_k2/forward/2026-07-14-23-46-20__te_wave4_3_mixture_density_k2_fw__simplified_setpoints/python/curve_aware_harmonic_residual_offset_probe-epoch=258-val_mae=0.00346706.ckpt` |
| backward | `models/simplified_dataset/setpoints/exported/wave4_3_mixture_density_k2/backward/2026-07-15-00-37-24__te_wave4_3_mixture_density_k2_bw__simplified_setpoints/onnx/model.onnx` | `models/simplified_dataset/setpoints/exported/wave4_3_mixture_density_k2/backward/2026-07-15-00-37-24__te_wave4_3_mixture_density_k2_bw__simplified_setpoints/python/curve_aware_harmonic_residual_offset_probe-epoch=185-val_mae=0.00360751.ckpt` |
| global | `models/simplified_dataset/setpoints/exported/wave4_3_mixture_density_k2/global/2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints/onnx/model.onnx` | `models/simplified_dataset/setpoints/exported/wave4_3_mixture_density_k2/global/2026-07-14-22-56-56__te_wave4_3_mixture_density_k2_global__simplified_setpoints/python/curve_aware_harmonic_residual_offset_probe-epoch=237-val_mae=0.00346790.ckpt` |

### Aggregate Metrics

| Surface | Curves | MAE [deg] | RMSE [deg] | Mean Error [%] | P95 Error [%] |
| --- | ---: | ---: | ---: | ---: | ---: |
| forward | 97 | 0.010679 | 0.012442 | 24.812 | 54.414 |
| backward | 97 | 0.011148 | 0.013701 | 26.465 | 42.420 |
| global | 194 | 0.022125 | 0.027346 | 52.474 | 81.762 |

Offset And Shape Metrics:

| Surface | Signed Offset [deg] | Absolute Offset [deg] | Centered MAE [deg] | P2P Error [deg] |
| --- | ---: | ---: | ---: | ---: |
| forward | 0.004585 | 0.009190 | 0.005742 | 0.016011 |
| backward | -0.005816 | 0.007644 | 0.008396 | 0.029506 |
| global | 0.005751 | 0.011646 | 0.019236 | 0.097188 |

### Forward 12-Curve Page

![simplified_dataset__setpoints forward 12-curve collage](assets/simplified_dataset__setpoints/forward_12_curve_collage.png)

### Backward 12-Curve Page

![simplified_dataset__setpoints backward 12-curve collage](assets/simplified_dataset__setpoints/backward_12_curve_collage.png)

### Global 12-Curve Page

![simplified_dataset__setpoints global 12-curve collage](assets/simplified_dataset__setpoints/global_12_curve_collage.png)

## Polished Dataset + Setpoints

- dataset: `polished_dataset`;
- input mode: `setpoints`;
- evaluated family: `wave4_3_mixture_density_k2`;
- dataset root: `data/polished_dataset`.

### Models Used

| Surface | Run Name | Run Instance | Dataset Schema |
| --- | --- | --- | --- |
| forward | `te_wave4_3_mixture_density_k2_fw__polished_setpoints` | `2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints` | `polished_setpoint_curve_v1` |
| backward | `te_wave4_3_mixture_density_k2_bw__polished_setpoints` | `2026-07-15-02-51-55__te_wave4_3_mixture_density_k2_bw__polished_setpoints` | `polished_setpoint_curve_v1` |
| global | `te_wave4_3_mixture_density_k2_global__polished_setpoints` | `2026-07-15-01-42-15__te_wave4_3_mixture_density_k2_global__polished_setpoints` | `polished_setpoint_curve_v1` |

Exact model paths:

| Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- |
| forward | `models/polished_dataset/setpoints/exported/wave4_3_mixture_density_k2/forward/2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints/onnx/model.onnx` | `models/polished_dataset/setpoints/exported/wave4_3_mixture_density_k2/forward/2026-07-15-02-19-32__te_wave4_3_mixture_density_k2_fw__polished_setpoints/python/curve_aware_harmonic_residual_offset_probe-epoch=101-val_mae=0.00184963.ckpt` |
| backward | `models/polished_dataset/setpoints/exported/wave4_3_mixture_density_k2/backward/2026-07-15-02-51-55__te_wave4_3_mixture_density_k2_bw__polished_setpoints/onnx/model.onnx` | `models/polished_dataset/setpoints/exported/wave4_3_mixture_density_k2/backward/2026-07-15-02-51-55__te_wave4_3_mixture_density_k2_bw__polished_setpoints/python/curve_aware_harmonic_residual_offset_probe-epoch=173-val_mae=0.00181733.ckpt` |
| global | `models/polished_dataset/setpoints/exported/wave4_3_mixture_density_k2/global/2026-07-15-01-42-15__te_wave4_3_mixture_density_k2_global__polished_setpoints/onnx/model.onnx` | `models/polished_dataset/setpoints/exported/wave4_3_mixture_density_k2/global/2026-07-15-01-42-15__te_wave4_3_mixture_density_k2_global__polished_setpoints/python/curve_aware_harmonic_residual_offset_probe-epoch=122-val_mae=0.00186311.ckpt` |

### Aggregate Metrics

| Surface | Curves | MAE [deg] | RMSE [deg] | Mean Error [%] | P95 Error [%] |
| --- | ---: | ---: | ---: | ---: | ---: |
| forward | 100 | 0.017215 | 0.021524 | 40.412 | 60.359 |
| backward | 94 | 0.013118 | 0.015721 | 30.408 | 60.543 |
| global | 194 | 0.019799 | 0.024430 | 46.824 | 72.498 |

Offset And Shape Metrics:

| Surface | Signed Offset [deg] | Absolute Offset [deg] | Centered MAE [deg] | P2P Error [deg] |
| --- | ---: | ---: | ---: | ---: |
| forward | 0.004753 | 0.006789 | 0.015895 | 0.071707 |
| backward | -0.007703 | 0.009631 | 0.008996 | 0.017015 |
| global | -0.000462 | 0.010660 | 0.016442 | 0.074638 |

### Forward 12-Curve Page

![polished_dataset__setpoints forward 12-curve collage](assets/polished_dataset__setpoints/forward_12_curve_collage.png)

### Backward 12-Curve Page

![polished_dataset__setpoints backward 12-curve collage](assets/polished_dataset__setpoints/backward_12_curve_collage.png)

### Global 12-Curve Page

![polished_dataset__setpoints global 12-curve collage](assets/polished_dataset__setpoints/global_12_curve_collage.png)

## Polished Dataset + Actual Values

- dataset: `polished_dataset`;
- input mode: `actual_values`;
- evaluated family: `wave4_3_mixture_density_k2`;
- dataset root: `data/polished_dataset`.

### Models Used

| Surface | Run Name | Run Instance | Dataset Schema |
| --- | --- | --- | --- |
| forward | `te_wave4_3_mixture_density_k2_fw__polished_actual_values` | `2026-07-15-05-01-50__te_wave4_3_mixture_density_k2_fw__polished_actual_values` | `polished_point_v1` |
| backward | `te_wave4_3_mixture_density_k2_bw__polished_actual_values` | `2026-07-15-06-02-16__te_wave4_3_mixture_density_k2_bw__polished_actual_values` | `polished_point_v1` |
| global | `te_wave4_3_mixture_density_k2_global__polished_actual_values` | `2026-07-15-04-04-29__te_wave4_3_mixture_density_k2_global__polished_actual_values` | `polished_point_v1` |

Exact model paths:

| Surface | ONNX Model Path | Python Model Path |
| --- | --- | --- |
| forward | `models/polished_dataset/actual_values/exported/wave4_3_mixture_density_k2/forward/2026-07-15-05-01-50__te_wave4_3_mixture_density_k2_fw__polished_actual_values/onnx/model.onnx` | `models/polished_dataset/actual_values/exported/wave4_3_mixture_density_k2/forward/2026-07-15-05-01-50__te_wave4_3_mixture_density_k2_fw__polished_actual_values/python/curve_aware_harmonic_residual_offset_probe-epoch=256-val_mae=0.00172453.ckpt` |
| backward | `models/polished_dataset/actual_values/exported/wave4_3_mixture_density_k2/backward/2026-07-15-06-02-16__te_wave4_3_mixture_density_k2_bw__polished_actual_values/onnx/model.onnx` | `models/polished_dataset/actual_values/exported/wave4_3_mixture_density_k2/backward/2026-07-15-06-02-16__te_wave4_3_mixture_density_k2_bw__polished_actual_values/python/curve_aware_harmonic_residual_offset_probe-epoch=129-val_mae=0.00180093.ckpt` |
| global | `models/polished_dataset/actual_values/exported/wave4_3_mixture_density_k2/global/2026-07-15-04-04-29__te_wave4_3_mixture_density_k2_global__polished_actual_values/onnx/model.onnx` | `models/polished_dataset/actual_values/exported/wave4_3_mixture_density_k2/global/2026-07-15-04-04-29__te_wave4_3_mixture_density_k2_global__polished_actual_values/python/curve_aware_harmonic_residual_offset_probe-epoch=252-val_mae=0.00175520.ckpt` |

### Aggregate Metrics

| Surface | Curves | MAE [deg] | RMSE [deg] | Mean Error [%] | P95 Error [%] |
| --- | ---: | ---: | ---: | ---: | ---: |
| forward | 100 | 0.005174 | 0.006329 | 12.160 | 21.195 |
| backward | 94 | 0.019883 | 0.024875 | 46.089 | 64.564 |
| global | 194 | 0.014640 | 0.017919 | 33.940 | 57.444 |

Offset And Shape Metrics:

| Surface | Signed Offset [deg] | Absolute Offset [deg] | Centered MAE [deg] | P2P Error [deg] |
| --- | ---: | ---: | ---: | ---: |
| forward | 0.001978 | 0.002181 | 0.004645 | 0.014298 |
| backward | -0.001380 | 0.005265 | 0.019178 | 0.087269 |
| global | 0.001971 | 0.009325 | 0.011718 | 0.044567 |

### Forward 12-Curve Page

![polished_dataset__actual_values forward 12-curve collage](assets/polished_dataset__actual_values/forward_12_curve_collage.png)

### Backward 12-Curve Page

![polished_dataset__actual_values backward 12-curve collage](assets/polished_dataset__actual_values/backward_12_curve_collage.png)

### Global 12-Curve Page

![polished_dataset__actual_values global 12-curve collage](assets/polished_dataset__actual_values/global_12_curve_collage.png)
