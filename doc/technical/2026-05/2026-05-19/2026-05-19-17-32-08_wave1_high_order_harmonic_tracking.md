# Wave 1 High-Order Harmonic Tracking

## Overview

The `TE Curve Verification Pipeline` curve plots show that the current `Wave 1` direct-TE models
smooth several transmission-error oscillations that are visibly present in the
original TE curves. This is especially clear when comparing the direct `Wave 1`
predictions with the `RCIM Model-Bank Reproduction` paper-faithful harmonic-wise model banks, where
the FFT-style separation lets different harmonic components be represented with
their own amplitudes and phases.

The immediate goal is to open a controlled `Wave 1` follow-up branch that tests
whether richer harmonic bases improve direct TE curve tracking for
`harmonic_regression` and `residual_harmonic_mlp` before broader temporal or
new architecture work is started.

## Technical Approach

The current `harmonic_regression` implementation uses a contiguous harmonic
order parameter `K`: it builds a bias term plus `sin(k theta)` and
`cos(k theta)` for every harmonic `k` from `1` through `K`. The current
`residual_harmonic_mlp` reuses that same structured branch and then adds a
feedforward residual branch.

The proposed change is to extend the harmonic-basis configuration so the
structured branch can be configured in two equivalent ways:

- `harmonic_order: K` keeps the existing backward-compatible contiguous basis
  from `1..K`.
- `harmonic_index_list: [...]` enables explicit sparse harmonic selections,
  with `0` treated as the bias/DC component and positive entries generating the
  corresponding sine/cosine pair.

The first experimental grid should compare:

- Existing baseline behavior, using the current `harmonic_order` values from
  the latest `Wave 1` directional runs.
- RCIM selected harmonic set: `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`.
- Dense paper-maximum set: `0..240`.
- Dense extended set: `0..360`.

The sparse RCIM set is the most directly paper-aligned test. The dense `0..240`
and `0..360` variants are useful stress tests, but they should be interpreted
carefully because high-order bases can overfit, amplify angular sampling issues,
and require regularization or validation focused on full-curve fidelity rather
than only aggregate scalar error.

## Involved Components

- `scripts/models/harmonic_regression.py`
  Extend the structured basis builder to accept an explicit harmonic-index
  list while preserving the current contiguous `harmonic_order` behavior.
- `scripts/models/residual_harmonic_network.py`
  Pass the optional harmonic-index list into the structured branch.
- `scripts/models/model_factory.py`
  Read the optional model configuration key and pass it to both affected model
  families.
- `scripts/training/train_feedforward_network.py`
  Keep configuration printing clear enough to distinguish contiguous order
  runs from sparse-list runs.
- `config/training/`
  Add follow-up campaign configurations only after this document and the
  campaign planning report are approved.
- `doc/reports/campaign_plans/`
  Create the required preliminary campaign plan before any training execution.
- `doc/running/active_training_campaign.yaml`
  Register the prepared campaign state before launch.
- `doc/reports/analysis/Track 2 Directional Model Comparison.md` and related
  `TE Curve Verification Pipeline` plotting outputs
  Use the comparison surface to judge whether the new models actually recover
  high-frequency TE curve content instead of only improving point metrics.

No subagent is planned for the initial implementation. If a subagent becomes
useful later, it must be proposed with a concrete scope and approved before
launch.

## Implementation Steps

1. Confirm approval of this technical document.
2. Create the required campaign planning report in
   `doc/reports/campaign_plans/` before preparing or launching any training.
3. Extend `HarmonicRegression` with an optional `harmonic_index_list` argument,
   including validation for unique, non-negative integer harmonics.
4. Preserve exact current behavior when `harmonic_index_list` is omitted.
5. Treat harmonic `0` as the existing bias/DC component and avoid adding
   duplicate `sin(0 theta)` or `cos(0 theta)` columns.
6. Pass the optional list through `ResidualHarmonicNetwork` and
   `create_model`.
7. Add focused tests or smoke checks that verify feature-count behavior for
   the current contiguous basis, the RCIM sparse set, `0..240`, and `0..360`.
8. Prepare a narrow campaign package comparing `harmonic_regression` and
   `residual_harmonic_mlp` across the selected harmonic banks, direction scopes,
   and current best learning-rate or stride settings.
9. Update launcher notes, active campaign state, and exact launch commands
   only after campaign-plan approval.
10. After execution, update the `TE Curve Verification Pipeline` curve comparison report and the
    relevant training-result registries if a new family-best model is promoted.
