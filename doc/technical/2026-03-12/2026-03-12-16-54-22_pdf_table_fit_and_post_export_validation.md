# PDF Table Fit And Post-Export Validation

## Overview

The user reported that the latest regenerated analytical PDF is improved but still not acceptable:

- in the `Technical Settings` table of
  `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
  the `Patience` header is still clipped or wrapped poorly;
- the report still shows that horizontal fit and safe print margins are not being controlled strictly enough;
- future PDF correction passes must include an explicit visual re-check of the exported PDF, not only HTML/CSS reasoning.

The goal of this pass is therefore narrower and stricter than the previous redesigns:

- guarantee that the `Technical Settings` table fits within the printable page area;
- prevent clipped borders and clipped table content;
- ensure short column headers remain fully readable;
- introduce a reliable final verification step on the real exported PDF output.

## Technical Approach

The correction should remain inside the current PDF export pipeline:

- `scripts/reports/generate_styled_report_pdf.py`

The issue is no longer overall styling quality. It is now a print-layout correctness issue.

### Table Width Rebalancing

The current split-table solution is directionally correct, but the technical table is still too dense for the chosen page width and font sizing.

This pass should rebalance the table more aggressively. The likely options are:

1. adjust technical column widths again so short headers such as `Workers` and `Patience` get enough guaranteed width;
2. reduce technical-table font size slightly if needed, but only if readability remains professional;
3. reduce horizontal padding inside technical-table header and body cells;
4. if still needed, split the technical table into two smaller technical tables rather than forcing a cramped single one.

The preferred solution is the smallest change that removes clipping while keeping the document professional.

### Safe Printable Area

The user explicitly asked for stronger attention to margins. This means the exporter should treat the A4 page as having a stricter safe content width than the nominal page width.

This correction may require:

- slightly larger right-side safety constraints;
- stricter `max-width` behavior on section cards and table wrappers;
- preventing any table from visually reaching the edge even when borders and rounded corners are rendered by Chrome PDF.

### Post-Export Verification Rule

The user also asked for a stronger validation habit:

- after each PDF regeneration, re-check the real PDF output and confirm that the layout is correct.

For this correction pass, that means:

1. regenerate the HTML and PDF;
2. inspect the generated structure for the technical table;
3. verify the final exported PDF output visually, with attention to:
   - right border visibility;
   - `Technical Settings` header fit;
   - full readability of `Patience`, `Workers`, and similar columns;
   - no clipped rounded rectangle edges.

## Involved Components

- `README.md`
  Main project index that must reference this technical document.
- `doc/README.md`
  Documentation index that must reference this technical document.
- `scripts/reports/generate_styled_report_pdf.py`
  Styled PDF generator that controls the table split, page sizing, and final export behavior.
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
  Target PDF artifact to regenerate and validate.
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md`
  Canonical Markdown source that remains unchanged unless content-level fixes become necessary.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, refine the technical table layout so no header is clipped or awkwardly wrapped.
3. Tighten safe-width handling and margins if the technical table or borders still approach the printable edge.
4. Regenerate the analytical PDF with the corrected exporter.
5. Re-check the real exported PDF and confirm that the problematic technical-table header cells are fully readable.
6. Commit the approved correction with a commit message aligned to the repository style.
