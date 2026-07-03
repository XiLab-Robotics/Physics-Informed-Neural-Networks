# Wave 2.3 Residual Harmonic Temporal Hybrid Models

## Overview

`Wave 2.3` introduces residual harmonic temporal hybrids for TE curve
prediction. The branch follows the positive `Wave 2.2` result, where explicit
sparse `RCIM` harmonic features improved recurrent temporal models, and tests a
stronger decomposition:

- a structured harmonic branch predicts the base TE shape;
- a recurrent temporal branch predicts the sequence-local residual;
- the final prediction is the sum of both outputs.

The first prepared families are:

- `residual_harmonic_gru_sequence`;
- `residual_harmonic_lstm_sequence`.

## Operating Principle

Each model receives the existing rank-3 Wave 2.1 sequence tensor with shape
batch, sequence, feature. The first feature remains physical angular position
in degrees, followed by normalized operating-condition features after the
shared training module applies normalization.

For each sequence window:

1. The configured readout timestep, initially `center`, is extracted from both
   the raw and normalized sequence tensors.
2. The readout raw angle and normalized operating conditions are passed through
   the structured `HarmonicRegression` branch.
3. The full normalized sequence window is passed through a recurrent residual
   branch.
4. The branch outputs are added to produce the normalized TE prediction.

This preserves the existing sequence-window contract while making the harmonic
base explicitly inspectable.

## Harmonic Basis Tiers

The first campaign compares three harmonic-basis tiers in one batch:

| Basis Tier | Harmonic Index Policy | Role |
| --- | --- | --- |
| `sparse_rcim` | `[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]` | continuity with Wave 2.2 |
| `dense_240` | explicit inclusive list `0..240` | paper-maximum dense stress test |
| `dense_360` | explicit inclusive list `0..360` | one-revolution dense stress test |

Dense tiers are materialized as explicit `harmonic_index_list` values so the
`0` DC convention remains unambiguous.

## Project Context

Advantages:

- keeps the TE harmonic prior as a separate structured branch;
- tests whether temporal recurrence is better used as residual correction than
  as direct harmonic-feature regression;
- preserves Wave 2.1 sequence data loading and Wave 2.2 direction-surface rules;
- exposes branch-level diagnostics for structured and residual predictions.

Disadvantages:

- dense harmonic tiers increase structured-branch parameter count;
- recurrent residual branches remain less PLC-friendly than static harmonic or
  tree candidates;
- dense tiers may overfit or slow campaign execution, so their value must be
  judged against sparse-tier results.

## Implemented Components

Python files:

- `scripts/models/residual_harmonic_temporal_sequence_network.py`
- `scripts/models/model_factory.py`
- `scripts/models/check_harmonic_basis_configuration.py`
- `scripts/training/run_training_campaign.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/campaigns/wave_2/prepare_wave2c_residual_harmonic_temporal_hybrid_campaign.py`

Model classes and functions:

- `ResidualHarmonicTemporalSequenceNetwork`
- `compute_auxiliary_output_dictionary`
- `resolve_readout_feature_tensor`

Factory model types:

- `residual_harmonic_gru_sequence`
- `residual_harmonic_lstm_sequence`

Configuration files:

- `config/training/hydra/wave2/model_family/residual_harmonic_gru_sequence.yaml`
- `config/training/hydra/wave2/model_family/residual_harmonic_lstm_sequence.yaml`
- `config/training/hydra/wave2/campaign_profile/wave2c_residual_harmonic_temporal_hybrid.yaml`

## Campaign Surface

The prepared campaign contains `18` queue files:

- `2` model families;
- `3` harmonic-basis tiers;
- `3` direction surfaces.

The campaign launcher is:

```powershell
.\scripts\campaigns\wave_2\run_wave2c_residual_harmonic_temporal_hybrid_campaign.ps1
```

Training remains operator-launched. The prepared package does not execute
training by itself.
