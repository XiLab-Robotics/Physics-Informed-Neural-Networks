# Campaign Launcher Location Reorganization

## Overview

The recently introduced short campaign launcher is currently stored under `scripts/training/`.

That location is not the right long-term home if the repository will generate one launcher per campaign. `scripts/training/` should remain reserved for reusable training entry points and shared training utilities, not for campaign-specific convenience wrappers tied to one concrete config package.

This document defines the planned reorganization for campaign launcher wrappers so that future campaign launch commands remain discoverable without polluting the generic training-script namespace.

## Technical Approach

The repository should distinguish between:

1. generic runnable training entry points;
2. campaign-specific launch wrappers.

The preferred direction is:

- keep generic runners in `scripts/training/`, including `run_training_campaign.py`;
- move campaign-specific launchers to a separate launcher-oriented location, for example `scripts/campaigns/` or an equivalent campaign-launch namespace;
- keep launcher names explicit and campaign-scoped;
- preserve the same underlying runner, logging, queue handling, and artifact generation.

The main design rule is that a reader should be able to infer:

- `scripts/training/` -> reusable training logic;
- launcher folder -> curated commands that start specific approved campaigns.

## Involved Components

- `scripts/training/run_training_campaign.py`
- `scripts/campaigns/run_wave1_structured_baseline_recovery_campaign.ps1`
- future campaign-specific launcher wrappers
- `doc/scripts/training/run_training_campaign.md`
- `doc/scripts/campaigns/run_wave1_structured_baseline_recovery_campaign.md`
- `doc/guide/project_usage_guide.md`
- `README.md`
- `doc/README.md`

## Implementation Steps

1. Define the new canonical folder for campaign-specific launchers.
2. Move the existing Wave 1 recovery launcher into that new folder.
3. Update all documentation and usage examples to point to the new location.
4. Keep `scripts/training/` focused on generic reusable training scripts only.
5. Reuse the same launcher folder for future campaign-specific wrappers instead of placing them under `scripts/training/`.
