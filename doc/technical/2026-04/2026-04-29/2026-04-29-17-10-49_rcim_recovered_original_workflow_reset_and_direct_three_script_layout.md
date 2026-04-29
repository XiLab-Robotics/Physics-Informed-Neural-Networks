# 2026-04-29-17-10-49 Rcim Recovered Original Workflow Reset And Direct Three Script Layout

## Overview

The current repository-owned recovered RCIM workflow under:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`

was built around an earlier staged reconstruction that split the copied source
across `dataframe_creation/`, `training/`, and `evaluation/` plus an external
runner. That structure no longer matches the newly recovered full original
pipeline root under:

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`

The user now wants to restart this recovered-workflow surface from zero and
rebuild it directly from the newly recovered original scripts, while keeping
the code as faithful as possible.

The requested target layout is:

- `create_dataframe.py`
- `training_models.py`
- `evaluate_models.py`
- `utilities/`

with `utilities/` containing:

- `statistics.py`
- `instance_v4.py`
- `instance_v5.py`
- `predictorML.py`

The new direct scripts should run without an external orchestration runner.
Instead, each main script should own sensible repository-style path handling in
its own `main()`/CLI layer.

The current workflow README should also be replaced with a new canonical guide
at:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`

That README should track the rebuilt workflow end to end, including:

- the new folder structure;
- the three main entrypoints;
- the role of each utility module;
- the execution order;
- the expected inputs and outputs;
- the mapping from original RCIM script names to the new repository-owned
  layout.

## Technical Approach

The reorganization should treat the newly recovered original root as the sole
source of truth for the copied workflow logic. The goal is not to rewrite the
prediction, statistics, or instance logic into a new repository abstraction.
The goal is to preserve those functions almost exactly and only modernize:

- file layout;
- entrypoint names;
- path resolution;
- artifact-root selection;
- script argument handling;
- the unification of `v17` and `v18` training behavior into one operator-facing
  script.

The target approach is:

1. discard the current staged reconstructed subtree as the implementation
   baseline for this surface;
2. rebuild the subtree from the newly recovered original scripts;
3. keep the core original logic in near-original copied modules under
   `utilities/`;
4. expose three top-level repository-owned entrypoints that call into those
   original modules with minimal path adaptation.

For training, `training_models.py` should unify:

- the `v17` export behavior;
- the `v17` plus hyperparameter-search behavior;
- the `v18` tuned `80/20` paper-style behavior;

through explicit CLI/config arguments rather than through separate copied main
files.

The new path policy should avoid original mutable local folders such as:

- `output_prediction/`
- `model_output_dir/`

inside the script folder as canonical outputs. Instead, the main scripts should
resolve inputs and outputs into repository-owned locations while still
producing original-style intermediate filenames when needed for compatibility.

No subagents are planned for this task.

## Involved Components

- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/` notes that point
  at the recovered workflow
- RCIM analysis reports if they need path updates after the subtree reset
- `doc/guide/project_usage_guide.md` and `site/` only if the new surface
  changes user-facing runnable workflow documentation materially

## Implementation Steps

1. Inspect the current `recovered_original_workflow/` subtree and identify what
   should be removed or replaced so the new structure is clean.
2. Re-read the newly recovered original scripts and map them into the desired
   repository layout:
   - `0-main_createDFforPrediction.py -> create_dataframe.py`
   - `1.1-main_prediction_v17.py` plus `1-main_prediction_v18.py -> training_models.py`
   - `2-main_evaluatePrediction_v4.py -> evaluate_models.py`
   - `statistic.py -> utilities/statistics.py`
   - `predictorML_v7.py -> utilities/predictorML.py`
   - `instance_v4.py`, `instance_v5.py -> utilities/`
3. Implement direct per-script path handling so the three main scripts can run
   without an external runner while still preserving the original inner logic.
4. Remove or retire the old external runner and the now-obsolete staged copied
   layout if it conflicts with the new canonical subtree.
5. Update the recovered-workflow README so it documents:
   - the three direct entrypoints;
   - the CLI modes for training;
   - the repository-owned input/output policy;
   - how `v17`, `v17+tuning`, and `v18` map into `training_models.py`;
   - the original-to-new filename mapping for the rebuilt subtree.
6. Run code verification and Markdown QA on the touched scope before closing
   the task.
