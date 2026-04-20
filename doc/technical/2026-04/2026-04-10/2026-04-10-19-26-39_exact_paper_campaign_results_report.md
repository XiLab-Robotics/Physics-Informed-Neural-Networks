# Overview

This technical document defines the final reporting pass for the completed
exact-paper model-bank campaign
`exact_paper_model_bank_campaign_2026_04_10_17_04_41`.

The campaign has now finished successfully after the `HGBM` ONNX export debug
fix. The repository therefore needs the normal post-campaign deliverables:

- a final Markdown campaign-results report under `doc/reports/campaign_results/`;
- a validated PDF export of that report;
- explicit winner reporting and campaign-level artifact references;
- synchronization of the canonical analysis reports that track paper-aligned
  status and current program state.

The report must explain what was executed, summarize the four run roles and
their outcomes, identify the best campaign configuration for this exact-paper
stabilization pass, and record the practical next steps.

## Technical Approach

The report should be built from the persisted campaign artifacts instead of
recomputing results manually.

1. Read the completed campaign state from `doc/running/active_training_campaign.yaml`.
2. Load the four generated `validation_summary.yaml` files and campaign log
   files for:
   - `exact_full_bank_diagnostic_continue`;
   - `exact_full_bank_strict_reference`;
   - `exact_svr_export_diagnostic`;
   - `exact_non_svr_export_reference`.
3. Extract comparison-friendly metrics and export-surface status:
   - enabled family scope;
   - winner family;
   - mean component metrics;
   - exported ONNX file count;
   - failed export count;
   - recovered-reference alignment counts where available.
4. Determine the campaign winner explicitly and serialize campaign-level winner
   artifacts under the campaign output root.
5. Write the final campaign-results Markdown report under
   `doc/reports/campaign_results/` with:
   - objective and outcome;
   - ranked run comparison;
   - run-by-run interpretation;
   - winner justification;
   - practical follow-up recommendations.
6. Export the styled PDF and validate the real PDF output against the
   repository golden standard.
7. Update canonical analysis tracking:
   - `doc/reports/analysis/Training Results Master Summary.md`;
   - `doc/reports/analysis/RCIM Paper Reference Benchmark.md`.

No Codex subagent use is planned for this reporting pass.

## Involved Components

Campaign state and produced artifacts:

- `doc/running/active_training_campaign.yaml`
- `output/training_campaigns/track1/exact_paper/exact_paper_model_bank_campaign_2026_04_10_17_04_41/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`

Expected report deliverables:

- `doc/reports/campaign_results/<timestamp>_exact_paper_model_bank_campaign_results_report.md`
- `doc/reports/campaign_results/<timestamp>_exact_paper_model_bank_campaign_results_report.pdf`
- campaign-level winner artifacts under
  `output/training_campaigns/track1/exact_paper/exact_paper_model_bank_campaign_2026_04_10_17_04_41/`

Supporting report/PDF tooling:

- `scripts/reports/run_report_pipeline.py`
- `scripts/reports/generate_styled_report_pdf.py`
- `scripts/reports/validate_report_pdf.py`

Canonical reports expected to be updated:

- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

## Implementation Steps

1. Inspect the completed campaign state and collect the four run summaries.
2. Build the comparison table and explicit winner selection for the campaign.
3. Serialize campaign-level winner artifacts inside the campaign output root.
4. Write the final campaign-results Markdown report.
5. Export the styled PDF and validate the real output.
6. Update the canonical analysis reports so the exact-paper campaign result is
   reflected in the repository-wide status surface.
7. Run the required Markdown checks on every touched repository-owned Markdown
   file before closing the task.
