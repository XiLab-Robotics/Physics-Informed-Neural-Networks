# Periodic MLP Explicit Harmonic Basis

## Overview

This document plans a narrow model-configuration extension for the existing
`periodic_mlp` family. The goal is to let the periodic-feature MLP use the
same explicit harmonic index lists introduced for `harmonic_regression` and
`residual_harmonic_mlp` in commit `8526aa1c41b966e9b656e539cc1ba044ac13beef`,
without changing the pure `feedforward` baseline and without reclassifying the
model as a future `Fourier-Feature MLP`.

The current `PeriodicFeatureNetwork` already expands the physical angular
position into fixed `sin(k theta)` and `cos(k theta)` inputs before a standard
feedforward backbone. This change should only make the harmonic dictionary
configurable:

- omitted `harmonic_index_list` keeps the current contiguous `1..K` behavior;
- provided `harmonic_index_list` uses the selected non-negative harmonic
  indices, with `0` treated only as the existing DC/bias convention and not as
  duplicate `sin(0 theta)` / `cos(0 theta)` features;
- `FeedForwardNetwork` remains the raw-feature MLP baseline.

## Technical Approach

The implementation should reuse the validation semantics already established
by `HarmonicRegression.resolve_harmonic_index_list(...)` rather than
introducing a divergent parser. `PeriodicFeatureNetwork` should store the
resolved list and a device-aware tensor of positive harmonic multipliers, then
build periodic features from that tensor.

Context7 was checked before planning the PyTorch-specific buffer behavior.
PyTorch documentation confirms that `register_buffer(..., persistent=False)`
is appropriate for fixed non-parameter tensors that should move with the module
device but not appear in the serialized `state_dict`. This matches the current
`HarmonicRegression` implementation pattern for positive harmonic indices.

The architecture boundary is deliberately conservative:

- `feedforward` stays unchanged as the raw normalized-input MLP.
- `periodic_mlp` remains a feedforward MLP with fixed engineered periodic
  inputs.
- `Fourier-Feature MLP` remains future work for a more general Fourier-feature
  design, such as learned frequencies, broader encoding policy, or a distinct
  coefficient/head formulation.

No subagent is planned for this implementation. If a subagent becomes useful,
the subagent name, task boundary, and approval requirement must be recorded in
an updated technical document before launching it.

## Involved Components

- `scripts/models/periodic_feature_network.py`
  Add optional `harmonic_index_list` support, preserve the current contiguous
  default, and build periodic features from the resolved positive harmonic
  indices.
- `scripts/models/model_factory.py`
  Pass `model.harmonic_index_list` into `PeriodicFeatureNetwork` when present.
- `scripts/training/train_feedforward_network.py`
  Print the optional harmonic index list for `periodic_mlp` runs so campaign
  logs clearly distinguish contiguous-order and sparse-list variants.
- `scripts/models/check_harmonic_basis_configuration.py`
  Extend the smoke check to cover `periodic_mlp` default and explicit-list
  feature construction.
- `doc/reports/campaign_plans/`
  Required later only if this model change is followed by a training campaign.
- `doc/running/active_training_campaign.yaml`
  Read before campaign preparation or launch. The current state is `none`, so
  no protected campaign files are active for this code-change planning step.

## Implementation Steps

1. Confirm explicit approval of this technical document.
2. Add `harmonic_index_list` as an optional `PeriodicFeatureNetwork`
   constructor argument.
3. Reuse `HarmonicRegression.resolve_harmonic_index_list(...)` to preserve the
   established validation and default behavior.
4. Store positive harmonic indices and register the multiplier tensor as a
   non-persistent buffer.
5. Compute `expanded_input_size` from the number of positive harmonic indices
   rather than from `harmonic_order` directly.
6. Update `build_periodic_feature_tensor(...)` to iterate over the registered
   positive harmonic index tensor.
7. Pass the optional list through `create_model(...)` for `periodic_mlp`.
8. Print `Harmonic Index List` for `periodic_mlp` configurations during
   training startup.
9. Extend the harmonic-basis smoke check for the default `periodic_mlp` basis
   and an explicit sparse RCIM-style basis.
10. Run focused validation after implementation:
    `python -B scripts/models/check_harmonic_basis_configuration.py`.
11. Run Markdown QA on touched authored Markdown files before closing the
    task.
