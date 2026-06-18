# Wave 1 Directional Best Hyperparameter Grid Search Campaign

## Overview

The repository now has completed `Wave 1` directional winners for all `15`
family-scope surfaces:

- `5` base families;
- `global`, `Fw`, and `Bw` variants for each family.

The next requested step is to prepare a new hyperparameter-search pass that
starts from those retrained `Wave 1` directional winners and searches for
better hyperparameters separately for all `15` surfaces.

The user also asked for an execution strategy that uses as much GPU capacity as
possible so the campaign does not saturate the workstation CPU and make the
search path unusably slow.

## Technical Approach

The new campaign should be treated as a bounded, winner-centered directional
grid-search campaign rather than a fresh broad architecture sweep.

For each of the `15` current directional `Wave 1` winners, the campaign should:

1. resolve the current best artifact and training config from the family
   registries;
2. derive a controlled hyperparameter grid around that winner's current
   configuration;
3. preserve the directional data scope as fixed input contract:
   - `global`
   - `Fw`
   - `Bw`
4. run the search as a new campaign with fresh immutable run-instance ids and
   isolated output roots.

The execution strategy must be heterogeneous by family type.

Neural families can use GPU-backed training execution:

- `feedforward`
- `periodic_mlp`
- `residual_harmonic_mlp`

For those families, the preparation should prefer explicit GPU-oriented runtime
settings and launcher orchestration that distributes work across the available
GPU inventory instead of letting many CPU-heavy training workers accumulate on
the same machine.

Non-neural families remain effectively CPU-bound in the current repository
stack:

- `tree`
- `harmonic_regression`

Those searches should therefore be throttled explicitly on the CPU side rather
than pretending they can benefit from the same GPU policy. The goal is not
only "use GPU when possible", but also "avoid pathological CPU oversubscription
for the surfaces that cannot use GPU materially".

This means the final preparation should likely split the campaign into at least
two execution classes:

- GPU-preferred neural search runs;
- CPU-throttled non-neural search runs.

## Involved Components

- `doc/reports/campaign_plans/wave_1/`
- `scripts/campaigns/wave_1/`
- `doc/scripts/campaigns/`
- `config/training/wave1_directional_retraining/`
- `output/registries/families/*/latest_family_best.yaml`
- `output/training_runs/*`
- `scripts/training/shared_training_infrastructure.py`
- family-specific `Wave 1` training configs and trainers

## Implementation Steps

1. Create the campaign planning report for the `Wave 1` directional
   hyperparameter-search pass before any training execution.
2. Define the `15` candidate search surfaces from the current `Wave 1`
   directional winners:
   - `tree`
   - `tree_fw`
   - `tree_bw`
   - `residual_harmonic_mlp`
   - `residual_harmonic_mlp_fw`
   - `residual_harmonic_mlp_bw`
   - `feedforward`
   - `feedforward_fw`
   - `feedforward_bw`
   - `periodic_mlp`
   - `periodic_mlp_fw`
   - `periodic_mlp_bw`
   - `harmonic_regression`
   - `harmonic_regression_fw`
   - `harmonic_regression_bw`
3. Formalize bounded per-family hyperparameter grids anchored to the current
   best config of each directional surface instead of regenerating an
   unconstrained search space.
4. Prepare a new campaign config root, campaign YAML queue, launcher, and
   launcher note dedicated to this search campaign.
5. Encode an explicit hardware policy in the generated configs and launcher:
   - GPU-preferred execution for the neural families;
   - CPU-throttled execution for `tree` and `harmonic_regression`;
   - avoid broad host-level CPU saturation from excessive concurrent search
     workers.
6. Verify that the unrelated `Track 1` cancelled campaign remains untouched and
   that none of its protected files are modified by this `Wave 1` campaign
   preparation.
7. Stop after preparing the technical document in this turn, wait for explicit
   user approval, then implement the planning report and campaign package in
   the follow-up step.
