# Track 1 Forward Paper-Faithful Grid-Search Closeout

## Overview

- campaign name: `track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30`
- started at: `2026-05-14T00:44:05+02:00`
- finished at: `2026-05-15T07:07:30+02:00`
- closed direction: `forward`
- refreshed archive root: `models/paper_reference/rcim_track1/forward`
- benchmark report: `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`

## Family Results

| Family | Run Instance | Mean MAE | Mean RMSE | Mean MAPE % | Exported ONNX | Exported PKL |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `2026-05-14-11-22-01__track1_paper_faithful_grid_search_forward_svr_campaign_validation` | `0.195558` | `0.303488` | `75.0189` | `19` | `19` |
| `MLP` | `2026-05-14-11-24-54__track1_paper_faithful_grid_search_forward_mlp_campaign_validation` | `0.219477` | `0.302771` | `4319.59` | `19` | `19` |
| `RF` | `2026-05-14-11-41-07__track1_paper_faithful_grid_search_forward_rf_campaign_validation` | `0.0807811` | `0.161448` | `22.1391` | `19` | `19` |
| `DT` | `2026-05-14-13-03-07__track1_paper_faithful_grid_search_forward_dt_campaign_validation` | `0.0954926` | `0.186076` | `40.5591` | `19` | `19` |
| `ET` | `2026-05-14-13-04-54__track1_paper_faithful_grid_search_forward_et_campaign_validation` | `0.120815` | `0.252001` | `39.387` | `19` | `19` |
| `ERT` | `2026-05-14-13-06-36__track1_paper_faithful_grid_search_forward_ert_campaign_validation` | `0.0644413` | `0.151992` | `18.2706` | `19` | `19` |
| `GBM` | `2026-05-14-15-36-42__track1_paper_faithful_grid_search_forward_gbm_campaign_validation` | `0.0836404` | `0.164166` | `27.7299` | `19` | `19` |
| `HGBM` | `2026-05-14-17-04-55__track1_paper_faithful_grid_search_forward_hgbm_campaign_validation` | `0.106506` | `0.189713` | `38.1651` | `19` | `19` |
| `XGBM` | `2026-05-14-19-27-11__track1_paper_faithful_grid_search_forward_xgbm_campaign_validation` | `0.123318` | `0.193609` | `58.1335` | `19` | `19` |
| `LGBM` | `2026-05-14-19-30-29__track1_paper_faithful_grid_search_forward_lgbm_campaign_validation` | `0.148417` | `0.222652` | `64.7701` | `19` | `19` |
| `ELM` | `2026-05-15-07-06-18__track1_paper_faithful_grid_search_forward_elm_campaign_validation` | `0.206277` | `0.277969` | `99.7177` | `19` | `19` |

## Benchmark Status

| Table | Green | Yellow | Red | Total |
| --- | ---: | ---: | ---: | ---: |
| Forward Table 2 - Amplitude MAE | `19` | `25` | `66` | `110` |
| Forward Table 3 - Amplitude RMSE | `21` | `28` | `61` | `110` |
| Forward Table 4 - Phase MAE | `23` | `21` | `55` | `99` |
| Forward Table 5 - Phase RMSE | `23` | `32` | `44` | `99` |

## Reference Archive Refresh

| Family | Archived Targets | Source Runs | Archive Root |
| --- | ---: | ---: | --- |
| `SVM` | `19` | `1` | `models/paper_reference/rcim_track1/forward/svm_reference_models` |
| `MLP` | `19` | `1` | `models/paper_reference/rcim_track1/forward/mlp_reference_models` |
| `RF` | `19` | `1` | `models/paper_reference/rcim_track1/forward/rf_reference_models` |
| `DT` | `19` | `1` | `models/paper_reference/rcim_track1/forward/dt_reference_models` |
| `ET` | `19` | `1` | `models/paper_reference/rcim_track1/forward/et_reference_models` |
| `ERT` | `19` | `1` | `models/paper_reference/rcim_track1/forward/ert_reference_models` |
| `GBM` | `19` | `1` | `models/paper_reference/rcim_track1/forward/gbm_reference_models` |
| `HGBM` | `19` | `1` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models` |
| `XGBM` | `19` | `1` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models` |
| `LGBM` | `19` | `1` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models` |
| `ELM` | `19` | `1` | `models/paper_reference/rcim_track1/forward/elm_reference_models` |

## Best Campaign Representative

- run: `track1_paper_faithful_grid_search_forward_ert`
- family: `ERT`
- mean MAE: `0.0644413`
- mean RMSE: `0.151992`

## Notes

- The original paper-family order for Tables `2`-`5` remains unchanged.
- `ELM` is archived and benchmarked as an operational Track 1 family because the completed campaign includes it.
- Backward Track 1 paper-reference archives were not modified by this forward-only closeout.
