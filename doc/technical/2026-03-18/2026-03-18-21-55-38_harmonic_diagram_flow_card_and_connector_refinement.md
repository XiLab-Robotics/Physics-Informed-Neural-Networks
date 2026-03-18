# Harmonic Diagram Flow Card And Connector Refinement

## Overview

This document defines a targeted repair pass for the harmonic-regression explanatory diagrams:

- `harmonic_regression_model_diagram.svg`
- `harmonic_regression_model_architecture_diagram.svg`

The current harmonic diagrams still show two classes of defects that should already have been reduced by the latest generator improvements, but are still visible in the current harmonic-specific compositions:

1. the vertical internal arrows in several flow cards still cover or visually crowd the sub-boxes and their labels;
2. some external connectors still use unnecessary 90-degree routing where a simpler straight or less forced connector should be possible.

The affected regions are:

- `Harmonic Basis` in the conceptual harmonic diagram;
- `Coefficient Resolver` in the conceptual harmonic diagram;
- `Conditioning Path` in the harmonic architecture diagram;
- some box-to-box links in the harmonic architecture diagram that currently bend at 90 degrees without adding readability.

The goal of this pass is to apply the already improved spacing and connector rules consistently to the harmonic diagrams, and to remove avoidable elbow routing where a more direct connection is visually cleaner.

## Technical Approach

### 1. Flow-Card Spacing In The Harmonic Conceptual Diagram

The current conceptual harmonic flow cards still rely on compact default geometry:

- `Harmonic Basis` has four internal rows in a relatively short card;
- `Coefficient Resolver` has three internal rows in a similarly compact card.

Even though `draw_flow_card()` now supports larger spacing and better connector guardrails, those harmonic cards are still using the default layout parameters, which leaves the internal arrows too short and too close to the row boxes.

This pass should:

- assign explicit harmonic-specific `flow_gap` and note spacing where needed;
- increase card height if needed rather than compressing the row stack;
- preserve visual balance with the surrounding boxes.

### 2. Flow-Card Spacing In The Conditioning Branch

The `Conditioning Path` card in the harmonic architecture diagram still uses the compact two-row default flow-card layout, which leaves the internal arrow too close to both rows.

This pass should:

- give the branch card more vertical room;
- increase the inter-row spacing enough to show a clear line segment rather than mostly an arrowhead;
- preserve readable note-free branch geometry without crowding the lower canvas area.

### 3. Remove Unnecessary 90-Degree Connectors

In the harmonic architecture diagram, some connectors currently use orthogonal bends despite not needing obstacle avoidance.

The current examples include:

- the connector from `Angle Input` to `Basis Features`;
- the connector from `Coefficient Vector` to `Multiply`.

These links should be reviewed individually.

If a straight connector becomes possible through:

- better vertical alignment;
- different source or target side selection;
- slightly improved block placement;

then the elbow should be removed.

The objective is not to ban orthogonal routing globally, but to avoid it when it adds no clarity and only makes the diagram look artificially bent.

### 4. Permanent Guardrails

The recent feedforward fixes showed that the generator already has the right primitives, but some model-specific diagrams still need to opt into them explicitly.

This pass should therefore keep the fix at the generator-definition level by:

- using the richer `draw_flow_card()` parameters in the harmonic-specific builders;
- preferring derived connector geometry over ad hoc elbow paths when straight routing is feasible;
- keeping layout assertions where useful to prevent future regressions.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  for harmonic-specific flow-card spacing and connector-layout tuning;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/harmonic_regression_model_diagram.svg`
  which will be regenerated;
- `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/harmonic_regression_model_architecture_diagram.svg`
  which will be regenerated;
- possibly `doc/scripts/reports/generate_model_report_diagrams.md`
  if the documented layout guarantees need to mention the broader harmonic adoption of the newer spacing rules.

No training code, model logic, or campaign artifacts should be changed by this pass.

## Implementation Steps

1. Refine `Harmonic Basis` flow-card spacing in the conceptual harmonic diagram.
2. Refine `Coefficient Resolver` flow-card spacing in the conceptual harmonic diagram.
3. Refine `Conditioning Path` flow-card spacing in the harmonic architecture diagram.
4. Review the harmonic architecture connectors and remove unnecessary 90-degree bends where straight routing is feasible.
5. Regenerate the two harmonic SVG diagrams.
6. Inspect the regenerated SVGs directly to confirm:
   - internal arrows no longer cover row labels or row boxes;
   - the harmonic flow cards show clear connector shafts;
   - avoidable elbow routing has been removed;
   - the overall composition remains balanced.
