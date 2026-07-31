# TE Curve Verification Pipeline Best Model Collage Report

## Overview

This report compares representative `TE Curve Verification Pipeline` TE-curve predictions for
the current best reference, RCIM Model-Bank Reproduction, Wave 1 directional, and Wave 1
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

### Backward Accepted Non PINN Incumbent Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `accepted_periodic_gru_sequence_bw` | `accepted_non_pinn_incumbent` | Bw | 0.001837 | 0.002196 | 3.494 |
| `accepted_periodic_mlp_harmonic_bw` | `accepted_non_pinn_incumbent` | Bw | 0.001912 | 0.002263 | 3.581 |

### Backward Wave52r Offline Leader Cross Surface Promotion Models

| Candidate | Source | Surface | Curve MAE [deg] | Curve RMSE [deg] | Mean Error |
| --- | --- | --- | ---: | ---: | ---: |
| `wave52r_promotion_k01_bw_seed_271828` | `wave52r_offline_leader_cross_surface_promotion` | Bw | 0.001587 | 0.001873 | 3.018 |
| `wave52r_promotion_h08_bw_seed_161803` | `wave52r_offline_leader_cross_surface_promotion` | Bw | 0.001933 | 0.002287 | 3.710 |

## Collage Gallery - Backward Accepted Non PINN Incumbent Models

accepted_periodic_gru_sequence_bw:

![accepted_periodic_gru_sequence_bw TE Curve Verification Pipeline collage](assets/auto_backward_accepted_non_pinn_incumbent/accepted_periodic_gru_sequence_bw.png)

accepted_periodic_mlp_harmonic_bw:

![accepted_periodic_mlp_harmonic_bw TE Curve Verification Pipeline collage](assets/auto_backward_accepted_non_pinn_incumbent/accepted_periodic_mlp_harmonic_bw.png)

## Collage Gallery - Backward Wave52r Offline Leader Cross Surface Promotion Models

wave52r_promotion_k01_bw_seed_271828:

![wave52r_promotion_k01_bw_seed_271828 TE Curve Verification Pipeline collage](assets/a_bw_wave_offl_lead_cros_surf_prom_2a04589ebf/wave52r_promotion_k01_bw_seed_271828.png)

wave52r_promotion_h08_bw_seed_161803:

![wave52r_promotion_h08_bw_seed_161803 TE Curve Verification Pipeline collage](assets/a_bw_wave_offl_lead_cros_surf_prom_2a04589ebf/wave52r_promotion_h08_bw_seed_161803.png)

## Output Artifacts

- output directory: `output\analysis\wave_5_2r\offline_leader_cross_surface_track2\visual_collages\backward\2026-07-31-13-38-48__track2_best_model_collage_report`;
- summary YAML: `output\analysis\wave_5_2r\offline_leader_cross_surface_track2\visual_collages\backward\2026-07-31-13-38-48__track2_best_model_collage_report\track2_best_model_collage_summary.yaml`;
- metrics CSV: `output\analysis\wave_5_2r\offline_leader_cross_surface_track2\visual_collages\backward\2026-07-31-13-38-48__track2_best_model_collage_report\track2_best_model_collage_metrics.csv`;
- report Markdown: `doc\reports\analysis\model_development_waves\wave_5_2\offline_leader_global_promotion\visual_collages\backward\[2026-07-31]\track2_best_model_collage_report.md`.
