# Residual Connector Tail And Flow Note Clearance Refinement

## Overview

This document defines a focused refinement pass for the residual-harmonic explanatory diagrams:

- `residual_harmonic_network_model_architecture_diagram.svg`
- `residual_harmonic_network_model_diagram.svg`

The previous residual pass fixed the major symmetry, centering, and dense-connectivity issues, but a few spacing details still need adjustment:

1. in the architecture diagram, the `Add` box should be slightly narrower so there is more horizontal room between `Shared Input` and the two branch cards, which will lengthen the final short horizontal tail before the arrowheads on the incoming branch connectors;
2. in the conceptual diagram, the gap between `Shared Input` and both branch cards should increase slightly for the same reason: the final short horizontal segment before the arrowhead is still too compressed;
3. in the conceptual flow cards, the notes `Can be frozen or joint-trained` and `Only models the remaining error` sit too close to the lower border, while the cards themselves remain too close to the header above and the `Interpretation` box below.

The goal of this pass is to keep the current residual layout logic while adding more breathing room to the branch-entry connector tails and slightly tightening the internal note spacing so the full composition feels more balanced.

## Technical Approach

### 1. Recover Horizontal Tail Length On The Incoming Branch Connectors

The current mirrored input connectors are geometrically correct, but the final small horizontal segment before each arrowhead is still too short.

This pass should:

- slightly increase the horizontal separation between `Shared Input` and the branch cards in the conceptual diagram;
- slightly narrow `Add` in the architecture diagram and rebalance the branch-card spacing so the incoming mirrored connectors gain a longer terminal horizontal segment;
- preserve the mirrored connector policy already established in the previous residual refinement.

### 2. Rebalance Conceptual Flow-Card Note Placement

The conceptual residual flow cards currently leave too much space between the final row and the note, but too little margin between the note and the lower card border.

This pass should:

- reduce the row-to-note gap slightly;
- increase or preserve a cleaner lower border clearance;
- make the overall cards feel less pressed against the surrounding header and interpretation card.

### 3. Keep The Residual Centerline Alignment Intact

The previous residual pass introduced an explicit centerline for `Shared Input`, `Add`, `TE`, and `Outputs`.

This pass should therefore:

- preserve the shared centerline alignment;
- avoid reintroducing asymmetry in the mirrored connectors;
- keep the restored dense residual-neural connections unchanged.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for residual-specific connector spacing, `Add` width, branch spacing, and flow-card note clearance;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/residual_harmonic_network_model_architecture_diagram.svg`
  which will be regenerated;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/residual_harmonic_network_model_diagram.svg`
  which will be regenerated.

No report PDF should change in this pass.

## Implementation Steps

1. Slightly narrow the architecture `Add` box and rebalance the nearby residual connector geometry.
2. Increase the conceptual spacing between `Shared Input` and the two branch cards.
3. Reduce the row-to-note gap inside the conceptual `Structured Branch` and `Residual Branch` cards while preserving clean lower-border clearance.
4. Regenerate the two residual SVG diagrams.
5. Inspect the regenerated SVGs directly to confirm:
   - the final horizontal tail before each branch-entry arrowhead is longer;
   - the conceptual branch notes sit farther from the lower border;
   - the mirrored-connector geometry remains symmetric;
   - the residual centerline alignment remains intact.
