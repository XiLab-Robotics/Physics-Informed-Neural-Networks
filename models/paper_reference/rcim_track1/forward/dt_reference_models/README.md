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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00334252` | `0.00448775` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `3.19493e-05` | `4.32286e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000150126` | `0.000387564` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000142924` | `0.000556478` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `8.49043e-05` | `0.000119526` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `2.48493e-05` | `3.36444e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `5.40545e-05` | `6.90261e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `3.3619e-05` | `4.23337e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `9.67335e-05` | `0.000121027` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `1.78349e-05` | `2.22354e-05` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00249641` | `0.00343561` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.83352` | `1.5605` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.290414` | `0.769901` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.344008` | `0.712705` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0417107` | `0.0507192` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0381584` | `0.0636581` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0568484` | `0.0735106` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.104668` | `0.160754` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0985556` | `0.134366` | `models/paper_reference/rcim_track1/forward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `DT`
- implementation family: `DT`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/dt_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/dt_reference_models/reference_inventory.yaml`
