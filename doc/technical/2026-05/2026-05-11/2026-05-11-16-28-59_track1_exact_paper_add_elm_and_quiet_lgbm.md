# RCIM Model-Bank Reproduction Exact-Paper Add ELM And Quiet LGBM

## Overview

The RCIM Model-Bank Reproduction exact-paper workflow now needs two aligned changes relative to the
recovered-original RCIM pipeline:

1. adopt the recovered-original `ELMRegressor` ONNX export fix from commit
   `e8f0372dbe9d51428f21585591f801805f89b1c0`; and
2. adopt the quieter repository-owned `LGBMRegressor` factory from commit
   `eaaf88b897f36ec927a1cfa939174a047db68f53`.

Unlike the earlier narrower plan, the user now explicitly wants the RCIM Model-Bank Reproduction
exact-paper workflow to **include the `ELM` family itself**, analogous to the
recovered-original pipeline. This means the change is no longer limited to
export-helper hardening. The canonical exact-paper family bank, family
registry, grid-search surface, reporting, and operator documentation must all
be extended from `10` families to `11`, with `ELM` added as a first-class
RCIM Model-Bank Reproduction exact-paper family.

This supersedes the earlier narrower plan in
`2026-05-11-16-26-01_track1_exact_paper_elm_export_hardening_and_quiet_lgbm.md`.

## Technical Approach

The implementation will apply two coordinated changes to the shared
exact-paper RCIM Model-Bank Reproduction layer.

### 1. Promote ELM To A Canonical RCIM Model-Bank Reproduction Exact-Paper Family

Mirror the recovered-original `ELM` family surface in the RCIM Model-Bank Reproduction exact-paper
workflow by:

- extending the canonical exact-paper family order, display map, estimator
  name map, and family alias map to include `ELM`;
- adding the exact-paper base estimator construction for `ELMRegressor`;
- adding the recovered-original-style `ELM` hyperparameter grid;
- allowing `ELM` through enabled-family resolution, ranking, report tables,
  export loops, and campaign-family selection surfaces; and
- porting the repo-owned `ELMRegressor` ONNX converter and fitted-feature-count
  resolver so the new RCIM Model-Bank Reproduction family can emit `Python + ONNX` artifacts just
  like the recovered-original branch.

### 2. Quiet Repository-Owned LGBM Factory

Mirror the recovered-original `LGBM` console-noise suppression by routing the
RCIM Model-Bank Reproduction exact-paper `LGBMRegressor` family through a repo-owned factory that
forces:

- `verbosity=-1`
- `force_col_wise=True`

while preserving the existing exact-paper tuned defaults and grid-search
surface.

These changes do not alter the intended mathematical search protocol for
existing exact-paper families. They extend the family surface with `ELM` and
improve the operational quality of the `LGBM` family.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
  Shared exact-paper family registry, `ELM` and `LGBM` base-estimator
  factories, exact-paper parameter grids, replay logic, export helper, and
  family-order-driven reporting.
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/original_dataset_exact_model_bank_support.py`
  Original-dataset reporting and validation surface that may need wording
  updates once `ELM` becomes part of the canonical RCIM Model-Bank Reproduction family bank.
- `scripts/paper_reimplementation/rcim_ml_compensation/README.md`
  Canonical exact-paper operator README for the shared RCIM Model-Bank Reproduction family list and
  workflow behavior.
- `doc/guide/project_usage_guide.md`
  User-facing workflow guide for the new `ELM` family availability and quieter
  `LGBM` behavior.
- `site/api/paper_reimplementation/exact_paper_model_bank_support.rst`
  Sphinx API surface for the shared exact-paper helper module.
- `doc/running/active_training_campaign.yaml`
  Current campaign-state reference. The parent RCIM Model-Bank Reproduction paper-faithful campaign
  is already `cancelled`, so no active campaign mutation is expected.

No subagent is planned for this change.

## Implementation Steps

1. Compare recovered-original `ELM` and quiet `LGBM` behavior against the
   current shared exact-paper RCIM Model-Bank Reproduction layer.
2. Add `ELM` to the canonical exact-paper family registry, estimator factory,
   hyperparameter grid, and family-order-driven report/export surfaces.
3. Port the repo-owned fitted-feature-count resolver and `ELMRegressor` ONNX
   converter support into the exact-paper shared exporter.
4. Add the quieter repository-owned `LGBMRegressor` factory and reuse it for
   the active RCIM Model-Bank Reproduction exact-paper `LGBM` family path.
5. Update exact-paper operator documentation and guide content to reflect the
   `11`-family RCIM Model-Bank Reproduction surface and the quieter `LGBM` behavior.
6. Run targeted verification:
   - compile the touched Python modules;
   - verify the `ELM` family registry and grid surface resolve correctly;
   - verify the quiet `LGBM` factory parameters;
   - validate at least one representative `ELM` export-helper path if the
     dependency is available.
7. Rebuild the Sphinx portal if the touched guide or API surface remains in
   scope.
8. Run Markdown QA on the touched repository-owned Markdown scope before
   closing the task.
