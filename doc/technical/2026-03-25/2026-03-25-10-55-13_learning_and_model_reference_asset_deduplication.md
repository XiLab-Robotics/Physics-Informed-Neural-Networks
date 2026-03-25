# Learning And Model Reference Asset Deduplication

## Overview

This document proposes the first concrete deduplication step for the current overlap between:

- `doc/guide/<Model Name>/`
- `doc/guide/model_reference/<Model Name>/`

The immediate scope of this pass is limited to duplicated visual assets. The user identified the `FeedForward Network` case as the reference example, and the same duplication pattern is expected across the other implemented model families.

At the moment, the learning-guide folders and the model-reference folders both keep their own copies of the same per-model SVG diagrams. This creates unnecessary duplication and makes future diagram updates risk drifting across two physical copies of the same visual source.

The goal of this pass is to establish one canonical asset location per implemented model family before addressing the later guide-content unification.

## Technical Approach

### 1. Keep `model_reference` As The Canonical Asset Owner

The current model-reference folders already function as the permanent technical reference surface for each implemented model family.

For that reason, the preferred canonical location for shared per-model diagrams is:

- `doc/guide/model_reference/<Model Name>/assets/`

The corresponding duplicated diagram copies under:

- `doc/guide/<Model Name>/assets/`

should no longer be treated as independent sources.

### 2. Retarget Learning Guides To The Canonical Asset Path

The learning guides should be updated so they reference the canonical model-reference assets instead of repository-local duplicate copies.

For example, the current `FeedForward Network` learning guide should stop depending on:

- `doc/guide/FeedForward Network/assets/feedforward_model_diagram.svg`
- `doc/guide/FeedForward Network/assets/feedforward_model_architecture_diagram.svg`

and should instead reference the canonical assets under:

- `doc/guide/model_reference/FeedForward Network/assets/`

The same path-normalization strategy should then be applied to the other implemented model families that duplicate the same diagrams.

### 3. Remove The Duplicate Learning-Guide Copies Only After Link Updates

The learning-guide asset files should be removed only after all active Markdown references have been updated to the canonical shared asset location.

This avoids broken image links during the transition.

### 4. Keep The Scope Narrow In This First Pass

This pass should not yet merge or rewrite the learning-guide and model-reference Markdown bodies.

The scope is intentionally limited to:

- deduplicating per-model SVG assets;
- updating the learning-guide Markdown links;
- keeping the model-reference folders as the single visual source of truth.

The broader textual unification should be addressed in a later approved step.

## Involved Components

- `doc/guide/FeedForward Network/`
- `doc/guide/Harmonic Regression/`
- `doc/guide/Periodic Feature Network/`
- `doc/guide/Residual Harmonic Network/`
- `doc/guide/model_reference/`
- `README.md`

Potentially affected supporting indexes or documentation pages:

- `doc/README.md`
- `doc/guide/TE Model Curriculum/TE Model Curriculum.md`

## Implementation Steps

1. Confirm the canonical shared asset owner as `doc/guide/model_reference/<Model Name>/assets/`.
2. Update each affected learning guide so its image links point to the canonical shared assets.
3. Verify that the updated Markdown paths resolve correctly for all implemented model families.
4. Remove the duplicate SVG files from the learning-guide asset folders once the links are confirmed.
5. Update any active documentation index if it currently implies that the duplicate learning-guide copies remain authoritative.
6. Stop after the asset deduplication pass so the later guide-content unification can be reviewed separately.
