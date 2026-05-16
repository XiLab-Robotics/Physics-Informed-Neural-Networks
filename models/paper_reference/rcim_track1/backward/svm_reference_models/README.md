# RCIM Track 1 Backward SVM Reference Models

This archive stores the accepted `SVM` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00429719` | `0.00624162` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\amplitude\SVR_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `7.21116e-05` | `0.000100359` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\amplitude\SVR_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000718831` | `0.00159816` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\amplitude\SVR_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.000751263` | `0.00247527` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\amplitude\SVR_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.0005152` | `0.00143899` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\amplitude\SVR_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `6.26989e-05` | `8.0137e-05` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\amplitude\SVR_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `0.000101174` | `0.000121816` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\amplitude\SVR_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `4.02579e-05` | `5.14725e-05` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\amplitude\SVR_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `0.00013487` | `0.000165646` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\amplitude\SVR_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `2.13117e-05` | `2.79301e-05` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\amplitude\SVR_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00267961` | `0.00384401` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\phase\SVR_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.572634` | `1.08322` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\phase\SVR_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.746112` | `1.44516` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\phase\SVR_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.715218` | `1.3595` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\phase\SVR_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0289354` | `0.0411088` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\phase\SVR_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `1.73853` | `2.12783` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\phase\SVR_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.226484` | `0.3468` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\phase\SVR_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.153255` | `0.350233` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\phase\SVR_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.171261` | `0.2245` | `models\paper_reference\rcim_track1\backward\svm_reference_models\onnx\phase\SVR_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `SVM`
- implementation family: `SVR`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models\paper_reference\rcim_track1\backward\svm_reference_models\dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models\paper_reference\rcim_track1\backward\svm_reference_models\reference_inventory.yaml`
