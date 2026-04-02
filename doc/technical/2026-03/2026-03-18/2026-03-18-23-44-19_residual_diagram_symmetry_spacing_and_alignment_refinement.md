# Residual Diagram Symmetry Spacing And Alignment Refinement

## Overview

This document defines a targeted repair pass for the two residual-harmonic explanatory diagrams:

- `residual_harmonic_network_model_architecture_diagram.svg`
- `residual_harmonic_network_model_diagram.svg`

The current residual diagrams still show several layout defects that were already solved in the feedforward, harmonic, and periodic builders, but have not yet been applied consistently to the residual builders.

The reported issues are:

1. the internal vertical arrows in `Structured Path` and `Residual Path` are still too short and overlap the row labels and row boxes;
2. the same internal-arrow crowding also remains in `Structured Branch` and `Residual Branch`;
3. in the conceptual residual diagram, the `Shared Input` body text line `Common input to both branches` is still broken badly and visually escapes the intended box layout;
4. the connectors from `Shared Input` to the upper and lower branches are not symmetric;
5. the connectors from the upper and lower branch outputs into `Add` are also not symmetric;
6. `Shared Input`, `Add`, and the terminal output box should be vertically centered on the same horizontal axis;
7. the residual neural stack has lost its dense neuron-to-neuron connection lines;
8. the connector `Structured Path -> Structured Output` still uses an unnecessary 90-degree elbow;
9. the connector `Add -> TE` or `Add -> Outputs` still contains an unnecessary 90-degree bend.

The goal of this pass is to make both residual diagrams visually symmetric, vertically centered around the main merge axis, and consistent with the newer generator behavior already used successfully in the other model families.

## Technical Approach

### 1. Apply The Updated Flow-Card Spacing To Both Residual Builders

The residual flow cards still use compact default spacing. This causes the internal arrows to collapse down to almost only the arrowhead.

This pass should:

- use the richer `draw_flow_card()` spacing parameters already introduced earlier;
- increase vertical gaps between rows in:
  - `Structured Branch`
  - `Residual Branch`
  - `Structured Path`
  - `Residual Path`
- preserve readable note clearance below the final row.

### 2. Rebuild The Residual Layout Around A Shared Centerline

The residual diagrams should read around a central merge axis.

This pass should:

- align `Shared Input`, `Add`, and the terminal output card (`TE` or `Outputs`) on the same vertical center;
- keep the upper structured branch and lower residual branch mirrored around that centerline;
- make the input connectors from `Shared Input` into the two branches geometric mirror images of each other;
- make the two branch-to-merge connectors into `Add` geometric mirror images as well.

### 3. Restore Dense Residual MLP Connectivity

The residual architecture builder currently draws the residual neural stack without inter-layer connection lines.

This pass should:

- enable dense neuron-to-neuron connections in the residual neural backbone;
- use plain lines without arrowheads, consistent with the architecture-style diagrams already repaired earlier.

### 4. Straighten The Connectors That Do Not Need Elbows

Several residual connectors are still serialized as orthogonal paths even when the elements can be aligned well enough to use straight arrows.

This pass should:

- make `Structured Path -> Structured Output` straight;
- make `Add -> TE` straight;
- make `Add -> Outputs` straight in the conceptual diagram;
- keep orthogonal routing only where it still communicates the branch split or merge more clearly.

### 5. Fix The `Shared Input` Text Fit

The conceptual residual `Shared Input` card still carries a long phrase that is currently split across two awkward lines.

This pass should:

- rebalance the `Shared Input` card layout so the body text fits cleanly;
- avoid text overflow beyond the intended visual box;
- preserve the semantics that the same input feeds both branches.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for residual-specific spacing, alignment, symmetric routing, and neural-stack connectivity;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/residual_harmonic_network_model_architecture_diagram.svg`
  which will be regenerated;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/residual_harmonic_network_model_diagram.svg`
  which will be regenerated.

No training code, model logic, or report PDF should change in this pass.

## Implementation Steps

1. Increase flow-card spacing in the residual conceptual and architecture builders.
2. Re-center `Shared Input`, `Add`, and the terminal output cards on the common merge axis.
3. Rebuild the two `Shared Input -> branch` connectors as mirrored symmetric routes.
4. Rebuild the two `branch -> Add` connectors as mirrored symmetric routes.
5. Restore dense residual-neural connection lines in the architecture diagram.
6. Replace unnecessary elbows with straight arrows where the geometry allows it.
7. Refit the `Shared Input` text in the conceptual diagram.
8. Regenerate the two residual SVG diagrams.
9. Inspect the regenerated SVGs directly to confirm:
   - flow-card arrows no longer overlap labels or row boxes;
   - symmetric connectors are actually mirrored;
   - `Shared Input`, `Add`, and the output boxes share the same centerline;
   - the residual neural stack shows dense connection lines again;
   - no unnecessary elbow remains on the direct output connectors.
