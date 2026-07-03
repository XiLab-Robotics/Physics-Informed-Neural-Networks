# Wave 2.2 Harmonic Temporal Hybrid Models

## Overview

`Wave 2.2` extends the completed `Wave 2.1` temporal branch by adding explicit
harmonic angle features to each timestep in the sequence window.

The first `Wave 2.1` campaign verified `temporal_convolution`, `gru_sequence`,
and `lstm_sequence` in the official `TE Curve Verification Pipeline` workflow, but did not promote
them over the current repository-owned `tree` baseline. `Wave 2.2` tests the
more targeted hypothesis that the temporal backbones need the same TE-specific
periodic prior used by selected `Wave 1` harmonic and periodic models.

## Model Descriptions

The first implemented hybrid families are:

- `periodic_temporal_convolution`
- `periodic_gru_sequence`
- `periodic_lstm_sequence`

All three families keep the existing `Wave 2.1` sequence-window contract. The
input remains a rank-3 tensor shaped as batch, sequence, feature. The model
extracts angular position from the first raw input feature at every timestep,
builds fixed sine and cosine harmonic features, appends the normalized
operating-condition features, and then feeds the expanded sequence into the
selected temporal backbone.

The first configuration tier uses the RCIM sparse harmonic list:

```text
[0, 1, 3, 39, 40, 78, 81, 156, 162, 240]
```

This keeps the feature expansion compact enough for a first campaign while
preserving the high-value harmonics used by the earlier harmonic tracking
work. Dense `240` or `360` harmonic bases remain later tuning options, not the
default entry point.

## Operating Principle

The hybrid model receives two views of the same sequence from the shared
regression module:

- the raw input sequence, used to read physical angular position in degrees;
- the normalized input sequence, used for the raw-angle option and all
  operating-condition features.

For every timestep, the hybrid wrapper builds:

- optional normalized raw angle;
- `sin(k theta)` and `cos(k theta)` pairs for each positive harmonic index;
- normalized input speed, torque, oil temperature, and direction flag.

The resulting expanded sequence is passed unchanged to one of the existing
temporal backbones. This preserves the `Wave 2.1` readout behavior and keeps the
new logic isolated to feature construction.

## Project Context

Advantages:

- combines temporal curve context with explicit TE harmonic structure;
- reuses the verified `Wave 2.1` datamodule, normalization, readout, and metric
  path;
- keeps the first hybrid branch inspectable before introducing residual
  harmonic temporal models;
- preserves the official `TE Curve Verification Pipeline` `global`, `Fw`, and `Bw` verification rule.

Disadvantages:

- recurrent variants remain less deployment-friendly than static harmonic or
  tree candidates;
- harmonic feature expansion increases the sequence feature dimension;
- dense harmonic sweeps may overfit or inflate parameter count and should be
  treated as a later campaign branch.

## Implemented Components

Python files:

- `scripts/models/periodic_temporal_sequence_network.py`
- `scripts/models/model_factory.py`
- `scripts/models/check_harmonic_basis_configuration.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/run_training_campaign.py`

Model classes and functions:

- `PeriodicTemporalSequenceNetwork`
- `build_periodic_feature_tensor`
- `build_expanded_sequence_tensor`

Factory model types:

- `periodic_temporal_convolution`
- `periodic_gru_sequence`
- `periodic_lstm_sequence`

Configuration files:

- `config/training/hydra/wave2/model_family/periodic_temporal_convolution.yaml`
- `config/training/hydra/wave2/model_family/periodic_gru_sequence.yaml`
- `config/training/hydra/wave2/model_family/periodic_lstm_sequence.yaml`

## Verification Status

Focused verification completed for the first forward-scope candidates:

- harmonic basis smoke check passed for all static and periodic-temporal
  families;
- Hydra composition passed for the three new `Fw` model-family profiles;
- validation setup passed for `periodic_temporal_convolution`,
  `periodic_gru_sequence`, and `periodic_lstm_sequence`.

The next operational step is a campaign package, not immediate training. The
campaign package should create the official preliminary campaign plan, materialize
all `9` `global` / `Fw` / `Bw` configs, add the launcher, update active campaign
state, and provide the exact launch command.
