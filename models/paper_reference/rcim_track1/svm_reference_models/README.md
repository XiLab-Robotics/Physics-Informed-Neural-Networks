# SVM Reference Models

This archive stores the `19` canonical `SVM` reference model artifacts that
generate the currently accepted repository-owned `SVM` row in
`doc/reports/analysis/RCIM Paper Reference Benchmark.md`.

Important naming note:

- the paper family name is `SVM`;
- the repository implementation family is `SVR`;
- the archived ONNX files therefore retain the implementation-side `SVR_*`
  filenames.

Archive scope:

- `10` amplitude reference models for harmonics
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`;
- `9` phase reference models for harmonics
  `1, 3, 39, 40, 78, 81, 156, 162, 240`;
- phase harmonic `0` is intentionally excluded because it is not part of the
  `19`-model paper-facing `SVM` reference set requested for Tables `2-5`.

## Canonical Selection Rule

The benchmark `SVM` row is not sourced from one single validation run.

The canonical reference rule for this archive is:

1. choose the exact run whose target metrics match the accepted benchmark
   `SVM` cell values for that harmonic;
2. when several runs reproduce the same accepted metric pair, prefer the
   earliest stable canonical source run;
3. prefer the strict full-bank reference run
   `2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro`
   whenever later campaigns merely reproduce the same target result;
4. when a later `Track 1` repair or closure campaign introduced the accepted
   benchmark value, pin that later run explicitly instead of the older
   full-bank baseline.

## Source Surface

The canonical strict-reference baseline run is:

- validation run:
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/2026-04-10-19-10-37__exact_full_bank_strict_reference_post_hgbm_fix_strict_repro/`
- config:
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-10_exact_paper_model_bank_campaign/02_exact_full_bank_strict_reference.yaml`

Later `Track 1` `SVM` repair and closure runs contribute the harmonics whose
accepted benchmark values improved after the strict baseline:

- `2026-04-14-17-30-55__track1_svm_amplitude_repair_seed11_campaign_run`
- `2026-04-14-17-31-04__track1_svm_amplitude_repair_seed23_campaign_run`
- `2026-04-14-17-31-51__track1_svm_phase_repair_seed11_campaign_run`
- `2026-04-14-21-09-51__track1_svm_amplitude_full_closure_split15_campaign_run`
- `2026-04-14-21-10-28__track1_svm_phase_final_closure_split15_campaign_run`

## Training And Reconstruction References

Canonical training and validation code:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`

Canonical reconstruction inputs:

- dataframe source:
  `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv`
- recovered reference ONNX root:
  `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`

Search and fitting provenance:

- all archived entries come from repository-owned `SVR` exact-paper runs;
- the archive now stores target-level exact estimator parameters inside
  `reference_inventory.yaml` under `exact_estimator_params`;
- the run snapshots preserve dataset split, target scope, export settings, test
  size, random seed, and harmonic filter;
- when a config does not override the search block explicitly, the exact-paper
  workflow falls back to the repository default search resolver in
  `exact_paper_model_bank_support.py`;
- the archive now includes the extracted fitted Python estimators, so the
  accepted `SVM` row can be reloaded from Python without reconstructing ONNX
  surrogates or reopening the original campaign folders.

Large bundle note:

- the strict baseline run also produced
  `paper_family_model_bank.pkl`, but that bundle is `188.97 MB` and is not
  copied into this curated archive;
- the bundle remains referenced from its immutable validation artifact
  location instead.

## Inventory Files

- machine-readable inventory:
  `reference_inventory.yaml`
- dataset snapshot manifest:
  `dataset_snapshot_manifest.yaml`
- dataset snapshot copy:
  `data/filtered_dataframe_deg_le_35.csv`
- Python estimator archive:
  `python/amplitude/*.pkl`
  `python/phase/*.pkl`
- source-run reconstruction manifests:
  `source_runs/<run_instance_id>/split_manifest.yaml`
- source-run config and metadata snapshots:
  `source_runs/<run_instance_id>/training_config.snapshot.yaml`
  `source_runs/<run_instance_id>/run_metadata.snapshot.yaml`
- benchmark-facing canonical report:
  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

## Full Regeneration Coverage

The archive is now intended to support `100%` deterministic reconstruction of
the accepted repository-owned `SVM` benchmark row.

For each of the `19` canonical targets, the archive records:

- the accepted benchmark metrics;
- the canonical source validation run;
- the archived ONNX export path;
- the archived Python pickle path for the fitted estimator;
- the exact fitted estimator class and parameter dictionary;
- the filtered dataset snapshot hash;
- the feature list and target list;
- the train/test row counts and exact filtered row indices;
- the test size, random seed, harmonic filter, and target-scope mode;
- the source config snapshot and run metadata snapshot;
- the immutable source bundle path that contained the fitted estimator.

This means the repository now preserves both deployment-facing and
Python-facing access paths for the accepted `SVM` reference row:

- `onnx/` equivalent via `onnx/amplitude/*.onnx` and `onnx/phase/*.onnx`;
- Python-side fitted estimator access via `python/amplitude/*.pkl` and
  `python/phase/*.pkl`.
