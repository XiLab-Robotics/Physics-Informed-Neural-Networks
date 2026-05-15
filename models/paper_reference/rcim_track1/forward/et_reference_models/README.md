# RCIM Track 1 Forward ET Reference Models

This archive stores the accepted `ET` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00302836` | `0.00363044` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `3.40618e-05` | `4.51865e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000123802` | `0.000365913` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000119119` | `0.000307436` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.000223229` | `0.000607463` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `2.68639e-05` | `3.77537e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `5.40808e-05` | `7.3839e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `3.97516e-05` | `6.71039e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.000100007` | `0.000137482` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `2.35786e-05` | `3.08913e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00241905` | `0.00333782` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `1.16006` | `2.09517` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.404844` | `1.25598` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.391284` | `0.90783` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0424304` | `0.0579582` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0363294` | `0.0633639` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0682433` | `0.0982918` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.0960632` | `0.168641` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0900424` | `0.13214` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `ET`
- implementation family: `ET`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/et_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/et_reference_models/reference_inventory.yaml`
