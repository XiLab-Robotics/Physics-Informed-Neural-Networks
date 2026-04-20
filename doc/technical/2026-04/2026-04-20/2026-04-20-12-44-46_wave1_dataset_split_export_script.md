# Wave 1 Dataset Split Export Script

## Overview

This document proposes a repository-owned helper script that reconstructs the
canonical `Wave 1` dataset split exactly as used by the current training
pipeline and exports the resulting train, validation, and test partitions in a
colleague-friendly format.

The immediate use case is manual downstream work by a colleague who needs the
same `70/20/10` split, with the same randomization and seed, outside the
automated repository training flow.

## Technical Approach

- Reuse the existing `Wave 1` split logic from
  `scripts/datasets/transmission_error_dataset.py`, rather than re-inventing a
  new split rule.
- Read the canonical split parameters from
  `config/datasets/transmission_error_dataset.yaml`:
  - `validation_split: 0.2`
  - `test_split: 0.1`
  - `random_seed: 42`
- Preserve the current behavior exactly:
  - split on unique CSV file paths;
  - shuffle with the same Python `random.Random(random_seed)` logic;
  - assign `validation` first, then `test`, then the remaining files to
    `train`;
  - retain the directional labeling already used by the repository.
- Produce explicit exported artifacts that a colleague can inspect without
  reading repository code, ideally including:
  - one manifest for `train`;
  - one manifest for `validation`;
  - one manifest for `test`;
  - a compact summary file describing counts, percentages, and the seed.

## Involved Components

- `config/datasets/transmission_error_dataset.yaml`
- `scripts/datasets/transmission_error_dataset.py`
- new repository-owned export script under `scripts/datasets/`
- output artifact root for the exported split manifests
- `doc/README.md`
- `doc/technical/2026-04/2026-04-20/README.md`

## Implementation Steps

1. Create a small export script that loads the canonical dataset split config.
2. Reuse the repository split helper so the exported partitions match `Wave 1`.
3. Serialize train, validation, and test manifests in a simple handoff format.
4. Add a concise usage note in the script header or module docstring.
5. Run Markdown warning checks on the touched documentation scope.
6. Report completion and wait for user approval before any commit.
