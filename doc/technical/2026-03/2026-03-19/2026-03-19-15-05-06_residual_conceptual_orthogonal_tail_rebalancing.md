# Residual Conceptual Orthogonal Tail Rebalancing

## Overview

This document defines a narrow refinement pass for:

- `residual_harmonic_network_model_diagram.svg`

The current conceptual residual diagram already has the correct mirrored topology and spacing, but the four orthogonal connectors still bend too late:

1. `Shared Input -> Structured Branch`
2. `Shared Input -> Residual Branch`
3. `Structured Branch -> Add`
4. `Residual Branch -> Add`

In all four cases, the first horizontal segment is still longer than the final horizontal tail before the arrowhead. The requested refinement is the same one already applied to the residual architecture diagram: move the elbow earlier so the first horizontal run becomes shorter and the last horizontal run becomes longer. Ideally, the two horizontal runs in each connector should become equal in length.

## Technical Approach

### 1. Rebalance The Shared-Input Branch Connectors

The two mirrored input connectors currently use an elbow x-position that is too far to the right.

This pass should:

- move the shared elbow leftward;
- keep the two connectors mirrored around the conceptual residual centerline;
- rebalance the two horizontal runs so the first and last horizontal segments become equal or nearly equal.

### 2. Rebalance The Branch Connectors Into `Add`

The two mirrored branch-to-merge connectors currently show the same issue: the elbow x-position is too far to the right, so the final horizontal tail into `Add` is still too short.

This pass should:

- move the elbow leftward for both merge connectors;
- preserve their mirrored geometry;
- make the first and last horizontal runs equal or nearly equal.

### 3. Keep The Conceptual Residual Layout Otherwise Stable

The previous residual passes already fixed:

- flow-card spacing;
- centerline alignment;
- `Shared Input` text fit;
- straight `Add -> Outputs`.

This pass should therefore remain deliberately narrow and avoid changing card placement, note spacing, or the interpretation card.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for the residual conceptual connector lane positions;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/residual_harmonic_network_model_diagram.svg`
  which will be regenerated.

No architecture residual SVG, report PDF, or non-residual diagram should change in this pass.

## Implementation Steps

1. Recompute the elbow x-position for the two `Shared Input -> branch` connectors in the conceptual residual builder.
2. Recompute the elbow x-position for the two `branch -> Add` connectors in the conceptual residual builder.
3. Regenerate `residual_harmonic_network_model_diagram.svg`.
4. Inspect the regenerated SVG directly to confirm:
   - the first horizontal segment is shorter;
   - the final horizontal tail is longer;
   - the two horizontal segments are equal or nearly equal in each connector;
   - the mirrored symmetry is preserved.
