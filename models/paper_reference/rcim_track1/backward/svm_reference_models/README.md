# RCIM Track 1 Backward SVM Reference Models

This archive stores the accepted `SVM` target-level winners for the
`backward` branch of the bidirectional original-dataset Track 1 restart wave.

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

- lowest target `MAE`; ties break on target `RMSE`, then target `MAPE`, then run name.
- archive refresh is mandatory at closeout only when the accepted winner improves the stored target entry.

Accepted amplitude targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00244815` | `0.00297317` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/amplitude/SVR_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `0.00012218` | `0.00013583` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/amplitude/SVR_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000386544` | `0.000849184` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/amplitude/SVR_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `0.00042391` | `0.00148789` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/amplitude/SVR_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.000217944` | `0.000308034` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/amplitude/SVR_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `0.000122128` | `0.000144553` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/amplitude/SVR_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `9.19617e-05` | `0.000106955` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/amplitude/SVR_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `3.72479e-05` | `4.84461e-05` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/amplitude/SVR_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `0.000109804` | `0.000134146` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/amplitude/SVR_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `3.67643e-05` | `4.11811e-05` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/amplitude/SVR_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00195786` | `0.00302093` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/phase/SVR_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.34775` | `0.662342` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/phase/SVR_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.329799` | `0.618167` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/phase/SVR_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.539813` | `1.27925` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/phase/SVR_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0260747` | `0.0367106` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/phase/SVR_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.56393` | `0.995695` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/phase/SVR_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.119861` | `0.173432` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/phase/SVR_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.106436` | `0.152783` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/phase/SVR_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.11743` | `0.158214` | `models/paper_reference/rcim_track1/backward/svm_reference_models/onnx/phase/SVR_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `SVM`
- implementation family: `SVR`
- archived target count: `19`
- unique source runs: `14`
- unique source configs: `14`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/svm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/backward/svm_reference_models/reference_inventory.yaml`
