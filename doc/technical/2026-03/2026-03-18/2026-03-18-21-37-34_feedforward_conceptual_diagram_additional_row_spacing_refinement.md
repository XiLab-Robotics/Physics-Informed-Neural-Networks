# Feedforward Conceptual Diagram Additional Row Spacing Refinement

## Overview

This document defines a further layout refinement pass for `feedforward_model_diagram.svg`, still focused on the `FeedForward Network` flow card in the conceptual feedforward diagram.

The current version is improved, but the internal row stack still feels too compact. The user requested additional vertical spacing between the internal row boxes so the card reads more clearly and the internal arrows have even more room to breathe.

The goal of this pass is therefore straightforward:

- increase the vertical distance between the `FeedForward Network` sub-boxes again;
- preserve the visible arrow shafts already recovered in the previous pass;
- keep the note text and outer connectors visually balanced after the spacing increase.

## Technical Approach

### 1. Increase Feedforward Row Separation

The feedforward conceptual card currently uses a custom `flow_gap`, but the internal rows still read as too compact.

This pass should:

- increase the feedforward-specific `flow_gap` again;
- keep the current connector clearances and minimum shaft visibility constraints active;
- adjust the feedforward card height or vertical placement only if required to keep the composition balanced.

### 2. Preserve Internal Arrow Readability

The previous pass restored a visible connector shaft. This refinement must not regress that gain.

The updated spacing should therefore maintain:

- clear separation from row borders;
- a visibly readable arrow line segment;
- no overlap with row labels or the note text.

### 3. Keep The Card Composition Balanced

Increasing the row spacing may require a small companion adjustment so the card still feels centered and does not crowd adjacent elements.

The refinement should therefore recheck:

- note clearance from the lower border;
- relative placement of the card header, row stack, and note;
- alignment of the external connectors entering and leaving the card.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for feedforward-specific `draw_flow_card()` parameters in the conceptual diagram;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/feedforward_model_diagram.svg`
  which will be regenerated from the updated generator.

No model logic, training artifacts, or unrelated diagrams should be modified by this targeted pass.

## Implementation Steps

1. Increase the feedforward conceptual card row spacing again.
2. Adjust the card geometry only as much as needed to accommodate the larger spacing cleanly.
3. Regenerate `feedforward_model_diagram.svg`.
4. Inspect the regenerated SVG directly to confirm:
   - visibly larger vertical spacing between sub-boxes;
   - internal arrows still show a proper line segment;
   - the lower note remains comfortably clear of the bottom border;
   - the card remains aligned with the surrounding flow.
