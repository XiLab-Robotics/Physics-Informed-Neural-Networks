# RCIM Track 1 Forward HGBM Reference Models

This archive stores the accepted `HGBM` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.0032848` | `0.00394434` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `3.01984e-05` | `3.92211e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000192565` | `0.000417758` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000331003` | `0.000840289` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `9.24011e-05` | `0.000190047` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `2.74001e-05` | `3.57166e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `4.22901e-05` | `5.29581e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `2.7153e-05` | `4.08969e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `6.9168e-05` | `9.33812e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `1.56039e-05` | `2.04346e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00217747` | `0.00307036` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.884828` | `1.32219` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.441184` | `0.923536` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.41455` | `0.884716` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0285098` | `0.0373394` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.033155` | `0.0569335` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0470393` | `0.0714217` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.0900869` | `0.185849` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0779747` | `0.113812` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `HGBM`
- implementation family: `HGBM`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/hgbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/hgbm_reference_models/reference_inventory.yaml`
