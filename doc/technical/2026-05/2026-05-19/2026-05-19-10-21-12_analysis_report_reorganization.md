# Analysis Report Reorganization

## Overview

This document proposes a documentation-only reorganization of
`doc/reports/analysis/`, with immediate focus on the loose validation reports
under `doc/reports/analysis/validation_checks/`.

The current `validation_checks` folder contains thousands of generated or
semi-generated validation report Markdown files directly in the folder root.
That makes the canonical analysis reports hard to browse and makes related
report groups difficult to identify. The same root-level clutter exists at a
smaller scale in `doc/reports/analysis/`, where RCIM, Wave 1, infrastructure,
and utility-oriented reports are mixed together.

No subagent use is planned for this task.

## Technical Approach

Keep `doc/reports/analysis/` organized by topic roots, with dated subfolders
for repeated releases or companion bundles. Preserve existing filenames unless
there is a clear collision risk. Prefer pure file moves plus index updates over
content rewrites.

The proposed top-level analysis taxonomy is:

- `rcim_paper_reference/`: RCIM paper, recovered assets, original pipeline,
  exact-model-bank reimplementation, parity, benchmark, and retuned closeout
  reports.
- `wave1/`: Wave 1 closeout, best-model TE curve prediction, and later Wave 1
  comparison or recovery reports.
- `track2/`: TE Curve Verification Pipeline directional comparison reports and future TE Curve Verification Pipeline
  analytical bundles.
- `training_analysis/`: cross-family training summaries and general training
  analysis reports, keeping `Training Results Master Summary.md` as the
  canonical status report unless a later approval moves it.
- `te_modeling/`: structured TE modeling and analytical model-family reports.
- `utilities/`: operational reports for Linux script portability, skill and
  subagent workflows, local LAN AI infrastructure, and documentation-platform
  comparisons.
- `project_status/`: project status report and presentation bundles.
- `twincat_video_guides/`: TwinCAT/TestRig video-analysis campaign summaries.
- `validation_checks/`: generated validation report inventories grouped by
  campaign or validation purpose.

The proposed `validation_checks` taxonomy is:

- `validation_checks/rcim_paper_reimplementation/smoke/[2026-04-25]/`
  for the loose smoke reports.
- `validation_checks/rcim_paper_reimplementation/track1/original_dataset/[2026-04-25_to_2026-05-16]/`
  for loose RCIM Model-Bank Reproduction original-dataset exact-model-bank validation reports.
- `validation_checks/rcim_paper_reimplementation/track1/remote_diagnostic/[2026-04-25]/`
  for remote diagnostic reports.
- `validation_checks/rcim_paper_reimplementation/track1/remote_micro/[2026-04-25_to_2026-04-26]/`
  for remote micro reports.
- `validation_checks/rcim_paper_reimplementation/track1/forward_subset/[2026-04-29]/`
  for `forward_last_four` and `forward_last_three` validation reports.
- Existing `validation_checks/track1/`, `validation_checks/track2/`, and
  `validation_checks/infrastructure/` subtrees should be preserved unless a
  second pass confirms they need further consolidation.

## Involved Components

- `doc/reports/analysis/`
- `doc/reports/analysis/validation_checks/`
- `doc/README.md`
- Markdown QA tooling:
  - `python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning`
  - `python -B scripts/tooling/markdown/run_markdownlint.py`

## Implementation Steps

1. Move root-level RCIM analysis reports into `rcim_paper_reference/` and keep
   the existing `rcim_retuned_reference_closeout/` bundle under that root.
2. Move Wave 1 reports and existing Wave 1 dated bundles into `wave1/`.
3. Move TE Curve Verification Pipeline directional reports into `track2/`.
4. Move utility and operational reports into `utilities/`, including Linux
   portability, skill/subagent, local LAN AI, and documentation-platform
   comparison reports.
5. Move TwinCAT-friendly structured TE modeling into `te_modeling/` unless it
   is explicitly needed inside the TwinCAT video-guide topic.
6. Rehome loose `validation_checks` Markdown files into the proposed
   `rcim_paper_reimplementation/` subfolders.
7. Update `doc/README.md` links for moved canonical reports and add concise
   entries for the new topic roots.
8. Search for repository links to moved paths and update them where they are
   canonical references, without rewriting generated validation report bodies.
9. Run Markdown QA on touched authored Markdown files and resolve any warnings
   introduced by the reorganization.
