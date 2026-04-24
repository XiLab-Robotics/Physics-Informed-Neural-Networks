# Track 1 Remaining Yellow Cells Multi-Family Campaign Bundle

## Overview

This technical document defines the next exact-paper `Track 1` preparation
step after the residual `MLP` final-closure wave.

The user requested one new overnight-ready preparation package focused only on
the still-open yellow cells of the currently unfinished exact-paper families:

- `SVM`
- `MLP`
- `ET`
- `ERT`
- `HGBM`
- `XGBM`

The requested delivery shape is:

- one dedicated campaign per family;
- one global launcher that can start the whole overnight bundle in sequence.

This preparation remains tied to the canonical `Track 1` progress definition:
only the four full-matrix replication tables count as the status surface:

- `Table 2 - Amplitude MAE Full-Matrix Replication`
- `Table 3 - Amplitude RMSE Full-Matrix Replication`
- `Table 4 - Phase MAE Full-Matrix Replication`
- `Table 5 - Phase RMSE Full-Matrix Replication`

Harmonic-wise work remains outside this campaign bundle.

## Technical Approach

The new wave should avoid broad family-wide reruns. It should spend the
overnight budget only on family-target pairs that still produce yellow cells
in the accepted canonical benchmark.

The preparation strategy is:

1. re-read the current benchmark and extract only the yellow cells of the
   still-open families listed above;
2. deduplicate those yellow cells into exact-paper family-target pairs,
   because one accepted pair can affect one or more benchmark cells;
3. generate one family-local campaign folder per still-open family, keeping
   the family boundary explicit and inspectable;
4. assign retry depth family by family based on the number and hardness of the
   residual yellow pairs so the total overnight queue stays practical;
5. create one dedicated launcher per family plus one aggregate launcher that
   invokes the family launchers in a stable order;
6. keep all naming aligned across:
   - campaign names;
   - config folders;
   - run names;
   - launcher names;
   - launcher notes;
   - active campaign metadata.

The preparation must remain exact-paper-safe:

- exact-paper family-bank workflow only;
- immutable run-instance outputs;
- no new legacy output roots;
- canonical `doc/running/active_training_campaign.yaml` update only after the
  package is approved and prepared.

No subagent is planned for this work. The task remains a repository-owned
campaign preparation flow in the main rollout.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/`
- `scripts/campaigns/track1/exact_paper/`
- `doc/scripts/campaigns/`
- `doc/running/active_training_campaign.yaml`
- `output/training_campaigns/track1/exact_paper/`

After approval, the expected implementation outputs are:

- one new campaign planning report for the multi-family yellow-cell overnight
  bundle;
- one exact-paper config directory per targeted family;
- one launcher per family under `scripts/campaigns/track1/exact_paper/`;
- one matching launcher note per family under `doc/scripts/campaigns/`;
- one aggregate overnight launcher plus aggregate launcher note;
- one updated `doc/running/active_training_campaign.yaml` entry that points to
  the prepared global bundle.

## Implementation Steps

1. Re-read the canonical benchmark and extract the residual yellow cells for
   `SVM`, `MLP`, `ET`, `ERT`, `HGBM`, and `XGBM`.
2. Convert those cells into a deduplicated family-target inventory and decide
   one retry matrix per family.
3. Write the planning report with:
   - family-by-family residual inventory;
   - per-family run counts;
   - total overnight run count;
   - launch order and restart assumptions.
4. Generate one config folder per family under the exact-paper campaign root.
5. Create one family launcher and one family launcher note for each targeted
   family.
6. Create one aggregate overnight launcher and matching launcher note.
7. Update the active campaign state with the prepared multi-family bundle.
8. Run repository Markdown warning checks on the touched Markdown scope before
   closing the preparation step.
