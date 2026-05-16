# RCIM Track 1 Backward HGBM Reference Models

This archive stores the accepted `HGBM` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00378368` | `0.00429035` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\amplitude\HistGradientBoostingRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `2.91305e-05` | `4.75846e-05` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\amplitude\HistGradientBoostingRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000284131` | `0.000819717` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\amplitude\HistGradientBoostingRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.000338821` | `0.000840448` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\amplitude\HistGradientBoostingRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.000269172` | `0.000875059` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\amplitude\HistGradientBoostingRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `2.76483e-05` | `3.84266e-05` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\amplitude\HistGradientBoostingRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `2.06079e-05` | `2.73323e-05` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\amplitude\HistGradientBoostingRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.60511e-05` | `3.36259e-05` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\amplitude\HistGradientBoostingRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `7.61737e-05` | `9.68442e-05` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\amplitude\HistGradientBoostingRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `1.26117e-05` | `1.71525e-05` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\amplitude\HistGradientBoostingRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00187119` | `0.00299787` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\phase\HistGradientBoostingRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.240075` | `0.538131` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\phase\HistGradientBoostingRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.173083` | `0.292846` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\phase\HistGradientBoostingRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.405538` | `0.901278` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\phase\HistGradientBoostingRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0301106` | `0.0375849` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\phase\HistGradientBoostingRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.500873` | `0.954013` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\phase\HistGradientBoostingRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.112472` | `0.160093` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\phase\HistGradientBoostingRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0858941` | `0.182508` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\phase\HistGradientBoostingRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.110244` | `0.159944` | `models\paper_reference\rcim_track1\backward\hgbm_reference_models\onnx\phase\HistGradientBoostingRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `HGBM`
- implementation family: `HGBM`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models\paper_reference\rcim_track1\backward\hgbm_reference_models\dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models\paper_reference\rcim_track1\backward\hgbm_reference_models\reference_inventory.yaml`
