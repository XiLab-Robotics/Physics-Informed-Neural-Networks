# Recovered Original RCIM Pipeline Runner

## Overview

This note documents the repository-owned runner that makes the recovered RCIM
original workflow executable without editing the archived files under
`reference/rcim_ml_compensation_recovered_assets/`.

The runner is stored in:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_pipeline.py`

The copied recovered sources used by the runner are stored in:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/original_pipeline/`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/latest_snapshot/`

## What Is Actually Runnable

The copied recovered workflow is split into three stages:

1. dataframe creation;
2. prediction and export;
3. evaluation.

Current runnable status:

- prediction and export:
  runnable through the repository-owned wrapper using the copied
  `predictorML_v7.py` modules and the shipped recovered dataframe;
- dataframe creation:
  copied for audit fidelity, but not directly runnable because the recovered
  source imports `instance_v5.py`, which is not present in the archived trees;
- evaluation:
  copied for audit fidelity, but not directly runnable because the recovered
  source imports `instance_v4.py` and `instance_v5.py`, which are not present
  in the archived trees.

This split is intentional. The repository preserves the exact recovered files
for inspection while only claiming direct executability where the recovered
material is actually complete enough.

## Profiles

The runner exposes three recovered prediction profiles:

- `latest_snapshot_v17`
  Later narrowed snapshot with default-family export behavior.
- `original_v18_paper_family_bank`
  Original recovered `v18` surface restricted to the ten paper family-bank
  families.
- `original_v18_full`
  Original recovered `v18` surface including the code-only `ELM` branch, which
  requires `scikit-elm`.

## Usage

Print the honest stage-status summary:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_pipeline.py `
  --print-stage-status
```

Run one lightweight smoke prediction on the copied latest snapshot:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_pipeline.py `
  --profile latest_snapshot_v17 `
  --families DT `
  --output-suffix smoke_dt
```

Run the recovered original `v18` paper-family profile on two selected
families:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_pipeline.py `
  --profile original_v18_paper_family_bank `
  --families SVR,RF `
  --output-suffix paper_pair_probe
```

## Outputs

The runner writes immutable artifacts under:

- `output/validation_checks/paper_reimplementation_rcim_recovered_original_workflow/`

Each run contains:

- `run_summary.json`
- `original_style_output/`

The `original_style_output/` subtree preserves the original naming feel of the
recovered scripts, while the top-level immutable run folder keeps repository
artifact discipline.

## Practical Notes

- The default dataframe for all current profiles is the shipped recovered
  forward CSV:
  `latest_snapshot/dataFrame_prediction_Fw_v14_newFreq.csv`.
- The wrapper imports the copied `predictorML_v7.py` modules directly, so the
  trained behavior still comes from the recovered source copies rather than
  from a rewritten repository predictor.
- `latest_snapshot_v17` is the cleanest direct runnable path because it depends
  only on the shipped recovered dataframe and the copied prediction logic.
