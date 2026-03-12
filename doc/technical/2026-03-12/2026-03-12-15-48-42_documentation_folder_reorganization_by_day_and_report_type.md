# Documentation Folder Reorganization By Day And Report Type

## Overview

The current `doc/technical/` and `doc/reports/` folders have become dense enough that flat file listings are starting to hurt readability and maintenance.

The user requested a structural reorganization with two explicit goals:

1. split `doc/technical/` into day-based subfolders so technical planning documents remain easy to scan chronologically;
2. reorganize `doc/reports/` into report-type subfolders so planning reports, comparison reports, and analytical reports do not accumulate in one flat directory.

This change is document-structure work only. It does not change the training code, datasets, or model logic.

## Technical Approach

The reorganization should preserve the current timestamped filenames because those names are already part of the repository workflow and remain useful for chronological traceability.

The structure should therefore change at the folder level, not at the filename level.

### Proposed `doc/technical/` Structure

Technical documents should be grouped by calendar day:

- `doc/technical/2026-03-10/`
- `doc/technical/2026-03-11/`
- `doc/technical/2026-03-12/`

Each file should keep its current timestamped filename, for example:

- `doc/technical/2026-03-12/2026-03-12-15-48-42_documentation_folder_reorganization_by_day_and_report_type.md`

This preserves:

- strict chronological ordering;
- compatibility with the existing filename rule;
- easier visual scanning when one specific day produced many technical documents.

### Proposed `doc/reports/` Structure

The current reports are better grouped by function than by date.

The proposed report taxonomy is:

- `doc/reports/analysis/`
  for standalone analytical or explanatory reports that interpret one run, one topic, or one configuration family;
- `doc/reports/campaign_plans/`
  for pre-execution planning reports that define candidate runs, rationale, and comparison tables;
- `doc/reports/campaign_results/`
  for post-execution comparison reports that summarize outcomes across multiple runs.

With the current repository contents, the mapping would be:

- `doc/reports/analysis/`
  - `2026-03-12-13-18-30_feedforward_trial_analytical_report.md`
  - `2026-03-12-13-38-17_training_configuration_analysis_report.md`
  - `2026-03-12-13-38-17_training_configuration_analysis_report.pdf`
- `doc/reports/campaign_plans/`
  - `2026-03-12-15-32-28_mixed_training_campaign_plan_report.md`
- `doc/reports/campaign_results/`
  - `2026-03-12-15-04-34_feedforward_variant_comparison_report.md`

This split is preferable to a single mixed `planned_runs_and_results/` folder because it keeps the workflow stages explicit:

- planning before execution;
- results after execution;
- standalone analysis outside campaign execution.

### Documentation Index Strategy

The main repository indexes should be updated to reflect the new folder structure:

- `README.md`
- `doc/README.md`

The indexes should not become flatter. They should mirror the new grouped structure, for example:

- technical documents by day;
- reports by type.

All existing links and any internal references pointing to the moved files should also be updated.

## Involved Components

- `README.md`
  Main project document that must reference this technical document and reflect the new grouped documentation tree after approval.
- `doc/README.md`
  Internal documentation index that must be reorganized around the new folder layout.
- `doc/technical/`
  Current flat folder that should be converted into day-based subfolders.
- `doc/reports/`
  Current flat folder that should be converted into report-type subfolders.
- `AGENTS.md`
  Repository instruction file that may contain example report paths that must remain valid after the move.
- existing technical documents under `doc/technical/`
  All current technical files that would be moved into day folders.
- existing reports under `doc/reports/`
  All current report files that would be moved into report-type folders.

## Implementation Steps

1. Create this technical document and register it in the project documentation indexes.
2. After user approval, create day-based subfolders under `doc/technical/` and move the existing technical documents into their corresponding date folders.
3. After user approval, create report-type subfolders under `doc/reports/`:
   - `analysis/`
   - `campaign_plans/`
   - `campaign_results/`
4. Move the existing report files into the selected report-type folders without changing their filenames.
5. Update all references in:
   - `README.md`
   - `doc/README.md`
   - `AGENTS.md`
   - any technical or report documents that link to the moved files.
6. Verify that no stale paths remain in the repository.
7. Create the required Git commit immediately after the approved reorganization is completed.
