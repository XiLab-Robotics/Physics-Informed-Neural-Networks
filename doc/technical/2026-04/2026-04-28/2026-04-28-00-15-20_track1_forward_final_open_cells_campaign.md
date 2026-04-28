# Track 1 Forward Final Open-Cells Campaign

## Overview

This technical document defines the next `Track 1` campaign preparation step
after the completed forward open-cell repair closeout.

The objective is now narrow: prepare one final forward-only repair wave that
targets only the last non-green cells still present on the canonical forward
restart surfaces of:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

The current canonical forward status is:

- `Table 2`: `3` yellow, `3` red
- `Table 3`: `3` yellow, `1` red
- `Table 4`: `1` yellow, `0` red
- `Table 5`: `0` yellow, `0` red

This leaves `11` forward non-green cells, which collapse into `8` unique
repair pairs once grouped by family, target kind, and harmonic.

## Technical Approach

The next wave should not reopen another wide forward family sweep. It should be
packaged as a final target-level repair campaign over the exact residual
surface only.

The preparation should:

1. derive the residual forward non-green inventory from the canonical
   benchmark;
2. collapse repeated metric hits into one queue item per unique target pair;
3. allocate more retry depth to currently red late-harmonic amplitude pairs;
4. keep the `original_dataset_exact_model_bank` runner and remote launcher
   stack already validated on `xilab-remote`;
5. preserve the closeout rule that any promoted winner must refresh
   `models/paper_reference/rcim_track1/forward/`.

The intended residual repair surface is:

- direction fixed to `forward`;
- only target pairs that are still yellow or red in the canonical benchmark;
- no backward work;
- no family-bank reruns;
- no reopening of already green forward cells.

The residual target-pair inventory is:

- `ERT` amplitude harmonic `156`
- `ERT` amplitude harmonic `162`
- `ERT` amplitude harmonic `240`
- `GBM` amplitude harmonic `162`
- `LGBM` amplitude harmonic `0`
- `LGBM` amplitude harmonic `162`
- `XGBM` amplitude harmonic `240`
- `LGBM` phase harmonic `81`

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `doc/running/active_training_campaign.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/`
- `scripts/campaigns/track1/exact_paper/`
- `doc/scripts/campaigns/`
- `models/paper_reference/rcim_track1/forward/`

## Implementation Steps

1. Create the campaign planning report with the exact residual inventory and
   retry budget.
2. Wait for explicit user approval of this technical document and the planning
   report.
3. Generate the final forward residual campaign YAML package.
4. Create the dedicated PowerShell launcher and launcher note.
5. Update `doc/running/active_training_campaign.yaml` to the new prepared
   campaign state.
6. Provide the exact launch command for the remote wave.

No subagent use is planned for this campaign-preparation task.
