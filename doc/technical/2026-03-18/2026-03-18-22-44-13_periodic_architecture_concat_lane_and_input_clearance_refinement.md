# Periodic Architecture Concat Lane And Input Clearance Refinement

## Overview

This document defines a focused refinement pass for the remaining layout issues in:

- `periodic_feature_network_model_architecture_diagram.svg`

After the previous periodic-diagram repair, the conceptual diagram is now acceptable, but the architecture diagram still shows two residual connector problems:

1. the `Feature Expansion -> Concat` connector is routed too high and visually runs above the `Conditions` card;
2. the `Angle -> Feature Expansion` arrow is still slightly too short and should have more horizontal clearance.

The goal of this pass is to keep the current overall geometry while making the architecture routing cleaner, more intentional, and visually consistent with the connector spacing standards already established in the feedforward and harmonic diagrams.

## Technical Approach

### 1. Lower The `Feature Expansion -> Concat` Routing Lane

The current `Feature Expansion -> Concat` path departs from the lower-right area of the `Feature Expansion` card, but its horizontal lane is still placed too high relative to the `Conditions` box. This makes the connector visually dominate the area above `Conditions`.

This pass should:

- keep the orthogonal routing style requested for this branch;
- lower the effective routing lane so the connector reads as a deliberate lower branch rather than an overhanging top path;
- preserve separation from the `Conditions -> Concat` branch so the two inputs remain clearly distinguishable.

### 2. Extend The `Angle -> Feature Expansion` Arrow

The current straight connector from `Angle` to `Feature Expansion` is valid, but its visible shaft is still too short.

This pass should:

- keep the connector straight;
- increase its visible horizontal span by adjusting either the source card position, the feature card position, or the explicit connector endpoints;
- preserve box-border clearance so the connector does not visually touch the card outlines.

### 3. Keep The Fix Local To The Periodic Architecture Builder

No generator-wide primitive changes are required. The issue is localized to the periodic architecture builder geometry and routing choices.

This pass should therefore:

- adjust only the periodic architecture layout constants and connector routing parameters;
- avoid changing the already-correct periodic conceptual diagram;
- avoid changing unrelated model families.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for the periodic architecture connector geometry;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/periodic_feature_network_model_architecture_diagram.svg`
  which will be regenerated.

The periodic conceptual SVG should remain unchanged during this pass.

## Implementation Steps

1. Adjust the periodic architecture connector geometry for `Feature Expansion -> Concat`.
2. Lower the effective routing lane so it no longer reads as a path running above `Conditions`.
3. Increase the visible length of the straight `Angle -> Feature Expansion` arrow.
4. Regenerate `periodic_feature_network_model_architecture_diagram.svg`.
5. Inspect the regenerated SVG directly to confirm:
   - the `Feature Expansion -> Concat` connector no longer sits awkwardly above `Conditions`;
   - the `Angle -> Feature Expansion` arrow has a clearly visible shaft with comfortable box clearance;
   - no regressions were introduced in the other periodic architecture connectors.
