# Campaign Results PDF Requirement

## Overview

The user requested an extension to the current training-campaign reporting workflow.

In addition to the Markdown post-training results report, the final campaign report should also be produced as a PDF.

The user also requested that this become a permanent repository rule for future campaign-result reporting work.

This request affects:

- the current in-progress technical plan for the mixed-campaign final report;
- the permanent workflow instructions for future campaign-result reports.

## Technical Approach

The repository already has an established styled PDF direction and a golden-standard analytical PDF:

- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`

The new rule should extend that discipline to final campaign-results reports.

Proposed permanent rule:

1. the canonical content source remains the Markdown report in `doc/reports/campaign_results/`;
2. every final campaign-results report must also be exported to PDF;
3. the exported PDF must follow the existing restrained professional style direction already established by the analytical golden standard;
4. the real exported PDF must be validated before the task is considered complete.

This means future campaign-results work should no longer stop at the Markdown artifact alone.

For the currently pending mixed-campaign final report, the implementation should therefore include:

- the Markdown report in `doc/reports/campaign_results/`;
- a styled PDF export of that same report;
- a brief validation check of the produced PDF layout.

## Involved Components

- `README.md`
  Main project document that should reference this technical document and later reflect the stronger reporting rule after approval.
- `doc/README.md`
  Internal documentation index that should also reference this technical document.
- `AGENTS.md`
  Main repository instruction file that should be updated after approval to encode the new campaign-results PDF rule.
- `doc/technical/2026-03-13/2026-03-13-20-43-20_mixed_campaign_results_report_and_best_feedforward_config.md`
  Current technical document for the mixed-campaign final report that should be refined after approval.
- `doc/reports/campaign_results/`
  Target folder for canonical Markdown result reports and their PDF counterparts.
- `scripts/reports/generate_styled_report_pdf.py`
  Existing report-export utility that may be reused for campaign-results PDFs.
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
  Current PDF golden standard that should remain the visual direction reference.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, update the current mixed-campaign reporting technical document so the final deliverables explicitly include a PDF export.
3. Update the permanent repository rules so future campaign-results reports always require:
   - the Markdown report;
   - the PDF export;
   - post-export PDF validation.
4. Apply the rule immediately to the mixed-campaign final report task once its technical document is updated and approved.
