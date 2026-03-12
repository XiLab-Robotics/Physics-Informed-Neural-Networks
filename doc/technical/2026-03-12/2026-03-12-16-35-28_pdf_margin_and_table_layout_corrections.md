# PDF Margin And Table Layout Corrections

## Overview

The user requested a focused correction pass on the redesigned analytical PDF:

- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`

The current blue redesign is much closer to the requested professional look, but the user identified remaining layout defects that are not acceptable in a final technical report.

The issues to fix are explicit:

- the right page margin still clips the rounded rectangle border;
- the main configuration table still has header and wrapping problems;
- some column separators or visual boundaries are unclear;
- words such as `Workers` and `Patience` are broken awkwardly across lines;
- table headers should be centered both horizontally and vertically;
- splitting the configuration data into two tables is now preferred if that makes the report cleaner and more legible.

## Technical Approach

This should be treated as a print-layout correction pass on the existing export pipeline:

- `scripts/reports/generate_styled_report_pdf.py`

The goal is not to redesign the whole PDF again, but to stabilize the current design so it behaves correctly on the printed A4 page.

### Margin And Page Width Corrections

The current report still allows some horizontal content to reach too close to the printable edge, to the point that the right border can appear clipped.

The correction should therefore:

- increase the effective safe area on the right;
- ensure section cards and table wrappers never visually exceed the printable width;
- verify that border radius and stroke remain fully visible.

This likely requires a tighter combination of:

- `@page` margins;
- body or shell internal width constraints;
- table wrapper sizing;
- box-sizing and overflow handling.

### Table Redesign

The current single `Configurations` table is now too dense for a clean professional presentation.

The user proposed a good direction:

- split the current table into two coordinated tables.

The most sensible split is:

1. a **campaign summary** table
   covering:
   - config name;
   - status;
   - main intent;
2. a **technical settings** table
   covering:
   - curve batch;
   - point stride;
   - max points per curve;
   - workers;
   - pin memory;
   - hidden layers;
   - epoch budget;
   - patience.

This split should improve:

- width usage;
- header readability;
- professional scanning;
- reduced word-breaking pressure.

### Header And Cell Alignment Rules

The user explicitly requested:

- header text centered horizontally;
- header text centered vertically;
- no awkward line breaks such as:
  - `Wo` / `rkers`
  - `Pat` / `ience`

The corrected table design should therefore:

- prevent broken header words;
- assign realistic minimum widths to narrow-but-important columns;
- allow row content to wrap only where acceptable;
- keep the header row visually stable and aligned.

### Separator And Border Clarity

The user also noticed a missing or unclear white divider in the header area between columns such as `Curve Batch` and `Point Stride`.

The table styling should therefore improve:

- visible column separation in the header;
- consistent stroke contrast between header cells;
- clean internal grid lines without becoming visually heavy.

## Involved Components

- `README.md`
  Main project document that must reference this technical document.
- `doc/README.md`
  Internal documentation index that must include this technical document.
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
  Final PDF artifact to regenerate with corrected margins and improved table layout.
- `scripts/reports/generate_styled_report_pdf.py`
  Existing styled PDF exporter that must be updated for the margin and table corrections.
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md`
  Canonical Markdown report source that remains the content source of truth.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, correct the effective printable margins so no rounded border or card edge is visually clipped.
3. Replace the current single `Configurations` table with a cleaner split-table solution if that gives the best readability.
4. Ensure table headers are centered horizontally and vertically.
5. Prevent awkward word breaks in column headers and other short table labels.
6. Improve header cell dividers and internal table separation where needed.
7. Regenerate the PDF and verify the corrected layout through a local visual check.
8. Create the required Git commit immediately after the approved correction pass is completed.
