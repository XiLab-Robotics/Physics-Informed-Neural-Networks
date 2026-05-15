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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.0271161` | `0.0444009` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `0.0289634` | `0.0506314` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.0233848` | `0.0512525` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.0346719` | `0.0782889` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.0227904` | `0.0353102` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `0.013724` | `0.0280048` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `0.0150448` | `0.0312168` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `0.0229618` | `0.035164` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.0222392` | `0.0532152` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `0.0263144` | `0.0407882` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.0183255` | `0.0367435` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `1.7145` | `2.0493` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `1.01942` | `1.46987` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.62369` | `1.01822` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0656061` | `0.0860856` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.100654` | `0.127013` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0875861` | `0.127158` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.127547` | `0.164189` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.175523` | `0.225802` | `models/paper_reference/rcim_track1/forward/mlp_reference_models/onnx/phase/MLPRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `MLP`
- implementation family: `MLP`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/mlp_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/mlp_reference_models/reference_inventory.yaml`
