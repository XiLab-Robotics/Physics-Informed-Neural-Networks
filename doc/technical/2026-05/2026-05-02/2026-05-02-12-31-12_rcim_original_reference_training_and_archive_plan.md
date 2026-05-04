# RCIM Original Reference Training And Archive Plan

## Overview

This document defines the operator-run plan for retraining the recovered
original RCIM models with the repository-owned
`recovered_original_workflow/` pipeline and storing the resulting artifacts
under `models/paper_reference/rcim_original/`.

The immediate goal is to prepare exact launch commands, not to execute the
training in this implementation turn.

The plan separates:

- a `forward` replay based on the recovered `v18` tuned-parameter path;
- a `backward` retuning pass based on the recovered `v17` cross-validation
  path;
- a later `backward` tuned replay once the retuned parameters have been
  transferred into the `paper_eval` surface.

## Technical Approach

The operator-facing commands will target the repository-owned entrypoint:

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`

The selected modes are:

- `--mode paper_eval` for the `forward` replay with the recovered tuned
  hyperparameters;
- `--mode retune` for the `backward` hyperparameter search, which writes
  `summaryBestParameter+*.csv` artifacts under the chosen runtime root.

The runtime root will be redirected away from
`output/validation_checks/...` and into:

- `models/paper_reference/rcim_original/forward/source_runs/<run_instance_id>/`
- `models/paper_reference/rcim_original/backward/source_runs/<run_instance_id>/`

This keeps the raw Python and ONNX model bundles co-located with the intended
paper-reference archive root, even though the full family-by-family
`rcim_track1`-style curation surface is not yet automated for
`rcim_original/`.

Important limitation discovered during planning:

- the repository-owned `paper_eval` mode still reads its tuned estimators from
  the hardcoded `_build_paper_tuned_family_factory_map()` branch;
- the `retune` mode exports `best_params_` to CSV, but there is currently no
  CLI flag that injects those retuned `backward` parameters automatically into
  the later `paper_eval` run.

Because of that limitation, the `backward` flow is currently:

1. run `retune`;
2. inspect the exported `summaryBestParameter+*.csv`;
3. manually translate the chosen parameter set into the `paper_eval` tuned
   family map, or implement a dedicated parameter-ingestion surface later;
4. only then run the `backward` `paper_eval` replay.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/create_dataframe.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `reference/rcim_ml_compensation_recovered_assets/code/original_pipeline/README.md`
- `models/paper_reference/rcim_original/`
- `doc/reports/campaign_plans/mixed_training/`

Protected campaign state acknowledged but not edited:

- `doc/running/active_training_campaign.yaml`

## Implementation Steps

1. Create and register this technical document.
2. Create the matching training planning report under
   `doc/reports/campaign_plans/mixed_training/`.
3. Record exact operator-run commands for:
   - optional dataframe regeneration;
   - `forward` `paper_eval`;
   - `backward` `retune`;
   - the manual `backward` parameter handoff checkpoint;
   - the deferred `backward` `paper_eval` replay once tuned parameters are
     available in the `paper_eval` surface.
4. Stop for user approval before any training execution or implementation of
   the missing `backward` tuned-parameter ingestion surface.
