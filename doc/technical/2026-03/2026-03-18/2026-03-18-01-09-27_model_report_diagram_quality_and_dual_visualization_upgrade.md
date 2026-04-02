# Model Report Diagram Quality And Dual Visualization Upgrade

## Overview

This document defines the corrective work required for the newly generated model-report diagrams and PDFs.

The current output revealed three concrete issues:

1. some diagram labels overflow their boxes, which is the same class of layout defect previously addressed in the PDF workflow;
2. the figure container styling in the PDF clashes visually with the white-background diagrams;
3. the reports currently include only conceptual diagrams, while they should also include more explicit architecture diagrams that show the internal network structure and connection logic.

This work will correct the current four structured-model reports and improve the workflow for future diagram generation.

## Technical Approach

The corrective approach should address both the assets and the generation workflow.

### 1. Diagram Quality Control

Future generated diagrams must be checked after creation, not assumed correct.

The new workflow should therefore include:

- generation of the diagram asset;
- immediate visual verification that:
  - labels stay inside their boxes;
  - spacing is balanced;
  - no box boundaries are violated;
  - the figure remains readable at report scale.

This rule should be treated similarly to PDF validation: the asset is not complete until the actual generated visual is checked.

### 2. Reusable Diagram Generator

For this repository, the most practical choice is to build a small repository-owned Python generator for these diagrams instead of drawing them ad hoc every time.

Reasons:

- future model families will need the same kind of explanatory assets;
- consistency across diagrams is easier to maintain;
- text fitting and layout tuning can be centralized;
- corrections can be applied once and regenerated systematically.

The generator should remain lightweight and deterministic rather than introducing a heavy graphics stack unless necessary.

### 3. Figure Styling In PDF

The current figure wrapper background should be changed.

The visual direction should be:

- no blue-tinted panel behind a white image;
- clean white figure background;
- optional subtle border only if needed;
- caption styling that supports the image without competing with it.

This should keep the figure integrated with the report while avoiding the current visual clash.

### 4. Dual Diagram Requirement

Each model report should contain two complementary diagrams:

1. conceptual diagram
   Explains the model family logic, branch decomposition, or functional flow.

2. architecture diagram
   Explains the actual network or computational structure more concretely, including examples of how layers, branches, neurons, or feature blocks are connected.

This is especially important for:

- `feedforward`
- `periodic_feature_network`
- `residual_harmonic_network`

For `harmonic_regression`, the architecture-style diagram should show the effective computational graph even if it is not a dense neural network in the classical sense.

## Involved Components

The work will affect:

- the four explanatory reports in `doc/reports/analysis/`
- the current diagram assets under `doc/reports/analysis/assets/`
- `scripts/reports/generate_styled_report_pdf.py`
  Figure styling and PDF integration.

Potentially, the work should also add:

- a dedicated lightweight diagram-generation script under `scripts/reports/` or another suitable repository-owned location
  to generate and regenerate model-report diagrams consistently.

- `doc/guide/project_usage_guide.md`
  if the repository now exposes an explicit reusable diagram-generation workflow.

## Implementation Steps

1. Introduce a reusable repository-owned diagram-generation workflow for model-report images.
2. Regenerate the existing structured-model diagrams with corrected text fitting and spacing.
3. Add an explicit visual quality-check step for generated diagrams.
4. Produce two diagrams per model report:
   - conceptual diagram;
   - architecture/network-structure diagram.
5. Update the Markdown reports to include both diagrams where appropriate.
6. Remove the blue-tinted figure background from the PDF figure container styling and keep a cleaner neutral presentation.
7. Regenerate the four PDFs.
8. Revalidate the real exported PDFs after the updated images are embedded.
