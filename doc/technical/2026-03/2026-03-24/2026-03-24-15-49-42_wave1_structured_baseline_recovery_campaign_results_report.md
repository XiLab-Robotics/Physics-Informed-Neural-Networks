# Wave1 Structured Baseline Recovery Campaign Results Report

## Overview

This document defines the final reporting work for the completed recovery campaign:

- `wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42`

The campaign was executed to rerun the previously failed Wave 1 recovery configurations after the shared training-path fixes and the conservative random-forest memory changes.

The final deliverable must include:

- a Markdown campaign-results report under `doc/reports/campaign_results/`;
- a styled PDF export aligned with the repository golden standard;
- a validation pass on the real exported PDF;
- a written interpretation of the recovered harmonic, residual, and tree results;
- an explicit statement of the campaign winner and its relation to the broader program leaderboard.

## Technical Approach

The final report should synthesize the following evidence sources:

1. the persistent campaign state in `doc/running/active_training_campaign.yaml`;
2. the campaign-level execution artifacts under `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/`;
3. the per-run metrics in the six `metrics_summary.yaml` files produced by the campaign;
4. the per-run `training_test_report.md` files for model-specific interpretation;
5. the family and program registries under `output/registries/`.

The report should make two levels of interpretation explicit:

- campaign-local ranking within the six recovery runs;
- program-level context, especially whether the recovery winner became the global best solution or only a family-level best.

The report should also capture the practical operational result of the recovery campaign:

- the previous failure modes were resolved well enough to complete all six recovery runs end to end;
- the conservative random-forest configuration traded runtime for execution reliability on the current workstation.

## Involved Components

- `README.md`
  Main project document that must reference this technical note.
- `doc/running/active_training_campaign.yaml`
  Persistent campaign state that must be updated from `prepared` to `completed`.
- `doc/reports/campaign_plans/wave1/2026-03-20-15-40-42_wave1_structured_baseline_recovery_campaign_plan_report.md`
  Approved planning report for the completed recovery campaign.
- `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/campaign_execution_report.md`
  Campaign execution summary with run durations and artifact references.
- `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/campaign_leaderboard.yaml`
  Explicit ranked ordering of the completed recovery runs.
- `output/training_campaigns/2026-03-20-16-11-22_wave1_structured_baseline_recovery_campaign_2026_03_20_15_40_42/campaign_best_run.yaml`
  Explicit campaign winner record.
- `output/training_runs/harmonic_regression/*/metrics_summary.yaml`
  Harmonic recovery metrics.
- `output/training_runs/residual_harmonic_mlp/*/metrics_summary.yaml`
  Residual recovery metrics.
- `output/training_runs/tree/*/metrics_summary.yaml`
  Random-forest recovery metrics.
- `output/registries/families/*/latest_family_best.yaml`
  Family-level winner context.
- `output/registries/program/current_best_solution.yaml`
  Program-level best solution context.
- `scripts/reports/run_report_pipeline.py`
  Existing export and validation pipeline for styled PDFs.

## Implementation Steps

1. Create this technical document and register it in `README.md`.
2. Update the active campaign state to `completed` with the actual campaign output directory and completion timestamps.
3. Write the final Markdown campaign-results report using the campaign execution report, leaderboard, and per-run metrics.
4. Export the report to PDF with the existing repository-owned reporting pipeline.
5. Validate the real exported PDF and keep the task open until the layout quality is acceptable.
