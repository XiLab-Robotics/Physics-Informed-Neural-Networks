# RCIM Track 1 Forward MLP Reference Models

This archive stores the accepted `MLP` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00345704` | `0.00441997` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `0.00171012` | `0.0021178` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.00246043` | `0.00306965` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.00211723` | `0.00276464` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.00255737` | `0.00311164` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `0.00210367` | `0.00274825` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `0.00194599` | `0.00246956` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `0.00215552` | `0.00294075` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.00206027` | `0.00269949` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `0.00179699` | `0.00216725` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00317452` | `0.00387037` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.658122` | `1.00843` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.35434` | `0.687019` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.463599` | `0.739707` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0233929` | `0.0320967` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0216331` | `0.0313669` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0376109` | `0.0548608` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.0743748` | `0.106545` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0516697` | `0.0748398` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `MLP`
- implementation family: `MLP`
- archived target count: `19`
- unique source runs: `13`
- unique source configs: `13`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/mlp_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/mlp_reference_models/reference_inventory.yaml`
