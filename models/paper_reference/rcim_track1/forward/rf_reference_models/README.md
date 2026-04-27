# RCIM Track 1 Forward RF Reference Models

This archive stores the accepted `RF` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.0027414` | `0.00349851` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `2.16036e-05` | `2.87058e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `3.65455e-05` | `0.000123423` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `3.84016e-05` | `9.18693e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `2.86232e-05` | `4.42349e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `1.75022e-05` | `2.51533e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `2.48662e-05` | `3.39759e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `2.09579e-05` | `2.92267e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `3.65863e-05` | `5.18908e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `9.25868e-06` | `1.25482e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00158251` | `0.00211702` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.333473` | `0.676607` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.131089` | `0.438288` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.14954` | `0.425903` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0181623` | `0.0248681` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0194139` | `0.0286565` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0299737` | `0.0482205` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.0465618` | `0.0864449` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0463556` | `0.060343` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `RF`
- implementation family: `RF`
- archived target count: `19`
- unique source runs: `12`
- unique source configs: `12`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/rf_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/rf_reference_models/reference_inventory.yaml`
