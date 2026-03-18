# Second Pass Model Report Diagram Layout Refinement

## Overview

This document defines the next refinement pass for the structured-model explanatory diagrams used in the model reports and their PDF exports.

The first correction pass improved the diagrams substantially, but the current assets still have visible presentation defects that reduce readability and visual quality:

1. dense incoming neuron connectors collapse into the same arrival point and create an unattractive overlap cluster;
2. the full diagram composition is still top-heavy instead of being vertically centered inside the slide canvas;
3. some card internals still rely on excessive text shrinking instead of proper multiline wrapping and spacing;
4. some vertical flow arrows are too large and overlap the cards or the text they are meant to connect;
5. some routed connectors still pass over unrelated cards;
6. some card text still escapes the intended content region in a few model-specific diagrams.

This pass should improve both the layout engine and the model-specific compositions so the diagrams are visually balanced, centered, and presentation-grade before the next PDF export.

## Technical Approach

### 1. Staggered Connector Anchors For Dense Neural Links

The architecture diagrams should no longer route all incoming edges to the exact same point on the destination neuron.

Instead, the generator should support:

- distributed border anchors around the destination circle;
- per-edge angular or vertical offset assignment;
- optional fan-in spacing so the last segment of each connector remains distinct near the destination neuron;
- arrowheads that remain visible and do not visually merge into a single dark cluster.

This is especially important for the feedforward and residual-style architecture views.

### 2. Canvas-Level Vertical Centering

The diagram generator should treat the slide as a full composition area rather than placing the content block immediately below the header.

The generator should:

- compute the content bounding region below the header;
- vertically center the grouped cards and connectors inside that region;
- preserve enough breathing room below the header and above the canvas bottom;
- avoid diagrams that look compressed toward the top of the page.

### 3. Better Card Text Layout

Cards should prefer readable multiline layout over aggressive font shrinking.

The generator should therefore support:

- explicit line wrapping for longer labels such as `Five normalized scalar features`;
- configurable vertical spacing between semantic groups inside the same card;
- model-specific content splitting where a long sentence is better rendered as two short lines;
- stricter validation against card-content collisions with separators and borders.

This is required for the `Inputs`, `Raw Angles`, and similar compact cards.

### 4. Scaled Internal Flow Arrows

The conceptual diagrams currently contain some internal vertical arrows that are too large for the available space.

Those arrows should be refined so that:

- they are shorter and thinner;
- they stay between blocks instead of crossing over text;
- the card stack is spaced to accommodate them;
- the visual emphasis remains on the processing stages, not on oversized connectors.

### 5. Safer Routed Connectors Between Cards

Some routed links still cross unrelated boxes, such as the periodic-feature architecture connector that visually crosses the conditions card.

The routing logic should therefore support:

- obstacle-aware elbow paths;
- lane-based horizontal and vertical routing;
- model-specific rerouting when a generic path would cross another card;
- connector spacing that respects neighboring box borders.

### 6. Diagram-Specific Composition Refinement

The next pass should not stop at generic engine changes.

Each of the eight diagrams should be rechecked individually for:

- content centering;
- card height and spacing;
- text wrapping;
- connector size;
- connector routing;
- balance of the whole slide composition.

### 7. Validation Discipline

The refinement should be validated at two levels:

- direct SVG inspection;
- real PDF export inspection after embedding the updated diagrams into the reports.

Completion criteria should explicitly include:

- no connector pile-up on the destination neuron;
- no text touching separator lines or card borders;
- no top-heavy slide composition;
- no arrows crossing card titles or card bodies unnecessarily;
- no connector crossing through unrelated cards;
- no escaped text in the listed model-specific problem areas.

## Involved Components

The refinement will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for connector geometry, wrapping rules, vertical centering, and model-specific layout tuning;
- the SVG assets in `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/`
  which will be regenerated;
- the explanatory Markdown reports in `doc/reports/analysis/`
  if any figure order or spacing needs a minor update;
- the PDF exports in `doc/reports/analysis/`
  which will need regeneration and validation after the new diagrams are embedded.

The report-pipeline orchestrator may also need a small update if additional validation hooks become useful during diagram generation.

## Implementation Steps

1. Extend the diagram generator with distributed destination anchors for dense neuron fan-in connectors.
2. Add composition-level vertical centering for the diagram content region below the header.
3. Improve card text wrapping and semantic intra-card spacing so long labels do not shrink excessively.
4. Reduce and reposition internal vertical flow arrows in the conceptual diagrams.
5. Refine routed card-to-card connectors to avoid crossing unrelated boxes.
6. Apply diagram-specific layout tuning to the eight current structured-model SVG assets.
7. Regenerate the SVG diagrams and inspect them directly.
8. Regenerate the four explanatory PDFs with the updated figures.
9. Validate the real exported PDFs again before closing the task.
