# RCIM Track 1 Forward ERT Reference Models

This archive stores the accepted `ERT` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.0032981` | `0.00402504` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `2.99936e-05` | `3.95159e-05` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `5.42847e-05` | `0.000226686` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `8.02514e-05` | `0.000326493` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `3.96275e-05` | `7.97047e-05` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `1.90726e-05` | `2.5487e-05` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `2.58271e-05` | `3.32522e-05` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `2.06984e-05` | `2.74003e-05` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `3.40623e-05` | `4.85815e-05` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `1.13607e-05` | `1.56353e-05` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00213975` | `0.00307895` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.505565` | `0.924908` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.20839` | `0.708327` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.311603` | `0.845185` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0211093` | `0.0289877` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0271126` | `0.0522371` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0327383` | `0.0507968` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.0664968` | `0.207215` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0456165` | `0.0622622` | `models/paper_reference/rcim_track1/forward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `ERT`
- implementation family: `ERT`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/ert_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/ert_reference_models/reference_inventory.yaml`
