# Run RCIM Original Backward Reference Training

## Overview

This launcher runs the repository-owned backward paper-reference workflow for
the recovered original RCIM training surface.

Script:

- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1`

Underlying training entrypoint:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`

## Behavior

The launcher supports two operator stages:

1. `Retune`
2. `PaperEval`

`Retune` writes the hyperparameter-search artifacts under:

- `output/training_campaigns/rcim_original/backward/<run_instance_id>/retune/`

`PaperEval` orchestrates:

1. `paper_eval`
2. `paper_export`

under:

- `output/training_campaigns/rcim_original/backward/<run_instance_id>/`

Each stage also writes:

- `logs/<stage>.stdout.log`
- `logs/<stage>.stderr.log`
- `logs/<stage>.combined.log`

The launcher summary is written to:

- `launcher_summary.json`

## Typical Usage

Run the backward retune stage:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_backward_reference_training.ps1" -Stage Retune
```

Run the backward paper-eval plus export stage:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_backward_reference_training.ps1" `
  -Stage PaperEval `
  -BestParameterSummaryPath "C:\path\to\summaryBestParameter+_3.8_allFreq.csv"
```

Preview only:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_backward_reference_training.ps1" `
  -Stage PaperEval `
  -BestParameterSummaryPath "C:\path\to\summaryBestParameter+_3.8_allFreq.csv" `
  -PrintOnly
```

## Notes

- When `-BestParameterSummaryPath` is provided, `PaperEval` and
  `paper_export` load tuned family parameters from the retune summary CSV.
- Curated final model archives under
  `models/paper_reference/rcim_original/backward/`
  are a later closeout step, not the live runtime root.
