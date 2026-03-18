# Third Pass Model Report Arrow And Spacing Refinement

## Overview

This document defines a third correction pass for the structured-model explanatory diagrams used in the model reports and their PDF exports.

The second pass improved centering, routing, and multiline layout, but the current diagrams still contain several connector-related defects that reduce visual quality:

1. dense neuron-to-neuron arrows remain visually noisy and may not justify their cost;
2. box-to-box arrows still touch or overlap box borders, especially at arrowheads;
3. diagonal connectors still scrape card corners instead of entering and leaving perpendicularly;
4. vertical mini-arrows inside flow cards still overlap rows or labels in several models;
5. some model-specific labels or notes still sit too close to surrounding graphics or escape their intended card region.

This pass should prioritize diagram clarity over decorative density. If a class of arrows hurts readability more than it helps explanation, it should be simplified or removed.

## Technical Approach

### 1. Re-evaluate Dense Neuron-to-Neuron Connectors

The current feedforward-style architecture diagrams still look visually overloaded when all dense neuron connections are drawn explicitly.

The preferred correction is:

- remove the dense per-neuron fan-in/fan-out arrows entirely, or reduce them to a much lighter abstraction;
- keep the layer structure visually explicit through node grouping and left-to-right stage ordering;
- preserve only the main input-to-stack and stack-to-output flow arrows if that communicates the architecture more cleanly.

The guiding rule is that the architecture diagram should explain the layer structure, not simulate every edge of the computational graph if that makes the image uglier.

### 2. Perpendicular Box Connectors Only

Box-to-box arrows should always enter and leave cards orthogonally.

The generator should therefore:

- avoid diagonal arrow contact with card borders;
- use elbow or polyline connectors with 90-degree turns;
- ensure the last segment approaches the target box perpendicularly;
- ensure the first segment leaves the source box perpendicularly.

This should become the default policy for inter-card arrows.

### 3. Arrowhead Clearance From Card Borders

Several current arrows terminate too close to the target box, so the arrowhead visually overlaps the border.

The connector geometry should include:

- explicit clearance distance before the card border;
- shorter arrowheads or slightly shorter final segments where needed;
- a consistent rule so that the arrowhead is visible but never sits on top of the card stroke.

### 4. Smaller Internal Flow Connectors

The vertical mini-arrows inside flow cards are still too large and interfere with row labels.

The internal flow-card connector rules should be refined so that:

- the vertical gap between rows is increased if needed;
- the arrow shaft is shorter and thinner;
- the arrow occupies only the intended gap between rows;
- the arrow never crosses row text or row borders.

This is required for the feedforward, harmonic, periodic-feature, and residual conceptual or branch cards.

### 5. Diagram-Specific Composition Fixes

The next pass must apply targeted corrections, not just generic engine tweaks.

Required model-specific fixes include:

- `feedforward_model_architecture_diagram.svg`
  - increase vertical spacing between the example-layout note and the neural stack;
  - ensure the output connector does not place its arrowhead on the output-card border;
  - simplify or remove dense neuron connectors if they remain visually poor.
- `feedforward_model_diagram.svg`
  - prevent the internal vertical arrows in `Feedforward Network` from overlapping the flow rows.
- `harmonic_regression_model_architecture_diagram.svg`
  - prevent the vertical arrow in `Conditioning Path` from overlapping the row text;
  - ensure all box-to-box arrows enter and leave orthogonally.
- `harmonic_regression_model_diagram.svg`
  - prevent vertical arrows in `Harmonic Basis` and `Coefficient Resolver` from overlapping row content;
  - keep `Compact periodic estimator` safely inside the `Prediction` card.
- `periodic_feature_network_model_architecture_diagram.svg`
  - move `Conditions` upward;
  - route both incoming connectors to `Concat` with clean 90-degree turns;
  - eliminate the current diagonal/crossing connector look.
- `periodic_feature_network_model_diagram.svg`
  - prevent vertical arrows in `Periodic Feature Builder` and `FeedForward Backbone` from overlapping row content;
  - use the repository-consistent title spelling `FeedForward Backbone`.
- `residual_harmonic_network_model_architecture_diagram.svg`
  - prevent vertical arrows in `Structured Path` and `Residual Path` from overlapping row content;
  - make the `Shared Input` split connectors vertically symmetric;
  - reduce box-to-box arrow size where only an arrowhead remains visible, especially near `Add` and `TE`.
- `residual_harmonic_network_model_diagram.svg`
  - prevent vertical arrows in `Structured Branch` and `Residual Branch` from overlapping row content;
  - keep `Common input to both branches` inside the `Shared Input` card;
  - keep the output note text fully clear of the `Outputs` card border.

### 6. Validation Standard

The completion standard for this pass should explicitly require:

- no dense-neuron connector clutter if those arrows are retained;
- no arrowhead overlapping a card border;
- no diagonal arrow touching a card corner;
- no internal flow-card arrow crossing text or row boxes;
- no note text touching or escaping card borders;
- regenerated PDF pages that confirm the fixes in the real final export.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for connector policy, flow-card spacing, and diagram-specific tuning;
- the SVG assets in `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/`
  which will be regenerated;
- the exported PDFs in `doc/reports/analysis/`
  which will need regeneration and validation again;
- script-level report documentation and the usage guide
  if the connector policy or recommended pipeline command needs clarification.

## Implementation Steps

1. Simplify or remove dense neuron-to-neuron connectors where they harm readability.
2. Enforce perpendicular box-to-box connector routing with 90-degree turns by default.
3. Add arrowhead clearance rules so arrow tips never overlap card borders.
4. Reduce and reposition internal flow-card arrows so they stay only in the row gaps.
5. Apply the listed per-diagram composition fixes for the eight structured-model SVG assets.
6. Regenerate the SVG diagrams and inspect them directly.
7. Regenerate the four explanatory PDFs.
8. Validate the real exported PDFs again through rasterized page inspection.
