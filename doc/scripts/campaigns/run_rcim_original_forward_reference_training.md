# Run RCIM Original Forward Reference Training

## Overview

This launcher runs the repository-owned forward paper-reference workflow for
the recovered original RCIM training surface.

Script:

- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1`

Underlying training entrypoint:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`

## Behavior

The launcher orchestrates two stages under one campaign root:

1. `paper_eval`
2. `paper_export`

Raw runtime artifacts are written under:

- `output/training_campaigns/rcim_original/forward/<run_instance_id>/`

Each stage also writes:

- `logs/<stage>.stdout.log`
- `logs/<stage>.stderr.log`
- `logs/<stage>.combined.log`

The launcher summary is written to:

- `launcher_summary.json`

## Typical Usage

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_forward_reference_training.ps1"
```

Preview only:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_forward_reference_training.ps1" -PrintOnly
```

Limit the family subset:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_forward_reference_training.ps1" `
  -Families "SVR,MLP,RF"
```

## Notes

- The launcher keeps the full warning surface in log files even when the live
  terminal shows only progress-oriented lines.
- Curated final model archives under
  `models/paper_reference/rcim_original/forward/`
  are a later closeout step, not the live runtime root.
