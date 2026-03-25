# Periodic Feature Network

## Overview

This report documents the implemented `periodic_mlp` model, whose Python class is `PeriodicFeatureNetwork`.

This model sits between a plain feedforward baseline and a fully structured harmonic regressor:

- it injects periodic bias explicitly;
- but it still uses an MLP as the main nonlinear function approximator.

## Model Description

`PeriodicFeatureNetwork` is a feature-engineered neural network.

Instead of feeding only the raw angular position to an MLP, it first expands the angle into periodic harmonic features and then concatenates those features with the operating-condition channels.

The expanded feature vector is passed to a standard feedforward backbone.

So the model combines:

- explicit periodic representation;
- flexible nonlinear neural regression.

## Operating Principle

The model works in two stages.

Stage 1: periodic feature construction

- the raw angular position is converted to radians;
- `sin(k theta)` and `cos(k theta)` are generated up to the chosen harmonic order;
- optionally the normalized raw angular feature is also kept.

Stage 2: nonlinear regression

- the periodic features are concatenated with normalized operating-condition features;
- the resulting expanded feature vector is processed by an MLP.

Conceptually, the model says:

`first encode periodicity explicitly, then let the network learn the remaining nonlinear interactions`

## Conceptual Map

![Periodic feature network conceptual diagram](assets/2026-03-18_model_explanatory_diagrams/periodic_feature_network_model_diagram.svg)

The model can be read as:

```text
Input Point
  -> raw angle theta
  -> periodic expansion [sin(theta), cos(theta), ..., sin(K theta), cos(K theta)]
  -> optional raw normalized angle
  -> normalized condition features [speed, torque, temperature, direction]
  -> concatenation
  -> MLP
  -> scalar TE prediction
```

In repository terms:

```text
Raw angle for periodic basis
  + normalized condition channels
  -> expanded feature tensor
  -> FeedForwardNetwork
  -> TE
```

## Architecture Diagram

![Periodic feature network architecture diagram](assets/2026-03-18_model_explanatory_diagrams/periodic_feature_network_model_architecture_diagram.svg)

This second diagram makes the architecture more explicit:

- the periodic basis is built first;
- the operating-condition channels remain as standard inputs;
- all channels are concatenated;
- the expanded vector is passed through a dense MLP.

## Why This Model Exists

This model exists because a plain MLP may be forced to learn periodic structure inefficiently.

By inserting periodic features explicitly, the model receives a representation better aligned with TE behavior while preserving the flexibility of a neural network.

It is therefore a middle-ground model:

- more structured than `feedforward`;
- less rigid than `harmonic_regression`.

## Advantages

- Explicit periodic inductive bias.
- More expressive than a pure harmonic regressor.
- Can model nonlinear interactions between periodic structure and operating conditions.
- Still relatively simple and compatible with the existing training path.

## Disadvantages

- Less interpretable than coefficient-based harmonic regression.
- More parameters than a pure structured harmonic model.
- Still relies on MLP fitting quality and hyperparameter choice.
- Periodic structure is explicit only in the feature map, not in the output decomposition.

## Expected Behavior In The TE Context

This model is expected to be attractive when:

- periodicity clearly matters;
- but a purely harmonic model is too restrictive;
- operating conditions modulate TE in nonlinear ways.

It is a strong candidate when we want a structured prior without giving up neural flexibility.

## Python Model Implementation

The implementation lives in `scripts/models/periodic_feature_network.py`.

### `PeriodicFeatureNetwork.__init__(...)`

This constructor defines the expanded input representation and creates the internal MLP.

Main responsibilities:

- validate the TE input layout;
- validate positive harmonic order;
- compute the expanded input size from:
  - periodic features;
  - optional raw angle feature;
  - operating-condition features;
- build `self.feature_network` as a `FeedForwardNetwork`.

This means the periodic model is implemented as:

- handcrafted front-end feature map;
- standard MLP back-end.

### `build_periodic_feature_tensor(...)`

This function builds the periodic basis from the raw angle.

It:

- converts angle to radians;
- appends sine and cosine channels for each harmonic order.

Unlike `harmonic_regression`, these periodic features are not directly weighted and summed. They become input features for a downstream MLP.

### `forward_with_input_context(...)`

This is the repository-specific forward method used because the model needs both:

- raw angle for periodic expansion;
- normalized inputs for the remaining channels.

The function:

- extracts the raw angular position;
- optionally keeps the normalized raw angle;
- adds periodic features;
- appends normalized condition features;
- concatenates everything;
- forwards the expanded tensor through the internal MLP.

## Repository Integration

The model is registered in `scripts/models/model_factory.py` under `model_type == "periodic_mlp"`.

This lets the training workflow construct it directly from YAML.

## Training Workflow Overview

This model uses the same training script as the other structured-neural baselines:

- `scripts/training/train_feedforward_network.py`

At high level:

1. data is flattened into TE points;
2. normalization statistics are computed;
3. the periodic network is instantiated by the factory;
4. the regression module detects `forward_with_input_context(...)`;
5. training, checkpointing, validation, testing, and registry updates follow the standard pipeline.

## Training Logic Relevant To This Model

### `TransmissionErrorRegressionModule.forward_regression_model(...)`

This is the critical function for `PeriodicFeatureNetwork`.

The training module does not assume that every backbone only wants normalized inputs. Instead, it checks whether the model asks for contextual forwarding.

For this model, that matters because:

- periodic features must be built from the raw angle;
- the remaining channels are naturally passed in normalized form.

### `train_feedforward_network(...)`

The outer training workflow is unchanged relative to the feedforward baseline.

What changes is the backbone behavior:

- same optimizer family;
- same metrics;
- same output artifacts;
- different feature construction inside the model.

This is useful because improvements can be attributed more clearly to the modeling bias rather than to a different training framework.

## Practical Interpretation

`PeriodicFeatureNetwork` should be read as a compromise architecture:

- if the plain feedforward network is too generic;
- and the harmonic regressor is too rigid;
- this model is the natural middle option.

It explicitly respects periodic structure, but still leaves room for nonlinear residual behavior to be captured by the MLP.
