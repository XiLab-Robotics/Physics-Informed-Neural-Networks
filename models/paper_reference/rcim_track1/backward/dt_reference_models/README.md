# RCIM Model-Bank Reproduction Backward DT Reference Models

This archive stores the accepted `DT` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00362216` | `0.00536033` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\amplitude\DecisionTreeRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `2.65706e-05` | `4.02372e-05` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\amplitude\DecisionTreeRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000132202` | `0.000461825` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\amplitude\DecisionTreeRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.000109396` | `0.000574387` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\amplitude\DecisionTreeRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.000120005` | `0.000355973` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\amplitude\DecisionTreeRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `2.42053e-05` | `3.67906e-05` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\amplitude\DecisionTreeRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `2.01634e-05` | `2.77918e-05` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\amplitude\DecisionTreeRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.57958e-05` | `3.65537e-05` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\amplitude\DecisionTreeRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `5.25319e-05` | `7.35572e-05` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\amplitude\DecisionTreeRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `1.14882e-05` | `1.64362e-05` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\amplitude\DecisionTreeRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00184067` | `0.00254115` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\phase\DecisionTreeRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.120792` | `0.641618` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\phase\DecisionTreeRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.0532046` | `0.0809374` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\phase\DecisionTreeRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.168514` | `0.590811` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\phase\DecisionTreeRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.024766` | `0.0341871` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\phase\DecisionTreeRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.203102` | `0.82471` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\phase\DecisionTreeRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.101007` | `0.149163` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\phase\DecisionTreeRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0523841` | `0.0880881` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\phase\DecisionTreeRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0912207` | `0.135455` | `models\paper_reference\rcim_track1\backward\dt_reference_models\onnx\phase\DecisionTreeRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `DT`
- implementation family: `DT`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models\paper_reference\rcim_track1\backward\dt_reference_models\dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models\paper_reference\rcim_track1\backward\dt_reference_models\reference_inventory.yaml`
