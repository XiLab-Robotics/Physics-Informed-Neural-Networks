# Run RCIM Original Backward Reference Training

## Overview

This launcher is now a compatibility wrapper around the unified RCIM original
reference launcher.

Script:

- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.sh`
- canonical unified launcher:
  `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`

Underlying training entrypoint:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`

## Behavior

The wrapper preserves the historical operator surface:

1. `Retune`
2. `PaperEval`

Internally it delegates to the unified launcher as:

- `Retune` -> `-Branch Backward -Stage Retune`
- `PaperEval` -> `-Branch Backward -Stage LoadBest`

`Retune` still writes the hyperparameter-search artifacts under:

- `output/training_campaigns/rcim_original/backward/<run_instance_id>/retune/`

The legacy `PaperEval` wrapper path now orchestrates:

1. `Eval`
2. `Export`

under:

- `output/training_campaigns/rcim_original/backward/<run_instance_id>/`

Each stage also writes:

- `logs/<stage>.stdout.log`
- `logs/<stage>.stderr.log`
- `logs/<stage>.combined.log`

`combined.log` is the main persistent live-log surface and mirrors the terminal
output. `stdout.log` is kept as a compatibility mirror of the same live stream;
`stderr.log` is retained for launcher metadata and completion compatibility.

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

Canonical unified equivalent:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_reference_training.ps1" `
  -Branch Backward `
  -Stage LoadBest `
  -BestParameterSummaryPath "C:\path\to\summaryBestParameter+_3.8_allFreq.csv"
```

Preview only:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_backward_reference_training.ps1" `
  -Stage PaperEval `
  -BestParameterSummaryPath "C:\path\to\summaryBestParameter+_3.8_allFreq.csv" `
  -PrintOnly
```

Linux Bash equivalent:

```bash
bash scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.sh \
  --stage Retune
```

Linux dry run without launching training:

```bash
bash scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.sh \
  --stage PaperEval \
  --families SVR \
  --print-only
```

## Notes

- When `-BestParameterSummaryPath` is provided, `PaperEval` and
  the downstream export stage load tuned family parameters from the retune
  summary CSV.
- The unified launcher also exposes the new direct stages:
  `Original`, `Retune`, `Eval`, `Export`, and `LoadBest`.
- Curated final model archives under
  `models/paper_reference/rcim_original/backward/`
  are a later closeout step, not the live runtime root.
