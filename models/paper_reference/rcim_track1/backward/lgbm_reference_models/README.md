# RCIM Track 1 Backward LGBM Reference Models

This archive stores the accepted `LGBM` target-level winners for the
`backward` branch of the bidirectional original-dataset Track 1 restart wave.

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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00229855` | `0.00287786` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `2.25836e-05` | `3.28906e-05` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000187064` | `0.000459123` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `8.70423e-05` | `0.000194276` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `7.79646e-05` | `0.000154784` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `1.66943e-05` | `2.59054e-05` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `1.45366e-05` | `2.13157e-05` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.39831e-05` | `3.58482e-05` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `2.6598e-05` | `3.59238e-05` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `8.48355e-06` | `1.36578e-05` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00150908` | `0.00216154` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.129653` | `0.257105` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.0621016` | `0.0882539` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.243286` | `0.466785` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0180053` | `0.0228194` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.268393` | `0.654804` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.090958` | `0.140965` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0469313` | `0.0716468` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0764587` | `0.103333` | `models/paper_reference/rcim_track1/backward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `LGBM`
- implementation family: `LGBM`
- archived target count: `19`
- unique source runs: `9`
- unique source configs: `9`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/lgbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/backward/lgbm_reference_models/reference_inventory.yaml`
