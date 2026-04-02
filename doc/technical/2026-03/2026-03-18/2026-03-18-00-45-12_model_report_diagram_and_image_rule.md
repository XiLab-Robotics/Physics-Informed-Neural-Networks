# Model Report Diagram And Image Rule

## Overview

This document formalizes a new documentation rule for future model-explanatory reports in this repository.

When the user asks for conceptual maps, model descriptions, or architecture explanations, the resulting report should not remain text-only. It should also include visual explanatory material integrated into both the Markdown report and the final PDF.

The goal is to make each model understandable at a glance through both:

- written technical explanation;
- explicit visual diagrams or schematic images.

## Technical Approach

Future model-explanatory reports should include one or more generated images that support the textual explanation.

These images should be used for:

- conceptual maps;
- network schematics;
- branch decompositions;
- data-flow summaries;
- model-family positioning diagrams when useful.

The report should not rely only on prose for the conceptual map if a compact visual summary would materially improve readability.

The rule should cover two levels:

1. content rule
   Every model-explanatory report should contain visual explanatory material whenever the user asks for conceptual maps, network schematics, or architecture framing.

2. integration rule
   The generated image assets should be inserted into the Markdown report and preserved in the exported PDF so the final deliverable remains visually self-contained.

This implies that future implementation work may need:

- a standard location for model-report image assets;
- a predictable naming convention for the generated images;
- explicit support in the Markdown-to-PDF export path for embedded images when not already available.

## Involved Components

This rule will affect:

- `AGENTS.md`
  Persistent workflow rules for future model-report generation.

- `README.md`
  Main documentation index for the technical rule.

- `doc/README.md`
  Internal documentation index for the technical rule.

- future model-explanatory reports under `doc/reports/analysis/`
  These reports will need to include visual assets when requested or when clearly useful.

- future report asset locations under `doc/reports/analysis/` or a dedicated sibling asset folder
  The image files should remain close to the report they document.

- `scripts/reports/generate_styled_report_pdf.py`
  This exporter may need explicit support or verification for embedded report images.

## Implementation Steps

1. Add a persistent rule requiring visual explanatory material in future model-explanatory reports when conceptual maps or schematic explanations are requested or clearly useful.
2. Clarify that the images must be integrated into both the Markdown report and the final PDF deliverable.
3. Clarify that image assets should be stored in a consistent and discoverable report-local location.
4. Treat image integration as part of the report task, not as an optional post-processing step.
5. When needed in future tasks, extend the PDF export workflow so embedded images render correctly in the final PDF.
6. Reference this technical rule document from `README.md` and `doc/README.md`.
