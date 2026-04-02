# Retroactive Model Explanatory Reports For Existing Structured Models

## Overview

This document defines the retroactive documentation work needed to bring the already implemented structured TE models into compliance with the newly approved model-explanatory-report rule.

The scope covers the currently implemented model families:

- `feedforward`
- `harmonic_regression`
- `periodic_feature_network`
- `residual_harmonic_network`

The goal is to create dedicated explanatory reports that make each model understandable at a glance, both conceptually and at code level.

## Technical Approach

The work will produce four dedicated model reports, one per implemented family.

Each report will include:

1. an accurate description of the model;
2. the operating principle and why the model belongs to its family;
3. a conceptual map or schematic textual network description;
4. the main strengths, weaknesses, and practical expectations in the TE context;
5. a technical explanation of the Python implementation.

Because the current four models use the same structured-neural training path, the reports will also include a training section whenever it materially helps explain how the model is actually trained in this repository.

This means:

- the `feedforward` report will explain the training workflow in detail because it is the baseline user-facing training path;
- the `harmonic_regression`, `periodic_feature_network`, and `residual_harmonic_network` reports will include a concise but explicit explanation of how they are trained through the same shared structured-neural workflow, with model-specific code notes where relevant.

The reports should be stored in a discoverable documentation location, aligned with the current analysis/report structure of the repository.

## Involved Components

The retroactive reports will be based on:

- `scripts/models/feedforward_network.py`
- `scripts/models/harmonic_regression.py`
- `scripts/models/periodic_feature_network.py`
- `scripts/models/residual_harmonic_network.py`

They will also reference the shared training path where relevant:

- `scripts/training/train_feedforward_network.py`
- `scripts/training/transmission_error_regression_module.py`
- `scripts/models/model_factory.py`

The new reports will be indexed from:

- `README.md`
- `doc/README.md`

## Implementation Steps

1. Create one explanatory report for `feedforward`.
2. Create one explanatory report for `harmonic_regression`.
3. Create one explanatory report for `periodic_feature_network`.
4. Create one explanatory report for `residual_harmonic_network`.
5. Ensure each report includes:
   - conceptual description;
   - operating principle;
   - schematic or conceptual map;
   - pros and cons;
   - Python implementation walkthrough.
6. Include the training explanation where it materially affects how the model is used in the repository.
7. Add the new reports to `README.md` and `doc/README.md`.
