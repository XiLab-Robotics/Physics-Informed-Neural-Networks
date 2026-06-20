# RCIM Model-Bank Reproduction Forward GBM Reference Models

This archive stores the accepted `GBM` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00342451` | `0.00429076` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `3.36664e-05` | `4.40207e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000169589` | `0.00036332` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.000225139` | `0.0006087` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `8.29394e-05` | `0.000184329` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `2.68844e-05` | `3.51095e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `4.56841e-05` | `5.66209e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `2.48912e-05` | `3.373e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `7.29048e-05` | `9.95071e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `1.38016e-05` | `1.92187e-05` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/amplitude/GradientBoostingRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00193875` | `0.00273946` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.680302` | `1.0587` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.304907` | `0.757983` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.374422` | `0.93035` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0208532` | `0.027172` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0338847` | `0.0482154` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0347052` | `0.048643` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.0649534` | `0.146262` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0690813` | `0.0933574` | `models/paper_reference/rcim_track1/forward/gbm_reference_models/onnx/phase/GradientBoostingRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `GBM`
- implementation family: `GBM`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/gbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/gbm_reference_models/reference_inventory.yaml`
