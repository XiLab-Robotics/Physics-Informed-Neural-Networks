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
