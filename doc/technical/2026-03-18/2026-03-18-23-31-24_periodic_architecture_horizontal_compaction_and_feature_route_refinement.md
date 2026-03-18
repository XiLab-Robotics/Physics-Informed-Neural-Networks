# Periodic Architecture Horizontal Compaction And Feature Route Refinement

## Overview

This document defines a final geometry cleanup pass for:

- `periodic_feature_network_model_architecture_diagram.svg`

The current periodic architecture diagram is much closer to the desired result, but a few horizontal-balance and routing details still need refinement:

1. the cards `Angle`, `Feature Expansion`, and `Conditions` should be narrowed further so the neural backbone sits more comfortably inside the right canvas margin;
2. the spacing between the last hidden layer and the output layer should be reduced slightly;
3. the connector `Feature Expansion -> Concat` should use an explicit two-elbow orthogonal route so the final approach into `Concat` is horizontal rather than descending directly into the arrowhead.

The requested connector shape is:

- leave `Feature Expansion` from the right side;
- move horizontally to the right;
- turn 90 degrees upward;
- travel vertically upward;
- turn 90 degrees to the right again;
- use a short final horizontal segment into `Concat`.

## Technical Approach

### 1. Tighten The Left And Middle Cards

The current left-side and middle card widths still consume more horizontal room than necessary.

This pass should:

- reduce the width of `Angle`;
- reduce the width of `Feature Expansion`;
- reduce the width of `Conditions`;
- preserve readable text fit and centered labels while recovering right-side margin for the neural stack.

### 2. Pull The Neural Backbone Slightly Left And Compact The Last Gap

The current neural stack already fits better than before, but the right margin can still improve.

This pass should:

- keep the backbone vertically aligned with `Concat`;
- preserve dense neuron-to-neuron connectivity;
- reduce the horizontal distance between the hidden layer and the output layer slightly;
- keep a readable `Concat -> backbone` connector length.

### 3. Replace The Current `Feature Expansion -> Concat` Path With A Deliberate Polyline

The current connector still ends with a vertical drop into the final arrowhead area. The requested visual language is a cleaner stepped route with a final horizontal entry.

This pass should:

- stop relying on the generic horizontal-to-horizontal connector for this branch;
- draw the route explicitly as a custom polyline arrow;
- preserve the already-approved lower branch assignment into `Concat`;
- keep the `Conditions -> Concat` connector straight and unchanged.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for periodic architecture card widths, backbone spacing, and the custom `Feature Expansion -> Concat` route;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/periodic_feature_network_model_architecture_diagram.svg`
  which will be regenerated.

No other periodic diagram or PDF should change in this pass.

## Implementation Steps

1. Reduce the widths of `Angle`, `Feature Expansion`, and `Conditions`.
2. Rebalance the dependent x-positions so the neural backbone regains more right-side margin.
3. Slightly reduce the spacing between the hidden layer and output layer.
4. Replace the `Feature Expansion -> Concat` connector with an explicit stepped polyline that ends horizontally into `Concat`.
5. Regenerate `periodic_feature_network_model_architecture_diagram.svg`.
6. Inspect the regenerated SVG directly to confirm:
   - the neural backbone sits farther from the right edge;
   - the last hidden-to-output gap is slightly tighter;
   - `Feature Expansion -> Concat` follows the requested right-up-right-horizontal approach;
   - `Conditions -> Concat` remains straight and clean.
