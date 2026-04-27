# RCIM Track 1 Forward LGBM Reference Models

This archive stores the accepted `LGBM` target-level winners for the
`forward` branch of the bidirectional original-dataset Track 1 restart wave.

Archive contents:

- `reference_inventory.yaml`
- `onnx/amplitude/`
- `onnx/phase/`
- `python/amplitude/`
- `python/phase/`
- `data/filtered_dataframe_deg_le_35.csv`
- `dataset_snapshot_manifest.yaml`
- `source_runs/<run_instance_id>/training_config.snapshot.yaml`
- `source_runs/<run_instance_id>/run_metadata.snapshot.yaml`
- `source_runs/<run_instance_id>/split_manifest.yaml`

Selection rule:

- lowest target `MAE`; ties break on target `RMSE`, then target `MAPE`, then run name.
- archive refresh is mandatory at closeout only when the accepted winner improves the stored target entry.

Accepted amplitude targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00599484` | `0.00703257` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `2.38161e-05` | `3.13631e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000271427` | `0.000349297` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000294093` | `0.000563996` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.000113644` | `0.000202821` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `5.04073e-05` | `6.24599e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `9.81963e-05` | `0.000116485` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `3.45316e-05` | `4.81988e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.000176727` | `0.000210241` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `2.35726e-05` | `3.03546e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00179832` | `0.00260982` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `1.04653` | `1.38511` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.55861` | `0.812561` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.298069` | `0.469953` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.045093` | `0.0535386` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0722734` | `0.0940117` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0523988` | `0.0684755` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.136832` | `0.206742` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.130158` | `0.177617` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `LGBM`
- implementation family: `LGBM`
- archived target count: `19`
- unique source runs: `13`
- unique source configs: `13`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/lgbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/lgbm_reference_models/reference_inventory.yaml`
