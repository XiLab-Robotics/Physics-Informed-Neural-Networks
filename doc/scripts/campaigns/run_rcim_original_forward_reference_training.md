# Run RCIM Original Forward Reference Training

## Overview

This launcher is now a compatibility wrapper around the unified RCIM original
reference launcher.

Script:

- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.sh`
- canonical unified launcher:
  `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`

Underlying training entrypoint:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`

## Behavior

The wrapper delegates to the unified launcher with:

- `-Branch Forward`
- `-Stage Original`

That means it still runs the original tuned forward replay and then chains:

1. `Eval`
2. `Export`

Raw runtime artifacts are still written under:

- `output/training_campaigns/rcim_original/forward/<run_instance_id>/`

Each stage writes:

- `logs/<stage>.stdout.log`
- `logs/<stage>.stderr.log`
- `logs/<stage>.combined.log`

`combined.log` is the main persistent live-log surface and mirrors the terminal
output. `stdout.log` is kept as a compatibility mirror of the same live stream;
`stderr.log` is retained for launcher metadata and completion compatibility.

The launcher summary is written to:

- `launcher_summary.json`

## Typical Usage

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_forward_reference_training.ps1"
```

Canonical unified equivalent:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_reference_training.ps1" `
  -Branch Forward `
  -Stage Original
```

Preview only:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_forward_reference_training.ps1" -PrintOnly
```

Linux Bash equivalent:

```bash
bash scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.sh
```

Linux dry run without launching training:

```bash
bash scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.sh \
  --families SVR \
  --print-only
```

Limit the family subset:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_forward_reference_training.ps1" `
  -Families "SVR,MLP,RF"
```

## Notes

- The launcher mirrors the Python stage output to the terminal and to the stage
  log files so live progress and later diagnostics use the same stream content.
- New operator-facing stage names now live in the unified launcher:
  `Original`, `Retune`, `Eval`, `Export`, and `LoadBest`.
- Curated final model archives under
  `models/paper_reference/rcim_original/forward/`
  are a later closeout step, not the live runtime root.
