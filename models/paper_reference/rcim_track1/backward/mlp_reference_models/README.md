# RCIM Track 1 Backward MLP Reference Models

This archive stores the accepted `MLP` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.0187638` | `0.0329994` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\amplitude\MLPRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `0.0180434` | `0.0290015` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\amplitude\MLPRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.0350925` | `0.0685187` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\amplitude\MLPRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.0281716` | `0.0433351` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\amplitude\MLPRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.024987` | `0.0376344` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\amplitude\MLPRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `0.0142052` | `0.0267382` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\amplitude\MLPRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `0.0222598` | `0.0368861` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\amplitude\MLPRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `0.0259821` | `0.0464764` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\amplitude\MLPRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `0.0175306` | `0.0387349` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\amplitude\MLPRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `0.0223986` | `0.0349958` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\amplitude\MLPRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.0250021` | `0.0377578` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\phase\MLPRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.636549` | `0.96245` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\phase\MLPRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.94923` | `1.29006` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\phase\MLPRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.708315` | `1.17318` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\phase\MLPRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.085401` | `0.109135` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\phase\MLPRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `1.46551` | `1.8702` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\phase\MLPRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.19159` | `0.296805` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\phase\MLPRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.158349` | `0.213038` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\phase\MLPRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.221734` | `0.290191` | `models\paper_reference\rcim_track1\backward\mlp_reference_models\onnx\phase\MLPRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `MLP`
- implementation family: `MLP`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models\paper_reference\rcim_track1\backward\mlp_reference_models\dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models\paper_reference\rcim_track1\backward\mlp_reference_models\reference_inventory.yaml`
