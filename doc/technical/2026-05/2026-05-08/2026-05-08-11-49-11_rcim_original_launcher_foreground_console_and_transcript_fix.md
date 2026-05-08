# RCIM Original Launcher Foreground Console And Transcript Fix

## Overview

The current recovered-original RCIM unified PowerShell launcher still does not
match the behavior of the direct `python -u -B ... training_models.py` command
for long `Retune` stages.
The operator-facing failure mode is now precise:

- the launcher prints the early `[INFO]` and `[PROGRESS]` lines;
- it reaches `Fitting 5 folds for each of 48 candidates, totalling 240 fits`;
- it does not continue to show the native scikit-learn and joblib `[CV ...]`
  progress lines that are visible in the direct Python invocation;
- `Ctrl+C` does not interrupt the training surface as cleanly as the direct
  Python command.

This means the current relay implementation still interferes with the real
foreground-console behavior of the training process. The next fix must stop
wrapping the training child through a `subprocess.Popen(..., stdout=PIPE,
stderr=PIPE)` relay and instead preserve the native console attachment while
still producing readable persistent logs.

## Technical Approach

Replace the current Python console relay approach with a foreground console
execution path in the PowerShell shared launcher.

The fix will be guided by one invariant:

- the launcher path must behave as close as possible to the direct
  `python -u -B scripts/.../training_models.py ...` command.

The planned direction is:

1. remove the stage relay dependency from the active execution path;
2. execute the environment-local `python.exe` directly in the foreground from
   the launcher;
3. capture a persistent operator log using a console-compatible mechanism that
   does not re-pipe the child stdout and stderr through PowerShell or Python;
4. preserve the existing stage metadata and launcher summary flow;
5. re-test specifically for:
   - visible `[CV ...]` lines at `RetuneGridSearchVerbose 10`;
   - clean `Ctrl+C` interruption;
   - persistent stage log output that updates during the run.

If the split `stdout` and `stderr` mirroring contract cannot coexist with the
native foreground-console behavior, the implementation will explicitly degrade
the contract to an authoritative combined live transcript plus compatibility
side logs, while preserving the operator-visible progress and clean interrupt
semantics as the higher-priority requirements.

## Involved Components

- `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/rcim_original_console_relay.py`
- `doc/scripts/campaigns/run_rcim_original_reference_training.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/guide/project_usage_guide.md`

## Implementation Steps

1. Reproduce the broken launcher behavior again with a short `Backward/Retune`
   `SVR` probe and confirm the mismatch against the direct Python command.
2. Replace the active stage-launch path so the environment-local `python.exe`
   runs in true foreground-console mode without the current Python relay pipe
   layer.
3. Rework the stage logging contract to preserve an updating persistent log
   without sacrificing native `[CV ...]` progress visibility.
4. Re-test the launcher command and confirm that:
   - verbose `10` `[CV ...]` output remains visible;
   - `Ctrl+C` stops the run cleanly;
   - the stage log surface updates during execution.
5. Update the operator documentation to describe the corrected logging and
   interrupt behavior.
6. Run Markdown QA on the touched documentation scope and the relevant
   validation commands for the launcher code path.
