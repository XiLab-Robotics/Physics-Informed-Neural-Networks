# RCIM Track 1 Backward LGBM Reference Models

This archive stores the accepted `LGBM` target-level winners for the
`backward` branch of the canonical original-dataset Track 1 benchmark surface.

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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00245033` | `0.00322629` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\amplitude\LGBMRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `2.25836e-05` | `3.28906e-05` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\amplitude\LGBMRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000290743` | `0.00099465` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\amplitude\LGBMRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `9.43304e-05` | `0.000232247` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\amplitude\LGBMRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.000116581` | `0.000225442` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\amplitude\LGBMRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `2.0776e-05` | `2.92663e-05` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\amplitude\LGBMRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `1.6854e-05` | `2.23516e-05` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\amplitude\LGBMRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.48788e-05` | `3.40799e-05` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\amplitude\LGBMRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `2.6598e-05` | `3.59238e-05` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\amplitude\LGBMRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `9.64368e-06` | `1.37455e-05` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\amplitude\LGBMRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00174038` | `0.00233636` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\phase\LGBMRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.179082` | `0.458084` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\phase\LGBMRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.0927631` | `0.145162` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\phase\LGBMRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.384359` | `0.772565` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\phase\LGBMRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0180247` | `0.0272988` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\phase\LGBMRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.368428` | `0.938005` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\phase\LGBMRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.0975133` | `0.12908` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\phase\LGBMRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0469313` | `0.0716468` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\phase\LGBMRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0814266` | `0.105663` | `models\paper_reference\rcim_track1\backward\lgbm_reference_models\onnx\phase\LGBMRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `LGBM`
- implementation family: `LGBM`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models\paper_reference\rcim_track1\backward\lgbm_reference_models\dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models\paper_reference\rcim_track1\backward\lgbm_reference_models\reference_inventory.yaml`
