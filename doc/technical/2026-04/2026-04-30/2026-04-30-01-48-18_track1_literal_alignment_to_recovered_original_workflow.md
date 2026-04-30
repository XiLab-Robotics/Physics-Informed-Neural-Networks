# 2026-04-30-01-48-18 Track1 Literal Alignment To Recovered Original Workflow

## Overview

This task will realign the Track 1 exact-paper reimplementation to the
recovered original RCIM workflow with literal fidelity, not only
paper-aligned behavior.

The immediate trigger is the persistent forward residual plateau on the last
three `Table 2` yellow cells after multiple repair campaigns. The current
reimplementation already matches many recovered family classes and several
recovered hyperparameter anchors, but it still diverges from the original
workflow in the operational surfaces that matter for reproducibility:
base-estimator configuration for some families, family-specific
`GridSearchCV` spaces, and the shared exact-paper training path that encodes
those behaviors independently from the recovered original code.

The goal of this feature is therefore to make the repository-owned Track 1
training path use the same family definitions and the same search behavior as
the recovered original workflow for all ten paper families:
`SVM`, `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `XGBM`, and `LGBM`.

## Technical Approach

The implementation will treat the recovered original workflow under
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow`
as the canonical source of truth for Track 1 family behavior.

The alignment will be done in three layers.

First, we will perform a family-by-family literal audit between the recovered
original workflow and the current repository-owned exact-paper branch. The
comparison surface will include:

- estimator class identity;
- fixed base-estimator hyperparameters;
- family-specific `GridSearchCV` parameter names and candidate values;
- training/search protocol details that affect deterministic behavior.

Second, we will update the shared exact-paper support layer so that it
reproduces the recovered original family registry and search-space builder
instead of keeping a partially re-encoded approximation. This is especially
important because the original-dataset exact-model-bank branch currently
depends on that shared layer, so one fix there propagates to the Track 1
campaign surface used by the paper-reimplementation workflow.

Third, we will verify that the resulting exact-paper/original-dataset branch
still produces valid training bundles, validation artifacts, and campaign
launcher behavior, then prepare the next residual-cell campaign on top of the
literalized implementation instead of on top of the current approximated one.

No algorithm substitutions are allowed in this task. If a family is used in
the recovered original workflow, the repository implementation must reproduce
that same family behavior rather than replacing it with a nearby alternative.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/run_original_dataset_exact_model_bank_validation.py`
- `doc/reports/analysis/RCIM Original Pipeline To Reimplementation Companion.md`
- `doc/reports/analysis/RCIM Original Pipeline And Reimplementation Audit.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/running/active_training_campaign.yaml`
- future planning artifact under `doc/reports/campaign_plans/track1/exact_paper/`

Subagents:

- none planned;
- if later code-review delegation becomes useful, it will require explicit
  user approval before any launch.

## Implementation Steps

1. Audit all ten Track 1 families against the recovered original workflow and
   freeze the exact divergence list for base estimators, grids, and search
   protocol.
2. Refactor the shared exact-paper family registry so that the repository code
   uses the recovered original family definitions literally wherever the Track
   1 exact-paper/original-dataset branches depend on them.
3. Refactor the shared exact-paper parameter-grid builder so that each family
   reproduces the recovered original `predictorML.py` search surface, including
   candidate keys that are currently omitted or renamed.
4. Verify that the exact-paper and original-dataset exact-model-bank branches
   still build, fit, and validate successfully after the alignment.
5. Write the campaign-preparation note for the next residual forward repair
   wave on top of the literalized implementation, rather than reusing the old
   approximate branch unchanged.
