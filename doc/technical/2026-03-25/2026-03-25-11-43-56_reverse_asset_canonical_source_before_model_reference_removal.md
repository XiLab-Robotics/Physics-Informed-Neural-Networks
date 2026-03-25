# Reverse Asset Canonical Source Before Model Reference Removal

## Overview

This document corrects the recently introduced asset-deduplication direction between:

- `doc/guide/<Model Name>/`
- `doc/guide/model_reference/<Model Name>/`

The previous asset-deduplication pass made `doc/guide/model_reference/<Model Name>/assets/` the canonical asset owner.

That direction is not aligned with the user's intended final documentation architecture. The user's stated target is to eventually remove the `doc/guide/model_reference/` subtree after the guide-content unification is complete.

Because of that final target, the canonical asset source must live on the side that will remain:

- `doc/guide/<Model Name>/assets/`

This pass therefore reverses the canonical asset ownership so the repository does not converge on an asset location that is planned for removal.

## Technical Approach

### 1. Make The Learning-Guide Asset Folders Canonical

The corrected canonical shared asset location for the implemented model families should be:

- `doc/guide/<Model Name>/assets/`

This applies at least to:

- `FeedForward Network`
- `Harmonic Regression`
- `Periodic Feature Network`
- `Residual Harmonic Network`

These folders should become the stable long-term home for the shared model diagrams if the repository intends to retire `doc/guide/model_reference/`.

### 2. Retarget The Current Links Back To The Guide Asset Paths

The latest asset-deduplication pass changed the learning guides and their `video_guide_package` figure references so they now point to:

- `doc/guide/model_reference/<Model Name>/assets/`

This pass should reverse those references so they again point to the guide-local assets under:

- `doc/guide/<Model Name>/assets/`

This keeps the surviving documentation branch self-contained.

### 3. Restore Or Copy The Asset Files Back Into The Guide Folders

Because the previous pass removed the guide-local duplicate SVG files, this correction pass must restore the required diagrams into the guide-local `assets/` folders before the repository can safely stop depending on `model_reference` assets.

The corrected workflow should therefore:

- repopulate the guide-local `assets/` folders from the current `model_reference` copies;
- verify that the learning-guide image paths resolve against the restored files.

### 4. Keep `model_reference` Temporarily Intact During The Reversal

This pass should not remove `doc/guide/model_reference/` yet.

Even if the final direction is to retire that subtree, the safe order is:

1. restore the guide-local assets;
2. retarget the active guide links;
3. confirm the guide-local assets are now authoritative;
4. only later, during the broader content-unification pass, decide how and when `model_reference` should be removed.

### 5. Limit This Pass To Asset Canonicalization Correction

This corrective pass should not yet merge the guide Markdown bodies with the model-reference Markdown bodies.

The scope should remain limited to:

- reversing the canonical asset owner;
- restoring the guide-local SVG files;
- updating the active learning-guide and video-guide references accordingly.

## Involved Components

- `doc/guide/FeedForward Network/`
- `doc/guide/Harmonic Regression/`
- `doc/guide/Periodic Feature Network/`
- `doc/guide/Residual Harmonic Network/`
- `doc/guide/model_reference/`
- `README.md`

Potentially affected supporting indexes or follow-up surfaces:

- `doc/README.md`
- the later guide-content unification work

## Implementation Steps

1. Confirm `doc/guide/<Model Name>/assets/` as the corrected canonical asset owner.
2. Restore the currently needed SVG files into each affected guide-local `assets/` folder.
3. Update the four learning guides so they again point to their guide-local assets.
4. Update the four `video_guide_package/video_guide_figure_reference.md` files so they again point to the guide-local assets.
5. Verify that no active learning-guide surface still depends on `doc/guide/model_reference/<Model Name>/assets/`.
6. Stop after the asset-canonicalization correction so the broader `model_reference` retirement can be handled in a dedicated later pass.
