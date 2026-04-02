# Feedforward Conceptual Diagram Note Clearance And Connector Length Refinement

## Overview

This document defines a follow-up refinement pass for `feedforward_model_diagram.svg`, still focused on the `FeedForward Network` flow card in the conceptual feedforward diagram.

The previous correction improved the internal arrow overlap, but two layout defects remain:

- the note text `Learns TE structure implicitly` sits too close to the bottom border of the card;
- the vertical connectors between the internal row boxes now avoid overlapping the boxes, but the visible shaft of each arrow is still too short and reads mostly as an arrowhead rather than a real connector line.

The goal of this pass is to rebalance the flow-card vertical composition so the note gets more breathing room from the card bottom and the inter-row arrows regain a visibly readable line segment.

## Technical Approach

### 1. Bottom Note Clearance

The current flow-card helper vertically centers the full composition, but the combination of:

- four internal rows;
- three connectors;
- a note gap that is still relatively small;
- the note baseline placement;

leaves the note visually too close to the lower card boundary.

This pass should:

- increase the reserved vertical separation between the last row block and the note;
- ensure the note block keeps a stable minimum clearance from the card bottom;
- avoid pushing the content upward so aggressively that the top rows start to feel cramped again.

The fix should be handled in the generic `draw_flow_card()` layout rather than by manually offsetting the feedforward card alone.

### 2. Connector Shaft Length

The current connector geometry avoids the row boxes, but the usable distance between `arrow_start_y` and `arrow_end_y` remains visually too short.

This pass should therefore:

- increase the inter-row gap enough to expose a real vertical line segment between the row boxes;
- keep explicit top and bottom clearances so the connectors still do not visually touch the rounded row borders;
- preserve a compact overall card layout without causing content overflow.

The intended result is a connector that reads as:

- a line with an arrowhead;
- not only an arrowhead suspended between rows.

### 3. Permanent Guardrails

This follow-up should strengthen the helper constraints so the same regression does not reappear after later spacing tweaks.

Useful protections include:

- a minimum visible connector shaft length assertion;
- a minimum note-to-bottom clearance rule for flow cards;
- helper constants that make the spacing policy explicit instead of implicit.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for additional `draw_flow_card()` spacing refinement and guardrails;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/feedforward_model_diagram.svg`
  which will be regenerated from the updated generator;
- `doc/scripts/reports/generate_model_report_diagrams.md`
  if the documented layout guarantees need to mention bottom-note clearance and minimum visible connector length.

No model implementation, training asset, or campaign configuration should be modified by this refinement.

## Implementation Steps

1. Increase the usable vertical spacing between consecutive flow-card rows.
2. Enforce a minimum visible shaft length for the internal vertical connectors.
3. Increase the separation between the last row and the note text.
4. Enforce a safer minimum clearance between the note and the card bottom.
5. Regenerate `feedforward_model_diagram.svg`.
6. Inspect the regenerated SVG directly to confirm:
   - the note no longer sits too close to the lower border;
   - each internal connector shows a clearly visible line segment in addition to the arrowhead;
   - no row boxes or labels are overlapped again.
