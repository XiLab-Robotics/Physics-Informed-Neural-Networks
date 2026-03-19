# Model Report Diagram Generator

## Overview

This script generates the repository-owned SVG diagrams used inside the model explanatory reports.

The script is stored in:

- `scripts/reports/generate_model_report_diagrams.py`

## Main Role

The script generates two visual assets for each currently documented model:

1. a conceptual diagram;
2. an architecture-style diagram.

The current implemented targets are:

- `feedforward`
- `harmonic_regression`
- `periodic_feature_network`
- `residual_harmonic_network`

## Main Output

The script writes SVG assets into the model-explanatory report folders under:

- `doc/reports/analysis/model_explanatory/<Model Name>/assets/`

These assets are designed to be:

- embedded directly in the Markdown reports;
- preserved in the styled PDF exports;
- regenerated consistently when the diagram style or layout is improved;
- checked against built-in layout assertions before the SVG files are accepted.

## Practical Use

Typical usage from the project root:

```powershell
conda run -n standard_ml_codex_env python scripts/reports/generate_model_report_diagrams.py
```

Use this script when:

- a model explanatory report is first created;
- a diagram layout issue must be corrected;
- the visual style of the diagrams is updated;
- the report diagrams need to be regenerated before PDF export.

For the full repository-owned report workflow, prefer the orchestration runner:

- `scripts/reports/run_report_pipeline.py`

The script is intended to keep diagram generation deterministic and repository-owned instead of relying on one-off manual SVG edits.

## Layout Guarantees

The current generator now enforces a stricter diagram-layout policy:

- card headers and card content are laid out as separate regions;
- card text is vertically balanced inside the usable content area;
- whole-slide compositions are centered below the diagram header instead of being compacted at the top;
- dense neuron-to-neuron connectivity can be rendered as distributed plain lines when arrowheads reduce readability;
- flow-card internal arrows keep explicit clearance from both the source row and the next row;
- flow cards can reserve explicit bottom clearance for their note text and minimum visible shaft length for internal arrows;
- box-to-box connectors use orthogonal routing so arrows enter and leave cards perpendicularly;
- arrowheads stop short of the target border instead of sitting on top of the card stroke;
- architecture diagrams can use straight external connectors when vertical alignment removes the need for elbow routing;
- compact cards prefer multiline wrapping and spacing over aggressive text shrinking;
- directional links use real arrowheads instead of textual pseudo-arrows inside the drawing.

If a diagram definition would overflow its available card space, the generator fails instead of silently writing a broken SVG.
