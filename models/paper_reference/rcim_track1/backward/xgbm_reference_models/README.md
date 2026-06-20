# RCIM Model-Bank Reproduction Backward XGBM Reference Models

This archive stores the accepted `XGBM` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.004586` | `0.00542501` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\amplitude\XGBRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `6.52717e-05` | `0.000108672` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\amplitude\XGBRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000408884` | `0.00104628` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\amplitude\XGBRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.00028056` | `0.000698929` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\amplitude\XGBRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.0003725` | `0.00103448` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\amplitude\XGBRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `7.24577e-05` | `9.3682e-05` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\amplitude\XGBRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `7.90442e-05` | `9.63518e-05` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\amplitude\XGBRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `3.96378e-05` | `4.96259e-05` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\amplitude\XGBRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `0.000145479` | `0.000194315` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\amplitude\XGBRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `2.76087e-05` | `3.34652e-05` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\amplitude\XGBRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00210362` | `0.00314551` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\phase\XGBRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.26358` | `0.559001` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\phase\XGBRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.162021` | `0.311383` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\phase\XGBRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.482149` | `0.863736` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\phase\XGBRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0463593` | `0.05994` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\phase\XGBRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.822733` | `1.18958` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\phase\XGBRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.158859` | `0.259128` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\phase\XGBRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.104748` | `0.224614` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\phase\XGBRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.113511` | `0.15135` | `models\paper_reference\rcim_track1\backward\xgbm_reference_models\onnx\phase\XGBRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `XGBM`
- implementation family: `XGBM`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models\paper_reference\rcim_track1\backward\xgbm_reference_models\dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models\paper_reference\rcim_track1\backward\xgbm_reference_models\reference_inventory.yaml`
