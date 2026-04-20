# Dataset Split Export Script Rename

## Overview

This document covers the narrow rename of the current dataset-split export
helper from a `Wave 1`-specific filename to a more general repository-owned
name.

The goal is to keep the script reusable and make the local README wording more
generic, while preserving the current default behavior and command-line usage.

## Technical Approach

- Rename the script from `export_wave1_dataset_split.py` to
  `export_dataset_split.py`.
- Keep the current CLI behavior unchanged so existing usage remains obvious.
- Update repository-owned document references that still point to the old
  filename.
- Make the local README wording more generic by removing unnecessary `Wave 1`
  framing from the script naming and usage guidance.

## Involved Components

- `scripts/datasets/export_wave1_dataset_split.py`
- `scripts/datasets/export_dataset_split.py`
- `scripts/datasets/README.md`
- `doc/technical/2026-04/2026-04-20/README.md`
- `doc/README.md`

## Implementation Steps

1. Rename the dataset split export script to the generic target name.
2. Update repository-owned references to the new script path.
3. Rewrite the local dataset README so the script naming is generic.
4. Run Markdown warning checks on the touched Markdown scope.
5. Report completion without creating a commit unless explicitly requested.
