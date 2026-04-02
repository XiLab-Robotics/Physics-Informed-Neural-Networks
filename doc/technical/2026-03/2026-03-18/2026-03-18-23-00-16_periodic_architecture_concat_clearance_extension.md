# Periodic Architecture Concat Clearance Extension

## Overview

This document defines a final spacing refinement for:

- `periodic_feature_network_model_architecture_diagram.svg`

The current connector routing is now conceptually correct:

- the two incoming branches reach the correct target points on `Concat`;
- the orthogonal turns follow the intended path.

However, the remaining issue is connector clearance between `Conditions` and `Concat`. The last horizontal segment before the arrowhead is still too short, so the arrow tip appears too close to the final corner.

The goal of this pass is to create more horizontal breathing room between `Conditions` and `Concat`, so the last segment of each branch is longer and the arrowhead no longer feels crowded against the bend.

## Technical Approach

### 1. Increase Horizontal Separation Between `Conditions` And `Concat`

The most direct fix is to increase the gap between the two cards rather than trying to distort the connector shape.

This pass should:

- keep the current branch ordering and target points on `Concat`;
- keep the orthogonal routing style already approved;
- move `Concat` slightly to the right so the final horizontal segment of both branches becomes longer.

### 2. Preserve The Rest Of The Periodic Architecture Layout

The previous fixes already established the desired behavior for:

- the restored neuron-to-neuron dense lines;
- the longer `Angle -> Feature Expansion` arrow;
- the swapped `Concat` arrival points;
- the general orthogonal path layout.

This pass should therefore remain narrow and avoid unnecessary movement of:

- `Conditions`;
- `Feature Expansion`;
- the neural backbone.

### 3. Revalidate Connector Legibility

After increasing the spacing, the regenerated SVG should be checked to confirm:

- the final horizontal segment before each arrowhead is visibly longer;
- the arrowhead does not sit visually on top of the last bend;
- no new overlap is introduced toward the neural backbone.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for the periodic architecture horizontal placement of `Concat` and the dependent connector geometry;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/periodic_feature_network_model_architecture_diagram.svg`
  which will be regenerated.

No other diagram should change in this pass.

## Implementation Steps

1. Increase the horizontal clearance between `Conditions` and `Concat`.
2. Update any dependent connector coordinates in the periodic architecture builder.
3. Regenerate `periodic_feature_network_model_architecture_diagram.svg`.
4. Inspect the regenerated SVG directly to confirm:
   - both branches keep the approved target ordering on `Concat`;
   - the final straight segment before the arrowhead is longer;
   - the arrowheads no longer sit uncomfortably close to the last corner.
