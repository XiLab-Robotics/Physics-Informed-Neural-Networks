# RCIM Model-Bank Reproduction Exact-Paper ELM Export Hardening And Quiet LGBM

## Overview

Two recovered-original fixes now need to be reflected in the RCIM Model-Bank Reproduction
exact-paper workflow:

1. commit `e8f0372dbe9d51428f21585591f801805f89b1c0`
   hardened ONNX export for `ELMRegressor` by removing the fragile
   `n_features_in_` assumption and adding repo-owned converter support for the
   fitted `skelm` surface; and
2. commit `eaaf88b897f36ec927a1cfa939174a047db68f53`
   made the recovered-original `LGBMRegressor` family quiet by forcing
   `verbosity=-1` and `force_col_wise=True`.

The RCIM Model-Bank Reproduction exact-paper shared pipeline already uses the canonical `10`
family bank and therefore does **not** currently expose `ELM` as one of its
active paper-faithful families. That means the recovered-original `ELM` fix is
not a direct family-level port. Instead, the relevant RCIM Model-Bank Reproduction equivalent is to
harden the shared exact-paper export helper so it can safely handle future
estimators that do not expose the common `n_features_in_` surface, and so the
shared exporter can support `ELMRegressor` deterministically if that estimator
is ever routed through the exact-paper export path.

The `LGBM` fix is directly applicable today because `LGBM` is part of the
active RCIM Model-Bank Reproduction exact-paper family bank.

## Technical Approach

The implementation will split into two narrow changes in the shared
exact-paper support layer.

### 1. Shared ONNX Export Hardening For ELM-Like Estimators

Mirror the recovered-original exporter hardening in the exact-paper shared
export layer by:

- introducing a fitted-estimator feature-count resolver instead of assuming one
  specific attribute surface;
- optionally importing `skelm.ELMRegressor` and its hidden-layer metadata when
  available;
- registering the same repo-owned `ELMRegressor` ONNX converter in the
  exact-paper export helper; and
- using that converter only when the exported estimator is actually an
  `ELMRegressor`.

This does **not** change the canonical RCIM Model-Bank Reproduction exact-paper family inventory.
It only makes the shared exact-paper export surface parity-ready with the
recovered-original exporter fix.

### 2. Quiet Repository-Owned LGBM Factory

Mirror the recovered-original `LGBM` console-noise suppression by routing the
RCIM Model-Bank Reproduction exact-paper `LGBMRegressor` family through a repo-owned factory that
forces:

- `verbosity=-1`
- `force_col_wise=True`

while preserving the current exact-paper tuned defaults and grid-search
surface.

This keeps the mathematical search protocol unchanged and only improves the
quality-of-life of exact-paper training and remote logging.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`
  Shared exact-paper family registry, `LGBM` estimator factory, and ONNX
  export helper.
- `scripts/paper_reimplementation/rcim_ml_compensation/README.md`
  Canonical exact-paper operator README for shared workflow behavior.
- `doc/guide/project_usage_guide.md`
  User-facing workflow guide that should describe any user-visible `LGBM`
  logging change or export-surface hardening.
- `site/api/paper_reimplementation/exact_paper_model_bank_support.rst`
  Sphinx API surface if shared helper names or export semantics become more
  explicit.
- `doc/running/active_training_campaign.yaml`
  Current campaign-state reference. The parent RCIM Model-Bank Reproduction paper-faithful campaign
  is already `cancelled`, so no active campaign mutation is expected.

No subagent is planned for this change.

## Implementation Steps

1. Compare commits `e8f0372dbe9d51428f21585591f801805f89b1c0` and
   `eaaf88b897f36ec927a1cfa939174a047db68f53` against the current shared
   exact-paper support layer.
2. Port the generic estimator feature-count resolver and optional repo-owned
   `ELMRegressor` ONNX converter support into the exact-paper export helper
   without adding `ELM` to the canonical RCIM Model-Bank Reproduction family list.
3. Add one repo-owned quiet `LGBMRegressor` factory in the shared exact-paper
   family registry and reuse it for the active `LGBM` family path.
4. Update the exact-paper operator documentation to reflect the quieter `LGBM`
   surface and the export-helper hardening scope.
5. Run targeted verification:
   - compile the touched Python modules;
   - validate the quiet `LGBM` factory parameters;
   - validate the hardened export helper on at least one representative
     estimator path.
6. Rebuild the Sphinx portal if the touched guide or API surface remains in
   scope.
7. Run Markdown QA on the touched repository-owned Markdown scope before
   closing the task.
