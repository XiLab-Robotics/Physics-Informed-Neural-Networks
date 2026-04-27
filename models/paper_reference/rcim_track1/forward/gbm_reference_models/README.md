# RCIM Track 1 Forward GBM Reference Models

This archive stores the accepted `GBM` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00306606` | `0.0035555` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `2.24145e-05` | `2.91983e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000108567` | `0.000163884` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000118525` | `0.000352059` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `4.39369e-05` | `6.78321e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `2.45673e-05` | `3.13798e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `4.08111e-05` | `5.06426e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `2.38098e-05` | `3.18227e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `6.74426e-05` | `8.39781e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `1.08931e-05` | `1.49892e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00167712` | `0.00243444` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.490354` | `0.850627` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.236174` | `0.485444` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.219106` | `0.440246` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0227536` | `0.0303319` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.029536` | `0.037133` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0346363` | `0.04588` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.0636816` | `0.0988506` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0673461` | `0.0893568` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `GBM`
- implementation family: `GBM`
- archived target count: `19`
- unique source runs: `8`
- unique source configs: `8`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/gbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/gbm_reference_models/reference_inventory.yaml`
