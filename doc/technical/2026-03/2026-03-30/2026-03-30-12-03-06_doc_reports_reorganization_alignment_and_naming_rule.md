# Doc Reports Reorganization Alignment And Naming Rule

## Overview

The `doc/reports/` tree has been manually reorganized.

The observed repository state shows three important changes:

1. several analysis reports previously stored as flat timestamp-prefixed files
   under `doc/reports/analysis/` were renamed to human-readable title-based
   filenames;
2. the `project_status` material was regrouped into a topic-rooted folder with
   a dated subfolder:
   - `doc/reports/analysis/project_status/[2026-03-27]/`
3. report-adjacent assets such as presentations, exports, and
   `notebook_lm_assets/` were moved under that topic-local dated folder instead
   of remaining in a flat timestamped asset root.

This task should:

1. analyze the manual reorganization and treat it as the new intended report
   structure;
2. realign repository documentation so indexes and references match the new
   layout;
3. formalize the newly observed structure as an explicit repository rule for
   future `doc/reports/` work.

No subagent is planned for this work. The scope is repository-local
documentation alignment only. If a later subagent-based audit were ever useful,
runtime launch would still require explicit user approval.

## Technical Approach

The work should proceed in three passes.

First, verify the new structure directly from the file tree and current Git
state, distinguishing:

- renamed reports;
- moved reports;
- deleted legacy paths that are now replaced by new canonical locations;
- newly introduced topic-root folders and dated subfolders.

Second, realign the documentation surfaces that expose the report tree, mainly:

- `doc/README.md`
- `README.md` when the public-facing entry points are affected
- any touched guide or running-state document that still points at the
  pre-reorganization paths

This realignment should preserve the user's new organization instead of forcing
the old timestamp-flat layout back into place.

Third, convert the inferred structure into a persistent repository rule. The
rule should explain:

- when a report should use a human-readable filename;
- when a topic folder should be introduced;
- when a dated subfolder is appropriate;
- where companion assets should live relative to the canonical report;
- how future indexes should refer to those reports.

The formalized rule should be documented in a repository-owned technical note
and reflected in the relevant documentation index.

## Involved Components

- `doc/reports/analysis/`
- `doc/reports/campaign_plans/`
- `doc/reports/campaign_results/`
- `doc/README.md`
- `README.md`
- the manually reorganized report files under:
  - `doc/reports/analysis/project_status/[2026-03-27]/`
  - the renamed title-based analysis reports at the `analysis/` root

## Implementation Steps

1. Inspect the current `doc/reports/` tree and identify the new structural
   pattern introduced by the manual reorganization.
2. Compare the new canonical locations against existing documentation indexes
   and references.
3. Update `doc/README.md` and any other affected documentation entry points so
   they point to the new canonical report locations.
4. Write a concise repository-owned rule that formalizes the observed
   `doc/reports/` organization pattern for future work.
5. Register the new technical rule document from `README.md` if required by the
   repository workflow.
6. Run scoped Markdown warning checks on all touched Markdown files and fix any
   local warning regressions.
7. Report completion and wait for explicit approval before any Git commit.
