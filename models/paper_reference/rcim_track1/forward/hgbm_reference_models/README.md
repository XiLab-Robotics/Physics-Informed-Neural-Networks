# RCIM Track 1 Forward HGBM Reference Models

This archive stores the accepted `HGBM` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00230286` | `0.00357874` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `2.15532e-05` | `2.83106e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `7.95097e-05` | `0.000174311` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `5.79553e-05` | `0.000158348` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `2.82265e-05` | `4.40781e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `1.40313e-05` | `2.11261e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `2.0816e-05` | `2.87325e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `2.16954e-05` | `2.91001e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `2.60491e-05` | `3.783e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `8.91012e-06` | `1.24157e-05` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00147875` | `0.00211531` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.47611` | `0.748709` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.271985` | `0.560556` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.234177` | `0.499349` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0186126` | `0.0246378` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0167981` | `0.0219907` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0339588` | `0.0551468` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.0590081` | `0.0950965` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.043818` | `0.0618701` | `models/paper_reference/rcim_track1/forward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `HGBM`
- implementation family: `HGBM`
- archived target count: `19`
- unique source runs: `11`
- unique source configs: `11`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/hgbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/hgbm_reference_models/reference_inventory.yaml`
