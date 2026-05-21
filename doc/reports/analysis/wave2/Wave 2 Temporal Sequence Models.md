# Wave 2 Temporal Sequence Models

## Overview

`Wave 2` introduces temporal sequence baselines for TE curve prediction. The
new branch keeps the existing scalar TE regression objective, but changes the
model input from one point at a time to short centered windows of neighboring
curve samples.

The first implemented families are:

- `temporal_convolution`
- `gru_sequence`
- `lstm_sequence`

All three families remain bound to the official `Track 2` verification rule:
every accepted family must be checked as `global`, `Fw`, and `Bw`, then routed
back through the direction-aware matrix and visual curve reports.

## Model Descriptions

`temporal_convolution` is a compact one-dimensional convolutional network over
the sampled TE input sequence. It is the lowest-complexity temporal baseline
and is intended to test whether local context around a target angle improves
prediction.

`gru_sequence` is a recurrent gated model that reads the same sequence windows
with a `GRU` backbone. It adds learned recurrent memory while keeping fewer
state components than an `LSTM`.

`lstm_sequence` is the matched recurrent baseline with an `LSTM` backbone. It
uses hidden state plus cell state internally and is included by default so that
Wave 2 compares convolutional context, simpler gated recurrence, and the
standard recurrent cell-state family in the same campaign.

## Operating Principle

The shared datamodule now supports two collation modes:

- `point`, preserving the original Wave 1 point-level batches;
- `sequence`, emitting rank-3 tensors shaped as batch, sequence, feature.

For Wave 2, each sampled curve is converted into overlapping windows. The
configured target point is the center of the window, so the model predicts the
TE target at the same angular neighborhood that it observes.

The regression module still normalizes input and target tensors with the
existing train-split statistics. Broadcasting keeps the same normalization
contract valid for rank-3 sequence inputs.

## Project Context

Advantages:

- tests whether neighboring angular samples carry useful local TE context;
- keeps the existing target, loss, optimizer, metrics, and registry contracts;
- preserves the direction-aware `Track 2` comparison rule;
- keeps the first temporal branch small enough to debug before heavier
  sequence models are considered.

Disadvantages:

- recurrent families are less inspectable than static harmonic and residual
  harmonic baselines;
- sequence batching increases memory use relative to point-level training;
- later TwinCAT deployment will require additional scrutiny before a recurrent
  model can be accepted as the practical compensation path.

## Implemented Components

Python files:

- `scripts/models/temporal_sequence_network.py`
- `scripts/models/model_factory.py`
- `scripts/models/__init__.py`
- `scripts/training/transmission_error_datamodule.py`
- `scripts/training/shared_training_infrastructure.py`
- `scripts/training/train_feedforward_network.py`

Model classes and functions:

- `TemporalConvolutionNetwork`
- `RecurrentSequenceNetwork`
- `resolve_sequence_readout_tensor`
- `extract_sequence_tensor_from_curve_sample`
- `collate_transmission_error_sequences`

Factory model types:

- `temporal_convolution`
- `gru_sequence`
- `lstm_sequence`

Configuration root:

- `config/training/hydra/wave2/`
