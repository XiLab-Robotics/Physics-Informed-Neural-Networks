# RCIM Original Forward ET Reference Models

This archive stores the exported `ET` target-level models for the
`forward` branch of the recovered original RCIM reference-training workflow.

Archive contents:

- `reference_inventory.yaml`
- `onnx/amplitude/`
- `onnx/phase/`
- `python/amplitude/`
- `python/phase/`
- `data/dataFrame_prediction_Fw_v14_newFreq.csv`
- `dataset_snapshot_manifest.yaml`
- `source_runs/<run_instance_id>/launcher_summary.snapshot.json`
- `source_runs/<run_instance_id>/eval.run_summary.snapshot.json`
- `source_runs/<run_instance_id>/export.run_summary.snapshot.json`
- `source_runs/<run_instance_id>/eval_prediction.snapshot.csv`
- `source_runs/<run_instance_id>/export_prediction.snapshot.csv`
- `source_runs/<run_instance_id>/eval.stdout.log`
- `source_runs/<run_instance_id>/export.stdout.log`

Selection rule:

- store the full exported target surface produced by the accepted recovered-original forward reference bundle;
- preserve Python model artifacts for every exported target;
- preserve ONNX artifacts when export succeeds and retain the `*.onnx.export_error.txt` sidecar when export fails;
- preserve the source bundle summaries and logs required to reconstruct the archive provenance.

Archived amplitude targets:

| Target | Harmonic | Archived ONNX | Archived Python | ONNX Status |
| --- | ---: | --- | --- | --- |
| `fft_y_Fw_filtered_ampl_0` | `0` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl0.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/amplitude/ExtraTreeRegressor_ampl0.pkl` | `exported` |
| `fft_y_Fw_filtered_ampl_1` | `1` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl1.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/amplitude/ExtraTreeRegressor_ampl1.pkl` | `exported` |
| `fft_y_Fw_filtered_ampl_3` | `3` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl3.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/amplitude/ExtraTreeRegressor_ampl3.pkl` | `exported` |
| `fft_y_Fw_filtered_ampl_39` | `39` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl39.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/amplitude/ExtraTreeRegressor_ampl39.pkl` | `exported` |
| `fft_y_Fw_filtered_ampl_40` | `40` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl40.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/amplitude/ExtraTreeRegressor_ampl40.pkl` | `exported` |
| `fft_y_Fw_filtered_ampl_78` | `78` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl78.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/amplitude/ExtraTreeRegressor_ampl78.pkl` | `exported` |
| `fft_y_Fw_filtered_ampl_81` | `81` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl81.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/amplitude/ExtraTreeRegressor_ampl81.pkl` | `exported` |
| `fft_y_Fw_filtered_ampl_156` | `156` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl156.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/amplitude/ExtraTreeRegressor_ampl156.pkl` | `exported` |
| `fft_y_Fw_filtered_ampl_162` | `162` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl162.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/amplitude/ExtraTreeRegressor_ampl162.pkl` | `exported` |
| `fft_y_Fw_filtered_ampl_240` | `240` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/amplitude/ExtraTreeRegressor_ampl240.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/amplitude/ExtraTreeRegressor_ampl240.pkl` | `exported` |

Archived phase targets:

| Target | Harmonic | Archived ONNX | Archived Python | ONNX Status |
| --- | ---: | --- | --- | --- |
| `fft_y_Fw_filtered_phase_0` | `0` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase0.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/phase/ExtraTreeRegressor_phase0.pkl` | `exported` |
| `fft_y_Fw_filtered_phase_1` | `1` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase1.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/phase/ExtraTreeRegressor_phase1.pkl` | `exported` |
| `fft_y_Fw_filtered_phase_3` | `3` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase3.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/phase/ExtraTreeRegressor_phase3.pkl` | `exported` |
| `fft_y_Fw_filtered_phase_39` | `39` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase39.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/phase/ExtraTreeRegressor_phase39.pkl` | `exported` |
| `fft_y_Fw_filtered_phase_40` | `40` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase40.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/phase/ExtraTreeRegressor_phase40.pkl` | `exported` |
| `fft_y_Fw_filtered_phase_78` | `78` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase78.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/phase/ExtraTreeRegressor_phase78.pkl` | `exported` |
| `fft_y_Fw_filtered_phase_81` | `81` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase81.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/phase/ExtraTreeRegressor_phase81.pkl` | `exported` |
| `fft_y_Fw_filtered_phase_156` | `156` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase156.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/phase/ExtraTreeRegressor_phase156.pkl` | `exported` |
| `fft_y_Fw_filtered_phase_162` | `162` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase162.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/phase/ExtraTreeRegressor_phase162.pkl` | `exported` |
| `fft_y_Fw_filtered_phase_240` | `240` | `models/paper_reference/rcim_original/forward/et_reference_models/onnx/phase/ExtraTreeRegressor_phase240.onnx` | `models/paper_reference/rcim_original/forward/et_reference_models/python/phase/ExtraTreeRegressor_phase240.pkl` | `exported` |

Provenance summary:

- direction label: `forward`
- paper family: `ET`
- implementation family: `ET`
- archived target count: `20`
- ONNX exported target count: `20`
- ONNX export error count: `0`
- source bundle run instance id: `2026-05-04-23-19-35__fw_original_bundle`
- dataset snapshot manifest: `models/paper_reference/rcim_original/forward/et_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_original/forward/et_reference_models/reference_inventory.yaml`
