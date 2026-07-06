# RCIM Model-Bank Reproduction Forward SVM Reference Models

This archive stores the accepted `SVM` target-level winners for the
`forward` branch of the canonical original-dataset RCIM Model-Bank Reproduction benchmark surface.

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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00305677` | `0.00338731` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `6.56573e-05` | `8.19255e-05` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000519983` | `0.00110312` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000680543` | `0.00225189` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.000242616` | `0.000607111` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `7.61143e-05` | `8.95392e-05` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `5.12792e-05` | `6.45351e-05` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `5.42676e-05` | `7.34706e-05` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.000130489` | `0.000159871` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `4.18793e-05` | `5.33825e-05` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/amplitude/SVR_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00293219` | `0.00397461` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `2.005` | `2.41283` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.711488` | `1.53987` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.519536` | `1.00731` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0336004` | `0.0506014` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0378276` | `0.0614727` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0992124` | `0.131569` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.163665` | `0.332271` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.137422` | `0.218491` | `models/paper_reference/rcim_track1/forward/svm_reference_models/onnx/phase/SVR_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `SVM`
- implementation family: `SVR`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/svm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/svm_reference_models/reference_inventory.yaml`
