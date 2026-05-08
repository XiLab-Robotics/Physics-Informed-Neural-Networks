# RCIM Original Launcher Process Relay And Console Attachment Fix

## Overview

The first launcher hardening pass did not resolve the actual failure mode seen
on the gaming workstation.

The new confirmed behavior is stricter than the previous diagnosis:

- the launcher resolves the correct environment-local `python.exe`;
- the launcher prints the `[INFO] Command | ...` line correctly;
- the launcher then returns control to the PowerShell prompt immediately;
- the operator does not receive the live Python progress lines;
- `Ctrl+C` still does not behave like the direct Python invocation because the
  launcher is no longer attached to the real long-running stage in the way the
  operator expects.

This means the remaining fault is not just stdout filtering.
The shared launcher still uses a process-relay strategy that breaks the
foreground attachment contract of the training stage on at least one Windows
machine.

The direct Python command remains the reference behavior:

- it stays attached to the active console;
- it shows the `[INFO]`, `[PROGRESS]`, `Fitting ...`, and `[CV ...]` lines;
- it allows normal interactive operator control.

## Technical Approach

The fix will stop trying to partially intermediate the native Python training
stage with a wrapper behavior that differs from a real direct console launch.

The goal is to make the PowerShell launcher behave as close as possible to this
reference:

- direct foreground execution of the resolved environment-local
  `python.exe -u -B ... training_models.py ...`

The repair will therefore focus on the following:

1. reproduce the exact failure mode locally from the launcher, not just from
   the direct Python command;
2. identify why the current PowerShell invocation returns to the prompt
   immediately on the affected machine;
3. replace the failing process-relay pattern with one that keeps the launcher
   attached to the real training process until completion or interruption;
4. preserve operator-visible live console output exactly as the direct Python
   training command exposes it;
5. preserve clean interactive interruption behavior;
6. keep compatibility log files only insofar as they do not interfere with the
   console attachment contract.

The implementation must not change:

- the recovered-original RCIM ML protocol;
- the family grids or cross-validation protocol;
- the existing launcher CLI surface;
- the branch/stage semantics already formalized for operators.

## Involved Components

- `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`
- `scripts/campaigns/paper_reference/rcim_original/rcim_original_console_relay.py`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_forward_reference_training.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_backward_reference_training.ps1`
- `doc/scripts/campaigns/run_rcim_original_reference_training.md`
- `doc/guide/project_usage_guide.md`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`

No subagent use is planned for this fix.

## Implementation Steps

1. reproduce the launcher failure locally with the same operator-facing
   `powershell -ExecutionPolicy Bypass -File ...` surface;
2. inspect and replace the remaining execution-relay pattern in the shared
   launcher helper;
3. verify that the launcher remains attached to the real stage instead of
   returning immediately to the prompt;
4. verify that the launcher now surfaces the same live console output as the
   direct Python invocation, including the verbose `GridSearchCV` worker
   messages;
5. verify that the operator can stop the attached run cleanly with `Ctrl+C`;
6. update the operator-facing docs to describe the final, real behavior;
7. run Markdown QA on the touched documentation scope before closing the pass.
