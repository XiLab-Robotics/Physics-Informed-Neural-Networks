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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.0029211` | `0.0035838` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `3.17912e-05` | `4.03765e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000122525` | `0.000372638` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000199132` | `0.000615249` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `8.14611e-05` | `0.000155537` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `2.20406e-05` | `3.01094e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `3.03707e-05` | `3.91365e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `2.359e-05` | `3.33647e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `5.99545e-05` | `7.90751e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `1.40259e-05` | `1.9156e-05` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/amplitude/RandomForestRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00191692` | `0.00259315` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.651807` | `1.06046` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.228596` | `0.647753` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.436112` | `0.940516` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0213333` | `0.0282609` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0271451` | `0.0360729` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0354547` | `0.0529926` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.070632` | `0.211336` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0583387` | `0.0825679` | `models/paper_reference/rcim_track1/forward/rf_reference_models/onnx/phase/RandomForestRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `RF`
- implementation family: `RF`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/rf_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/rf_reference_models/reference_inventory.yaml`
