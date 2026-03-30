# AGENTS Rule For Doc Reports Topic Root And Readable Filenames

## Overview

The repository now has an observed and partially documented `doc/reports/`
structure based on:

- readable standalone filenames for canonical analysis reports;
- topic-root folders for multi-artifact report families;
- dated snapshot subfolders inside those topic roots;
- topic-local asset storage instead of parallel `*_assets/` roots.

The structure has already been:

- analyzed from the manually reorganized repository state;
- documented in repository-owned technical notes;
- integrated into the documentation indexes and active entry points.

The remaining step is to promote that structure into a hard repository rule
inside `AGENTS.md` so future work follows the same convention by default.

No subagent is planned for this work. The task is a direct repository-rule
update only.

## Technical Approach

The `AGENTS.md` update should add a compact but explicit documentation rule that
captures the new `doc/reports/` convention without duplicating the full
technical note.

The rule should cover:

- `doc/reports/analysis/` standalone reports using readable filenames;
- topic-root folders for analysis topics with multiple companion artifacts;
- dated subfolders inside those topic roots for concrete bundles or releases;
- keeping companion assets inside the topic-local dated bundle;
- keeping `campaign_plans/` and `campaign_results/` on the existing
  timestamp-based convention;
- treating bracketed date folders such as `[2026-03-27]` as literal paths in
  tooling-sensitive contexts.

The update should stay concise and fit naturally inside the `Documentation`
section of `AGENTS.md`.

## Involved Components

- `AGENTS.md`
- `README.md`
- `doc/technical/2026-03-30/2026-03-30-12-03-06_doc_reports_reorganization_alignment_and_naming_rule.md`
- `doc/technical/2026-03-30/2026-03-30-12-04-47_doc_reports_topic_root_and_readable_filename_rule.md`

## Implementation Steps

1. Add the new `doc/reports/` organization rule to the `Documentation` section
   of `AGENTS.md`.
2. Keep the rule compact, but include the key structural decisions needed for
   future repository work.
3. Preserve the current rule set for campaign plans and campaign results.
4. Re-run scoped Markdown checks on the touched Markdown files.
5. Report completion and wait for explicit approval before any Git commit.
