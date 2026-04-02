# PDF Export For Existing Model Explanatory Reports

## Overview

This document defines the work required to export the newly created model-explanatory reports to styled PDF artifacts and validate the real exported PDFs.

The scope covers the four explanatory reports already added for the implemented structured TE models:

- `feedforward`
- `harmonic_regression`
- `periodic_feature_network`
- `residual_harmonic_network`

The goal is to make these reports available both as Markdown and as validated PDF deliverables, aligned with the repository PDF rules.

## Technical Approach

The repository already contains the required tooling:

- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`

The work therefore does not require a new exporter. It requires:

1. exporting one styled PDF per explanatory report;
2. validating each real PDF artifact through page rasterization;
3. checking that the generated PDFs remain readable and consistent with the restrained project report style;
4. indexing the newly generated `.pdf` artifacts in the documentation indexes.

The explanatory reports are simpler than the large comparison reports already handled by the exporter, so the main risks are not complex table balancing but:

- section-card flow;
- page-break cleanliness;
- code/identifier rendering;
- general readability of list-heavy technical content.

## Involved Components

The export and validation work will involve:

- `doc/reports/analysis/2026-03-18-00-31-18_feedforward_model_explanatory_report.md`
- `doc/reports/analysis/2026-03-18-00-31-58_harmonic_regression_model_explanatory_report.md`
- `doc/reports/analysis/2026-03-18-00-32-37_periodic_feature_network_model_explanatory_report.md`
- `doc/reports/analysis/2026-03-18-00-33-16_residual_harmonic_network_model_explanatory_report.md`

- `scripts/reports/generate_styled_report_pdf.py`
  Styled PDF export utility.

- `scripts/reports/validate_report_pdf.py`
  Real-PDF rasterization validation utility.

- `README.md`
  Main documentation index.

- `doc/README.md`
  Internal documentation index.

## Implementation Steps

1. Export one styled PDF for each of the four model-explanatory Markdown reports.
2. Store the PDFs beside the corresponding Markdown files in `doc/reports/analysis/`.
3. Validate each real exported PDF with `scripts/reports/validate_report_pdf.py`.
4. Inspect the validation output for readability and layout discipline.
5. Add the resulting `.pdf` files to `README.md` and `doc/README.md`.
6. Report completion only after the PDF exports and validation artifacts both exist.
