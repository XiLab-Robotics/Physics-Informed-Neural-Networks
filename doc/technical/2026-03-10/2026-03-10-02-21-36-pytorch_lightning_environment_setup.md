# PyTorch Lightning Environment Setup

## Overview

This document defines the Python dependency baseline for implementing the neural network stack in PyTorch with PyTorch Lightning inside the `standard_ml_codex_env` Conda environment.

The objective is to:

- add a project-level `requirements.txt`;
- document a reproducible installation flow for new users;
- keep the environment compatible with future training, evaluation, and export utilities;
- configure the environment for NVIDIA GPU execution on Windows with CUDA-enabled PyTorch wheels.

This setup decision is aligned with the current repository direction:

- PyTorch is the main deep learning framework;
- PyTorch Lightning is the training orchestration layer;
- the workflow must remain compatible with future TwinCAT-oriented export and runtime simplification.

Current local hardware/toolchain observation:

- `nvcc --version` reports `Cuda compilation tools, release 13.1, V13.1.115` on March 10, 2026.

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

- keep Python at `3.12` in the Conda environment;
- keep the full Python dependency list tracked in `requirements.txt`, including `torch`;
- install the CUDA-enabled `torch` wheel explicitly from the official PyTorch index;
- install the remaining tracked dependencies with `python -m pip install -r requirements.txt`;
- verify installation through direct imports of `torch`, `lightning`, and the main scientific packages.

CUDA decision:

- the local CUDA Toolkit is `13.1`;
- the official PyTorch wheel index checked again on March 16, 2026 exposes `cu130` wheels for Windows and Python 3.12;
- the project will therefore align the installation with the local NVIDIA CUDA 13.x toolchain and use the official `cu130` index.

Planned installation command:

- `python -m pip install torch --index-url https://download.pytorch.org/whl/cu130`
- `python -m pip install -r requirements.txt`

If future project components require `torchvision` or `torchaudio`, they can be added later once they become actual repository dependencies.

## Involved Components

- `requirements.txt`
  Root dependency file for the repository.

- `README.md`
  Main onboarding and setup instructions for new users.

- `doc/technical/2026-03-10/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md`
  Technical decision record for this environment setup feature.

- `standard_ml_codex_env`
  Target Conda environment for dependency installation and validation.

## Implementation Steps

1. Create the technical document and register it in the main `README.md`.
2. Add the root `requirements.txt` with the agreed dependency list, including `torch`, and keep it aligned with the actual imported third-party libraries.
3. Update `README.md` with the exact setup commands for a new user:
   - create the Conda environment;
   - activate it;
   - upgrade `pip`;
   - install the CUDA-enabled `torch` wheel explicitly from the official PyTorch index;
   - install the remaining tracked dependencies from `requirements.txt`.
4. Install the dependencies into `standard_ml_codex_env`.
5. Run a lightweight verification step by importing the installed packages and printing their versions.
