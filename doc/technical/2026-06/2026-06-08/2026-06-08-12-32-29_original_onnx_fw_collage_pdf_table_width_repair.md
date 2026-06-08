# Original ONNX Forward Collage PDF Table Width Repair

## Overview

This technical note covers a narrow PDF layout repair for the `Track 2`
original `ONNX` forward collage report:

`doc/reports/analysis/track2/original_onnx_fw_collage_report/[2026-06-05]/track2_original_onnx_fw_collage_report.pdf`

The requested correction is to apply the usual table-width adjustments so the
PDF tables fit cleanly inside the styled report cards without crushed
identifier columns, excessive wrapping, or right-edge pressure.

This is a report-layout task only. It must not change the `ONNX` inference
logic, the `19` loaded target models, curve reconstruction, or reported metric
values.

No subagent is planned.

## Technical Approach

The repair will inspect the real exported PDF raster pages and then adjust the
report Markdown or report builder output so the problematic tables are PDF
friendly by construction. The preferred fixes are:

- keep long file paths and full traceability in YAML and CSV artifacts;
- use compact display labels in PDF tables;
- avoid long monospace cells where they force narrow wrapped columns;
- rebalance table columns by replacing verbose identifiers with short labels;
- regenerate the Markdown, PDF, and validation page images after every layout
  change.

The likely implementation point is
`scripts/reports/analysis/build_track2_original_onnx_fw_collage_report.py`,
because the report is generated from that script. If the PDF exporter itself
already has a reusable table-width helper suitable for this report, the repair
may reuse it instead of adding ad hoc formatting.

## Involved Components

- `scripts/reports/analysis/build_track2_original_onnx_fw_collage_report.py`
- `doc/reports/analysis/track2/original_onnx_fw_collage_report/[2026-06-05]/track2_original_onnx_fw_collage_report.md`
- `doc/reports/analysis/track2/original_onnx_fw_collage_report/[2026-06-05]/track2_original_onnx_fw_collage_report.pdf`
- `doc/reports/analysis/track2/original_onnx_fw_collage_report/[2026-06-05]/assets/`
- `output/validation_checks/track2_original_onnx_fw_collage_report/`
- `doc/README.md`

PDF export and validation will use the repository-owned entry points:

- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/validate_report_pdf.py`

## Implementation Steps

1. Rasterize the current PDF and inspect the pages with table-width issues.
2. Adjust the report builder so generated Markdown uses compact PDF-facing
   table labels while preserving full path information in YAML and CSV.
3. Regenerate the report Markdown and PDF.
4. Rasterize the regenerated PDF and inspect the real pages for table fit,
   clipped borders, wrapped headers, and right-edge pressure.
5. Run Markdown QA on touched Markdown files.
6. Run Python compilation checks on touched scripts.
7. Run Sphinx if portal-facing documentation is affected.
