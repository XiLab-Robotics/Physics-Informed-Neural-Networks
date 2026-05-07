# RCIM Original Launcher Live Output And Ctrl+C Fix

## Overview

The unified recovered-original RCIM PowerShell launcher still has one critical
operator-facing defect in its shared execution wrapper.

When the operator launches a long `Retune` stage through:

- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`

the launcher now resolves the Conda environment-local `python.exe` correctly,
but the wrapper still fails to preserve the same live console behavior that is
observed when the training script is run directly with Python.

The confirmed symptoms are:

- the launcher prints the initial `[INFO]` and `[PROGRESS]` lines correctly;
- the launcher reaches `Fitting 5 folds for each of 48 candidates, totalling
  240 fits`;
- the launcher does not continue to surface the high-verbosity
  `GridSearchCV` worker lines such as `[CV ...] START ...` and
  `[CV ...] END ...`;
- `Ctrl+C` does not terminate the run cleanly from the PowerShell launcher,
  forcing manual process termination from Task Manager;
- the direct `python.exe -u -B ... training_models.py ...` command does expose
  the desired `[CV ...]` progress and remains the current diagnostic
  reference.

The issue is therefore no longer the training code itself. The remaining fault
surface is the shared PowerShell execution and log-capture strategy.

## Technical Approach

The fix will keep the current direct-environment Python preference, but it will
replace the current wrapper pattern that pipes the training process output
through PowerShell line interception.

The current behavior strongly suggests that the wrapper:

- interferes with the high-verbosity worker output emitted during
  `GridSearchCV`;
- changes foreground console semantics enough to break clean `Ctrl+C`
  propagation;
- preserves only part of the live operator signal even though the Python
  process itself is healthy.

The repair will therefore:

1. keep the training process as a direct foreground child of the launcher when
   possible;
2. remove the current output-capture pattern that appears to suppress or delay
   the joblib and scikit-learn worker lines;
3. preserve the same high-verbosity console surface seen in the direct Python
   command;
4. restore clean interactive interruption behavior with `Ctrl+C`;
5. continue to write stage log files in a repo-owned and operator-readable way.

The implementation must not change:

- the recovered-original RCIM ML protocol;
- the retune search space;
- the stage semantics of `Original`, `Retune`, `Eval`, `Export`, and
  `LoadBest`;
- the launcher CLI surface already documented for operators.

## Involved Components

- `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1`
- `doc/scripts/campaigns/run_rcim_original_reference_training.md`
- `doc/guide/project_usage_guide.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`

No subagent use is planned for this fix.

## Implementation Steps

1. replace the current shared PowerShell stage-execution wrapper with a launch
   strategy that preserves direct live console output and clean process
   interruption behavior;
2. keep the Conda environment-local `python.exe` path as the preferred
   execution surface, with fallback behavior only where strictly necessary;
3. verify that high-verbosity `Retune` runs now surface the same `[CV ...]`
   lines when launched through the PowerShell wrapper as when launched with the
   direct Python command;
4. verify that `Ctrl+C` cleanly stops the active launcher-managed training
   process chain;
5. update the launcher note and adjacent workflow documentation so the real
   operator behavior matches the documented behavior;
6. run Markdown QA on the touched documentation scope before closing the
   implementation pass.
