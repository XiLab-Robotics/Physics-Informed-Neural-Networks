# RCIM Original Retune Progress Logging And Monitoring

## Overview

This document plans a narrow observability pass over the recovered-original
RCIM reference-training surface so the long-running `Retune` stage becomes
monitorable in real time without changing the historical nested search
protocol.

The current behavior is operationally weak for the slowest families, especially
`SVR`, because the launcher only receives sparse family-level progress, several
inner `print(...)` calls are still buffered, and the retune branch can spend
many hours inside `GridSearchCV(...)` plus repeated `cross_validate(...)`
passes before emitting any readable output.

The goal of this pass is to keep the historical compute protocol intact while
making the stage observable from both the terminal and the persisted log files.

## Technical Approach

The implementation will preserve the current retune workflow:

- `GridSearchCV(...)` remains in place.
- The historical post-search `cross_validate(...)` passes remain in place.
- The family ordering, grid contents, and evaluation/export chaining semantics
  remain unchanged.

The work will instead improve observability at three layers:

1. Python training-stage progress emission
   - add explicit progress banners around retune sub-phases:
     - training split preparation
     - grid-search start
     - grid-search end
     - global cross-validation start/end
     - per-target cross-validation progress
     - summary writing
   - ensure progress prints flush immediately so redirected stdout is updated
     continuously
   - add readable counters such as target index, target name, and expected
     target count

2. Launcher-side streaming and log persistence
   - keep the current shared PowerShell streaming wrapper
   - expand the progress-line matcher so the launcher surfaces the new Python
     progress lines directly in the terminal
   - keep writing `stdout`, `stderr`, and combined logs incrementally while the
     stage is running

3. Optional runtime verbosity controls
   - introduce narrow CLI/runtime controls for observability, not protocol
     changes
   - examples:
     - Python unbuffered execution
     - explicit retune-progress verbosity
     - optional `GridSearchCV(verbose=...)` integration when safe
   - these controls must not alter the actual search space or validation
     protocol

CUDA/GPU acceleration will not be treated as the primary fix in this pass.
The slowest reported branch is `SVR`, which remains CPU-bound in the current
scikit-learn retune protocol. Any GPU-related follow-up must therefore be
treated as family-specific optimization, not as the core solution to the
observability problem.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/guide/project_usage_guide.md`
- `doc/scripts/campaigns/run_rcim_original_reference_training.md`

No subagent use is planned for this task.

## Implementation Steps

1. Add fine-grained retune progress messages inside the recovered-original
   Python retune path without changing the nested training protocol.
2. Force timely flushing and unbuffered output so long-running phases update
   terminal and log files while still in progress.
3. Expand the shared launcher progress-line recognition so the new progress
   messages stay visible in the terminal instead of being counted only as
   suppressed lines.
4. Add any narrow observability flags needed by the unified launcher and pass
   them through to the training stage.
5. Update the recovered-original workflow README and launcher documentation
   with the new monitoring behavior and operator expectations.
6. Verify with at least one short retune-family smoke run that:
   - logs are non-empty during execution
   - terminal progress is readable
   - the final stage still closes normally
   - the historical retune outputs remain structurally unchanged
