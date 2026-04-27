# Presentation Pipeline Runner

## Overview

This script orchestrates the repository-owned Markdown-to-presentation workflow.

The canonical script path is:

- `scripts/reports/presentation/run_presentation_pipeline.py`

## Main Role

The runner coordinates:

- slide-deck generation through `scripts/reports/presentation/generate_markdown_presentation.py`;
- slide-PDF validation through `scripts/reports/pdf/validate_report_pdf.py`;
- PowerPoint-driven PDF export between those two stages.

## Practical Use

Typical usage from the repository root:

```powershell
python scripts/reports/presentation/run_presentation_pipeline.py `
  --input-markdown-path "doc/reports/analysis/[2026-03-27]/presentation.md"
```

## Notes

- the canonical presentation tooling now lives under `scripts/reports/presentation/`;
- PDF validation is shared with the styled-report pipeline under `scripts/reports/pdf/`.
