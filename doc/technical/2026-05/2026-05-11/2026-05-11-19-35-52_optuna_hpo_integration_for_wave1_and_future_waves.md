# Optuna HPO Integration For Wave 1 And Future Waves

## Overview

The user requested that the repository adopt `Optuna` as the preferred
hyperparameter-optimization surface instead of relying only on:

- explicit YAML campaign grids for neural families;
- sklearn-style `GridSearchCV` for every case.

This is motivated by both immediate and future needs:

- `Wave 1` now has `15` directional winner surfaces that need best-parameter
  refinement;
- future `Wave 2+` model families will likely make fixed exhaustive grids less
  efficient and less scalable;
- the neural families should benefit from a search workflow that remains
  natural for `PyTorch` and `Lightning` training instead of forcing them into
  an sklearn-centered retune wrapper.

## Technical Approach

The repository should promote `Optuna` into a first-class HPO layer for model
families that are trained through the native `PyTorch` / `Lightning` stack.

This does not mean every training surface should use the same search engine.
The correct split is:

1. keep sklearn-style bounded retune logic for the families that are already
   naturally CPU-bound and estimator-based:
   - `tree`
   - `harmonic_regression`
2. introduce `Optuna` as the canonical HPO engine for the neural families:
   - `feedforward`
   - `periodic_mlp`
   - `residual_harmonic_mlp`
3. make the `Optuna` integration reusable so later waves can onboard new
   neural or hybrid families without inventing a new ad hoc search pipeline.

The repository implementation should use `Optuna` in the standard study-based
way:

- one persisted study per family-scope search surface;
- trial parameters sampled inside an objective function;
- one training run executed per trial through the existing trainer stack;
- repository ranking metrics reported back to the study;
- optional early stopping or pruning support for neural runs when the monitored
  validation metric makes that safe and useful.

The `PyTorch Lightning` built-in `Tuner` is not a replacement for this. The
official Lightning support covers local utilities such as learning-rate finding
and batch-size scaling, but not a full repository-wide study engine equivalent
to `GridSearchCV`. `Optuna` is therefore the better fit for the neural search
surface.

The search state should be persistent and resumable, using a local study
storage backend instead of ephemeral in-memory state. This is important because
future waves and remote campaigns will likely need interrupted-resume behavior
and inspectable optimization history.

## Involved Components

- `requirements.txt`
- `scripts/training/`
- `scripts/campaigns/infrastructure/`
- `scripts/campaigns/wave_1/`
- `doc/reports/campaign_plans/wave_1/`
- `doc/scripts/campaigns/`
- `config/training/`
- future wave campaign-preparation and closeout surfaces

## Implementation Steps

1. Add `Optuna` as an explicit repository dependency and update the relevant
   usage surfaces accordingly.
2. Introduce one reusable repository-owned HPO support layer for neural model
   families that:
   - builds or loads an `Optuna` study;
   - defines the trial search space from repository config metadata;
   - launches one trial through the existing `Lightning` training stack;
   - records the canonical objective metric and the key artifact paths.
3. Keep `tree` and `harmonic_regression` on a bounded sklearn-like search path
   rather than forcing them through the new `Optuna` layer.
4. Use the new HPO layer to prepare the `Wave 1` directional best-parameter
   campaign for the `15` current winner surfaces, with `Optuna` applied to the
   three neural families across `global`, `Fw`, and `Bw`.
5. Preserve explicit GPU-preferred execution for neural trials and explicit
   CPU-throttled execution for the non-neural families.
6. Define the `Optuna` study and artifact layout so the same structure can be
   reused by `Wave 2+` families without redesigning the campaign machinery.
7. After implementation, generate the campaign planning report, the campaign
   package, the launcher, and the launcher note before any training execution.
