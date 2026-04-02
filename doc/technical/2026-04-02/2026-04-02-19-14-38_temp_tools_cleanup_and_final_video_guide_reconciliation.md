# Overview

This scope closes two remaining repository-hygiene and knowledge-quality tasks.

First, it audits `.temp/` and `.tools/` to decide what should be preserved,
promoted into tracked repository locations, or removed as stale runtime residue.

Second, it re-evaluates the canonical video source bundle under
`reference/video_guides/` against the currently promoted guide artifacts under
`doc/reference_codes/video_guides/`, using the repository-owned TwinCAT/TestRig
video-analysis workflow as the review baseline. The objective is to converge on
the definitive canonical state of the video-guide corpus and to ensure that the
implementation-facing TwinCAT/TestRig knowledge extracted from those videos is
fully integrated into the persistent reference notes.

## Technical Approach

The work will proceed in two phases.

Phase 1 is a repository-temp audit:

* inventory `.temp/` and `.tools/`;
* classify contents into:
  * keep as tracked canonical artifact candidates;
  * keep as runtime cache or environment support;
  * remove as stale or superseded residue;
* promote any still-useful untracked artifact before cleanup.

Phase 2 is a final video-guide reconciliation pass:

* use the canonical source bundle in `reference/video_guides/`;
* review the already promoted artifacts in `doc/reference_codes/video_guides/`;
* if needed, rerun or narrowly re-analyze the strongest validated video path;
* compare new results with the currently promoted transcripts and reports;
* identify quality deltas, inconsistencies, merge candidates, and canonical
  corrections;
* merge the final implementation-facing findings into the persistent
  TwinCAT/TestRig reference notes.

The work should preserve the distinction between:

* repository-owned final deliverables;
* runtime caches and scratch outputs;
* video-confirmed facts versus code-confirmed facts versus engineering
  inference.

## Involved Components

* `.temp/`
* `.tools/`
* `reference/video_guides/`
* `doc/reference_codes/video_guides/`
* `doc/reference_codes/testrig_twincat_video_guides_reference.md`
* `doc/reference_codes/testrig_twincat_ml_reference.md`
* `doc/reports/analysis/twincat_video_guides/`
* `doc/guide/project_usage_guide.md` if the cleanup changes user-facing
  runtime expectations

## Implementation Steps

1. Inventory `.temp/` and `.tools/`, including sizes and artifact roles.
2. Decide what must be preserved, promoted, or deleted.
3. Promote any still-useful artifacts that should become tracked repository
   assets.
4. Clean the remaining stale runtime residue from `.temp/` and `.tools/`.
5. Re-review the canonical video-guide assets against the source bundle under
   `reference/video_guides/`.
6. Re-run or narrowly re-analyze video-guide processing when needed to resolve
   remaining quality uncertainty.
7. Compare the new review outputs against the currently promoted canonical
   transcripts and reports, and identify definitive merges or replacements.
8. Update the persistent TwinCAT/TestRig reference notes with any newly
   confirmed implementation-facing knowledge.
9. Run scoped Markdown warning checks on the touched Markdown files before
   closing the task.
