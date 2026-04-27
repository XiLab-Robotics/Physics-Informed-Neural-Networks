# RCIM Track 1 Backward MLP Reference Models

This archive stores the accepted `MLP` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00393679` | `0.00500305` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `0.00182461` | `0.00217587` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.00232499` | `0.00359669` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.00225488` | `0.00333342` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.00259757` | `0.0031084` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `0.00247029` | `0.00305953` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `0.0024777` | `0.00306248` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `0.00248698` | `0.00306197` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `0.00212886` | `0.0027425` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `0.00246561` | `0.00304781` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/amplitude/MLPRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00318003` | `0.00394886` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/phase/MLPRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.157558` | `0.368369` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/phase/MLPRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.0767902` | `0.152055` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/phase/MLPRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.299699` | `0.473102` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/phase/MLPRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0200177` | `0.0251177` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/phase/MLPRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.281941` | `0.752583` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/phase/MLPRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.086572` | `0.117351` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/phase/MLPRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0553362` | `0.0848492` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/phase/MLPRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0770297` | `0.106173` | `models/paper_reference/rcim_track1/backward/mlp_reference_models/onnx/phase/MLPRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `MLP`
- implementation family: `MLP`
- archived target count: `19`
- unique source runs: `10`
- unique source configs: `10`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/mlp_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/backward/mlp_reference_models/reference_inventory.yaml`
