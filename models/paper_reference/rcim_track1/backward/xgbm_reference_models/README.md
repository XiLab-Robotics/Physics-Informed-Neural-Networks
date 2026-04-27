# RCIM Track 1 Backward XGBM Reference Models

This archive stores the accepted `XGBM` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00229591` | `0.00272319` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `5.91334e-05` | `0.000106882` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000335013` | `0.000773105` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.000149581` | `0.000234227` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.000141314` | `0.000200511` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `6.92384e-05` | `9.0386e-05` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `7.69295e-05` | `9.52484e-05` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `3.69048e-05` | `4.83494e-05` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `0.000105099` | `0.000139793` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `2.32094e-05` | `2.96543e-05` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00179753` | `0.00267142` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/phase/XGBRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.157072` | `0.236763` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/phase/XGBRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.151022` | `0.275683` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/phase/XGBRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.356205` | `0.692858` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/phase/XGBRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0166029` | `0.0223981` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/phase/XGBRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.303307` | `0.61998` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/phase/XGBRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.137977` | `0.200606` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/phase/XGBRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0623943` | `0.0891048` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/phase/XGBRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0861429` | `0.108707` | `models/paper_reference/rcim_track1/backward/xgbm_reference_models/onnx/phase/XGBRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `XGBM`
- implementation family: `XGBM`
- archived target count: `19`
- unique source runs: `12`
- unique source configs: `12`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/xgbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/backward/xgbm_reference_models/reference_inventory.yaml`
