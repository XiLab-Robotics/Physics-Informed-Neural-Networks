# LGBM Reference Models

This archive stores the canonical `LGBM` Track 1 reference model artifacts that
reproduce the currently accepted repository-owned family row in
`doc/reports/analysis/RCIM Paper Reference Benchmark.md`.

Archive scope:

- `10` amplitude reference models for harmonics `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`;
- `9` phase reference models for harmonics `1, 3, 39, 40, 78, 81, 156, 162, 240`;
- phase harmonic `0` is intentionally excluded because it is not part of the Track 1 paper-facing `19`-model family archive.

## Canonical Selection Rule

The canonical reference rule for this archive is:

1. choose the exact run whose family-target metrics reproduce the currently accepted benchmark cell values for that target;
2. when several runs reproduce the same accepted metric pair, prefer the earliest stable canonical source run;
3. when a later Track 1 campaign introduced the accepted improvement, pin that later run explicitly instead of the older baseline;
4. when a later campaign merely reproduces the same accepted value, retain the earlier canonical source run.

## Source Surface

Current pinned source runs:

- `2026-04-10-17-15-30__exact_full_bank_diagnostic_continue_smoke_full_continue_after_fix`

Canonical reconstruction config paths represented in this archive:

- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-10_exact_paper_model_bank_campaign/01_exact_full_bank_diagnostic_continue.yaml`

## Training And Reconstruction References

Canonical training and validation code:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`

Canonical reconstruction inputs:

- dataframe source:
  `reference/rcim_ml_compensation_recovered_assets/code/latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv`
- recovered reference ONNX root:
  `reference/rcim_ml_compensation_recovered_assets/models/exact_onnx_paper_release`

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

The archive is intended to support deterministic reconstruction of the
accepted repository-owned `LGBM` benchmark row.

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

This means the repository preserves both deployment-facing and Python-facing
access paths for the accepted `LGBM` reference row:

- `onnx/` via `onnx/amplitude/*.onnx` and `onnx/phase/*.onnx`;
- Python-side fitted estimator access via `python/amplitude/*.pkl` and `python/phase/*.pkl`.
