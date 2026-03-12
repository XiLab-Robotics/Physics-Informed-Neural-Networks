# PDF Golden Standard And Report Style Rules

## Overview

The user requested two related repository updates:

1. treat the current analytical PDF
   `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
   as the project **golden standard** for future styled technical reports;
2. add persistent rules so future reports are generated with the same style discipline and the same level of layout care.

This request is not about changing the current report content again. It is about turning the current approved visual result into a reusable project standard.

## Technical Approach

The change should formalize the current PDF as the canonical style reference and encode the associated rules in the repository instructions and documentation.

### Golden Standard Definition

The current PDF should be referenced explicitly as the approved visual benchmark for:

- color palette;
- white background with restrained blue accents;
- rounded section cards;
- readable A4-safe margins;
- structured configuration tables;
- professional, non-flashy styling;
- mandatory post-export inspection.

The corresponding Markdown source and exporter implementation should also be referenced, but the PDF itself should be named as the visual target.

### Persistent Style Rules

The project instructions should require future report generation to preserve the same report-design principles:

- use the current approved blue palette and restrained professional tone;
- keep page background white;
- prefer clear hierarchy over decorative styling;
- preserve A4-safe spacing and border visibility;
- avoid clipped content, wrapped headers, and overcrowded tables;
- repeat key row anchors such as `Config` when tables are split;
- prefer centered alignment when it improves comparison readability in configuration matrices;
- perform a post-export validation of the real PDF, not only the HTML source.

### Documentation Updates

The style standard should be documented in the places that the repository already uses for durable rules:

- `AGENTS.md`
- `README.md`
- `doc/README.md`

If needed, a short section can also be added to the usage/documentation guidance so future report generation follows a stable workflow.

## Involved Components

- `AGENTS.md`
  Main persistent repository instructions that should carry the new report-style rules.
- `README.md`
  Main project index that must reference this technical document and may reference the golden standard report.
- `doc/README.md`
  Documentation index that must reference this technical document and the report-style convention.
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
  Approved PDF to designate as the visual golden standard.
- `scripts/reports/generate_styled_report_pdf.py`
  Existing exporter that already implements the approved visual direction and may be referenced as the generation path for future reports.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, designate the current analytical PDF as the golden standard report in the repository documentation.
3. Add persistent report-style rules to `AGENTS.md` so future analytical PDFs are expected to match this design quality and structure.
4. Update the relevant documentation indexes to reference the golden standard and the new rule set.
5. Commit the approved documentation and instruction updates with a repository-aligned commit message.
