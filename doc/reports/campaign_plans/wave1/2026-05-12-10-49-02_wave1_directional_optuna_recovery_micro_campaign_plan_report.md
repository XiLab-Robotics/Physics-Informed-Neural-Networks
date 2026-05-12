# Wave 1 Directional Optuna Recovery Micro Campaign Plan Report

## Overview

This is a lightweight validation campaign used to reproduce and fix the blocked
neural `Optuna` phase of the `Wave 1` directional best-hyperparameter search
workflow.

The production campaign already completed the bounded non-neural grid phase.
This micro-campaign exists only to validate launcher and study-runner recovery
before resuming the real neural study package.

## Objective

Prepare and execute a small, fast neural `Optuna` test package that:

- uses the same launcher and study runner as the production campaign;
- proves that the correct Python interpreter is used by spawned study
  processes;
- proves that `optuna` is available in the chosen runtime environment;
- completes at least one end-to-end study with persisted artifacts.

## Planned Scope

The micro-campaign should stay intentionally small:

- target one neural family-direction surface first;
- use a very small trial budget such as `1` to `3` trials;
- if needed, extend to one additional surface only after the first surface is
  green.

## Acceptance Criteria

The micro-campaign is considered successful only if:

- the launcher starts the neural study without `ModuleNotFoundError: optuna`;
- the study process exits with an explicit successful exit code;
- the study output root contains `study.sqlite3`, `trial_configs/`,
  `trial_results/`, `best_trial.yaml`, and `study_summary.yaml`;
- the corresponding training run writes the normal repository artifacts under
  `output/training_runs/<family>/...`.

## Hardware Policy

Use the lightest practical execution mode:

- single GPU slot if the neural runner still requires GPU-visible execution;
- otherwise a single local device path sufficient to validate the launcher and
  dependency contract;
- no broad parallelism for this micro-campaign.

## Execution Gate

Before execution:

1. the recovery technical document must be approved;
2. the micro-campaign package and launcher note must exist;
3. the intended Python interpreter path must be explicit in the launcher
   surface;
4. the validation run must remain clearly separated from the production
   campaign closeout.

## Expected Outcome

If this micro-campaign succeeds, the same fix can be applied to resume the
production neural study phase and complete the real campaign closeout.
