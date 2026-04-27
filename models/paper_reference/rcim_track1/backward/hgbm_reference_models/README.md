# RCIM Track 1 Backward HGBM Reference Models

This archive stores the accepted `HGBM` target-level winners for the
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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.0022091` | `0.002885` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `1.94415e-05` | `2.82635e-05` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000203439` | `0.000691378` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `7.37356e-05` | `0.000174312` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `8.15566e-05` | `0.000128594` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `1.60564e-05` | `2.28014e-05` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `1.43313e-05` | `2.09007e-05` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.17759e-05` | `3.10076e-05` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `2.43281e-05` | `3.28317e-05` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `8.08478e-06` | `1.12506e-05` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/amplitude/HistGradientBoostingRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00146077` | `0.00198454` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.126681` | `0.201806` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.0800121` | `0.134257` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.266872` | `0.564205` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0176262` | `0.0255339` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.239677` | `0.707389` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.0810616` | `0.145841` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0501669` | `0.0758641` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0785164` | `0.107151` | `models/paper_reference/rcim_track1/backward/hgbm_reference_models/onnx/phase/HistGradientBoostingRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `HGBM`
- implementation family: `HGBM`
- archived target count: `19`
- unique source runs: `10`
- unique source configs: `10`
- dataset snapshot manifest: `models/paper_reference/rcim_track1/backward/hgbm_reference_models/dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models/paper_reference/rcim_track1/backward/hgbm_reference_models/reference_inventory.yaml`
