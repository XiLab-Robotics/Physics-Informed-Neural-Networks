# Remote Exact-Paper SSH Runtime Smoke Stabilization

## Overview

The `SVR` exact-paper `GridSearchCV` path is now healthy on the local
workstation, including the high-throughput `24`-core profile intended for the
LAN node. The remaining blocker is the SSH/noninteractive remote execution
chain: the smoke campaign reaches the remote workstation, spawns the remote
`python` and `loky` worker processes, but still does not complete reliably or
return a synchronized validation bundle.

This document scopes the next stabilization pass to the remote runtime path
only. The scheduled `Track 1` `SVR` reference-grid repair campaign remains in
`prepared` state and must not be relaunched until the smoke campaign closes
end-to-end on the LAN node.

## Technical Approach

The stabilization pass will proceed in this order:

1. keep the scientific `SVR` exact-paper path unchanged because the local
   `24`-core validation already proves that `GridSearchCV` and the target
   configuration are valid;
2. use the remote smoke campaign as the only execution target until the LAN
   wrapper becomes reliable;
3. reduce the remote smoke to the smallest deterministic configuration that can
   still prove remote end-to-end correctness, including a single-core fallback
   profile when needed;
4. inspect the remote runtime under SSH directly so the failure surface can be
   attributed to one of:
   - SSH/noninteractive process ownership;
   - `conda run` streaming behavior;
   - `joblib`/`loky` remote parallel execution;
   - remote log/marker propagation;
   - artifact finalization and sync-back;
5. only after the smoke campaign closes remotely with a real
   `validation_summary.yaml`, promote the validated runtime path back to the
   scheduled four-run campaign.

The remote hardware budget should remain aggressive for the real campaign:

- `grid_search_n_jobs: 24`
- `joblib_cpu_limit: 24`
- `grid_search_pre_dispatch: 24`
- `threadpool_limit: 1`

But the smoke campaign may temporarily use a lighter fallback profile when that
is the fastest way to prove whether the residual blocker is the remote runtime
transport itself or high-parallel `loky` execution under SSH.

## Involved Components

- `scripts/campaigns/run_track1_svr_reference_grid_search_repair_campaign_remote.ps1`
- `scripts/campaigns/run_track1_svr_reference_grid_smoke_campaign.ps1`
- `scripts/campaigns/run_track1_svr_reference_grid_smoke_campaign_remote.ps1`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `scripts/training/shared_training_infrastructure.py`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/2026-04-16_track1_svr_reference_grid_smoke_campaign/`
- `doc/scripts/campaigns/run_track1_svr_reference_grid_search_repair_campaign_remote.md`
- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Reproduce the remote smoke failure under the current wrapper and capture the
   exact remote state:
   remote `python` command line, worker processes, log growth, and artifact
   directory contents.
2. Introduce the smallest safe runtime adjustment needed to isolate the failing
   stage, starting with a single-core smoke fallback if the remote `24`-core
   path remains non-conclusive.
3. Harden the remote wrapper or remote smoke launcher so that the active stage,
   child process state, and failure exit are always explicit and synchronized.
4. Run the smoke campaign repeatedly until one remote execution closes with a
   real `validation_summary.yaml`, synchronized artifacts, and a clean wrapper
   exit.
5. Re-evaluate the scheduled four-run launcher only after the smoke campaign
   proves that the remote runtime path is trustworthy.
