# Professional Blue PDF Report Redesign

## Overview

The user requested a second, stricter redesign of the styled PDF report:

- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`

The first styled redesign improved the report substantially compared to the original plain-text-like PDF, but the user identified several professional-layout issues that still need correction.

The requested new direction is explicit:

- use a restrained blue-based palette;
- keep a white page background;
- preserve rounded boxes where useful;
- remove empty or weak heading transitions;
- improve content flow around sub-sections such as `Baseline` and its following blocks;
- reduce oversized typography and decorative emphasis;
- make the document feel professional, serious, and readable rather than visually loud.

## Technical Approach

The existing export pipeline should remain reusable:

- `scripts/reports/generate_styled_report_pdf.py`

The required work is therefore a layout-system redesign, not a tool replacement.

The redesign should target five concrete areas.

### 1. Color System

The new PDF should use a restrained blue palette derived from the user-provided colors:

- `#16193B`
- `#35478C`
- `#4E7AC7`
- `#7FB2F0`
- `#ADD5F7`

The palette should be applied conservatively:

- deep blue for headings and key accents;
- medium blue for borders, badges, separators, or table headers;
- lighter blues only for subtle emphasis, not for dominant page fills.

The page background itself should remain white.

### 2. Typography And Visual Tone

The current typography is too large and too visually insistent for a professional technical report.

The redesign should therefore:

- use a more standard, professional type stack;
- reduce title, section, and body sizes;
- improve spacing without oversized text;
- keep the overall tone serious rather than decorative.

### 3. Section Flow And Orphan Headings

The current renderer can leave headings visually detached from their real content, for example:

- `Configuration Entries Explained One By One`

when the visible page break makes it appear empty, with the real content starting only on the next page.

The redesign should improve page-flow rules so that:

- section headings stay visually attached to the start of their content;
- subsection labels such as `Baseline` are not left hanging awkwardly before `Strengths`;
- grouped blocks remain readable and intentional.

This likely requires better print CSS rules such as:

- `break-inside: avoid` for specific heading-content groups;
- more careful spacing and card splitting;
- possibly reducing unnecessary wrapper headings altogether.

### 4. Semantic Emphasis

The current label treatment is too aggressive in places, especially for words like:

- `MEANING`

The user correctly pointed out that the configuration key itself, such as:

- `paths.dataset_root`

should be the visual focus, not the helper label.

The redesign should therefore either:

- remove helper labels like `Meaning`, `What it does`, `Effect on training` when they add noise;
- or restyle them to become much lighter and less attention-grabbing.

The final decision should be made based on readability, not on preserving the current visual convention.

### 5. Table Fit And Readability

The `Configurations` table currently does not use the page width well enough.

The redesign should ensure that:

- the table fits the printable page cleanly;
- column sizing is more intentional;
- text remains readable without looking cramped;
- the table still feels like part of the report rather than a pasted spreadsheet.

If necessary, the export should introduce:

- smaller table font sizing than the body;
- tighter cell spacing;
- controlled word wrapping for long columns;
- explicit width hints per column.

## Involved Components

- `README.md`
  Main project document that must reference this technical document.
- `doc/README.md`
  Internal documentation index that must include this technical document.
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md`
  Canonical Markdown content source that should remain the report source of truth.
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
  Final PDF artifact to regenerate with the corrected professional design.
- `scripts/reports/generate_styled_report_pdf.py`
  Existing report-export utility that should be refined rather than replaced.
- `doc/guide/project_usage_guide.md`
  User-facing guide that may need a small update if the export workflow or output assumptions change.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, update the styled export pipeline to use the requested professional blue palette and white page background.
3. Reduce the visual aggressiveness of the typography and section-label system.
4. Improve page-flow behavior so headings and subsection blocks do not appear visually orphaned.
5. Redesign the table layout so the `Configurations` table fits the printable page more cleanly.
6. Regenerate the target PDF and verify readability through a local visual check.
7. Update the usage guide only if the export workflow or its documented assumptions materially change.
8. Create the required Git commit immediately after the approved redesign is completed.
