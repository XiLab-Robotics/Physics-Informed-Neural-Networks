# RCIM Track 1 Backward RF Reference Models

This archive stores the accepted `RF` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00248235` | `0.00334782` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `1.91284e-05` | `2.68348e-05` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `7.90409e-05` | `0.000269695` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `4.94272e-05` | `0.000139798` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `5.05932e-05` | `8.98524e-05` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `1.6782e-05` | `2.33095e-05` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `1.50283e-05` | `2.09622e-05` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.22018e-05` | `3.10832e-05` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `3.45098e-05` | `4.61607e-05` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `6.83012e-06` | `1.01763e-05` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00148515` | `0.00219941` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/phase/RandomForestRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.0597704` | `0.216907` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/phase/RandomForestRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.0486596` | `0.0824429` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/phase/RandomForestRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.0918517` | `0.195657` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/phase/RandomForestRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0202588` | `0.029553` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/phase/RandomForestRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.153195` | `0.596752` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/phase/RandomForestRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.0753753` | `0.11356` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/phase/RandomForestRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0348443` | `0.0595121` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/phase/RandomForestRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0725617` | `0.097616` | `models/paper_reference/rcim_track1/backward/rf_reference_models/onnx/phase/RandomForestRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `RF`
- implementation family: `RF`
- archived target count: `19`
- unique source runs: `12`
- unique source configs: `12`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/rf_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/backward/rf_reference_models/reference_inventory.yaml`
