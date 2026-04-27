# Track 1 Forward Open-Cell Repair Campaign

## Overview

This technical document defines the next `Track 1` campaign package after the
completed bidirectional original-dataset mega-campaign closeout.

The immediate goal is not another bidirectional full-bank sweep. The immediate
goal is a forward-only repair wave that attacks the still non-green cells in the
forward restart surfaces of:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

The current forward-side restart status is:

- `Table 2`: `2` yellow, `16` red
- `Table 3`: `6` yellow, `12` red
- `Table 4`: `0` yellow, `8` red
- `Table 5`: `6` yellow, `3` red

This yields `53` forward non-green cells in total.

## Technical Approach

The campaign should be packaged as a forward-only targeted repair surface
instead of a fresh `10 x 20` family-bank rerun.

The preparation should:

1. derive the forward non-green target queue from the canonical benchmark;
2. map each non-green forward cell to the corresponding
   family-target-table-direction repair item;
3. generate a narrow queue that retries only those forward repair items;
4. keep the original-dataset exact-model-bank runner and remote launcher stack;
5. preserve the post-micro remote hardening already validated on
   `xilab-remote`.

The intended repair surface is target-level and forward-only:

- direction fixed to `forward`;
- only family-target pairs that are currently yellow or red on the forward
  surfaces are eligible;
- retry multiplicity is applied per repair item instead of per whole
  family-bank surface.

The `53` non-green forward cells collapse into `30` unique repair items once
the benchmark residuals are grouped by:

- family;
- target kind: `ampl` or `phase`;
- harmonic order.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `doc/running/active_training_campaign.yaml`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/`
- `scripts/campaigns/track1/exact_paper/`
- `doc/scripts/campaigns/`

## Implementation Steps

1. Create the forward-only campaign planning report with the exact repair scope
   and queue policy.
2. Wait for explicit user approval of this technical document and the planning
   report.
3. Generate the forward-only repair campaign YAML package.
4. Create the dedicated PowerShell launcher and launcher note.
5. Update `doc/running/active_training_campaign.yaml` to the new prepared
   campaign state.
6. Provide the exact launch command.

No subagent use is planned for this campaign-preparation task.
