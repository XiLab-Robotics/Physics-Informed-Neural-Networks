# Track 2 Best Model Collage Report

## Overview

This report compares representative `Track 2` TE-curve predictions for
the current best reference, Track 1, Wave 1 directional, and Wave 1
global models. Each model is shown as one four-image collage so local
oscillation tracking can be inspected directly.

## Scope

- each collage contains four deterministic held-out test curves;
- forward models are shown on forward curves only;
- backward models are shown on backward curves only;
- global Wave 1 models are shown on two forward and two backward curves;
- `Measured TE` uses the same line width as predictions and a dark-gray
  color for balanced visual comparison.

## Metrics Summary

### Forward Reference Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_original_best_Fw` | `rcim_original` | Fw | 0.002769 | 0.002951 | 6.250 |
| `paper_retuned_best_Fw` | `rcim_retuned` | Fw | 0.001839 | 0.002041 | 4.109 |
| `track1_best_Fw` | `rcim_track1` | Fw | 0.003014 | 0.003204 | 6.819 |

### Forward Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_fw` | `wave1_current_registry` | Fw | 0.003404 | 0.003855 | 7.551 |
| `harmonic_regression_fw` | `wave1_current_registry` | Fw | 0.003230 | 0.003494 | 7.185 |
| `periodic_mlp_fw` | `wave1_current_registry` | Fw | 0.003254 | 0.003553 | 7.232 |
| `residual_harmonic_mlp_fw` | `wave1_current_registry` | Fw | 0.003273 | 0.003563 | 7.266 |
| `tree_fw` | `wave1_current_registry` | Fw | 0.003053 | 0.003395 | 6.731 |
| `periodic_mlp_harmonic_fw` | `wave1_periodic_mlp_harmonic_campaign` | Fw | 0.003254 | 0.003553 | 7.232 |

### Backward Reference Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `paper_retuned_best_Bw` | `rcim_retuned` | Bw | 0.003675 | 0.004284 | 7.572 |
| `track1_best_Bw` | `rcim_track1` | Bw | 0.005027 | 0.005212 | 11.860 |

### Backward Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_bw` | `wave1_current_registry` | Bw | 0.003586 | 0.004023 | 7.832 |
| `harmonic_regression_bw` | `wave1_current_registry` | Bw | 0.003678 | 0.004012 | 8.058 |
| `periodic_mlp_bw` | `wave1_current_registry` | Bw | 0.003574 | 0.004006 | 7.807 |
| `residual_harmonic_mlp_bw` | `wave1_current_registry` | Bw | 0.003536 | 0.003874 | 7.728 |
| `tree_bw` | `wave1_current_registry` | Bw | 0.003258 | 0.003651 | 7.051 |
| `periodic_mlp_harmonic_bw` | `wave1_periodic_mlp_harmonic_campaign` | Bw | 0.003583 | 0.003925 | 7.875 |

### Global Wave 1 Family Best Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `feedforward_global` | `wave1_current_registry` | global | 0.003465 | 0.003897 | 7.636 |
| `harmonic_regression_global` | `wave1_current_registry` | global | 0.018129 | 0.018330 | 41.458 |
| `periodic_mlp_global` | `wave1_current_registry` | global | 0.003447 | 0.003872 | 7.582 |
| `residual_harmonic_mlp_global` | `wave1_current_registry` | global | 0.003407 | 0.003822 | 7.486 |
| `tree_global` | `wave1_current_registry` | global | 0.003144 | 0.003533 | 6.854 |
| `periodic_mlp_harmonic_global` | `wave1_periodic_mlp_harmonic_campaign` | global | 0.003516 | 0.003810 | 7.779 |

## Collage Gallery - Forward Reference Best Models

paper_original_best_Fw:

![paper_original_best_Fw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/forward_reference/paper_original_best_fw.png)

paper_retuned_best_Fw:

![paper_retuned_best_Fw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/forward_reference/paper_retuned_best_fw.png)

