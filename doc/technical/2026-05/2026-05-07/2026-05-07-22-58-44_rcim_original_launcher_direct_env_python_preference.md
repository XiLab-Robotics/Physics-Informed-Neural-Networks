# RCIM Original Launcher Direct Env Python Preference

## Overview

This document plans a narrow launcher-hardening follow-up for the recovered
original RCIM paper-reference training surface.

The current shared PowerShell launcher still executes training stages through
`conda run ...`, which has now been shown to suppress or delay live
stdout/stderr streaming on at least one operator workstation even when the
underlying Python training stage is healthy and already emits flush-safe
progress lines.

The goal of this pass is to make the shared launcher prefer the resolved
`python.exe` inside the target Conda environment for training stages, while
keeping `conda run` as a fallback when the environment-local interpreter cannot
be resolved.

## Technical Approach

The implementation will stay narrow and mechanical:

- keep the current launcher command surface unchanged;
- keep the current logging files and progress filtering unchanged;
- change only the process-launch strategy in the shared helper;
- reuse the existing environment-Python resolver already used by the
  best-parameter registry helper;
- prefer:
  - `<conda_base>/envs/<env_name>/python.exe`
- fall back to:
  - `conda.exe run -n <env> python ...`
  when the direct environment interpreter cannot be resolved;
- preserve unbuffered Python execution and the current argument surface.

## Involved Components

- `scripts/campaigns/paper_reference/rcim_original/shared_rcim_original_launcher_helpers.ps1`
- `scripts/campaigns/paper_reference/rcim_original/run_rcim_original_reference_training.ps1`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/scripts/campaigns/run_rcim_original_reference_training.md`
- `doc/guide/project_usage_guide.md`

No subagent use is planned for this task.

## Implementation Steps

1. Update the shared launcher helper so training stages prefer the resolved
   environment-local `python.exe`.
2. Keep `conda run` as the fallback path when the direct interpreter cannot be
   found.
3. Update the relevant operator documentation to note the launcher preference.
4. Verify with at least one `-PrintOnly` launcher pass and one scoped runtime
   smoke that stage logs still work and the command preview remains readable.
