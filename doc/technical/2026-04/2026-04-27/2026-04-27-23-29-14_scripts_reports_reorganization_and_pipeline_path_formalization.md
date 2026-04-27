# Scripts Reports Reorganization And Pipeline Path Formalization

## Overview

The current `scripts/reports/` root is too flat. It mixes:

- Track 1 closeout entrypoints;
- presentation-generation tooling;
- styled PDF export helpers;
- model-analysis helpers;
- Track 1 benchmark and archive refresh utilities.

That layout already caused one concrete gap: the `forward` closeout path was
implemented without refreshing `models/paper_reference/rcim_track1/`, while the
bidirectional mega closeout already handled archive refresh correctly. The user
also requested that future `backward` closeouts inherit the same behavior
without another round of path cleanup.

The requested change is therefore broader than a one-off closeout fix. The
repository should reorganize `scripts/reports/` into explicit subfolders and
formalize the new locations in the campaign and report documentation so future
closeout, presentation, and reporting work lands in the right place on the
first pass.

## Technical Approach

The reorganization should be done as one coherent migration rather than as
separate local moves. The target is to turn `scripts/reports/` into a small
taxonomy with clear ownership boundaries.

The proposed structure is:

- `scripts/reports/closeout/`
  - Track 1 closeout entrypoints and shared closeout helpers.
- `scripts/reports/presentation/`
  - presentation-generation and presentation-pipeline scripts.
- `scripts/reports/pdf/`
  - styled PDF generation, validation, and report-pipeline export entrypoints.
- `scripts/reports/analysis/`
  - generic report-analysis helpers that are not closeout-specific.
- `scripts/reports/track1/`
  - Track 1 benchmark-refresh and family-reference archive refresh utilities
    that are reused by closeouts but also remain independently runnable.

The closeout fix requested by the user should be implemented inside that
reorganized surface instead of being patched only in the old flat layout. In
practice:

1. move the closeout scripts into a dedicated closeout path;
2. promote reference-archive refresh into a shared reusable closeout stage;
3. make the same shared path callable from both current `forward` closeouts and
   future `backward` closeouts;
4. move presentation tooling into its own dedicated folder;
5. move the PDF pipeline into its own dedicated folder;
6. update repository-owned documentation so commands and canonical paths point
   to the new locations.

Backwards compatibility should be preserved where useful through thin wrapper
entrypoints or tightly scoped path updates, but the canonical documentation
should point to the new folder structure.

## Involved Components

- `scripts/reports/`
- current Track 1 closeout scripts under `scripts/reports/`
- `scripts/reports/presentation/generate_markdown_presentation.py`
- `scripts/reports/presentation/run_presentation_pipeline.py`
- `scripts/reports/pdf/generate_styled_report_pdf.py`
- `scripts/reports/pdf/run_report_pipeline.py`
- `scripts/reports/pdf/validate_report_pdf.py`
- `scripts/reports/analysis/generate_model_report_diagrams.py`
- `scripts/reports/analysis/generate_training_results_master_summary.py`
- `scripts/reports/analysis/plot_wave1_best_model_te_curves.py`
- `scripts/reports/track1/refresh_track1_benchmark_colored_markers.py`
- `scripts/reports/track1/refresh_track1_family_reference_archives.py`
- Track 1 campaign closeout and campaign-launch notes under `doc/scripts/campaigns/`
- report-tooling notes under `doc/scripts/reports/`
- `doc/guide/project_usage_guide.md`
- `doc/README.md`
- `site/`

## Implementation Steps

1. inventory the current `scripts/reports/` entrypoints and assign each one to
   a stable target subfolder;
2. move the Track 1 closeout scripts under a dedicated closeout folder and
   refactor any local imports or path assumptions that break after the move;
3. move the presentation pipeline scripts under a dedicated presentation folder;
4. move the styled PDF pipeline scripts under a dedicated PDF folder;
5. move or regroup the remaining report helpers into dedicated analysis and
   Track 1 support folders;
6. implement the missing closeout archive-refresh enforcement inside the new
   closeout structure so the current `forward` closeout and a future
   `backward` closeout both use the same shared refresh path;
7. update repository-owned notes and campaign-pipeline documents so canonical
   commands reference the reorganized script paths;
8. update `doc/guide/project_usage_guide.md`, `doc/README.md`, and the Sphinx
   portal where the old paths are user-facing;
9. run Markdown QA on the touched Markdown scope, run `py_compile` or
   equivalent script checks on the moved Python entrypoints, and run
   `python -m sphinx -W -b html site site/_build/html`.
