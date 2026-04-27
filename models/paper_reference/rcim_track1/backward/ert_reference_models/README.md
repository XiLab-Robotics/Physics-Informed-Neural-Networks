# RCIM Track 1 Backward ERT Reference Models

This archive stores the accepted `ERT` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00259573` | `0.00333832` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `1.75332e-05` | `2.5813e-05` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `5.3009e-05` | `0.000141236` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `3.22538e-05` | `8.91091e-05` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `5.68946e-05` | `0.00012125` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `1.96649e-05` | `2.84382e-05` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `1.5993e-05` | `2.25142e-05` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.31882e-05` | `3.34479e-05` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `3.48878e-05` | `4.72119e-05` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `6.95047e-06` | `1.02593e-05` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/amplitude/ExtraTreesRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00147949` | `0.00195305` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.0461639` | `0.0956603` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.0420995` | `0.0809778` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.14226` | `0.497061` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0203398` | `0.0256952` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.136584` | `0.617764` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.0743557` | `0.105595` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0386345` | `0.080009` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0715767` | `0.102052` | `models/paper_reference/rcim_track1/backward/ert_reference_models/onnx/phase/ExtraTreesRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `ERT`
- implementation family: `ERT`
- archived target count: `19`
- unique source runs: `9`
- unique source configs: `9`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/ert_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/backward/ert_reference_models/reference_inventory.yaml`
