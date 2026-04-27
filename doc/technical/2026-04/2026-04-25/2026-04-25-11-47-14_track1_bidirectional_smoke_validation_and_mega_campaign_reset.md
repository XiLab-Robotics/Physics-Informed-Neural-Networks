# 2026-04-25-11-47-14 Track1 Bidirectional Smoke Validation And Mega Campaign Reset

## Overview

This task resumes the new `Track 1` bidirectional branch after the repository
folder-taxonomy refactor.

The immediate goal is not to launch the full `10 x 19 x 2` training surface,
but to validate that the refactored original-dataset workflow still works end
to end:

- configuration loading;
- dataset-path resolution under the refactored taxonomy;
- file-level `70 / 20 / 10` splitting;
- forward-only and backward-only target generation;
- family fitting for all ten exact-paper families;
- artifact creation, report generation, and benchmark integration.

The user also requested a reset of the canonical
`doc/reports/analysis/RCIM Paper Reference Benchmark.md` tables because the
project is restarting the `Track 1` exact-model replication from zero on the
original dataset rather than continuing the older recovered forward-only wave.

## Technical Approach

The implementation is split into two stages.

Stage `1` is a smoke-validation wave:

- run one deliberately lightweight validation job per family for `forward`;
- run one deliberately lightweight validation job per family for `backward`;
- keep the goal purely structural, analogous to a `fast_dev_run`, without
  interpreting the resulting metrics as scientific evidence;
- verify that every family can complete the full runner path under the
  refactored folder structure.

Stage `2` is the preparation of the real bidirectional mega-campaign:

- build the campaign plan after the smoke wave confirms the new workflow is
  stable;
- generate the campaign YAMLs, launchers, launcher notes, and active-campaign
  state only after explicit approval;
- use the smoke findings to harden or narrow any family-specific settings
  before launching the large matrix.

The benchmark reset is handled as part of the approved implementation:

- replace the current forward-only historical repository-side matrices in
  `RCIM Paper Reference Benchmark.md` with a fresh restart state;
- preserve the paper-side reference matrices;
- add separate repository-owned sections for `forward` and `backward`;
- mark every repository-side cell as pending until new original-dataset runs
  exist.

## Involved Components

- `scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank_support.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank_support.py`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `scripts/campaigns/track1/exact_paper/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`

Subagent use:

- no subagents are planned for this task;
- all inspection, smoke validation, benchmark reset, and campaign preparation
  stay in the main rollout.

## Implementation Steps

1. Inspect the current refactored taxonomy and confirm the active campaign
   state no longer blocks a new preparation wave.
2. Create the required campaign-planning report for the bidirectional smoke
   validation plus the subsequent mega-campaign.
3. After approval, create narrow smoke configs for one lightweight run per
   family and per direction without modifying the canonical large-campaign
   configs.
4. Execute the `20` smoke validations and verify that every family completes
   runner setup, dataset construction, fitting, evaluation, export, and report
   writing.
5. Reset `RCIM Paper Reference Benchmark.md` so Tables `2-5` restart from a
   clean original-dataset `forward` / `backward` repository state.
6. If the smoke wave is structurally healthy, prepare the full bidirectional
   mega-campaign package under the refactored folder taxonomy.
