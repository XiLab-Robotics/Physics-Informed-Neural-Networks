# Remote Exact-Paper Runtime Observability, Interruptibility, And Utilization

## Overview

The current remote exact-paper launcher now reaches the real runtime phase on
the LAN node, but three operator-critical defects remain:

- the terminal becomes visually silent after `REMOTE_RUN_START::R:\`, so the
  operator cannot tell whether the run is healthy, slow, or hung;
- `Ctrl+C` does not stop the full remote execution tree reliably enough for an
  operator-facing workflow;
- remote CPU usage looks too low for a heavy `GridSearchCV` run, so the launcher
  must expose and, where needed, control the remote utilization strategy more
  explicitly.

The goal of this fix is not to change the scientific workflow. The goal is to
make the remote exact-paper campaign operationally usable: observable, safely
interruptible, and explicit about how much of the remote workstation it is
actually using.

## Technical Approach

The fix will harden the remote wrapper around the already restored exact-paper
parity flow:

1. add a terminal-facing runtime heartbeat or compact progress status line that
   appears during long silent phases without polluting the scientific per-run
   log files excessively;
2. make `Ctrl+C` terminate the local SSH wrapper and the remote spawned process
   tree reliably, including the current `conda` and Python child processes;
3. surface remote utilization signals directly in the terminal, such as current
   target config, elapsed runtime, and recent CPU activity;
4. review the exact-paper search configuration path so the remote node uses the
   intended parallelism settings and does not silently underutilize the LAN
   workstation.

This work is still part of the approved remote exact-paper launcher repair. It
does not introduce a new training method or change the paper-faithful model
selection logic.

## Involved Components

- `scripts/campaigns/run_track1_svr_reference_grid_search_repair_campaign_remote.ps1`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`
- `doc/scripts/campaigns/run_track1_svr_reference_grid_search_repair_campaign_remote.md`
- `doc/running/active_training_campaign.yaml`

Protected campaign files expected to require modification:

- `scripts/campaigns/run_track1_svr_reference_grid_search_repair_campaign_remote.ps1`
- `doc/scripts/campaigns/run_track1_svr_reference_grid_search_repair_campaign_remote.md`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`

No subagent is planned for this implementation.

## Implementation Steps

1. Add a remote runtime heartbeat or compact progress status line after
   `REMOTE_RUN_START` so the operator sees ongoing life signs during long
   silent phases.
2. Improve `Ctrl+C` handling so the remote exact-paper process tree is stopped
   cleanly and predictably from the local terminal.
3. Inspect the current exact-paper parallelism settings and expose them in the
   launcher output so low-utilization behavior becomes diagnosable.
4. If the current remote run is underutilizing the node because of an explicit
   config bottleneck, adjust the repository-owned setting in the exact-paper
   workflow rather than relying on manual workstation tweaking.
5. Update the remote launcher note and keep the campaign bookkeeping aligned
   with the active run state.
