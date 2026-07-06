# RCIM Model-Bank Reproduction Backward ET Reference Models

This archive stores the accepted `ET` target-level winners for the
`backward` branch of the canonical original-dataset RCIM Model-Bank Reproduction benchmark surface.

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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00323091` | `0.00396137` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\amplitude\ExtraTreeRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `2.79374e-05` | `3.80118e-05` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\amplitude\ExtraTreeRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000373914` | `0.0010175` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\amplitude\ExtraTreeRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.000196806` | `0.000604509` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\amplitude\ExtraTreeRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.000183825` | `0.000388673` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\amplitude\ExtraTreeRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `3.6441e-05` | `4.36729e-05` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\amplitude\ExtraTreeRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `2.89436e-05` | `3.85289e-05` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\amplitude\ExtraTreeRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `3.0195e-05` | `4.1416e-05` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\amplitude\ExtraTreeRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `0.000126116` | `0.000157222` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\amplitude\ExtraTreeRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `1.9469e-05` | `2.88975e-05` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\amplitude\ExtraTreeRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00224629` | `0.00348736` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\phase\ExtraTreeRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.278798` | `0.651211` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\phase\ExtraTreeRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.166394` | `0.58247` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\phase\ExtraTreeRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.520119` | `1.12751` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\phase\ExtraTreeRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0307531` | `0.0414338` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\phase\ExtraTreeRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.293192` | `1.21723` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\phase\ExtraTreeRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.131714` | `0.180527` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\phase\ExtraTreeRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0801005` | `0.138744` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\phase\ExtraTreeRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.12357` | `0.16677` | `models\paper_reference\rcim_track1\backward\et_reference_models\onnx\phase\ExtraTreeRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `ET`
- implementation family: `ET`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models\paper_reference\rcim_track1\backward\et_reference_models\dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models\paper_reference\rcim_track1\backward\et_reference_models\reference_inventory.yaml`
