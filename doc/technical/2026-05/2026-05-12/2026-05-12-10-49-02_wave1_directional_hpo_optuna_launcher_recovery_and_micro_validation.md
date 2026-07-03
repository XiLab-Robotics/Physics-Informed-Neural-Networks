# Wave 1 Directional HPO Optuna Launcher Recovery And Micro Validation

## Overview

The mixed `Wave 1` directional best-hyperparameter campaign completed the
bounded grid phase (`90/90` runs) but failed before the neural `Optuna` studies
could execute.

The observed failure is not a late training crash. The launcher attempted to
start `run_optuna_neural_hpo_study.py`, but the spawned Python process did not
have `optuna` available. Current inspection also shows that the launcher
resolved `python` to `C:\Users\XiLabTRig\miniconda3\python.exe` instead of the
intended `pinns_env` interpreter.

This recovery scope must:

- repair the launcher/interpreter contract for neural `Optuna` studies;
- ensure the required dependency is actually available in the canonical env;
- run a lightweight reproducer campaign to verify the fix before resuming the
  full neural study phase;
- determine whether the full campaign can be closed out cleanly after recovery;
- only commit campaign artifacts, recovery fixes, and closeout outputs once the
  campaign is genuinely complete.

## Technical Approach

The recovery will be handled in three layers.

First, repair the neural study execution contract:

- make the launcher prefer an explicit environment-local Python path instead of
  an ambiguous bare `python`;
- improve failure reporting so the launcher emits a concrete exit code and
  interpreter path when a study process fails;
- keep the existing GPU-slot batching logic intact.

Second, validate the fix with a repository-owned micro-campaign:

- create a minimal Optuna test package for one or a few directional neural
  surfaces with a very small trial budget;
- launch it locally through the same PowerShell and Python surfaces used by the
  real campaign;
- iterate on the implementation until the study runner completes and writes the
  expected artifacts.

Third, resume the blocked production campaign:

- install or verify `optuna` inside `pinns_env`;
- relaunch the real directional neural study phase;
- confirm whether `15/15` directional surfaces now expose best hyperparameters,
  winner artifacts, and the required Python plus ONNX model outputs;
- if complete, run the formal campaign closeout and prepare the final commit.

## Involved Components

- `scripts/campaigns/wave_1/run_wave1_directional_best_hyperparameter_search_campaign.ps1`
- `scripts/training/run_optuna_neural_hpo_study.py`
- `scripts/training/optuna_hpo_support.py`
- `requirements.txt`
- `doc/reports/campaign_plans/wave_1/2026-05-11-19-41-11_wave1_directional_best_hyperparameter_search_campaign_plan_report.md`
- `doc/reports/campaign_plans/wave_1/*wave1_directional_optuna_recovery_micro_campaign_plan_report.md`
- `output/training_campaigns/wave1/directional_best_hyperparameter_search/`
- `output/training_runs/feedforward*`
- `output/training_runs/periodic_mlp*`
- `output/training_runs/residual_harmonic_mlp*`
- `output/registries/families/*`
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`
- campaign closeout scripts and report surfaces that will be selected after the
  recovery state is confirmed

## Implementation Steps

1. Confirm the exact failure mode from launcher logs and current interpreter
   resolution.
2. Update the launcher so neural study processes use the intended environment
   interpreter and emit stronger diagnostics.
3. Verify the canonical environment dependency state for `optuna` and align the
   repo setup surfaces if needed.
4. Prepare a lightweight neural Optuna micro-campaign and its planning report.
5. Launch the micro-campaign, inspect artifacts, and iterate until the launcher
   and study runner complete successfully.
6. Resume the real directional neural study phase of the blocked campaign.
7. Inspect whether all `15` directional surfaces now have best hyperparameters,
   winner checkpoints, and ONNX exports.
8. If the campaign is complete, prepare the closeout report, closure artifacts,
   and the final commit scope covering campaign outputs plus recovery fixes.
