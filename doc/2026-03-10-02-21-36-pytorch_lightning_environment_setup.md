# PyTorch Lightning Environment Setup

## Overview

This document defines the Python dependency baseline for implementing the neural network stack in PyTorch with PyTorch Lightning inside the `standard_ml_codex_env` Conda environment.

The objective is to:

- add a project-level `requirements.txt`;
- document a reproducible installation flow for new users;
- keep the environment compatible with future training, evaluation, and export utilities;
- preserve a CPU-first setup path that remains simple to reproduce on Windows.

This setup decision is aligned with the current repository direction:

- PyTorch is the main deep learning framework;
- PyTorch Lightning is the training orchestration layer;
- the workflow must remain compatible with future TwinCAT-oriented export and runtime simplification.

## Technical Approach

The environment setup will use:

- Conda for Python environment creation and activation;
- `pip` inside the Conda environment for Python package installation;
- a single `requirements.txt` file stored at repository root.

The dependency baseline will be organized around four groups:

1. Core Deep Learning
   - `torch`
   - `lightning`
   - `torchmetrics`

2. Scientific Computing And Data Handling
   - `numpy`
   - `scipy`
   - `pandas`
   - `scikit-learn`

3. Visualization And Logging
   - `matplotlib`
   - `tensorboard`

4. Configuration And Export Support
   - `pyyaml`
   - `onnx`

Planned installation strategy:

- keep Python at `3.10` in the Conda environment;
- install dependencies with `python -m pip install -r requirements.txt`;
- verify installation through direct imports of `torch`, `lightning`, and the main scientific packages.

The setup will assume a CPU-first default. If a GPU-specific installation is needed later, the project can add a separate documented path without changing the baseline onboarding flow.

## Involved Components

- `requirements.txt`
  Root dependency file for the repository.

- `README.md`
  Main onboarding and setup instructions for new users.

- `doc/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md`
  Technical decision record for this environment setup feature.

- `standard_ml_codex_env`
  Target Conda environment for dependency installation and validation.

## Implementation Steps

1. Create the technical document and register it in the main `README.md`.
2. Add the root `requirements.txt` with the agreed dependency list.
3. Update `README.md` with the exact setup commands for a new user:
   - create the Conda environment;
   - activate it;
   - upgrade `pip`;
   - install from `requirements.txt`.
4. Install the dependencies into `standard_ml_codex_env`.
5. Run a lightweight verification step by importing the installed packages and printing their versions.
