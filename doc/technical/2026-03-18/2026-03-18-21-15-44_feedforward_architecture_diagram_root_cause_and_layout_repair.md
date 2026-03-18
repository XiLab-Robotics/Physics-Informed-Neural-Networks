# Feedforward Architecture Diagram Root Cause And Layout Repair

## Overview

This document defines a targeted repair pass for `feedforward_model_architecture_diagram.svg`, focused on fixing the recurring layout regressions at the generator level instead of applying one-off SVG edits.

The current feedforward architecture asset still contains several concrete defects:

- the `Example hidden layout: 5 to 4 to 4 to 3 to 1` label block is too close to the neuron stack;
- the connector from the `Inputs` card to the neuron stack is too short;
- the left and right external connectors use different styles, widths, and routing logic;
- the neuron-to-neuron connections are currently missing from the feedforward architecture diagram;
- the connector from the neuron stack to the `Output` card uses an unnecessary orthogonal elbow;
- the `Output` card is vertically misaligned relative to the neuron stack center, which forces the routed elbow.

The objective of this pass is to make these corrections permanent by tightening both the feedforward-specific layout definition and the generic generator helpers that control neural connectivity and connector style.

## Technical Approach

### 1. Feedforward-Specific Vertical Composition

The top annotation text in `build_feedforward_architecture_diagram()` is currently positioned with fixed `y` values that do not reserve an explicit vertical buffer above the top neuron row.

This pass should:

- define an explicit annotation block bottom boundary;
- define an explicit minimum gap between that annotation block and the topmost neuron circle;
- position the feedforward layer stack from that reserved region instead of relying on loosely chosen constants.

This should prevent the annotation from drifting too close to the diagram body when the layout is regenerated.

### 2. Consistent External Connector Policy

The current left connector is generated with `draw_box_connector()`, while the right connector is manually drawn with `draw_polyline_arrow()`. This causes inconsistent length, color, stroke width, and shape.

This pass should introduce one consistent policy for architecture-side entry and exit connectors:

- use the same stroke width on both sides;
- use the same arrow or line style on both sides where applicable;
- prefer a straight horizontal connector when the source and target can be vertically aligned;
- only use orthogonal elbows when a genuine routing obstacle exists.

### 3. Restore Dense Neuron Connectivity

The current feedforward architecture diagram calls `draw_layer_block()` without enabling dense connections, which removes all neuron-to-neuron links entirely.

This pass should:

- restore the inter-layer neuron connections in the feedforward architecture view;
- keep those connections as plain lines rather than arrowheaded links when representing internal dense layers;
- preserve readability by keeping the distributed per-node anchor logic instead of collapsing all links onto one point.

The generic dense-connection helper should therefore support a configurable `use_arrow_head` mode instead of always forcing arrowheads.

### 4. Output Alignment Instead Of Elbow Compensation

The current `Output` card is vertically centered around a different `y` coordinate than the last hidden layer, so the generator compensates with an unnecessary elbow connector.

This pass should:

- vertically align the `Output` card center with the neural stack output axis;
- replace the elbow with a normal straight connector;
- keep sufficient horizontal spacing so the right connector is visually balanced with the left connector.

### 5. Permanent Guardrails Against Recurrence

The problem has recurred because the current feedforward architecture composition mixes:

- hard-coded text positions;
- manually routed external arrows;
- helper defaults that silently disable dense connectivity.

This pass should reduce that fragility by:

- making the feedforward architecture composition explicitly parameterized around shared alignment anchors;
- using helper calls that express the intended style instead of ad hoc path fragments;
- adding local assertions or derived geometry checks where useful to protect connector spacing and vertical alignment.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for feedforward architecture layout tuning, dense-connection style control, and connector consistency;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/feedforward_model_architecture_diagram.svg`
  which will be regenerated from the updated generator;
- `doc/scripts/reports/generate_model_report_diagrams.md`
  if the documented layout guarantees need to be updated to reflect the refined connector policy.

No training configuration, model implementation, or campaign artifact should be modified by this repair pass.

## Implementation Steps

1. Refactor the feedforward architecture layout constants so the annotation block, neuron stack, and output card share explicit alignment anchors.
2. Restore neuron-to-neuron dense connectivity in the feedforward architecture diagram and render those links as lines without arrowheads.
3. Unify the left and right external connector style, length, and stroke width.
4. Vertically align the `Output` card with the neuron stack and replace the elbowed output path with a straight connector.
5. Regenerate `feedforward_model_architecture_diagram.svg`.
6. Inspect the generated SVG directly to confirm:
   - larger vertical space below the annotation text;
   - visible neuron connection lines;
   - longer and stylistically consistent left and right connectors;
   - no unnecessary 90-degree output bend;
   - correct vertical alignment of the `Output` card.
7. Update the generator documentation if the helper behavior or layout guarantees change.
