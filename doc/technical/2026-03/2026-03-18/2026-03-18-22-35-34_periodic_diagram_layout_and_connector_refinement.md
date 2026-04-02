# Periodic Diagram Layout And Connector Refinement

## Overview

This document defines a targeted repair pass for the periodic-feature explanatory diagrams:

- `periodic_feature_network_model_architecture_diagram.svg`
- `periodic_feature_network_model_diagram.svg`

The current periodic diagrams still show several layout issues that have already been solved in more recent feedforward and harmonic diagram refinements, but are not yet applied consistently in the periodic-specific builders.

The reported defects are:

1. the periodic architecture diagram still contains unnecessary 90-degree connectors;
2. the neural stack on the right side of the periodic architecture diagram no longer shows dense neuron-to-neuron connection lines;
3. the connector from `Feature Expansion` to `Concat` remains visually poor and should be rerouted through a cleaner orthogonal path;
4. the `Conditions` card should be moved upward and connected to `Concat` with a cleaner 90-degree path;
5. the conceptual periodic flow cards `Periodic Feature Builder` and `FeedForward Backbone` still have internal vertical arrows that cover or crowd the row boxes and labels;
6. the small box-to-box connectors in the conceptual periodic diagram still contain tiny unnecessary 90-degree bends instead of straight connectors.

The goal of this pass is to bring the periodic diagrams in line with the generator behavior already used successfully in the feedforward and harmonic diagrams.

## Technical Approach

### 1. Restore Dense Neural Connectivity In The Periodic Architecture Diagram

The current periodic architecture builder calls `draw_layer_block()` without enabling dense connectivity, which removes the neuron-to-neuron lines from the neural backbone.

This pass should:

- restore the dense inter-layer neural links;
- use plain lines without arrowheads, consistent with the current architecture-diagram policy;
- keep the distributed circle-anchor logic already available in the generator.

### 2. Reroute The Periodic Architecture Inputs More Intentionally

The current periodic architecture input routing relies on compact generic orthogonal connectors, which produces awkward elbows and an especially poor `Feature Expansion -> Concat` path.

The requested geometry is:

- move `Conditions` upward;
- route `Conditions -> Concat` with a clean orthogonal path from the right side of `Conditions`;
- route `Feature Expansion -> Concat` from the right side as well, but with a lower departure point and a cleaner orthogonal path;
- reduce or remove unnecessary orthogonal bends elsewhere when a straight connector is sufficient.

This pass should therefore treat the periodic architecture builder as a model-specific composition rather than relying only on default connector placement.

### 3. Refine Periodic Conceptual Flow-Card Spacing

The conceptual periodic diagram still uses compact default `draw_flow_card()` spacing for:

- `Periodic Feature Builder`;
- `FeedForward Backbone`.

This causes the internal vertical arrows to remain too short and too close to the row boxes.

This pass should:

- use wider flow-card spacing parameters already supported by the generator;
- enlarge card height if needed;
- preserve the visual balance of the conceptual flow.

### 4. Straighten Small Conceptual Box Connectors

The small connector paths between conceptual periodic boxes currently include tiny unnecessary vertical offsets, which creates visually pointless 90-degree corners.

This pass should:

- replace those with straight connectors where alignment already makes that possible;
- keep the spacing and border clearance language already used in the cleaned-up diagrams.

### 5. Permanent Guardrails

The generator already contains the primitives needed to solve these issues. The main problem is that the periodic builders are not yet using them consistently.

This pass should therefore fix the periodic diagrams at the builder-definition level by:

- enabling dense neural connectivity explicitly;
- applying the richer `draw_flow_card()` spacing parameters;
- defining periodic-specific connector routing where the generic routing is not visually adequate.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for periodic-specific flow-card spacing, neural-backbone connectivity, and connector routing;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/periodic_feature_network_model_architecture_diagram.svg`
  which will be regenerated;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/periodic_feature_network_model_diagram.svg`
  which will be regenerated.

No training code, model logic, or campaign artifacts should be changed by this pass.

## Implementation Steps

1. Restore dense neuron-to-neuron connection lines in the periodic architecture diagram.
2. Move `Conditions` upward in the periodic architecture diagram and reroute both inputs into `Concat` with cleaner orthogonal paths.
3. Remove unnecessary 90-degree bends from the other periodic architecture connectors where straight routing is sufficient.
4. Refine `Periodic Feature Builder` flow-card spacing in the conceptual periodic diagram.
5. Refine `FeedForward Backbone` flow-card spacing in the conceptual periodic diagram.
6. Replace the tiny bent conceptual box connectors with straight connectors where alignment allows it.
7. Regenerate the two periodic SVG diagrams.
8. Inspect the regenerated SVGs directly to confirm:
   - dense neural connectivity is visible again;
   - the `Feature Expansion -> Concat` and `Conditions -> Concat` routing is cleaner;
   - internal flow-card arrows no longer cover row labels or row boxes;
   - tiny unnecessary elbows are removed from the conceptual diagram.
