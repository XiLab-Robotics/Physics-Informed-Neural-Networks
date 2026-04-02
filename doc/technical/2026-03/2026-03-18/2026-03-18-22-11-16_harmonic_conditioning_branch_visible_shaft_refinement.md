# Harmonic Conditioning Branch Visible Shaft Refinement

## Overview

This document defines a final targeted refinement for `harmonic_regression_model_architecture_diagram.svg`.

The previous harmonic pass improved the internal flow-card spacing and removed unnecessary elbow routing, but one visible issue remains:

- the vertical connector from `Conditioning Path` to `Coefficient Vector` is now straight, but its visible shaft is still too short and reads mostly as an arrowhead.

The goal of this pass is to keep the branch straight while increasing the visible connector length so the branch clearly reads as a real upward connection.

## Technical Approach

### 1. Increase The Conditioning-Branch Shaft Length

The current straight branch is drawn as a short vertical arrow:

- starting at the top of `Conditioning Path`;
- ending just below the bottom of `Coefficient Vector`;
- with a span that is still visually too small.

This pass should:

- increase the vertical gap between the top of `Conditioning Path` and the bottom of `Coefficient Vector`;
- or otherwise reposition the branch card just enough to expose a longer visible shaft;
- preserve the straight vertical routing introduced in the previous pass.

### 2. Preserve The Improved Harmonic Layout

This refinement should not reintroduce:

- internal flow-card overlap;
- unnecessary elbow routing;
- canvas crowding in the lower region.

The adjustment should stay minimal and local to the conditioning branch geometry.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for the harmonic architecture conditioning-branch placement;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/harmonic_regression_model_architecture_diagram.svg`
  which will be regenerated.

## Implementation Steps

1. Increase the visible shaft length of the `Conditioning Path -> Coefficient Vector` branch while keeping it straight.
2. Regenerate `harmonic_regression_model_architecture_diagram.svg`.
3. Inspect the regenerated SVG directly to confirm:
   - the branch shows a clearly visible vertical line segment;
   - the branch remains straight;
   - the lower-card composition stays balanced.
