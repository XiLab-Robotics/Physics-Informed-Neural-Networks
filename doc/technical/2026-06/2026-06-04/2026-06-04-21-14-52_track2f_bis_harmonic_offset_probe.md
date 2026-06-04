# Track 2F-Bis Harmonic-Offset Probe

## Overview

This technical document prepares the next Track 2F follow-up branch after the
completed `sequential_residual_offset_probe` campaign and the clean-baseline
documentation update.

The completed Track 2F branch is useful as a non-harmonic control, but it does
not force the TE waveform shape through periodic or harmonic features. Track
2F-bis should therefore test whether an explicit harmonic or periodic shape
branch plus a separate causal offset branch restores curve shape while still
keeping a clean non-harmonic baseline in the same comparison frame.

The practical target remains continuous transmission-error compensation. The
model must predict TE from the same point-level operating inputs and, where a
sequence model is used, only from already available causal history. Track 2
curves remain an offline validation and promotion surface, not a future input
to the deployed model.

## Technical Approach

Track 2F-bis should be implemented as a compact, direction-parallel probe with
two model branches:

- clean control branch: retain a Track 2F-like
  `sequential_residual_offset_probe` candidate without harmonic forcing;
- harmonic-offset branch: add a new model type with an explicit harmonic or
  periodic shape prediction plus a separate causal offset or low-frequency
  residual prediction.

The first harmonic-offset architecture should stay close to existing local
code rather than opening a broad new family. The recommended structure is:

```text
final_te_prediction =
  structured_harmonic_shape_prediction
  + causal_offset_prediction
```

The structured branch should reuse the repository's `HarmonicRegression`
machinery with an explicit sparse `RCIM` harmonic index list first. Dense
harmonic banks can remain ablations, but the previous Wave 2C evidence says
they should not be the default first probe.

The offset branch should reuse the causal recurrent readout pattern from
`SequentialResidualOffsetNetwork`. The branch must remain unidirectional for
deployment discipline unless a specific non-deployable diagnostic run is
clearly labeled as such.

Initial training can still use the current pointwise normalized MSE so the
first code change stays narrow. The campaign should nevertheless log branch
diagnostics and later evaluate with Track 2 curve-first metrics. A later
approved step can add composite loss terms for pointwise error, centered-shape
error, mean-offset error, harmonic amplitude, and harmonic phase.

The campaign must preserve separate surfaces:

| Surface | Required branch |
| --- | --- |
| `global` | combined-direction candidate |
| `Fw` | forward-only candidate |
| `Bw` | backward-only candidate |

No scalar result may collapse these three surfaces into one winner.

## Involved Components

- `scripts/models/harmonic_regression.py`
- `scripts/models/residual_harmonic_temporal_sequence_network.py`
- `scripts/models/sequential_residual_offset_network.py`
- `scripts/models/model_factory.py`
- `scripts/models/__init__.py`
- `scripts/training/transmission_error_regression_module.py`
- `scripts/training/train_feedforward_network.py`
- `config/training/`
- `scripts/campaigns/track2/`
- `doc/scripts/campaigns/track2/`
- `doc/reports/campaign_plans/track2/`
- `doc/running/active_training_campaign.yaml`
- `doc/reports/analysis/te_modeling/Curve-First TE Training Strategy.md`
- `doc/reports/analysis/Training Results Master Summary.md`

No Codex subagent is planned for this implementation. If a subagent becomes
useful later, its name, scope, and approval requirement must be recorded before
launch.

## Implementation Steps

1. Create a preliminary Track 2F-bis campaign planning report under
   `doc/reports/campaign_plans/track2/` and wait for explicit approval before
   preparing runnable training entries.
2. Add a narrow harmonic-offset PyTorch model type, tentatively named
   `harmonic_residual_offset_probe`, that exposes:
   `structured_prediction_tensor`, `residual_offset_prediction_tensor`, and
   `prediction_tensor`.
3. Register the model in `model_factory.py` and `scripts/models/__init__.py`.
4. Extend branch diagnostic logging only if needed beyond the existing
   `structured_*`, `base_*`, and `residual_offset_*` metric hooks.
5. Prepare a campaign root such as
   `config/training/track2f_bis_harmonic_offset_probe/`.
6. Materialize queue YAMLs for `global`, `Fw`, and `Bw` for both:
   the clean Track 2F-like baseline and the harmonic-offset branch.
7. Create a dedicated PowerShell launcher under `scripts/campaigns/track2/`
   with both local and `-Remote` execution paths.
8. Create the matching launcher note under `doc/scripts/campaigns/track2/`.
9. Update `doc/running/active_training_campaign.yaml` with protected files,
   local command, and `-Remote` command.
10. Run compile, package validation, one-batch validation, and a focused smoke
    check before providing the final launch command.
11. Keep full Track 2 verification as a separate operator-launched refresh
    after the normal campaign closeout.
