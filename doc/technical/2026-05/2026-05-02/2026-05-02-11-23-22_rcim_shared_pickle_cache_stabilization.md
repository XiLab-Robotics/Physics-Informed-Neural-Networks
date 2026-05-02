# RCIM Shared Pickle Cache Stabilization

## Overview

The current recovered-original RCIM workflow stores cached instance pickles
under:

`data/paper_reimplementation_rcim_recovered_original_workflow/instance_pickle_cache/original_pipeline_instances_v3_<hash>/`

This layout is stable for one source-tree path, but it is still more granular
than needed for the current workflow. The user wants a simpler shared cache
root such as:

`data/original_pipeline_instances/`

so repeated validation or workflow reruns reuse the same cached pickles instead
of creating new per-source cache directories unnecessarily.

The user also wants an explicit runtime flag that controls whether the workflow:

- reuses existing cached pickles when present; or
- regenerates them from source data even if cache files already exist.

The future dataset-shrinking branch should not be implemented in this pass.
Instead, that future need should be tracked explicitly in the backlog because
it will require coordinated work on the original dataset surface and not only
on the recovered workflow wrapper.

## Technical Approach

The change will keep the recovered-original workflow logic intact while
simplifying the repository-owned cache contract.

The new plan is:

1. replace the hashed default cache root with a single shared directory:
   `data/original_pipeline_instances/`;
2. keep the explicit `--instance-cache-directory` override for advanced cases;
3. add a boolean CLI control for cache rebuild, exposed consistently in:
   - `create_dataframe.py`
   - `evaluate_models.py`
4. thread the rebuild flag into `Statistics`, so cache creation becomes:
   - reuse existing pickle by default;
   - overwrite and rebuild when the new flag is enabled;
5. update the workflow README and usage guide to document the new cache
   contract and the rebuild behavior;
6. record a deferred backlog note for the future dataset-shrinking branch,
   rather than implementing dataset-split-aware cache partitioning now.

This keeps the workflow simple for the current canonical case while preserving
an escape hatch for future experiments.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/workflow_runtime.py`
  - simplify the default cache-root resolution
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py`
  - expose the new cache-rebuild CLI flag
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/evaluate_models.py`
  - expose the same cache-rebuild CLI flag
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/statistics.py`
  - honor the rebuild policy when loading or writing pickle cache files
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/README.md`
  - update the cache-path description and the cache-policy explanation
- `doc/guide/project_usage_guide.md`
  - update the user-facing workflow notes if needed
- `doc/running/te_model_live_backlog.md`
  - add a deferred note for future dataset-shrinking-aware cache partitioning

## Implementation Steps

1. change the default cache root from the hashed workflow-local subtree to
   `data/original_pipeline_instances/`;
2. add a rebuild flag such as `--rebuild-instance-cache` to the relevant
   entrypoints;
3. propagate the rebuild policy into `Statistics` without changing the core
   numerical workflow;
4. verify that rerunning the workflow reuses cached pickles by default and only
   overwrites them when the rebuild flag is passed;
5. update the recovered-workflow README and the backlog note for the deferred
   dataset-shrinking case;
6. run the relevant smoke checks and scoped Markdown QA.
