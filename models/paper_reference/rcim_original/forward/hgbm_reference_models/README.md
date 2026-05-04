# RCIM Original Forward HGBM Reference Models

This archive stores the exported `HGBM` target-level models for the
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
| `fft_y_Fw_filtered_ampl_0` | `0` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/amplitude/HistGradientBoostingRegressor_ampl0.pkl` | `export error` |
| `fft_y_Fw_filtered_ampl_1` | `1` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/amplitude/HistGradientBoostingRegressor_ampl1.pkl` | `export error` |
| `fft_y_Fw_filtered_ampl_3` | `3` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/amplitude/HistGradientBoostingRegressor_ampl3.pkl` | `export error` |
| `fft_y_Fw_filtered_ampl_39` | `39` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/amplitude/HistGradientBoostingRegressor_ampl39.pkl` | `export error` |
| `fft_y_Fw_filtered_ampl_40` | `40` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/amplitude/HistGradientBoostingRegressor_ampl40.pkl` | `export error` |
| `fft_y_Fw_filtered_ampl_78` | `78` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/amplitude/HistGradientBoostingRegressor_ampl78.pkl` | `export error` |
| `fft_y_Fw_filtered_ampl_81` | `81` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/amplitude/HistGradientBoostingRegressor_ampl81.pkl` | `export error` |
| `fft_y_Fw_filtered_ampl_156` | `156` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/amplitude/HistGradientBoostingRegressor_ampl156.pkl` | `export error` |
| `fft_y_Fw_filtered_ampl_162` | `162` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/amplitude/HistGradientBoostingRegressor_ampl162.pkl` | `export error` |
| `fft_y_Fw_filtered_ampl_240` | `240` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/amplitude/HistGradientBoostingRegressor_ampl240.pkl` | `export error` |

Archived phase targets:

| Target | Harmonic | Archived ONNX | Archived Python | ONNX Status |
| --- | ---: | --- | --- | --- |
| `fft_y_Fw_filtered_phase_0` | `0` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/phase/HistGradientBoostingRegressor_phase0.pkl` | `export error` |
| `fft_y_Fw_filtered_phase_1` | `1` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/phase/HistGradientBoostingRegressor_phase1.pkl` | `export error` |
| `fft_y_Fw_filtered_phase_3` | `3` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/phase/HistGradientBoostingRegressor_phase3.pkl` | `export error` |
| `fft_y_Fw_filtered_phase_39` | `39` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/phase/HistGradientBoostingRegressor_phase39.pkl` | `export error` |
| `fft_y_Fw_filtered_phase_40` | `40` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/phase/HistGradientBoostingRegressor_phase40.pkl` | `export error` |
| `fft_y_Fw_filtered_phase_78` | `78` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/phase/HistGradientBoostingRegressor_phase78.pkl` | `export error` |
| `fft_y_Fw_filtered_phase_81` | `81` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/phase/HistGradientBoostingRegressor_phase81.pkl` | `export error` |
| `fft_y_Fw_filtered_phase_156` | `156` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/phase/HistGradientBoostingRegressor_phase156.pkl` | `export error` |
| `fft_y_Fw_filtered_phase_162` | `162` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/phase/HistGradientBoostingRegressor_phase162.pkl` | `export error` |
| `fft_y_Fw_filtered_phase_240` | `240` | Unavailable | `models/paper_reference/rcim_original/forward/hgbm_reference_models/python/phase/HistGradientBoostingRegressor_phase240.pkl` | `export error` |

Provenance summary:

- direction label: `forward`
- paper family: `HGBM`
- implementation family: `HGBM`
- archived target count: `20`
- ONNX exported target count: `0`
- ONNX export error count: `20`
- source bundle run instance id: `2026-05-04-23-19-35__fw_original_bundle`
- dataset snapshot manifest: `models/paper_reference/rcim_original/forward/hgbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_original/forward/hgbm_reference_models/reference_inventory.yaml`
