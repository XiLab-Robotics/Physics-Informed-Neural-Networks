# RCIM Track 1 Forward DT Reference Models

This archive stores the accepted `DT` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00297738` | `0.0037916` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `2.65389e-05` | `3.51154e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `4.25289e-05` | `0.000132915` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `4.42742e-05` | `0.000102053` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `3.60934e-05` | `6.12138e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `1.96269e-05` | `2.7134e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `3.50183e-05` | `4.87467e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `2.75625e-05` | `3.77766e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `4.74183e-05` | `6.89225e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `1.07044e-05` | `1.63082e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00196674` | `0.00242446` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.327853` | `1.03094` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.129959` | `0.629177` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.141427` | `0.578067` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0231842` | `0.030571` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0227185` | `0.0307026` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0365718` | `0.0532294` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.0525289` | `0.0890493` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0537444` | `0.0805034` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `DT`
- implementation family: `DT`
- archived target count: `19`
- unique source runs: `12`
- unique source configs: `12`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/dt_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/dt_reference_models/reference_inventory.yaml`
