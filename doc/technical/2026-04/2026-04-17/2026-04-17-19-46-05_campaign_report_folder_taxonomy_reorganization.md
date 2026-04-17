# Campaign Report Folder Taxonomy Reorganization

## Overview

The roots:

- `doc/reports/campaign_results/`
- `doc/reports/campaign_plans/`

have grown into flat timestamp-heavy directories. The timestamped filenames are
still useful and should remain the per-report naming convention, but the
directory surface is now too crowded for practical browsing.

This task reorganizes those two report roots into stable topic subfolders while
preserving the existing timestamp-prefixed filenames for each concrete campaign
report.

## Technical Approach

The reorganization should use semantic topic buckets rather than date buckets.
Date grouping would still leave the user searching through mixed campaign
themes, while topic grouping keeps related plans and results together.

Proposed top-level taxonomy for both:

- `wave1/`
- `track1/harmonic_wise/`
- `track1/exact_paper/`
- `track1/svm/`
- `infrastructure/`
- `mixed_training/`

Interpretation rule:

- `wave1/` for the historical Wave 1 campaign package;
- `track1/harmonic_wise/` for the repository-owned harmonic-wise Track 1
  campaigns;
- `track1/exact_paper/` for the strict paper-faithful family-bank and open-cell
  exact-paper campaigns that are not family-specific `SVM` closure batches;
- `track1/svm/` for `SVR/SVM`-focused Track 1 repair, closure, grid, smoke, and
  exact-faithful follow-up campaigns;
- `infrastructure/` for remote validation and infra-facing operator campaigns;
- `mixed_training/` for the earlier generic mixed-training and logging-validation
  campaign packages.

This keeps the timestamp naming convention intact while making the folder tree
inspectable by program area.

The reorganization should also update repository-owned references that point to
the moved reports, including:

- `doc/README.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- any other canonical report indexes or notes that still reference the old flat
  paths.

## Involved Components

- `doc/reports/campaign_results/`
- `doc/reports/campaign_plans/`
- `doc/README.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- any additional repository-owned Markdown files that reference the moved
  campaign report paths
- `doc/technical/2026-04/2026-04-17/README.md`

## Implementation Steps

1. Create the topic subfolder layout under both `campaign_results/` and
   `campaign_plans/`.
2. Move the existing timestamped reports into the appropriate topic subfolders
   without changing the filenames.
3. Update repository-owned references to the moved report paths.
4. Run scoped Markdown checks on all touched Markdown files before closing the
   task.
