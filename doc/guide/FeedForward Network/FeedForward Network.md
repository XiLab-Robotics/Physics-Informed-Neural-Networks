# FeedForward Network

## Overview

This learning guide explains the repository's `FeedForward Network` from a beginner-to-university perspective.

The goal is to show:

- what the model is;
- why it is the starting point for the TE architecture curriculum;
- how the computation works from input to prediction;
- how the implementation fits into the repository training workflow;
- why this model is the right baseline before moving to more structured architectures.

This guide is intentionally broader than the model-explanatory report.
It is written as a teaching document for readers who want to understand the architecture before reading the code.

## Model Description

The `FeedForward Network` is the simplest neural baseline currently implemented for TE regression.

It is a point-wise multilayer perceptron (`MLP`):

- each sample is treated independently;
- the model receives one TE point at a time;
- the output is a single scalar prediction.

In this repository, the model uses the point-wise TE representation built from:

- angular position;
- input speed;
- input torque;
- oil temperature;
- direction flag.

The model does not explicitly encode periodic structure.
It does not split the signal into analytical and residual components.
It simply learns a generic nonlinear mapping from inputs to TE.

## Operating Principle

The operating principle is standard nonlinear regression.

At a high level:

1. the dataset is flattened into point-wise samples;
2. the input channels are normalized using train-set statistics;
3. the MLP transforms the feature vector through stacked dense layers;
4. the final layer produces a scalar TE prediction;
5. loss and metrics are computed during training and evaluation.

The model therefore implements the mapping:

`x -> f_theta(x) -> TE`

where `f_theta` is a learned nonlinear function.

The important idea is that the model is flexible, but not structured.
It can learn correlations from data, but it must discover periodicity and operating-condition interactions implicitly.

## Conceptual Map

![FeedForward Network conceptual diagram](../model_reference/FeedForward%20Network/assets/feedforward_model_diagram.svg)

The conceptual reading is:

- input features describe a single TE sample;
- normalization prepares the data for stable training;
- the MLP learns layered feature combinations;
- the prediction is a scalar TE estimate;
- metrics are reported after denormalization so they stay physically meaningful.

Use this diagram to remember that the model is a generic nonlinear regressor, not a physics-aware decomposition.

## Architecture Diagram

![FeedForward Network architecture diagram](../model_reference/FeedForward%20Network/assets/feedforward_model_architecture_diagram.svg)

This diagram is the computational view of the same model.

The important architectural points are:

- the network is fully feedforward;
- information flows in one direction only;
- hidden layers are dense transformations;
- optional layer normalization and dropout can be inserted between dense layers;
- the output head is a single scalar regression layer.

The architecture is intentionally conventional because it serves as the reference baseline for the rest of the curriculum.

## Why This Model Exists

This model exists because the project needs a neutral, flexible, easy-to-train baseline.

Before adding explicit periodic structure, residual decomposition, or temporal memory, the repository needs to know how far a plain MLP can go on the TE task.

That makes the model useful for three reasons:

- it sets a minimum benchmark;
- it reveals how much gain later architectures actually provide;
- it provides a simple conceptual bridge from linear regression to neural networks.

## Advantages

- Very simple and easy to explain.
- Flexible enough to model generic nonlinear interactions.
- Cheap to experiment with compared with heavier models.
- A strong baseline for later structured architectures.
- Easy to integrate into the shared training pipeline.

## Disadvantages

- No explicit periodic prior.
- No explicit decomposition of structured and residual behavior.
- Less interpretable than harmonic models.
- May need more data to discover the same structure that a TE-aware model could encode directly.
- Can fit the data without revealing much about the underlying mechanism.

## Repository Implementation

The implementation is centered on these files:

- `scripts/models/feedforward_network.py`
- `scripts/models/model_factory.py`
- `scripts/training/train_feedforward_network.py`
- `scripts/training/transmission_error_regression_module.py`

### `scripts/models/feedforward_network.py`

This file contains the actual `FeedForwardNetwork` backbone.

Key pieces:

- `get_activation_module(...)`
  Resolves the configured activation name into the correct PyTorch module.

- `FeedForwardNetwork.__init__(...)`
  Builds the dense stack layer by layer.
  The constructor validates sizes and assembles:
  - linear layers;
  - optional layer normalization;
  - activation;
  - optional dropout;
  - final output head.

- `FeedForwardNetwork.forward(...)`
  Runs the input tensor through the assembled network.

The implementation is explicit and readable so the architecture can be inspected directly from the source.

### `scripts/models/model_factory.py`

The model is registered under `model_type == "feedforward"`.

This factory layer is what makes the architecture selectable from YAML and usable inside the shared training code.

### `scripts/training/train_feedforward_network.py`

This is the orchestration entry point.

It:

- reads the YAML configuration;
- resolves the output folder and runtime settings;
- builds the datamodule;
- instantiates the model through the factory;
- creates the Lightning training module;
- runs fit, validation, and test;
- saves the run-local report and metrics artifacts.

### `scripts/training/transmission_error_regression_module.py`

This file contains the shared regression logic.

For the feedforward baseline, the important responsibilities are:

- normalization of inputs and targets;
- loss computation;
- metric logging;
- denormalized evaluation output;
- checkpoint-aware validation and test flow.

## Training Workflow

The training workflow for this model is the standard structured-neural pipeline used in the repository.

At a high level:

1. TE curves are converted to point-wise samples;
2. train-set statistics are computed;
3. the model is instantiated from configuration;
4. the regression module handles normalization and loss;
5. the trainer performs optimization with validation monitoring;
6. the best checkpoint is reloaded;
7. final validation and test metrics are reported.

This is important because later architecture guides reuse the same outer workflow, even when the backbone changes.

## Practical Interpretation

In TE terms, the `FeedForward Network` is the "how far can we go with a generic nonlinear regressor?" baseline.

If it performs well, that tells us the task may not require strong structure.
If it performs poorly, that tells us the problem needs explicit periodic, residual, or temporal inductive bias.

That is why this model is the first guide in the architecture series.

## Summary

The `FeedForward Network` is the simplest implemented neural architecture in the TE program.

It is easy to train, easy to compare, and easy to understand.
It is also the reference point from which the rest of the architecture curriculum becomes meaningful.
