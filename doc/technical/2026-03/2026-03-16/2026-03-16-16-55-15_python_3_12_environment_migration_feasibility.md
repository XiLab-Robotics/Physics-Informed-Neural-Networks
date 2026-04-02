# Python 3.12 Environment Migration Feasibility

## Overview

This document records the feasibility check that preceded the project migration from Python 3.10 to Python 3.12.

After the feasibility check was approved on March 16, 2026, the repository baseline and the main Conda environment were migrated in place.

The current validated environment state is:

- Conda environment: `standard_ml_codex_env`
- Active Python series: `3.12`
- Observed interpreter version in the environment: `3.12.12`
- Observed core stack:
  - `torch 2.10.0+cu130`
  - `lightning 2.6.1`
  - CUDA available: `True`

The repository baseline now documents Python 3.12 in the main setup instructions and in the original environment technical note.

## Technical Approach

The feasibility check should answer three distinct questions:

1. Is Python 3.12 supported by the main ML stack used in this repository?
2. Is there any project-local reason to stay on Python 3.10 for now?
3. If migration is technically possible, should the repository baseline actually change?

### Current Reason Python 3.10 Was Chosen

The original project baseline selected Python 3.10 as the conservative environment target for:

- PyTorch + Lightning stability on Windows;
- CUDA-enabled PyTorch wheel availability for the local workstation;
- lower risk for training, export, and future deployment workflows.

That was a pragmatic compatibility-first decision, not a claim that Python 3.10 is inherently better than 3.12.

### What Must Be Verified

The migration decision should be based on:

- official PyTorch support for Python 3.12 on Windows;
- official Lightning support for Python 3.12;
- practical package-resolution compatibility for the repository requirements;
- whether the local CUDA installation path still has a clean install story for the desired Python version.

### Expected Decision Logic

If:

- PyTorch supports Python 3.12 with the required CUDA wheel family;
- Lightning supports Python 3.12;
- the repository requirements install cleanly;
- the current project code has no obvious 3.10-only assumptions;

then Python 3.12 becomes a reasonable candidate for the new baseline.

If any of those checks fail or remain unclear, the repository should stay on Python 3.10 until a fully verified migration path exists.

### Actual Validation Outcome

The validation and migration were successful:

- a temporary `standard_ml_codex_env_py312` environment installed the repository requirements cleanly;
- the main `standard_ml_codex_env` environment was then upgraded in place to Python 3.12;
- the binary `pip` packages had to be rebuilt after the interpreter change, as expected for compiled wheels on Windows;
- the final environment passed direct import checks for the tracked stack;
- the main project CLI entry points still run correctly with `--help`.

The repository should therefore use Python 3.12 as the documented baseline going forward.

### Recommended Validation Scope

The practical validation should remain lightweight at first:

1. inspect official support information;
2. inspect the currently installed stack;
3. optionally create a temporary Python 3.12 environment;
4. attempt dependency installation or at least package resolution;
5. run smoke-test imports for:
   - `torch`
   - `lightning`
   - `torchmetrics`
   - `numpy`
   - `scipy`
   - `pandas`
   - `sklearn`
   - `matplotlib`
   - `onnx`
   - `fitz`
6. run a small command-level smoke test against one project script if installation succeeds.

This validation scope was sufficient to approve and execute the baseline migration.

## Involved Components

- `README.md`
  Main environment setup instructions now updated to Python 3.12.
- `doc/guide/project_usage_guide.md`
  User-facing guide aligned with the Python 3.12 environment baseline.
- `requirements.txt`
  Repository dependency baseline to test against Python 3.12.
- `doc/technical/2026-03/2026-03-10/2026-03-10-02-21-36-pytorch_lightning_environment_setup.md`
  Original environment baseline decision, updated after the approved migration.
- `standard_ml_codex_env`
  Current validated Python 3.12 environment.
- Temporary test environment such as `standard_ml_codex_env_py312`
  Validation environment used to confirm package and CUDA compatibility before the in-place migration.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. Wait for explicit user approval before modifying the documented environment baseline or repository setup instructions.
3. Verify official Python-version support for PyTorch and Lightning.
4. Inspect the currently installed project stack in `standard_ml_codex_env`.
5. If needed, create a temporary Python 3.12 validation environment and attempt installation of the repository requirements.
6. Record whether the installation path, imports, and basic project smoke tests succeed.
7. Present a recommendation on whether the repository should remain on Python 3.10 or migrate its documented baseline to Python 3.12.
8. After approval, migrate `standard_ml_codex_env` in place, rebuild the binary wheels, and re-run the smoke tests.
