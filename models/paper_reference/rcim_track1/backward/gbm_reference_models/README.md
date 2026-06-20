# RCIM Model-Bank Reproduction Backward GBM Reference Models

This archive stores the accepted `GBM` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00302314` | `0.00368222` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\amplitude\GradientBoostingRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `2.0832e-05` | `2.94098e-05` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\amplitude\GradientBoostingRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000274177` | `0.00120215` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\amplitude\GradientBoostingRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.000153256` | `0.000406253` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\amplitude\GradientBoostingRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.000174127` | `0.000532606` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\amplitude\GradientBoostingRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `1.90749e-05` | `2.55762e-05` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\amplitude\GradientBoostingRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `1.94171e-05` | `2.56806e-05` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\amplitude\GradientBoostingRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.20437e-05` | `3.02315e-05` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\amplitude\GradientBoostingRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `4.97133e-05` | `6.41438e-05` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\amplitude\GradientBoostingRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `1.02443e-05` | `1.51924e-05` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\amplitude\GradientBoostingRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.0015294` | `0.00209734` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\phase\GradientBoostingRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.163144` | `0.424279` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\phase\GradientBoostingRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.0940569` | `0.213448` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\phase\GradientBoostingRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.29418` | `0.647993` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\phase\GradientBoostingRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0226183` | `0.0294579` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\phase\GradientBoostingRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.336998` | `0.94203` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\phase\GradientBoostingRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.0978393` | `0.132488` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\phase\GradientBoostingRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0455842` | `0.0837849` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\phase\GradientBoostingRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0870526` | `0.126905` | `models\paper_reference\rcim_track1\backward\gbm_reference_models\onnx\phase\GradientBoostingRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `GBM`
- implementation family: `GBM`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models\paper_reference\rcim_track1\backward\gbm_reference_models\dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models\paper_reference\rcim_track1\backward\gbm_reference_models\reference_inventory.yaml`
