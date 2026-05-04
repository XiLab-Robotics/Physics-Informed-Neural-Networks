# 2026-05-03-13-23-46 Track1 Bidirectional Paper Faithful Grid Search Campaign Replacement

## Overview

This document replaces the currently running `Track 1` bidirectional
literal-workflow refresh mega campaign with a paper-faithful campaign design.

The current `400`-run design is not aligned with the recovered original RCIM
workflow because it repeats the same family-direction surface across many seed
attempts. The recovered original workflow instead performs one
hyperparameter-search pass per model using a fixed split and a single
`GridSearchCV` execution.

The replacement campaign must therefore cover:

- `10` model families in the `forward` direction;
- `10` model families in the `backward` direction;
- exactly `1` grid-search training run per family-direction surface.

The resulting campaign surface is `20` total runs, not `400`.

## Technical Approach

Treat the recovered original workflow under
`scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow`
as the behavioral source of truth for campaign structure.

The replacement campaign will:

1. preserve the already literalized family definitions and family grids in the
   shared exact-paper support layer;
2. remove repeated seed attempts from the campaign design;
3. materialize one config per family-direction surface using the original
   single-search semantics;
4. keep the current exact-paper artifact layout and repo bookkeeping rules;
5. replace the running `400`-run campaign only after explicit approval because
   `doc/running/active_training_campaign.yaml` is protected while the campaign
   is active.

The campaign policy must explicitly mirror the paper-faithful interpretation:

- one fixed train/test split policy per family-direction surface;
- one `GridSearchCV` pass per family-direction surface;
- no retry wave, no seed sweep, no robustness repetition layer.

## Involved Components

- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `scripts/campaigns/track1/exact_paper/`
- `doc/scripts/campaigns/`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/training_models.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/utilities/predictorML.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/exact_paper_model_bank/exact_paper_model_bank_support.py`

No subagent is planned for this scope. If subagent assistance becomes useful
later, it must be declared and approved before use.

## Implementation Steps

1. Freeze the replacement campaign design in a planning report that explicitly
   supersedes the current `400`-run mega campaign.
2. After approval, prepare a new bidirectional exact-paper campaign with `20`
   total runs, one per family-direction surface.
3. Generate the matching YAML set, PowerShell launcher, and launcher note.
4. Update `doc/running/active_training_campaign.yaml` from the current active
   `400`-run campaign state to the new replacement campaign state only after
   explicit approval.
5. Provide the exact launch command for the new paper-faithful campaign.
