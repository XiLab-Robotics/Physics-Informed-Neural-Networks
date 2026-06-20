# RCIM Model-Bank Reproduction Forward LGBM Reference Models

This archive stores the accepted `LGBM` target-level winners for the
`forward` branch of the canonical original-dataset RCIM Model-Bank Reproduction benchmark surface.

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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00608785` | `0.00766252` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `3.53012e-05` | `4.64541e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000334592` | `0.000543088` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000453492` | `0.00117065` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.000153304` | `0.000291955` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `5.23761e-05` | `6.46017e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `0.0001078` | `0.000124724` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `3.71074e-05` | `5.54452e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.000176727` | `0.000210241` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `2.41069e-05` | `3.00738e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00261033` | `0.00362244` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `1.22009` | `1.54621` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.632576` | `1.02708` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.476992` | `0.950281` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.045093` | `0.0535386` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.077429` | `0.10155` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0640331` | `0.0871438` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.144583` | `0.259432` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.149051` | `0.191343` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `LGBM`
- implementation family: `LGBM`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/lgbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/lgbm_reference_models/reference_inventory.yaml`
