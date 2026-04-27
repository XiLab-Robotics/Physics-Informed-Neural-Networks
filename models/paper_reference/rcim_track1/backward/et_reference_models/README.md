# RCIM Track 1 Backward ET Reference Models

This archive stores the accepted `ET` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.0030276` | `0.0037362` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `2.47334e-05` | `3.68429e-05` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `7.92687e-05` | `0.000197998` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `5.12173e-05` | `0.000128692` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `7.48752e-05` | `0.000145861` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `2.49502e-05` | `3.6898e-05` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `2.00874e-05` | `2.74252e-05` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.54493e-05` | `3.9828e-05` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `5.48314e-05` | `7.6e-05` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `9.33761e-06` | `1.43082e-05` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00164147` | `0.00263308` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.0653404` | `0.124204` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.0534907` | `0.0712563` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.229348` | `0.510765` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.024494` | `0.0339203` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.113296` | `0.633153` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.0911072` | `0.125636` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.045039` | `0.0780663` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0961469` | `0.13548` | `models/paper_reference/rcim_track1/backward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `ET`
- implementation family: `ET`
- archived target count: `19`
- unique source runs: `12`
- unique source configs: `12`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/et_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/backward/et_reference_models/reference_inventory.yaml`
