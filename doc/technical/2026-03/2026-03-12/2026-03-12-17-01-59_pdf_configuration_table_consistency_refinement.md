# PDF Configuration Table Consistency Refinement

## Overview

The user requested one more focused correction pass on the analytical PDF:

- keep the rest of the report unchanged;
- continue using three separate tables for the configuration comparison block;
- ensure the left-most column of each table always contains the configuration name;
- make the cells visually more uniform in size;
- center the table data consistently instead of mixing alignments in an ad hoc way.

The affected target remains:

- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`

This pass is limited to the configuration-comparison tables and should not alter the rest of the report layout.

## Technical Approach

The changes should remain confined to:

- `scripts/reports/generate_styled_report_pdf.py`

The current three-table split is directionally correct, but it does not yet provide the visual consistency the user wants.

### Repeated Configuration Anchor

Each of the three tables should start with the `Config` column. This will:

- make each table readable on its own;
- reduce left-to-right scanning burden;
- improve row association across the three blocks.

The intended structure becomes:

1. `Campaign Summary`
   - `Config`
   - `Status`
   - `Main Intent`
2. `Data Pipeline Settings`
   - `Config`
   - `Curve Batch`
   - `Point Stride`
   - `Max Points/Curve`
   - `Workers`
   - `Pin Memory`
3. `Model And Schedule Settings`
   - `Config`
   - `Hidden Layers`
   - `Epoch Budget`
   - `Patience`

### Alignment Consistency

The user explicitly wants the values visually centered rather than mixed left/right alignment.

This pass should therefore:

- center the headers;
- center the body values for the configuration tables;
- avoid random-looking differences between numeric and textual columns unless there is a strong readability reason.

### Cell Proportion Consistency

The tables should look more regular and balanced.

That does not require mathematically identical widths for every column, but it does require:

- a more uniform width allocation inside each table;
- consistent padding;
- row height that feels stable across all three tables.

## Involved Components

- `README.md`
  Main project index that must reference this technical document.
- `doc/README.md`
  Documentation index that must reference this technical document.
- `scripts/reports/generate_styled_report_pdf.py`
  PDF generator that controls the split configuration table structure and styling.
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
  Final PDF artifact to regenerate.

## Implementation Steps

1. Create this technical document and register it in the project indexes.
2. After user approval, update the three configuration tables so each one begins with the `Config` column.
3. Rebalance widths and alignment so the three tables look more regular and centered.
4. Regenerate the PDF.
5. Re-check the exported PDF with specific attention to the configuration tables only.
6. Commit the approved correction with a repository-aligned commit message.
