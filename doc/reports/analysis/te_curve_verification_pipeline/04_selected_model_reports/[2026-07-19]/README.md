# TE Curve Verification Pipeline Selected Active Model Bundle

## Overview

This bundle regenerates the selected-active TE Curve Verification Pipeline
reports after the full model-family retraining pass. It includes only the
selected active direct-model families and keeps `global` surfaces out of the
decision report.

## Report Index

| Scope | Report | Surface Leader | MAE [deg] | Mean Percentage Error [%] | P95 Mean Percentage Error [%] |
| --- | --- | --- | ---: | ---: | ---: |
| Simplified setpoints forward | [track2_selected_active_simplified_setpoints_forward_report.md](track2_selected_active_simplified_setpoints_forward_report.md) | `simplified_setpoints_tree_Fw` | 0.003065 | 6.740 | 11.934 |
| Simplified setpoints backward | [track2_selected_active_simplified_setpoints_backward_report.md](track2_selected_active_simplified_setpoints_backward_report.md) | `simplified_setpoints_tree_Bw` | 0.003345 | 7.249 | 13.745 |
| Polished setpoints forward | [track2_selected_active_polished_setpoints_forward_report.md](track2_selected_active_polished_setpoints_forward_report.md) | `polished_setpoints_wave4_1_mae_robust_loss_Fw` | 0.016970 | 36.104 | 88.789 |
| Polished setpoints backward | [track2_selected_active_polished_setpoints_backward_report.md](track2_selected_active_polished_setpoints_backward_report.md) | `polished_setpoints_tree_Bw` | 0.003928 | 7.417 | 14.932 |
| Polished actual values forward | [track2_selected_active_polished_actual_values_forward_report.md](track2_selected_active_polished_actual_values_forward_report.md) | `polished_actual_values_wave4_1_mae_robust_loss_Fw` | 0.001681 | 3.355 | 8.132 |
| Polished actual values backward | [track2_selected_active_polished_actual_values_backward_report.md](track2_selected_active_polished_actual_values_backward_report.md) | `polished_actual_values_periodic_gru_sequence_Bw` | 0.001333 | 2.625 | 5.438 |

## Included Families

- `feedforward`
- `tree`
- `harmonic_regression`
- `periodic_mlp_harmonic`
- `periodic_gru_sequence`
- `wave4_1_mae_robust_loss`
- `wave4_2_quantile_p10_p50_p90`

## Notes

The RCIM Model-Bank Reproduction polished input-mode reruns remain a separate
paper-reference benchmark path. They are intentionally not included in this
selected-active model-only bundle because the current operational selection is
based on the direct model families.
