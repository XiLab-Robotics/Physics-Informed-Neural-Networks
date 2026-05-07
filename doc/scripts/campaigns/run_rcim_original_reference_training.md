# Run RCIM Original Reference Training

## Overview

This is the canonical unified launcher for the repository-owned RCIM original
paper-reference workflow.

Script:

- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`

Underlying training entrypoint:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`

Best-parameter registry helper:

- `scripts/campaigns/paper_reference/rcim_original/rcim_original_best_parameter_registry.py`

## Behavior

The launcher exposes one branch-aware and stage-aware operator surface:

- `-Branch Forward|Backward|Both`
- `-Stage Original|Retune|Eval|Export|LoadBest`
- `-NoEval`
- `-NoExport`
- `-BestParameterSummaryPath`
- `-RetuneGridSearchVerbose`
- `-RetuneCrossValidateVerbose`

Raw runtime artifacts are written under:

- `output/training_campaigns/rcim_original/forward/<run_instance_id>/`
- `output/training_campaigns/rcim_original/backward/<run_instance_id>/`

Persistent best-parameter entries are written under:

- `output/registries/program/rcim_original_best_hyperparameters.yaml`

Each executed stage also writes:

- `logs/<stage>.stdout.log`
- `logs/<stage>.stderr.log`
- `logs/<stage>.combined.log`

The launcher now runs the Python stage in unbuffered mode so these log files
are updated while the stage is still running instead of only after process
exit.
The shared launcher now prefers the resolved Conda environment-local
`python.exe` for training stages and falls back to `conda run` only when the
direct interpreter cannot be resolved.

Each campaign root writes:

- `launcher_summary.json`

## Stage Semantics

- `Original`
  - `forward`: use the recovered original built-in tuned parameter map, then
    run `Eval` and `Export` unless they are suppressed.
  - `backward`: print that no original paper backward tuned parameter map is
    available, then exit cleanly.
- `Retune`
  - run retuning first;
  - update the persistent YAML best-parameter registry;
  - continue automatically to `Eval` and `Export` unless they are suppressed.
- `Eval`
  - run only the held-out replay stage;
  - use `-BestParameterSummaryPath` if provided;
  - otherwise use the stored YAML registry if it covers the requested family
    surface.
- `Export`
  - run only the full-dataset export stage;
  - resolve parameters the same way as `Eval`.
- `LoadBest`
  - use `-BestParameterSummaryPath` if provided;
  - otherwise use the stored YAML registry if available;
  - if the stored registry does not cover the requested family surface, fall
    back automatically to `Retune`.

## Typical Usage

Run the original tuned forward branch:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_reference_training.ps1" `
  -Branch Forward `
  -Stage Original
```

Run one backward retune bundle with automatic eval and export:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_reference_training.ps1" `
  -Branch Backward `
  -Stage Retune
```

Run only one backward family through retune:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_reference_training.ps1" `
  -Branch Backward `
  -Stage Retune `
  -Families "SVR"
```

Run one backward family through retune with quieter progress output:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_reference_training.ps1" `
  -Branch Backward `
  -Stage Retune `
  -Families "SVR" `
  -RetuneGridSearchVerbose 1 `
  -RetuneCrossValidateVerbose 0
```

Run one forward tuned replay from the stored best-parameter registry:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_reference_training.ps1" `
  -Branch Forward `
  -Stage LoadBest
```

Run both branches in one operator call:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_reference_training.ps1" `
  -Branch Both `
  -Stage LoadBest
```

Preview only:

```powershell
powershell -ExecutionPolicy Bypass -File "scripts\campaigns\paper_reference\rcim_original\run_rcim_original_reference_training.ps1" `
  -Branch Forward `
  -Stage Original `
  -PrintOnly
```

## Notes

- The old forward and backward launcher files are still present as
  compatibility wrappers, but this unified launcher is now the canonical
  operator surface.
- Long `Retune` stages now emit live progress for:
  - split preparation;
  - `GridSearchCV` setup and start;
  - wrapper-level `cross_validate(...)`;
  - target-by-target post-search `cross_validate(...)`;
  - summary writing.
- The terminal keeps showing `[INFO]`, `[PROGRESS]`, `MODEL:`,
  `TRAINING START:`, `TRAINING END:`, and the scikit-learn `GridSearchCV`
  `Fitting ...` / `[CV] ...` progress lines.
- The combined log is the safest file to monitor during long retune runs
  because it preserves both stdout and stderr in arrival order.
- The default retune verbosity is now intentionally high so the slowest family
  searches expose frequent `GridSearchCV` and `[CV]` progress lines.
- Final curated model archives under
  `models/paper_reference/rcim_original/forward/` and
  `models/paper_reference/rcim_original/backward/`
  remain a later closeout step, not the live runtime root.
