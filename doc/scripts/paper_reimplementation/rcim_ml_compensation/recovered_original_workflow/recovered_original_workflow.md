# Recovered Original RCIM Workflow Note

## Overview

This note points to the rebuilt direct recovered-original workflow surface
under:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`

The canonical code-adjacent guide is:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`

The canonical direct entrypoints are:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluate_models.py`

The shared repo-owned operational helper is:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/workflow_runtime.py`

## Repository Role

This workflow is the recovered RCIM original pipeline made runnable inside the
repository without treating the reference archive itself as mutable source.
The implementation is intentionally literal or near-literal where possible:
the original dataframe-creation, training/export/tuning, and evaluation stages
remain visible, while repository-owned changes are limited to path handling,
CLI entrypoints, runtime-output roots, logging, compatibility fixes, and
documentation.

The faithful Track 1 reimplementation that uses this recovered pipeline as the
protocol reference is:

- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`

Its accepted forward/backward model archives and Tables `2`-`5` benchmark
surface are:

- `models/paper_reference/rcim_track1/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

## Short Usage

Create a backward dataframe:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py `
  --direction backward `
  --output-suffix bw_dataframe
```

Run the `v18` paper-style forward replay:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py `
  --mode paper_eval `
  --direction forward `
  --test-size 0.20 `
  --output-suffix v18_fw
```

Run the paper-reference export companion mode:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py `
  --mode paper_export `
  --direction forward `
  --output-suffix v18_export_fw
```

Run forward evaluation on a prepared prediction directory:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluate_models.py `
  --direction forward `
  --prediction-directory "C:\path\to\output_prediction\instV3.8_Fw_allFreq_def" `
  --output-suffix eval_fw
```

Use the code-adjacent README for the full structure, original-to-new file
mapping, runtime-output policy, and the detailed explanation of:

- `v17` export
- `v17` plus retuning
- `v18` paper-style replay
- `paper_export` for full-dataset artifact generation with tuned family parameters
- current `Fw` versus `Bw` coverage across dataframe, training, and evaluation
- the shared `data/original_pipeline_instances/` pickle-cache contract used by
  dataframe creation and evaluation, including the `--rebuild-instance-cache`
  override
- the paper-reference launchers under
  `scripts/campaigns/paper_reference/rcim_original/`, including the
  `output/training_campaigns/rcim_original/` artifact roots and persistent
  stage logs plus the unified `Forward|Backward|Both` and
  `Original|Retune|Eval|Export|LoadBest` operator surface
- tracked repository-owned cleanup differences versus the original reference root
