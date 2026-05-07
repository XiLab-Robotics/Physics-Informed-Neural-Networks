# Training Results Master Summary Directional Sectioning And Future Wave Policy

## Overview

The current `doc/reports/analysis/Training Results Master Summary.md` already
stores distinct family identifiers for the new directional `Wave 1` retraining
surface, but the report still presents several ranking tables and family
breakdowns as one mixed sequence across:

- `global` models;
- `Fw` models;
- `Bw` models.

This mixed presentation weakens the reporting contract that was already
introduced for training, closeout, and exported-model archival work. The user
request is to formalize a durable reporting rule: `global`, `Fw`, and `Bw`
surfaces must remain explicitly separated in the canonical master summary, and
the same structure must be carried forward for every later wave that introduces
directional or otherwise scope-split training variants.

## Technical Approach

The reporting policy should be promoted from an implicit naming convention to
an explicit master-summary structure rule.

For `Wave 1`, the canonical report should stop mixing directional variants in
shared grids when the intent is to summarize winner rankings, implemented
families, or family-by-family outcome tables. Instead, the report should expose
dedicated sections and tables for:

1. `global` model surfaces;
2. `Fw` model surfaces;
3. `Bw` model surfaces.

This policy should apply both to high-level report surfaces and to the detailed
family-result breakdowns whenever the underlying content is directional. The
goal is to make comparisons fair and readable inside each scope before any
cross-scope interpretation is made.

The same structural contract should then be defined as the default for future
waves:

- if a wave only has one canonical training scope, its summary can remain
  single-surface;
- if a wave introduces multiple canonical scopes such as `global`, `Fw`, `Bw`,
  or another future split taxonomy, the master summary generator and report
  layout must render those scopes as first-class separated blocks rather than a
  merged ranking.

This turns direction scope into an explicit reporting dimension, not just a
suffix on family names.

## Involved Components

- `doc/reports/analysis/Training Results Master Summary.md`
- `scripts/reports/analysis/generate_training_results_master_summary.py`
- `doc/reports/analysis/Wave 1 - Closeout Status.md`
- `output/registries/families/*/latest_family_best.yaml`
- `output/registries/program/current_best_solution.yaml`
- future wave-specific campaign closeout and reporting surfaces that feed the
  canonical master summary

## Implementation Steps

1. Define the canonical scope taxonomy for master-summary reporting, starting
   with `global`, `Fw`, and `Bw` for `Wave 1`.
2. Refactor the master-summary generation logic so high-level tables and wave
   breakdowns are grouped by reporting scope instead of one mixed ranking.
3. Update the `Wave 1` sections of
   `doc/reports/analysis/Training Results Master Summary.md` so the grids and
   detailed family tables are presented in separate `global`, `Fw`, and `Bw`
   blocks.
4. Add an explicit future-wave reporting rule so later wave families inherit
   the same scope-separated layout whenever multiple canonical training scopes
   exist.
5. Refresh any closeout-owned analysis surface that directly depends on the old
   mixed presentation if that surface would become inconsistent after the
   master-summary change.
6. Run Markdown QA on the touched repository-authored Markdown files after the
   implementation work is completed.
7. Stop after implementation and report completion without committing, waiting
   for explicit user approval before any Git commit.
