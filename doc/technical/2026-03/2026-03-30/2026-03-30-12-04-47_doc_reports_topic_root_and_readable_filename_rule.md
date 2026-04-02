# Doc Reports Topic-Root And Readable-Filename Rule

## Overview

The `doc/reports/` tree now follows a more human-readable structure than the
older timestamp-flat layout used by many earlier report files.

This rule formalizes the manually introduced structure already present in the
repository so future report work stays aligned with it instead of drifting back
to mixed conventions.

## Technical Approach

The new structure separates report organization into three layers:

1. report domain;
2. topic root when a report grows into a reusable package;
3. dated snapshot folder when one topic has multiple concrete releases or asset
   bundles.

The main intent is:

- keep report entry points readable to humans;
- keep multi-artifact packages grouped by topic;
- preserve date traceability without forcing every canonical filename to start
  with a timestamp.

## Involved Components

- `doc/reports/analysis/`
- `doc/reports/campaign_plans/`
- `doc/reports/campaign_results/`
- `doc/README.md`
- future report packages, especially under `doc/reports/analysis/`

## Implementation Steps

1. Use the report-type root first:
   - `analysis/`
   - `campaign_plans/`
   - `campaign_results/`
2. For standalone analysis reports, prefer readable title-based filenames at
   the domain root when no larger package is needed.
3. When a report has multiple companion assets or repeated releases, introduce a
   topic-root folder under the domain root.
4. When one topic-root contains multiple dated report bundles, place each
   bundle inside a dated subfolder.
5. Keep companion assets inside the same topic-local bundle instead of creating
   a second parallel asset root.
6. Update `doc/README.md` whenever the canonical report location changes.

## Rule

### 1. Keep `doc/reports/` Grouped By Report Domain

The first grouping level remains report type:

- `doc/reports/analysis/`
- `doc/reports/campaign_plans/`
- `doc/reports/campaign_results/`

Do not mix campaign plans, campaign results, and general analytical studies in
the same folder.

### 2. Prefer Readable Filenames For Canonical Analysis Reports

For analysis reports that are effectively standalone, prefer human-readable
filenames rather than timestamp-prefixed canonical names.

Examples of the adopted pattern:

- `Code Documentation Platform Comparison.md`
- `Skill and Subagent Operational Test.md`
- `Twincat-Friendly Structured TE Modeling.md`
- `Wave 1 - Closeout Status.md`

Use title-based names when:

- the report is a stable canonical document;
- the topic is clearer than the creation timestamp;
- there is no need to distinguish several releases of the same topic in the
  same folder.

### 3. Introduce A Topic Root For Multi-Artifact Report Families

When one analysis topic grows beyond a single Markdown file, create a topic
folder under the relevant report domain.

Example:

- `doc/reports/analysis/project_status/`

Use a topic root when the topic has:

- a main report;
- a PDF companion;
- presentation files;
- media exports;
- `NotebookLM` source assets;
- or multiple dated snapshots of the same reporting stream.

### 4. Use Dated Snapshot Folders Inside Topic Roots

When a topic root contains one or more concrete releases, store each release in
its own dated subfolder.

Observed canonical pattern:

- `doc/reports/analysis/project_status/[2026-03-27]/`

This keeps the topic stable while preserving time-specific bundles.

Recommended dated-folder rules:

- use one folder per completed report snapshot or release bundle;
- keep the date in the folder name, not necessarily in every child filename;
- keep the bracketed date literal when it improves visual scanning and topic
  grouping.

### 5. Keep Companion Assets Inside The Same Topic-Local Bundle

If a report snapshot has companion files, keep them under the same dated topic
folder instead of creating a second asset root with duplicated naming.

Example package contents:

- `Project Status Report.md`
- `Project Status Report.pdf`
- `Project Status Presentation.md`
- `Project Status Presentation.pdf`
- `Project Status Presentation.pptx`
- media exports
- `notebook_lm_assets/`

Do not create a separate sibling folder such as `*_assets/` when the
topic-root bundle already provides a natural home.

### 6. Treat Bracketed Date Folders As Literal Paths

Folders such as:

- `[2026-03-27]`

must be treated as literal path components in tooling and scripts.

Operational consequence:

- PowerShell commands should use `-LiteralPath` when reading or updating files
  under those folders.

### 7. Keep Documentation Indexes Aligned To The New Canonical Location

Whenever a report is moved, renamed, or regrouped under a topic root:

- update `doc/README.md`;
- update any active usage guide or current operational document that points to
  the old path;
- preserve historical technical notes unless they must become runnable current
  references.

### 8. Keep Campaign Reports On The Existing Timestamped Convention

This rule does not replace the current conventions for:

- `doc/reports/campaign_plans/`
- `doc/reports/campaign_results/`

Those folders still benefit from timestamped filenames because they represent
distinct execution instances of campaigns rather than long-lived topic reports.

## Structural Pattern Summary

The current adopted pattern can be summarized as:

```text
doc/reports/
  analysis/
    <Readable Standalone Report>.md
    <Readable Standalone Report>.pdf
    <topic_root>/
      [YYYY-MM-DD]/
        <Readable Main Report>.md
        <Readable Main Report>.pdf
        <Readable Companion Files...>
        notebook_lm_assets/
  campaign_plans/
    <timestamped campaign plan>.md
  campaign_results/
    <timestamped campaign result>.md
    <timestamped campaign result>.pdf
```

## Notes

- readable names are now preferred for canonical analysis-entry documents;
- topic roots are preferred for asset-heavy report families;
- dated subfolders preserve historical traceability without forcing every file
  to expose the date in the filename;
- campaign-specific reporting remains on the existing timestamp-based workflow.
