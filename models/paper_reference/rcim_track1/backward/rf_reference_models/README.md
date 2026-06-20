# RCIM Model-Bank Reproduction Backward RF Reference Models

This archive stores the accepted `RF` target-level winners for the
`backward` branch of the canonical original-dataset RCIM Model-Bank Reproduction benchmark surface.

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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00326128` | `0.00388728` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\amplitude\RandomForestRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `2.12857e-05` | `3.17179e-05` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\amplitude\RandomForestRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000260409` | `0.000994547` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\amplitude\RandomForestRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.00019246` | `0.00054455` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\amplitude\RandomForestRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.000178183` | `0.000523307` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\amplitude\RandomForestRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `2.36905e-05` | `3.21038e-05` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\amplitude\RandomForestRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `2.28753e-05` | `2.90596e-05` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\amplitude\RandomForestRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.18196e-05` | `2.95874e-05` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\amplitude\RandomForestRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `5.50349e-05` | `7.49419e-05` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\amplitude\RandomForestRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `1.07872e-05` | `1.53213e-05` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\amplitude\RandomForestRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00151443` | `0.00206574` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\phase\RandomForestRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.180663` | `0.441122` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\phase\RandomForestRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.100225` | `0.228194` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\phase\RandomForestRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.322211` | `0.740668` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\phase\RandomForestRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0227093` | `0.0314359` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\phase\RandomForestRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.36563` | `0.958068` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\phase\RandomForestRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.093876` | `0.128839` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\phase\RandomForestRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0500226` | `0.0953936` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\phase\RandomForestRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0804635` | `0.118077` | `models\paper_reference\rcim_track1\backward\rf_reference_models\onnx\phase\RandomForestRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `RF`
- implementation family: `RF`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models\paper_reference\rcim_track1\backward\rf_reference_models\dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models\paper_reference\rcim_track1\backward\rf_reference_models\reference_inventory.yaml`
