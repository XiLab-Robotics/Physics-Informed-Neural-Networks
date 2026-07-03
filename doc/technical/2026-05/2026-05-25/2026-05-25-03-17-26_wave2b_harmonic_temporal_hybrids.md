# Wave 2.2 Harmonic Temporal Hybrids

## Overview

Plan the `Wave 2.2` extension that combines the explicit harmonic structure of
selected `Wave 1` periodic models with the sequence context introduced by the
`Wave 2.1` temporal families.

The completed `Wave 2.1` campaign verified `temporal_convolution`,
`gru_sequence`, and `lstm_sequence` candidates in the official `TE Curve Verification Pipeline`
workflow, but did not promote them over the current repository-owned `tree`
baseline. The next modeling branch should therefore test whether the temporal
families were missing the TE-specific harmonic prior rather than simply more
sequence capacity.

This document only approves the design and implementation preparation. No
training campaign will be executed until a separate preliminary campaign plan
under `doc/reports/campaign_plans/` is created and explicitly approved.

No subagent use is planned for this task. If a subagent becomes useful, this
document must be updated with the proposed subagent name, task boundary, and
approval requirement before launching it.

## Technical Approach

Implement the first hybrid branch as periodic feature expansion applied at
each timestep before the existing temporal backbones.

The first implementation tier should add three model families:

- `periodic_temporal_convolution`;
- `periodic_gru_sequence`;
- `periodic_lstm_sequence`.

Each family should preserve the current `Wave 2.1` rank-3 sequence input
contract, using tensors shaped as `(batch, sequence, features)` for recurrent
families with `batch_first=True`. Context7 was checked for the PyTorch API
surface before planning this behavior: PyTorch recurrent layers accept
`(batch, seq, feature)` when `batch_first=True`, and fixed non-parameter
tensors should be registered as module buffers so they move with the module
device without becoming learned parameters.

The harmonic feature encoder should reuse the validation semantics already
established by `HarmonicRegression.resolve_harmonic_index_list(...)`:

- omitted `harmonic_index_list` keeps the contiguous `1..K` behavior;
- provided lists use explicit non-negative harmonic indices;
- harmonic `0` is treated as the existing DC/bias convention, not as duplicate
  `sin(0 theta)` / `cos(0 theta)` inputs;
- the initial campaign should prefer the RCIM sparse harmonic list before any
  dense `240` or `360` harmonic sweep.

The first tier should not implement a full residual harmonic temporal branch.
That more complex branch should remain a second tier, with names such as
`residual_harmonic_gru_sequence` and `residual_harmonic_lstm_sequence`, only
after the lighter periodic-temporal models show useful evidence.

Every hybrid family must preserve the repository direction rule:

| Surface | Training Scope | Evaluation Scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` | forward only | forward curves only |
| `Bw` | backward only | backward curves only |

Wave 2.2 candidates must be evaluated back through the official `TE Curve Verification Pipeline`
verification workflow. A model is not accepted only because its training MAE is
good; it must refresh the direction-aware matrix, visual reports, and official
`TE Curve Verification Pipeline` update ledger when promoted.

## Involved Components

- `doc/running/active_training_campaign.yaml`
  Current state is `none`, so no protected campaign files are active for this
  planning step.
- `doc/reports/analysis/model_development_waves/wave_2/Wave 2 Temporal Sequence Models.md`
  Existing explanatory surface for the temporal sequence families.
- `doc/reports/analysis/model_development_waves/wave_1/Wave 1 - Closeout Status.md`
  Closed static harmonic and periodic baseline context.
- `doc/reports/analysis/te_curve_verification_pipeline/01_official_decisions/official_model_verification_report/[2026-05-24]/track2_official_model_verification_report.md`
  Current official verification verdict for Wave 2.1 temporal candidates.
- `scripts/models/harmonic_regression.py`
  Source of the canonical harmonic index-list validation semantics.
- `scripts/models/periodic_feature_network.py`
  Source of the existing static periodic feature expansion.
- `scripts/models/temporal_sequence_network.py`
  Source of the temporal convolution, `GRU`, and `LSTM` sequence backbones.
- `scripts/models/model_factory.py`
  Required registry point for new model-family names.
- `scripts/models/check_harmonic_basis_configuration.py`
  Focused smoke check to extend for rank-3 periodic sequence inputs.
- `scripts/training/train_feedforward_network.py`
  Current shared training entry point for neural TE model families.
- `config/training/hydra/wave2/`
  Existing Wave 2.1 Hydra config root to extend or mirror for Wave 2.2.
- `doc/reports/campaign_plans/wave_2/`
  Required later for the campaign package before any training launch.
- `output/training_runs/`, `output/validation_checks/`,
  `output/training_campaigns/`, and `output/registries/`
  Required artifact targets after campaign execution.

## Implementation Steps

1. Confirm explicit approval of this technical document.
2. Inspect the current angle-feature ordering in the temporal datamodule output
   and confirm the angular-position column used by the existing periodic
   family.
3. Add a reusable harmonic feature-expansion helper that supports both rank-2
   static inputs and rank-3 sequence inputs without changing existing
   `periodic_mlp` behavior.
4. Add `periodic_temporal_convolution`,
   `periodic_gru_sequence`, and `periodic_lstm_sequence` model construction
   paths.
5. Preserve the existing temporal backbones and feed the expanded per-timestep
   feature tensor into them.
6. Pass `harmonic_order` and optional `harmonic_index_list` through
   `create_model(...)` for the new families.
7. Add Wave 2.2 Hydra model-family configs for `global`, `Fw`, and `Bw` surfaces.
8. Extend the harmonic-basis smoke check to cover explicit sparse harmonic
   expansion on rank-3 sequence inputs.
9. Run focused validation after implementation:
   `python -B scripts/models/check_harmonic_basis_configuration.py`.
10. Run a no-training setup validation or minimal smoke test for each new
    family before preparing the campaign package.
11. Create a preliminary campaign plan under
    `doc/reports/campaign_plans/wave_2/` before any full training execution.
12. For the first Wave 2.2 campaign, keep the run count narrow:
    three model families across `global`, `Fw`, and `Bw`, for `9` candidates.
13. After campaign approval and execution, route the results through:
    family and program registries, the training master summary, the official
    `TE Curve Verification Pipeline` matrix, collage report, overlay report, and update ledger.
