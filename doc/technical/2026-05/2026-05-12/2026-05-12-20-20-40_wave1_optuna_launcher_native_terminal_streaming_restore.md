# Wave 1 Optuna Launcher Native Terminal Streaming Restore

## Overview

The current `Wave 1` directional best-hyperparameter launcher restores the
`Optuna` execution path correctly, but it redirects child-process `stdout` and
`stderr` to launcher log files.

This hides the native `PyTorch Lightning` progress bars from the terminal that
started the campaign. The requested behavior is to restore the earlier
interactive surface: the neural `Optuna` studies must show their native
Lightning progress output directly in the launching terminal while preserving
the recovery fixes already added for interpreter resolution, `Optuna`
availability preflight, and persisted-study resume.

The logging contract should not drop file-based traces. The desired result is a
`tee`-style surface where the main user-facing stream is the live terminal
output and the same study output is also preserved under the launcher log files
for later inspection.

The launcher must also remain interruptible from the same terminal. The
current detached child-process pattern makes `CTRL+C` ineffective for stopping
the live neural study batch. The restored interactive launcher must propagate
user interrupts so the running `Optuna` study process can be stopped from the
same console session.

## Technical Approach

The launcher should keep the current study orchestration and environment
resolution logic, but change the neural-study execution surface from detached
background child processes with redirected logs to terminal-visible execution
with mirrored log persistence.

The implementation should:

- preserve the resolved canonical Conda interpreter path;
- preserve `Optuna` preflight and `-SkipGridPhase`;
- preserve persisted-study resume behavior;
- restore direct terminal streaming for `stdout` and `stderr` from the neural
  study runner as the primary runtime surface;
- preserve file-based study logs by mirroring the streamed output into the
  existing launcher log files;
- allow the user to stop the active neural-study execution path with `CTRL+C`,
  with the interrupt propagated to the running study process;
- keep failure messages explicit enough that the user can still identify the
  failing study config and GPU slot.

The desired target behavior is the same terminal experience that existed before
the log-redirection recovery hardening, but without reintroducing the original
bootstrap failures, without losing the saved launcher logs, and without losing
interactive `CTRL+C` stop control from the caller terminal.

## Involved Components

- `scripts/campaigns/wave_1/run_wave1_directional_best_hyperparameter_search_campaign.ps1`
- `doc/scripts/campaigns/run_wave1_directional_best_hyperparameter_search_campaign.md`
- `doc/README.md`
- `doc/technical/2026-05/2026-05-12/README.md`

## Implementation Steps

1. Refactor the `Wave 1` HPO launcher so neural `Optuna` studies stream their
   native console output to the caller terminal while also mirroring that
   output into launcher log files.
2. Refactor the launcher execution path so `CTRL+C` from the caller terminal
   stops the active neural `Optuna` study process instead of leaving detached
   child processes running.
3. Keep the current interpreter-resolution and `Optuna` preflight logic intact.
4. Update the launcher note so the runtime logging and interrupt behavior
   match the real script behavior.
5. Run scoped Markdown QA on touched documentation.
6. Report completion and wait for explicit commit approval before creating any
   Git commit.
