# Residual Conceptual Vertical Gap Rebalance

## Overview

This document defines a final spacing refinement for:

- `residual_harmonic_network_model_diagram.svg`

The residual conceptual diagram now has the correct connector geometry, but the two branch cards still sit too close to the elements above and below them:

1. `Structured Branch` is too close to the diagram header area;
2. `Residual Branch` is too close to the `Interpretation` box.

The user-requested fix is to reduce the vertical gap between the two branch cards so that both cards move slightly toward the middle, creating more breathing room at the top and bottom of the composition.

## Technical Approach

### 1. Reduce The Inter-Branch Vertical Gap

The current branch-card positions leave a larger-than-needed gap between `Structured Branch` and `Residual Branch`.

This pass should:

- move `Structured Branch` slightly downward;
- move `Residual Branch` slightly upward;
- keep the cards mirrored around the established conceptual residual centerline.

### 2. Preserve The Existing Connector And Centerline Logic

The previous residual passes already fixed:

- the mirrored connector routing;
- the balanced orthogonal connector tails;
- the centered `Shared Input`, `Add`, and `Outputs`;
- the note spacing inside the flow cards.

This pass should therefore:

- keep the current connector geometry coherent with the adjusted card positions;
- avoid changing widths, labels, or note contents;
- keep the `Interpretation` card unchanged.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for the residual conceptual branch y-positions and dependent connector geometry;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/residual_harmonic_network_model_diagram.svg`
  which will be regenerated.

No architecture residual SVG, report PDF, or non-residual diagram should change in this pass.

## Implementation Steps

1. Reduce the vertical gap between `Structured Branch` and `Residual Branch`.
2. Regenerate `residual_harmonic_network_model_diagram.svg`.
3. Inspect the regenerated SVG directly to confirm:
   - the top branch is farther from the header;
   - the bottom branch is farther from `Interpretation`;
   - the mirrored layout remains visually balanced.
