# RCIM Track 1 Forward ELM Reference Models

This archive stores the accepted `ELM` target-level winners for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | `0.00636693` | `0.00848451` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/amplitude/ELMRegressor_ampl0.onnx` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `3.42378e-05` | `4.29732e-05` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/amplitude/ELMRegressor_ampl1.onnx` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `0.000661327` | `0.00104785` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/amplitude/ELMRegressor_ampl156.onnx` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `0.00095085` | `0.00228557` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/amplitude/ELMRegressor_ampl162.onnx` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `0.000313632` | `0.000596099` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/amplitude/ELMRegressor_ampl240.onnx` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `7.05152e-05` | `9.23106e-05` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/amplitude/ELMRegressor_ampl3.onnx` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `0.00010553` | `0.000150356` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/amplitude/ELMRegressor_ampl39.onnx` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `4.4305e-05` | `6.42287e-05` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/amplitude/ELMRegressor_ampl40.onnx` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `0.000253924` | `0.000341396` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/amplitude/ELMRegressor_ampl78.onnx` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `3.27129e-05` | `4.17627e-05` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/amplitude/ELMRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Fw_filtered_phase_1` | `1` | `0.00269276` | `0.00356586` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/phase/ELMRegressor_phase1.onnx` |
| `fft_y_Fw_filtered_phase_156` | `156` | `1.74182` | `2.08167` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/phase/ELMRegressor_phase156.onnx` |
| `fft_y_Fw_filtered_phase_162` | `162` | `1.02676` | `1.53247` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/phase/ELMRegressor_phase162.onnx` |
| `fft_y_Fw_filtered_phase_240` | `240` | `0.633718` | `0.976902` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/phase/ELMRegressor_phase240.onnx` |
| `fft_y_Fw_filtered_phase_3` | `3` | `0.0662808` | `0.0830624` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/phase/ELMRegressor_phase3.onnx` |
| `fft_y_Fw_filtered_phase_39` | `39` | `0.0722836` | `0.0971095` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/phase/ELMRegressor_phase39.onnx` |
| `fft_y_Fw_filtered_phase_40` | `40` | `0.065352` | `0.0922018` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/phase/ELMRegressor_phase40.onnx` |
| `fft_y_Fw_filtered_phase_78` | `78` | `0.147244` | `0.201695` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/phase/ELMRegressor_phase78.onnx` |
| `fft_y_Fw_filtered_phase_81` | `81` | `0.15427` | `0.199579` | `models/paper_reference/rcim_track1/forward/elm_reference_models/onnx/phase/ELMRegressor_phase81.onnx` |

Provenance summary:

- direction label: `forward`
- paper family: `ELM`
- implementation family: `ELM`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/forward/elm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/forward/elm_reference_models/reference_inventory.yaml`
