# RCIM Track 1 Backward ERT Reference Models

This archive stores the accepted `ERT` target-level winners for the
`backward` branch of the canonical original-dataset Track 1 benchmark surface.

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
| `fft_y_Bw_filtered_ampl_0` | `0` | `0.00346948` | `0.00414577` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\amplitude\ExtraTreesRegressor_ampl0.onnx` |
| `fft_y_Bw_filtered_ampl_1` | `1` | `2.06273e-05` | `2.92237e-05` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\amplitude\ExtraTreesRegressor_ampl1.onnx` |
| `fft_y_Bw_filtered_ampl_156` | `156` | `0.000109416` | `0.000432476` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\amplitude\ExtraTreesRegressor_ampl156.onnx` |
| `fft_y_Bw_filtered_ampl_162` | `162` | `8.52257e-05` | `0.000370452` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\amplitude\ExtraTreesRegressor_ampl162.onnx` |
| `fft_y_Bw_filtered_ampl_240` | `240` | `0.000135207` | `0.000485608` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\amplitude\ExtraTreesRegressor_ampl240.onnx` |
| `fft_y_Bw_filtered_ampl_3` | `3` | `2.62655e-05` | `3.50008e-05` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\amplitude\ExtraTreesRegressor_ampl3.onnx` |
| `fft_y_Bw_filtered_ampl_39` | `39` | `1.76074e-05` | `2.37344e-05` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\amplitude\ExtraTreesRegressor_ampl39.onnx` |
| `fft_y_Bw_filtered_ampl_40` | `40` | `2.412e-05` | `3.24177e-05` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\amplitude\ExtraTreesRegressor_ampl40.onnx` |
| `fft_y_Bw_filtered_ampl_78` | `78` | `3.64268e-05` | `5.1696e-05` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\amplitude\ExtraTreesRegressor_ampl78.onnx` |
| `fft_y_Bw_filtered_ampl_81` | `81` | `8.76046e-06` | `1.26104e-05` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\amplitude\ExtraTreesRegressor_ampl81.onnx` |

Accepted phase targets:

| Target | Harmonic | MAE | RMSE | Archived ONNX |
| --- | ---: | ---: | ---: | --- |
| `fft_y_Bw_filtered_phase_1` | `1` | `0.00158011` | `0.00213017` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\phase\ExtraTreesRegressor_phase1.onnx` |
| `fft_y_Bw_filtered_phase_156` | `156` | `0.106373` | `0.334748` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\phase\ExtraTreesRegressor_phase156.onnx` |
| `fft_y_Bw_filtered_phase_162` | `162` | `0.0626116` | `0.133295` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\phase\ExtraTreesRegressor_phase162.onnx` |
| `fft_y_Bw_filtered_phase_240` | `240` | `0.286918` | `0.743524` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\phase\ExtraTreesRegressor_phase240.onnx` |
| `fft_y_Bw_filtered_phase_3` | `3` | `0.0236435` | `0.0356001` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\phase\ExtraTreesRegressor_phase3.onnx` |
| `fft_y_Bw_filtered_phase_39` | `39` | `0.243882` | `0.849285` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\phase\ExtraTreesRegressor_phase39.onnx` |
| `fft_y_Bw_filtered_phase_40` | `40` | `0.0790123` | `0.107083` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\phase\ExtraTreesRegressor_phase40.onnx` |
| `fft_y_Bw_filtered_phase_78` | `78` | `0.0553777` | `0.124823` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\phase\ExtraTreesRegressor_phase78.onnx` |
| `fft_y_Bw_filtered_phase_81` | `81` | `0.0804235` | `0.125367` | `models\paper_reference\rcim_track1\backward\ert_reference_models\onnx\phase\ExtraTreesRegressor_phase81.onnx` |

Provenance summary:

- direction label: `backward`
- paper family: `ERT`
- implementation family: `ERT`
- archived target count: `19`
- unique source runs: `1`
- unique source configs: `1`
- dataset snapshot manifest: `models\paper_reference\rcim_track1\backward\ert_reference_models\dataset_snapshot_manifest.yaml`
- machine-readable inventory: `models\paper_reference\rcim_track1\backward\ert_reference_models\reference_inventory.yaml`
