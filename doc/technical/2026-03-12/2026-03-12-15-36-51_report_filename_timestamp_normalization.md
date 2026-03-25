# Report Filename Timestamp Normalization

## Overview

The user requested a naming cleanup for the documents currently stored in `doc/reports/`.

At the moment, the report filenames use only the date prefix:

- `2026-03-12-feedforward_trial_analytical_report.md`
- `2026-03-12-training_configuration_analysis_report.md`
- `2026-03-12-training_configuration_analysis_report.pdf`
- `2026-03-12-feedforward_variant_comparison_report.md`
- `2026-03-12-mixed_training_campaign_plan_report.md`

The requested change is to normalize these report filenames so they also include the time component, consistent with the timestamp style already used for technical documents in `doc/technical/`.

## Technical Approach

This is a documentation-structure change only.

The implementation should:

1. rename the existing report files in `doc/reports/` from date-only filenames to full timestamp filenames using the pattern:
   - `YYYY-MM-DD-HH-mm-SS-report_name.ext`
2. keep the Markdown and PDF pair for the training-configuration analysis report aligned under the same timestamp prefix;
3. update every reference to these report files inside:
   - `README.md`
   - `doc/README.md`
4. avoid changing the report contents unless a path reference inside the report body also needs adjustment.

The planned filename mapping is:

- `doc/reports/2026-03-12-feedforward_trial_analytical_report.md`
  ->
  `doc/reports/analysis/2026-03-12-13-18-30_feedforward_trial_analytical_report.md`

- `doc/reports/2026-03-12-training_configuration_analysis_report.md`
  ->
  `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md`

- `doc/reports/2026-03-12-training_configuration_analysis_report.pdf`
  ->
  `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.pdf`

- `doc/reports/2026-03-12-feedforward_variant_comparison_report.md`
  ->
  `doc/reports/campaign_results/2026-03-12-15-04-34_feedforward_variant_comparison_report.md`

- `doc/reports/2026-03-12-mixed_training_campaign_plan_report.md`
  ->
  `doc/reports/campaign_plans/2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`

These timestamps are chosen to keep the report filenames chronologically informative and internally consistent with the current document set.

## Involved Components

- `README.md`
  Main project document that references the current report filenames and must be updated.
- `doc/README.md`
  Internal documentation index that references the current report filenames and must be updated.
- `doc/reports/`
  Folder containing the report files to rename.
- `doc/technical/2026-03-12/2026-03-12-15-36-51_report_filename_timestamp_normalization.md`
  This technical planning document.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, rename the existing report files in `doc/reports/` to the timestamp-complete filenames listed above.
3. Update `README.md` so the main project report references point to the renamed files.
4. Update `doc/README.md` so the internal documentation index points to the renamed files.
5. Verify that no stale references to the old report filenames remain.
6. Create the required Git commit immediately after the approved rename update is completed.
