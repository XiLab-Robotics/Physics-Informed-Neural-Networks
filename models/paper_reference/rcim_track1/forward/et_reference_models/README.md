# RCIM Track 1 Forward ET Reference Models

This archive stores the accepted `ET` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00289541` | `0.00372992` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `2.72356e-05` | `3.87746e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `4.21641e-05` | `9.85037e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `4.20594e-05` | `8.58138e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `4.49836e-05` | `7.24233e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `1.97413e-05` | `2.75335e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `3.35054e-05` | `4.96286e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `2.66845e-05` | `4.00261e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `4.82001e-05` | `7.49928e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `1.16915e-05` | `1.83752e-05` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00220789` | `0.00306814` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `0.482571` | `1.36028` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `0.132855` | `0.459432` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.174853` | `0.645875` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0254555` | `0.035136` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0227454` | `0.0346159` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.0411961` | `0.0665412` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.064332` | `0.118259` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.0565684` | `0.0726197` | `models/paper_reference/rcim_track1/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `ET`
- implementation family: `ET`
- archived target count: `19`
- unique source runs: `12`
- unique source configs: `12`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/et_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/et_reference_models/reference_inventory.yaml`
