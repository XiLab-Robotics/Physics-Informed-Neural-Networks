# RCIM Track 1 Backward DT Reference Models

This archive stores the accepted `DT` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00278626` | `0.00387706` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `2.56777e-05` | `3.63799e-05` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `6.61816e-05` | `0.000130625` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `4.61088e-05` | `0.000113406` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `7.03775e-05` | `0.000127643` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `2.19025e-05` | `3.62724e-05` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `1.97372e-05` | `2.74815e-05` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.57958e-05` | `3.65537e-05` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `5.06834e-05` | `7.22581e-05` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `8.54166e-06` | `1.26956e-05` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/amplitude/DecisionTreeRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00174665` | `0.00234214` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.0492645` | `0.0925728` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.0512655` | `0.0801539` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.0885101` | `0.165663` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0223217` | `0.0311835` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.10863` | `0.621849` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.0945902` | `0.142264` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0458503` | `0.0785874` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0816804` | `0.111159` | `models/paper_reference/rcim_track1/backward/dt_reference_models/onnx/phase/DecisionTreeRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `DT`
- implementation family: `DT`
- archived target count: `19`
- unique source runs: `9`
- unique source configs: `9`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/dt_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/backward/dt_reference_models/reference_inventory.yaml`
