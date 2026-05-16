# Track 1 Backward Paper-Faithful Grid-Search Closeout

## Overview

- campaign name: `track1_bidirectional_paper_faithful_grid_search_campaign_2026-05-04_12_26_30`
- started at: `2026-05-14T00:44:05+02:00`
- finished at: `2026-05-16T19:04:25+02:00`
- closed direction: `backward`
- refreshed archive root: `models/paper_reference/rcim_track1/backward`
- benchmark report: `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

## Family Results

| Family | Run Instance | Mean MAE | Mean RMSE | Mean MAPE % | Exported ONNX | Exported PKL |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `SVM` | `2026-05-15-23-28-01__track1_paper_faithful_grid_search_backward_svr_campaign_validation` | `0.22957` | `0.368131` | `48.8009` | `19` | `19` |
| `MLP` | `2026-05-15-23-30-56__track1_paper_faithful_grid_search_backward_mlp_campaign_validation` | `0.245743` | `0.349376` | `3411.06` | `19` | `19` |
| `RF` | `2026-05-15-23-47-53__track1_paper_faithful_grid_search_backward_rf_campaign_validation` | `0.0642822` | `0.144738` | `23.0516` | `19` | `19` |
| `DT` | `2026-05-16-01-10-50__track1_paper_faithful_grid_search_backward_dt_campaign_validation` | `0.0432093` | `0.134447` | `24.1088` | `19` | `19` |
| `ET` | `2026-05-16-01-12-39__track1_paper_faithful_grid_search_backward_et_campaign_validation` | `0.0858495` | `0.216616` | `36.2701` | `19` | `19` |
| `ERT` | `2026-05-16-01-14-27__track1_paper_faithful_grid_search_backward_ert_campaign_validation` | `0.0496713` | `0.129551` | `20.12` | `19` | `19` |
| `GBM` | `2026-05-16-03-42-16__track1_paper_faithful_grid_search_backward_gbm_campaign_validation` | `0.0603563` | `0.137289` | `23.0803` | `19` | `19` |
| `HGBM` | `2026-05-16-05-10-28__track1_paper_faithful_grid_search_backward_hgbm_campaign_validation` | `0.0876331` | `0.170341` | `32.8818` | `19` | `19` |
| `XGBM` | `2026-05-16-07-29-43__track1_paper_faithful_grid_search_backward_xgbm_campaign_validation` | `0.113797` | `0.191087` | `43.5059` | `19` | `19` |
| `LGBM` | `2026-05-16-07-33-09__track1_paper_faithful_grid_search_backward_lgbm_campaign_validation` | `0.067018` | `0.13972` | `24.0255` | `19` | `19` |
| `ELM` | `2026-05-16-19-03-18__track1_paper_faithful_grid_search_backward_elm_campaign_validation` | `0.237422` | `0.337425` | `71.0273` | `19` | `19` |

## Benchmark Status

| Table | Green | Yellow | Red | Total |
| --- | ---: | ---: | ---: | ---: |
| Backward Table 2 - Amplitude MAE | `61` | `22` | `27` | `110` |
| Backward Table 3 - Amplitude RMSE | `63` | `20` | `27` | `110` |
| Backward Table 4 - Phase MAE | `65` | `21` | `13` | `99` |
| Backward Table 5 - Phase RMSE | `65` | `21` | `13` | `99` |

## Reference Archive Refresh

| Family | Archived Targets | Source Runs | Archive Root |
| --- | ---: | ---: | --- |
| `SVM` | `19` | `1` | `models/paper_reference/rcim_track1/backward/svm_reference_models` |
| `MLP` | `19` | `1` | `models/paper_reference/rcim_track1/backward/mlp_reference_models` |
| `RF` | `19` | `1` | `models/paper_reference/rcim_track1/backward/rf_reference_models` |
| `DT` | `19` | `1` | `models/paper_reference/rcim_track1/backward/dt_reference_models` |
| `ET` | `19` | `1` | `models/paper_reference/rcim_track1/backward/et_reference_models` |
| `ERT` | `19` | `1` | `models/paper_reference/rcim_track1/backward/ert_reference_models` |
| `GBM` | `19` | `1` | `models/paper_reference/rcim_track1/backward/gbm_reference_models` |
| `HGBM` | `19` | `1` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models` |
| `XGBM` | `19` | `1` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models` |
| `LGBM` | `19` | `1` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models` |
| `ELM` | `19` | `1` | `models/paper_reference/rcim_track1/backward/elm_reference_models` |

## Best Campaign Representative

- run: `track1_paper_faithful_grid_search_backward_dt`
- family: `DT`
- mean MAE: `0.0432093`
- mean RMSE: `0.134447`

## Notes

- The original paper-family order for Tables `2`-`5` remains unchanged.
- `ELM` is archived and benchmarked as an operational Track 1 family because the completed campaign includes it.
- Forward Track 1 paper-reference archives were not modified by this backward-only closeout.
