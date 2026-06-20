# RCIM Model-Bank Reproduction Forward XGBM Reference Models

This archive stores the accepted `XGBM` target-level winners for the
`forward` branch of the canonical original-dataset RCIM Model-Bank Reproduction benchmark surface.

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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00409938` | `0.00530128` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `5.8509e-05` | `7.53981e-05` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000213958` | `0.000416185` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000250252` | `0.000653461` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.000172708` | `0.000308105` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `7.00635e-05` | `9.14248e-05` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `0.000112889` | `0.000139317` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `6.52937e-05` | `8.88706e-05` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.000130015` | `0.000177205` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `4.84409e-05` | `5.99168e-05` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/amplitude/XGBRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00234852` | `0.00330225` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `1.06937` | `1.45745` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.44421` | `0.833064` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.438863` | `0.819865` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0317376` | `0.0399144` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0466152` | `0.0736494` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0602509` | `0.0857178` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.132517` | `0.201331` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.111915` | `0.156961` | `models/paper_reference/rcim_track1/forward/xgbm_reference_models/onnx/phase/XGBRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `XGBM`
- implementation family: `XGBM`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/xgbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/xgbm_reference_models/reference_inventory.yaml`
