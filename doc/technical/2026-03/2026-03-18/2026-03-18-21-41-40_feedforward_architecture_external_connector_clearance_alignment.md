# Feedforward Architecture External Connector Clearance Alignment

## Overview

This document defines a targeted refinement pass for `feedforward_model_architecture_diagram.svg`, focused on the two external horizontal connectors between:

- the `Inputs` card and the first neuron layer;
- the last neuron layer and the `Output` card.

The current version already uses straight connectors with matching style, but the two arrows sit too close to the box borders and slightly overlap the card outlines visually. The desired correction is to give these connectors the same kind of breathing room already present in the box-to-box connectors of `feedforward_model_diagram.svg`.

## Technical Approach

### 1. Add Explicit Border Clearance To Architecture Connectors

The current architecture connectors are drawn directly from:

- the exact outer edge of the source card;
- the exact outer edge of the target card or neuron circle.

This makes the arrow shaft and arrowhead appear visually attached to the borders.

This pass should:

- introduce explicit start and end clearance for the two architecture-side external connectors;
- keep the connectors straight and horizontally aligned;
- preserve the already-correct connector length and symmetry.

The intended visual result is:

- the connector starts slightly after leaving the `Inputs` box;
- the connector ends slightly before reaching the first neuron layer;
- the output-side connector starts slightly after the last neuron layer;
- the connector ends slightly before the `Output` box border.

### 2. Align With Existing Box-Connector Spacing Policy

The repository already uses border clearance values for box-to-box connectors through the box-connector helper.

This pass should align the feedforward architecture external connectors with that same spacing language so the diagram family feels visually consistent.

The implementation may:

- reuse the existing connector-clearance constants directly;
- or define a small architecture-specific connector clearance if the neuron-circle geometry requires a slightly different value.

### 3. Permanent Guardrails

To avoid the issue returning after later horizontal-layout adjustments, this pass should prefer derived geometry and small assertions instead of hard-coded end points that touch borders.

Useful protections include:

- explicit source and target clearance constants for the architecture connectors;
- assertions that the resulting visible connector span remains comfortably positive.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for feedforward architecture external-connector endpoint computation;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/feedforward_model_architecture_diagram.svg`
  which will be regenerated from the updated generator.

No model code, training artifacts, or unrelated diagrams should be modified by this pass.

## Implementation Steps

1. Add explicit start and end clearances to the `Inputs -> neuron stack` connector.
2. Add explicit start and end clearances to the `neuron stack -> Output` connector.
3. Keep both connectors straight, symmetric, and visually aligned with the current box-connector spacing language.
4. Regenerate `feedforward_model_architecture_diagram.svg`.
5. Inspect the regenerated SVG directly to confirm:
   - both external connectors no longer touch or visually overlap the card borders;
   - both connectors still match each other in style and length;
   - no unwanted elbow routing is reintroduced.
