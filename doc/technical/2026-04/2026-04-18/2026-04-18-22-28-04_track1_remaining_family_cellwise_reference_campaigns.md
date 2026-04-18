# Track 1 Remaining Family Cellwise Reference Campaigns

## Overview

This technical document prepares the next `Track 1` campaign wave after the
completion of the family-level full-matrix exact-paper passes.

The user-approved strategic direction is to stop treating the remaining
families only as full-matrix rows and instead replicate the `SVM` closure
pattern family by family:

- one dedicated training run per accepted paper cell;
- one curated reference-model bank per family;
- one explicit archive and provenance surface per family under `models/`;
- one canonical benchmark section per family inside
  `doc/reports/analysis/RCIM Paper Reference Benchmark.md`.

The remaining families are:

- `MLP`
- `RF`
- `DT`
- `ET`
- `ERT`
- `GBM`
- `HGBM`
- `XGBM`
- `LGBM`

The target surface is the same `Track 1` paper cell inventory already pinned
for `SVM`:

- `10` amplitude targets for harmonics
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`;
- `9` phase targets for harmonics
  `1, 3, 39, 40, 78, 81, 156, 162, 240`.

That implies a minimum exact-paper cellwise batch of `171` runs:

- `9` families;
- `19` target-specific runs per family.

No subagent usage is planned for this preparation. Campaign design,
documentation, YAML packaging, launcher generation, and later closeout are
expected to remain repository-local.

## Technical Approach

The new campaign wave should generalize the successful organizational part of
the `SVM` workflow, not only its scientific intent.

The exact-paper branch already works with the canonical RCIM feature and target
schema:

- input features: `rpm`, `deg`, `tor`;
- deterministic split: `test_size = 0.20`, `random_seed = 0`;
- target harmonics:
  `0, 1, 3, 39, 40, 78, 81, 156, 162, 240`;
- deployment-facing output: per-target `ONNX` exports plus Python-side fitted
  estimators.

The remaining-family cellwise wave should therefore be prepared as a
family-by-family extension of the same exact-paper workflow, but with each run
restricted to one target cell at a time instead of one full amplitude or phase
matrix.

The intended campaign contract is:

1. every remaining family gets one dedicated campaign package;
2. each family package contains `19` exact-paper single-target runs;
3. each family package exposes one hybrid launcher:
   - local by default;
   - remote through `-Remote`;
4. one aggregate launcher executes the `9` family packages in sequence;
5. successful closeout of each family must promote:
   - accepted cellwise winners into the canonical benchmark;
   - family archive content under
     `models/paper_reference/rcim_track1/<family>_reference_models/`;
   - the colored family-by-family replication tables in `Tables 2-5`;
   - `Training Results Master Summary.md`.

This wave should remain exact-paper in the same sense already used by the
repository:

- no new family outside the recovered paper inventory;
- no repository-invented target schema;
- no departure from the exact RCIM feature set;
- no loss of deterministic reconstruction metadata;
- no ad hoc archive layout different from the now-standardized `SVM` family
  archive contract.

The main practical change relative to the just-completed full-matrix campaign
is scale:

- previous remaining-family batch: `18` runs total;
- proposed remaining-family cellwise batch: `171` runs total.

Because of that scale increase, the preparation should keep the operator flow
strictly structured:

- one family campaign per launcher;
- one aggregate sequential wrapper;
- remote execution support through the already standardized `-Remote` flag;
- campaign state explicitly tracked in `doc/running/active_training_campaign.yaml`.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/technical/2026-04/2026-04-17/2026-04-17-18-52-51_svm_reference_model_inventory_and_archive.md`
- `doc/technical/2026-04/2026-04-17/2026-04-17-19-43-39_track1_reference_family_archive_standardization.md`
- `doc/technical/2026-04/2026-04-18/2026-04-18-00-47-14_track1_remaining_exact_paper_family_campaigns.md`
- `doc/technical/2026-04/2026-04-18/2026-04-18-00-54-22_hybrid_campaign_launcher_remote_flag_standard.md`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `doc/running/active_training_campaign.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `scripts/campaigns/`
- `doc/scripts/campaigns/`
- `models/paper_reference/rcim_track1/`

## Implementation Steps

1. Create a dedicated planning report for the remaining-family cellwise
   campaign wave, including the `171`-run matrix and the family-by-family
   launcher structure.
2. Ask for explicit user approval of this technical document and the planning
   report before generating any campaign YAML or launcher.
3. If approved, prepare `9` family campaign packages, each containing `19`
   target-specific exact-paper runs aligned to the canonical `Track 1` cell
   inventory.
4. Generate one hybrid launcher per family plus one aggregate sequential
   launcher, all local by default and remote-capable through `-Remote`.
5. Register the prepared campaign state in
   `doc/running/active_training_campaign.yaml` before any execution.
6. After eventual execution, close out each completed family through:
   - validated campaign-results reporting;
   - benchmark and master-summary refresh;
   - colored `Tables 2-5` refresh when accepted best cells improve;
   - creation or extension of the family reference-model archive under
     `models/paper_reference/rcim_track1/`.
7. Run Markdown warning checks on the touched Markdown scope before closing the
   preparation task.
