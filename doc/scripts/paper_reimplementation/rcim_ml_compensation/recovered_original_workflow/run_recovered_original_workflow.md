# Recovered Original RCIM Workflow Note

## Overview

This note points to the reorganized recovered-original workflow surface under
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`.

The canonical runner is stored in:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py`

The canonical detailed usage guide is now the code-adjacent README:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`

The reorganized workflow is now split into:

- `dataframe_creation/`
- `training/`
- `evaluation/`

## Usage

Print the reorganized stage-status summary:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --print-stage-status
```

Run the canonical recovered-original training stage:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --stage training `
  --direction forward `
  --families DT `
  --output-suffix smoke_dt
```

Run the full forward chain:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/run_recovered_original_workflow.py `
  --stage all `
  --direction forward `
  --instances-path "C:\path\to\original_instance_csv_dir" `
  --output-suffix full_forward_rebuild
```

For detailed stage behavior, runtime assumptions, and code-level mapping,
use the code-adjacent README rather than this short note.
