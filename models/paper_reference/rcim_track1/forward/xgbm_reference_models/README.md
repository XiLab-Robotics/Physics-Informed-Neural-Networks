# RCIM Track 1 Forward XGBM Reference Models

This archive stores the accepted `XGBM` target-level winners for the
`forward` branch of the canonical original-dataset Track 1 benchmark surface.

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

- store the accepted canonical target winner currently visible in the benchmark matrices.
- when a later closeout improves the accepted target winner, replace the archived entry.
- when the accepted target winner does not improve, retain the existing archived entry unchanged.
- archive refresh is mandatory at closeout only when the accepted winner improves the stored target entry.

Accepted amplitude targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00232205` | `0.00289955` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `4.56825e-05` | `5.79546e-05` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000180962` | `0.00038103` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000130144` | `0.000196509` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.00013604` | `0.000217637` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `7.00635e-05` | `9.14248e-05` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `8.81748e-05` | `0.000115491` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `5.75063e-05` | `7.78107e-05` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.000100894` | `0.000140424` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `4.43722e-05` | `5.66951e-05` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00173949` | `0.00233203` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.681762` | `1.09919` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.411338` | `0.727396` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.305486` | `0.57162` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0199928` | `0.0308796` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.022019` | `0.0330328` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0471478` | `0.0632661` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.0931998` | `0.135906` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0688463` | `0.100681` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `XGBM`
- implementation family: `XGBM`
- archived target count: `19`
- unique source runs: `11`
- unique source configs: `11`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/xgbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/xgbm_reference_models/reference_inventory.yaml`
