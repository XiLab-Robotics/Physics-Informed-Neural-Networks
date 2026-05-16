# RCIM Track 1 Backward ELM Reference Models

This archive stores the accepted `ELM` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00739232` | `0.00974713` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\amplitude\ELMRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `3.01773e-05` | `4.4137e-05` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\amplitude\ELMRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.00104357` | `0.00173176` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\amplitude\ELMRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.00104482` | `0.00239836` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\amplitude\ELMRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.00044025` | `0.00128115` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\amplitude\ELMRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `5.92126e-05` | `7.84404e-05` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\amplitude\ELMRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `5.49178e-05` | `7.36454e-05` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\amplitude\ELMRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `3.63881e-05` | `4.71594e-05` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\amplitude\ELMRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `0.000280435` | `0.000372533` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\amplitude\ELMRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `2.07512e-05` | `2.70445e-05` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\amplitude\ELMRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.0029446` | `0.00393481` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\phase\ELMRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.623933` | `0.976768` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\phase\ELMRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.874472` | `1.24462` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\phase\ELMRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.750818` | `1.1873` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\phase\ELMRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0801661` | `0.104573` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\phase\ELMRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `1.68169` | `2.19552` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\phase\ELMRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.176486` | `0.276721` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\phase\ELMRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.130431` | `0.169502` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\phase\ELMRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.179679` | `0.236343` | `models\paper_reference\rcim_track1\backward\elm_reference_models\onnx\phase\ELMRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `ELM`
- implementation family: `ELM`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models\paper_reference\rcim_track1\backward\elm_reference_models\dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models\paper_reference\rcim_track1\backward\elm_reference_models\reference_inventory.yaml`
