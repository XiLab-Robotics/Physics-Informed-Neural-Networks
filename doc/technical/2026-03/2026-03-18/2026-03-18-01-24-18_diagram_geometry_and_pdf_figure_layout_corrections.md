# Diagram Geometry And PDF Figure Layout Corrections

## Overview

This document defines the next correction pass for the structured-model explanatory diagrams and their PDF integration.

The current generated assets improved the first version, but they still contain several real layout defects:

1. some labels still collide with header regions or exceed their intended content area;
2. some cards look top-aligned instead of visually centered and balanced;
3. neuron-to-neuron connections start from circle centers and cross the neuron labels;
4. some connectors behave visually like plain lines instead of clear arrows;
5. some diagrams still contain literal textual arrow tokens such as `->` inside labels;
6. some routed connectors cross cards or pass too close to unrelated boxes;
7. the overall figure composition still needs stronger centering and page-friendly placement.

This work should correct the existing four model-report diagram sets and harden the reusable generation workflow so the same class of defects does not reappear later.

## Technical Approach

The correction should be handled at the geometry and rendering level, not by hand-editing a few isolated SVG files.

### 1. Geometry-Safe Card Layout

The diagram generator should treat each card as a real layout region with:

- an isolated header band;
- a separate content band below the header;
- vertical centering or balanced spacing inside the content band;
- text fitting that is checked against the usable inner content area rather than the whole card rectangle.

This is required to avoid cases where content is technically inside the outer box but visually hidden behind the header block.

### 2. Proper Connectors

Dense-network connectors should be drawn as true arrows when the visual intent is directional.

The revised connector rules should include:

- arrowheads for directional links;
- connection anchor points on the border of neuron circles instead of the center;
- routing that avoids crossing text or overlapping unrelated cards whenever practical;
- explicit support for straight, elbow, or routed connectors depending on the diagram.

This is especially important for the feedforward, periodic-feature, and residual-harmonic architecture diagrams.

### 3. No Textual Fake Arrows Inside Cards

Labels such as `Linear -> LayerNorm? -> ...` should not rely on ASCII arrow tokens inside the visual diagram.

Instead, the diagrams should use either:

- stacked pipeline bullets or rows inside the card; or
- real mini-connectors between sub-elements; or
- clean multiline text without pseudo-graphics.

The same rule applies to conditioning-path cards and other internal flow summaries.

### 4. Stronger Visual Balance

The figures should be recomposed so that:

- cards are centered more cleanly on the page;
- card contents are vertically balanced;
- input and conditioning blocks are not awkwardly top-loaded;
- spacing between cards is consistent;
- the resulting SVG looks intentional both inside Markdown preview and inside the exported PDF.

### 5. PDF Figure Placement Discipline

The PDF exporter should preserve a neutral figure container and avoid extra styling that fights the white-background SVGs.

The figure layout should keep:

- centered images;
- clean caption separation;
- no tinted panel behind the image;
- page-safe spacing so figures do not feel cramped or off-center.

### 6. Validation Standard

The diagram workflow should now be treated similarly to the PDF workflow:

- generate the SVG;
- inspect the real SVG result;
- inspect the embedded PDF result;
- only then consider the artifact complete.

Validation must explicitly check:

- no header overlap;
- no text outside boxes;
- no clipped labels;
- no literal `->` pseudo-arrows used as visual connectors;
- no connector crossing through neuron labels;
- no obvious off-center figure composition.

## Involved Components

The work will affect:

- `scripts/reports/generate_model_report_diagrams.py`
  Diagram geometry, text layout, connector routing, and quality checks.
- `scripts/reports/generate_styled_report_pdf.py`
  Figure container and image placement behavior in the PDF export.
- the explanatory reports under `doc/reports/analysis/`
  if captions or figure ordering need minor alignment updates.
- the SVG assets under `doc/reports/analysis/assets/2026-03-18_model_explanatory_diagrams/`
  which will be regenerated.
- the exported PDFs under `doc/reports/analysis/`
  which will need regeneration and revalidation.

The usage references may also need a small update if the diagram-generation workflow description changes materially.

## Implementation Steps

1. Update the diagram generator to enforce separate header/content geometry and balanced inner layout.
2. Revise dense-network connector generation so links start from neuron borders and render with real arrowheads where appropriate.
3. Replace textual pseudo-arrows inside cards with cleaner internal layout primitives.
4. Adjust routing and spacing to avoid connector overlap with unrelated cards and labels.
5. Regenerate all eight explanatory SVG diagrams.
6. Visually inspect the regenerated SVGs and fix any remaining composition defects.
7. Ensure the PDF exporter keeps the figures centered and visually neutral.
8. Regenerate the four explanatory PDFs.
9. Validate the real exported PDFs again after the new figures are embedded.