## Collage Gallery - Forward Reference Best Models Continued

track1_best_Fw:

![track1_best_Fw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/forward_reference/track1_best_fw.png)

## Collage Gallery - Forward Wave 1 Family Best Models

feedforward_fw:

![feedforward_fw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/forward_wave1/feedforward_fw.png)

harmonic_regression_fw:

![harmonic_regression_fw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/forward_wave1/harmonic_regression_fw.png)

## Collage Gallery - Forward Wave 1 Family Best Models Continued

periodic_mlp_fw:

![periodic_mlp_fw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/forward_wave1/periodic_mlp_fw.png)

residual_harmonic_mlp_fw:

![residual_harmonic_mlp_fw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/forward_wave1/residual_harmonic_mlp_fw.png)

## Collage Gallery - Forward Wave 1 Family Best Models Continued 2

tree_fw:

![tree_fw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/forward_wave1/tree_fw.png)

periodic_mlp_harmonic_fw:

![periodic_mlp_harmonic_fw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/forward_wave1/periodic_mlp_harmonic_fw.png)

## Collage Gallery - Backward Reference Best Models

paper_retuned_best_Bw:

![paper_retuned_best_Bw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/backward_reference/paper_retuned_best_bw.png)

track1_best_Bw:

![track1_best_Bw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/backward_reference/track1_best_bw.png)

## Collage Gallery - Backward Wave 1 Family Best Models

feedforward_bw:

![feedforward_bw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/backward_wave1/feedforward_bw.png)

harmonic_regression_bw:

![harmonic_regression_bw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/backward_wave1/harmonic_regression_bw.png)

## Collage Gallery - Backward Wave 1 Family Best Models Continued

periodic_mlp_bw:

![periodic_mlp_bw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/backward_wave1/periodic_mlp_bw.png)

residual_harmonic_mlp_bw:

![residual_harmonic_mlp_bw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/backward_wave1/residual_harmonic_mlp_bw.png)

## Collage Gallery - Backward Wave 1 Family Best Models Continued 2

tree_bw:

![tree_bw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/backward_wave1/tree_bw.png)

periodic_mlp_harmonic_bw:

![periodic_mlp_harmonic_bw Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/backward_wave1/periodic_mlp_harmonic_bw.png)

## Collage Gallery - Global Wave 1 Family Best Models

feedforward_global:

![feedforward_global Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/global_wave1/feedforward_global.png)

harmonic_regression_global:

![harmonic_regression_global Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/global_wave1/harmonic_regression_global.png)

## Collage Gallery - Global Wave 1 Family Best Models Continued

periodic_mlp_global:

![periodic_mlp_global Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/global_wave1/periodic_mlp_global.png)

residual_harmonic_mlp_global:

![residual_harmonic_mlp_global Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/global_wave1/residual_harmonic_mlp_global.png)

## Collage Gallery - Global Wave 1 Family Best Models Continued 2

tree_global:

![tree_global Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/global_wave1/tree_global.png)

periodic_mlp_harmonic_global:

![periodic_mlp_harmonic_global Track 2 collage](../../../../../../output/validation_checks/track2_best_model_collage_report/2026-05-21-13-58-11__track2_best_model_collage_report/collages/global_wave1/periodic_mlp_harmonic_global.png)

## Output Artifacts

- output directory: `output\validation_checks\track2_best_model_collage_report\2026-05-21-13-58-11__track2_best_model_collage_report`;
- summary YAML: `output\validation_checks\track2_best_model_collage_report\2026-05-21-13-58-11__track2_best_model_collage_report\track2_best_model_collage_summary.yaml`;
- metrics CSV: `output\validation_checks\track2_best_model_collage_report\2026-05-21-13-58-11__track2_best_model_collage_report\track2_best_model_collage_metrics.csv`;
- report Markdown: `doc\reports\analysis\track2\best_model_collage_report\[2026-05-20]\track2_best_model_collage_report.md`.
