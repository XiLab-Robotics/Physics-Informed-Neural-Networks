# Track 1 Forward Open-Cell Repair Campaign Plan Report

## Overview

This planning report prepares a forward-only `Track 1` exact-paper repair
campaign on the original-dataset restart benchmark surface.

The campaign does not reopen the completed bidirectional mega-campaign. It
instead isolates the forward residual work and retries only the currently
non-green forward family-target cells in Tables `2-5`.

## Current Forward Restart Status

Canonical status source:

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`

Current forward-side counts:

| Table | Green | Yellow | Red | Non-Green |
| --- | ---: | ---: | ---: | ---: |
| `Table 2 - Amplitude MAE` | `82` | `2` | `16` | `18` |
| `Table 3 - Amplitude RMSE` | `82` | `6` | `12` | `18` |
| `Table 4 - Phase MAE` | `82` | `0` | `8` | `8` |
| `Table 5 - Phase RMSE` | `81` | `6` | `3` | `9` |
| Total | `327` | `14` | `39` | `53` |

## Campaign Objective

Prepare a forward-only repair campaign that tries to reduce the `53` non-green
forward cells without paying for a new bidirectional full-bank rerun.

The campaign must answer one program-level question:

1. which forward family-target residuals can still be closed or improved under
   the current original-dataset exact-model-bank workflow.

## Campaign Principle

The repair package should operate on target-level residual items, not on the
entire `10 x 19` family banks.

Each queue item should encode:

- one family;
- one direction fixed to `forward`;
- one target harmonic/component pair;
- one benchmark-table objective group;
- one retry attempt index.

This keeps the package inspectable and aligned with the real residual surface.

## Planned Repair Scope

The campaign should include only forward-side family-target pairs that are
currently yellow or red in the benchmark matrices for Tables `2-5`.

Expected target classes:

- amplitude targets from Tables `2-3`;
- phase targets from Tables `4-5`.

Expected grouped repair surface:

- `21` unique amplitude repair items
- `9` unique phase repair items
- `30` unique forward repair items in total

Expected high-pressure forward families from the current matrices:

- `ERT`
- `GBM`
- `LGBM`

Expected medium-pressure forward families:

- `SVM`
- `HGBM`
- `XGBM`

Families already fully green on the forward surfaces should not receive repair
items unless they are needed as comparators for a still-open target.

## Queue Policy

Recommended queue design:

| Setting | Planned Value |
| --- | --- |
| Direction Scope | `forward` only |
| Repair Surface | only current non-green forward family-target cells |
| Retry Multiplicity | `10` attempts per repair item |
| Baseline Family Bank Refresh | none in this package |
| Launch Mode | remote operator launcher |
| Runner Branch | `run_original_dataset_exact_model_bank_validation.py` |
| Dataset Root | `data/datasets` |
| Split Policy | canonical file-level `70 / 20 / 10` |

With `30` grouped repair items and `10` retries each, the expected queue size is:

- `300` total YAML runs

## Why This Surface Is Preferred

This campaign is preferred over a new forward full-bank rerun because:

- it spends compute only on cells that are still open;
- it keeps progress legible at family-target level;
- it produces a direct residual-closure readout for the benchmark;
- it is still large enough to explore retry variance where the mega-campaign
  already showed sensitivity.

## Evaluation Rules

The campaign summary must report:

1. how many forward yellow cells were closed;
2. how many forward red cells were upgraded to yellow or green;
3. which family-target pairs remain open after the repair wave;
4. whether any accepted target winner must replace the archived forward
   reference model under `models/paper_reference/rcim_track1`.

## Operator Deliverables

After approval, the preparation phase must generate:

1. the targeted forward repair YAML package;
2. a dedicated PowerShell launcher under `scripts/campaigns/track1/exact_paper/`;
3. a matching launcher note under `doc/scripts/campaigns/`;
4. the prepared campaign state under `doc/running/active_training_campaign.yaml`;
5. the exact remote launch command.

## Execution Gate

Before the campaign is launched:

1. the technical document must be approved;
2. this planning report must be approved;
3. the config package must exist;
4. the launcher and launcher note must exist;
5. the active campaign state must be updated to the new prepared campaign.
