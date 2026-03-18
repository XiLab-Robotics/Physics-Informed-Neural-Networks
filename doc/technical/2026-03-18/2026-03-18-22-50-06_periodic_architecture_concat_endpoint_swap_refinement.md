# Periodic Architecture Concat Endpoint Swap Refinement

## Overview

This document defines a minimal refinement pass for the remaining connector overlap in:

- `periodic_feature_network_model_architecture_diagram.svg`

The current architecture diagram still shows visual interference between the two orthogonal branches entering `Concat`:

1. `Feature Expansion -> Concat`
2. `Conditions -> Concat`

The user-requested adjustment is to swap the vertical arrival targets on the `Concat` box so that the first branch reaches the point currently used by the second one, and vice versa. This should be sufficient to remove the perceived overlap without changing the current card placement or the overall routing style.

## Technical Approach

### 1. Swap The Two `Concat` Arrival Offsets

The two incoming periodic branches already use distinct `target_offset` values on the left side of `Concat`, but the current assignment still creates an awkward visual crossing/stacking relationship.

This pass should:

- keep the existing orthogonal routing style;
- keep the current card positions unchanged;
- swap the `target_offset` assignments used by:
  - `Feature Expansion -> Concat`
  - `Conditions -> Concat`

The expected outcome is that the upper/lower relationship between the two input branches becomes more legible without any broader layout churn.

### 2. Keep All Other Periodic Geometry Stable

The previous periodic fixes already resolved:

- the conceptual diagram flow-card spacing;
- the straight box-to-box connectors in the conceptual diagram;
- the restored dense neuron connections in the architecture diagram;
- the longer `Angle -> Feature Expansion` arrow.

This pass should therefore remain intentionally narrow and avoid touching any of those already-correct elements.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for the periodic architecture `Concat` connector target offsets;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/periodic_feature_network_model_architecture_diagram.svg`
  which will be regenerated.

No other SVG or PDF should change in this pass.

## Implementation Steps

1. Swap the `target_offset` values used by the two periodic branches entering `Concat`.
2. Regenerate `periodic_feature_network_model_architecture_diagram.svg`.
3. Inspect the regenerated SVG directly to confirm:
   - the two incoming orthogonal branches no longer visually overlap in the same way;
   - the new routing remains clean and readable;
   - no regression appears in the `Angle -> Feature Expansion` connector or the neural backbone.
