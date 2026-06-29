# Campaign Best Run

## Overview

- Campaign Name: `polished_dataset_rcim_model_bank_reproduction_2026_06_22`
- Campaign Type: `RCIM Model-Bank Reproduction`
- Dataset: `polished_dataset`
- Dataset Root: `data\polished_dataset`
- Dataset Schema: `polished_point_v1`
- Selection Decision: `accept_direction_parallel_surfaces`

This campaign has two accepted direction-specific surfaces. The forward and
backward RCIM model banks are reported separately and are not collapsed into a
single destructive winner.

## Accepted Surfaces

| Surface | Run Instance | Winner | Mean MAPE % | Mean MAE | Mean RMSE |
| --- | --- | --- | ---: | ---: | ---: |
| `forward` | `2026-06-22-23-42-04__rcim_model_bank_reproduction_polished_dataset_fw_polished_dataset_campaign_validation` | `ERT / ExtraTreesRegressor` | 11.939192 | 0.062217 | 0.149061 |
| `backward` | `2026-06-25-15-19-40__rcim_model_bank_reproduction_polished_dataset_bw_polished_dataset_campaign_validation` | `ERT / ExtraTreesRegressor` | 18.399598 | 0.043815 | 0.110706 |

## Selection Policy

- Primary metric: `winning_mean_component_mae`
- Secondary metric: `winning_mean_component_rmse`
- Reporting policy: preserve separate `forward` and `backward` surfaces.
- `TE Curve Verification Pipeline`: not run during this normal closeout.

## Artifact Note

The generated `paper_family_model_bank.pkl` files are retained locally but are
not Git-tracked because each file exceeds GitHub's `100 MB` single-file limit.
