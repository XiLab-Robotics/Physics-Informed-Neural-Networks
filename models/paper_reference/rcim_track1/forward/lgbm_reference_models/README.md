# RCIM Track 1 Forward LGBM Reference Models

This archive stores the accepted `LGBM` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00242855` | `0.00287085` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `2.38161e-05` | `3.13631e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `8.16133e-05` | `0.000207545` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000128501` | `0.000335258` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.000113644` | `0.000202821` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `5.04073e-05` | `6.24599e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `2.17697e-05` | `2.82859e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `2.25468e-05` | `3.0187e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.000176727` | `0.000210241` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `9.78776e-06` | `1.44219e-05` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/amplitude/LGBMRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00179832` | `0.00260982` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.556185` | `1.03984` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.295841` | `0.547315` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.298069` | `0.469953` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0190467` | `0.0273235` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0722734` | `0.0940117` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0379708` | `0.0598769` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.136832` | `0.206742` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0537763` | `0.0819492` | `models/paper_reference/rcim_track1/forward/lgbm_reference_models/onnx/phase/LGBMRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `LGBM`
- implementation family: `LGBM`
- archived target count: `19`
- unique source runs: `17`
- unique source configs: `17`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/lgbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/lgbm_reference_models/reference_inventory.yaml`
