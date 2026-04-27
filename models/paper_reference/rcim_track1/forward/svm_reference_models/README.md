# RCIM Track 1 Forward SVM Reference Models

This archive stores the accepted `SVM` target-level winners for the
`forward` branch of the canonical original-dataset Track 1 benchmark surface.

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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00240236` | `0.00296139` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `4.74467e-05` | `6.03741e-05` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000316539` | `0.00057808` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000371459` | `0.0010278` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.000242439` | `0.000426407` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `0.000135655` | `0.000164272` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `6.97981e-05` | `8.96664e-05` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `7.72822e-05` | `9.65513e-05` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.00015192` | `0.000183971` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `6.98458e-05` | `8.16855e-05` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00206264` | `0.00288537` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `1.08053` | `1.56247` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.387766` | `0.913507` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.322142` | `0.504478` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0272462` | `0.0362175` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0199` | `0.0307171` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0475367` | `0.0686588` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.132166` | `0.18991` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0971196` | `0.157212` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `SVM`
- implementation family: `SVR`
- archived target count: `19`
- unique source runs: `11`
- unique source configs: `11`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/svm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/svm_reference_models/reference_inventory.yaml`
