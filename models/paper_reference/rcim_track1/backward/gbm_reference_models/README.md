# RCIM Track 1 Backward GBM Reference Models

This archive stores the accepted `GBM` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00306205` | `0.00417315` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `2.10163e-05` | `3.01611e-05` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000178687` | `0.000414926` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.000135366` | `0.000172889` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `6.98378e-05` | `9.90601e-05` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `1.90911e-05` | `2.74886e-05` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `1.8684e-05` | `2.70105e-05` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.17104e-05` | `2.90895e-05` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `7.34086e-05` | `9.02598e-05` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `8.54983e-06` | `1.22017e-05` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00153303` | `0.00232457` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.102615` | `0.202684` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.129266` | `0.191873` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.185277` | `0.387719` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0288352` | `0.034693` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.344885` | `0.73478` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.0870806` | `0.134991` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0501809` | `0.0903153` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0846315` | `0.113678` | `models/paper_reference/rcim_track1/backward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `GBM`
- implementation family: `GBM`
- archived target count: `19`
- unique source runs: `9`
- unique source configs: `9`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/gbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/backward/gbm_reference_models/reference_inventory.yaml`
