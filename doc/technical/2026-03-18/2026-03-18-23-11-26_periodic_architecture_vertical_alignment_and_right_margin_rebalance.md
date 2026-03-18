# Periodic Architecture Vertical Alignment And Right Margin Rebalance

## Overview

This document defines a focused refinement pass for the remaining layout issues in:

- `periodic_feature_network_model_architecture_diagram.svg`

The current periodic architecture diagram is improved, but three structural issues remain:

1. `Angle`, `Concat`, and the neural backbone are not vertically centered on the same axis;
2. the `Conditions -> Concat` branch still uses an unnecessary 90-degree turn and should become a straight connector;
3. the latest spacing changes pushed the neural backbone too close to the right edge of the canvas, reducing the visual margin.

The goal of this pass is to rebalance the architecture layout so that the central inference chain reads cleanly from left to right, the right-side margin is restored, and the `Conditions` injection remains readable without extra elbows.

## Technical Approach

### 1. Vertically Align `Angle`, `Concat`, And The Neural Backbone

The core periodic computation path should read along a common horizontal axis.

This pass should:

- place `Angle` so its vertical center matches the center of `Concat`;
- place the neural backbone so its base alignment and visual center match the same axis used by `Concat`;
- preserve the larger `Feature Expansion` card as the taller upstream element without forcing it to share the exact same full bounding-box center.

### 2. Make `Conditions -> Concat` Straight

The `Conditions` branch should now connect directly into `Concat` without an orthogonal bend.

This pass should:

- reposition `Conditions` as needed so a straight connector is geometrically valid;
- keep the connection visually distinct from `Feature Expansion -> Concat`;
- preserve good clearance from the `Concat` border.

### 3. Recover The Right Margin

The last spacing pass improved the incoming connector heads, but it reduced the room available for the neural stack on the right.

This pass should:

- slightly tighten box widths where reasonable;
- move the neural stack left enough to restore a clear right margin;
- keep the `Concat -> neural backbone` connector readable and longer than the too-short regression previously observed.

### 4. Keep The Current Approved Routing Intent

The recent approved changes already established:

- the target ordering of the two branches entering `Concat`;
- the lower routed path for `Feature Expansion -> Concat`;
- the longer `Angle -> Feature Expansion` connector;
- the restored dense neuron-to-neuron lines.

This pass should preserve those decisions while rebalancing the geometry.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for periodic architecture card geometry, connector routing, and neural-stack placement;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/periodic_feature_network_model_architecture_diagram.svg`
  which will be regenerated.

No other periodic diagram or PDF should change in this pass.

## Implementation Steps

1. Rebalance the periodic architecture card geometry so `Angle`, `Concat`, and the neural backbone share the same vertical centerline.
2. Adjust `Conditions` placement so `Conditions -> Concat` can be drawn as a straight connector.
3. Tighten widths and horizontal placement enough to restore a healthy right canvas margin.
4. Update the dependent connector endpoints and the neural-stack placement.
5. Regenerate `periodic_feature_network_model_architecture_diagram.svg`.
6. Inspect the regenerated SVG directly to confirm:
   - `Angle`, `Concat`, and the neural backbone are vertically aligned;
   - `Conditions -> Concat` is straight;
   - the rightmost neurons no longer sit too close to the image edge;
   - the approved `Feature Expansion -> Concat` path remains clean.
