# Track 1 Family Reference Archives And Closeout Integration

## Overview

This technical document defines the repository change needed to extend the
existing curated `Track 1` `SVM` reference-archive pattern to every other
exact-paper `Track 1` family and to make archive refresh a formal required
step of future `Track 1` campaign closeout.

The current repository already contains the first complete archive instance at
`models/paper_reference/rcim_track1/forward/svm_reference_models/`, and the benchmark
surface already declares the target contract for future family archives.
However, the remaining `Track 1` families do not yet expose the same stable
paper-reference package, and the closeout flow does not yet enforce archive
promotion whenever a campaign improves an accepted family result.

This work must stay compatible with the currently prepared
`track1_remaining_yellow_cell_campaigns_2026_04_22_01_40_43` state. The
prepared campaign files listed in `doc/running/active_training_campaign.yaml`
remain protected and must not be edited as part of this implementation unless
explicitly re-approved later.

The target family scope for this archive rollout is every non-`SVM` exact-paper
`Track 1` family already treated as canonical in the benchmark:

- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

No Codex subagent is planned for this work. If subagent use becomes desirable
later, it must be proposed explicitly and approved before launch.

## Technical Approach

The implementation should promote the current `SVM` archive layout from a
one-off curated package into a reusable repository mechanism that can be
applied to all accepted `Track 1` families and re-run during closeout.

The approved implementation should do five things:

1. Introduce one canonical family archive under
   `models/paper_reference/rcim_track1/<family>_reference_models/` for each
   non-`SVM` `Track 1` family, using the existing `SVM` package contract as the
   template instance.
2. Populate each archive with the family-best accepted target set for the four
   canonical replication tables, preserving both:
   - deployment-facing `ONNX` exports;
   - Python-usable serialized fitted estimators;
   together with dataset snapshot provenance, source-run snapshots, and a
   machine-readable `reference_inventory.yaml` that records the exact accepted
   source run for each target.
3. Add repository-owned tooling that can regenerate or refresh a family archive
   from the current accepted benchmark state rather than relying on manual
   archive assembly.
4. Formalize a closeout rule for exact-paper `Track 1` campaigns:
   when a campaign changes any accepted family result, closeout must refresh
   the affected family archive or archives before the benchmark is considered
   synchronized.
5. Update the benchmark and closeout documentation so the family-archive
   requirement is explicit, operational, and aligned with the existing colored
   table refresh obligations.

The archive refresh rule should remain selective rather than blindly copying
every latest run. The canonical selection rule must keep the same philosophy
already documented for `SVM`:

- pin the run whose accepted metrics match the benchmark cell that is currently
  canonical for that family-target pair;
- when a new closeout produces a better accepted family result, replace the
  archived target entry with the improved canonical source run;
- when a newer campaign merely reproduces an already accepted value, retain the
  earlier stable canonical source run instead of churning the archive.

To keep the closeout pipeline inspectable, the new archive-refresh step should
be callable from repository-owned scripts and should consume the same campaign
and validation artifacts already used to refresh:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- the family-by-family colored replication tables for `Table 2` through
  `Table 5`

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_results/track1/exact_paper/forward/`
- `doc/reports/campaign_plans/track1/exact_paper/2026-04-22-01-40-43_track1_remaining_yellow_cell_multi_family_campaign_bundle_plan_report.md`
- `doc/running/active_training_campaign.yaml`
- `models/README.md`
- `models/paper_reference/README.md`
- `models/paper_reference/rcim_track1/README.md`
- `models/paper_reference/rcim_track1/forward/svm_reference_models/`
- `models/paper_reference/rcim_track1/<family>_reference_models/`
- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/`
- `output/training_campaigns/track1/exact_paper/forward/`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- repository-owned closeout and report-refresh scripts under `scripts/reports/`

## Implementation Steps

1. Inspect the current exact-paper benchmark surface and determine the accepted
   target inventory for each non-`SVM` `Track 1` family.
2. Derive a reusable archive-generation workflow from the existing
   `svm_reference_models` package, including the per-target provenance fields,
   dataset snapshot handling, and source-run snapshot structure.
3. Create the missing family archive roots under
   `models/paper_reference/rcim_track1/` and populate them with the canonical
   accepted `ONNX`, Python, data, and metadata artifacts.
4. Update the relevant model-archive and benchmark documentation so every new
   family archive is discoverable and its regeneration rule is explicit.
5. Add or extend repository-owned closeout tooling so future `Track 1`
   campaign closeouts refresh affected family archives whenever accepted
   family-target cells improve.
6. Integrate that archive-refresh step into the exact-paper closeout workflow
   and document it as a mandatory synchronization obligation alongside the
   benchmark-table refresh.
7. Run Markdown QA on the touched Markdown scope before requesting final review
   or any later commit approval.
