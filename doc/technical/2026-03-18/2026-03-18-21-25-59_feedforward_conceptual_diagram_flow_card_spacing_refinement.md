# Feedforward Conceptual Diagram Flow Card Spacing Refinement

## Overview

This document defines a targeted correction pass for `feedforward_model_diagram.svg`, focused on the internal layout quality of the `FeedForward Network` flow card in the conceptual diagram.

The current asset still shows two visible presentation defects:

- the short vertical arrows between the internal flow rows visually overlap the row labels and the rounded row boxes;
- the `FeedForward Network` card border appears more prominent than the surrounding cards, which may be either an intended accent treatment or an overemphasized visual difference.

The goal of this pass is to correct the internal flow-card spacing so connectors stay clearly between the rows, and to review the accent-card border treatment so the visual emphasis remains intentional and controlled.

## Technical Approach

### 1. Internal Flow Connector Clearance

The current `draw_flow_card()` helper uses:

- row height `20`;
- row gap `12`;
- a vertical connector that starts only `3` px below the row and ends only `4` px before the next row.

With an arrow marker applied, that geometry leaves too little visible breathing room and causes the connector to intrude into the perceived row area.

This pass should refine the helper so that:

- internal flow connectors reserve a larger clear gap between rows;
- the arrow body and arrowhead do not visually touch the rounded row boxes;
- the connector remains centered between rows instead of competing with the text baseline.

This should be solved at the helper level so the same defect does not reappear in other flow-card diagrams.

### 2. Accent Border Review

The `FeedForward Network` card currently uses `accent=True`, which changes the border color from the standard card blue to the stronger accent blue while keeping the same stroke width.

This pass should explicitly review whether the accent treatment is still desirable for the conceptual feedforward block:

- if the stronger border is intentional and visually balanced, preserve it;
- if it reads as an unintended error or excessive emphasis, reduce the contrast in a controlled way without removing the ability to accent key blocks elsewhere.

The review should distinguish between:

- actual stroke-width inconsistency;
- purely color-driven visual prominence.

### 3. Permanent Guardrails

The current overlap risk comes from fixed connector clearances that are too small relative to the marker size.

This pass should therefore prefer generator-level guardrails such as:

- explicit connector top and bottom clearance constants for flow cards;
- assertions that ensure the usable inter-row connector span remains positive and visually safe;
- helper behavior that remains stable when row count or row gap changes.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for `draw_flow_card()` spacing and possible accent-style tuning;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/feedforward_model_diagram.svg`
  which will be regenerated from the updated generator;
- `doc/scripts/reports/generate_model_report_diagrams.md`
  if the documented layout guarantees need to mention the refined flow-card connector clearance policy.

No model logic, training workflow, or campaign artifact should be modified by this correction pass.

## Implementation Steps

1. Refine the flow-card connector geometry in `draw_flow_card()` so arrows stay visually between the row boxes.
2. Add helper-level spacing checks or constants to prevent connector overlap regressions.
3. Review the accent border treatment used by the `FeedForward Network` conceptual card.
4. Keep or adjust the accent styling based on whether the prominence is intentional and visually balanced.
5. Regenerate `feedforward_model_diagram.svg`.
6. Inspect the generated SVG directly to confirm:
   - internal arrows no longer cover labels or row boxes;
   - row spacing remains balanced;
   - the accent border reads as deliberate rather than accidental.
