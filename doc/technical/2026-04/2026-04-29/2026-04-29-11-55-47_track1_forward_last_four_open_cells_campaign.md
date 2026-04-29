# 2026-04-29-11-55-47 Track1 Forward Last Four Open Cells Campaign

## Overview

This document prepares one final targeted exact-paper `Track 1` forward-only
campaign after the completed maxi residual wave.

The canonical forward residual now contains only `4` non-green cells across
Tables `2-5`, and all remaining openings live on amplitude surfaces:

- `ERT ampl 156`: `Table 2` yellow
- `ERT ampl 240`: `Table 2` yellow and `Table 3` yellow
- `GBM ampl 162`: `Table 2` yellow

The implementation step after approval should therefore prepare a narrow
campaign that attacks only these last `3` pair targets and leaves every other
forward target untouched.

## Technical Approach

The campaign should reuse the exact-paper forward repair workflow already used
by the previous `open_cell_repair`, `final_open_cells`,
`last_non_green_cells`, and `maxi_last_non_green_cells` waves.

The queue should stay small and inspectable relative to the maxi wave while
still giving extra depth to the only remaining multi-surface residue:

- `ERT ampl 156`: single-surface yellow retry tier
- `GBM ampl 162`: single-surface yellow retry tier
- `ERT ampl 240`: multi-surface yellow retry tier

The intended implementation path after approval is:

1. create one new planning report under `doc/reports/campaign_plans/`;
2. generate one dedicated config root under
   `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/`;
3. generate one dedicated preparer and one dedicated remote launcher under
   `scripts/campaigns/track1/exact_paper/`;
4. generate the matching launcher note under `doc/scripts/campaigns/`;
5. update `doc/running/active_training_campaign.yaml` with the prepared queue;
6. after execution, run the normal forward closeout path and refresh the
   canonical reports and forward reference archives only if accepted winners
   improve.

No subagent use is planned for this task. If subagent delegation becomes
useful later, it must be proposed explicitly and approved before use.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/campaign_plans/track1/exact_paper/`
- `doc/running/active_training_campaign.yaml`
- `scripts/campaigns/track1/exact_paper/`
- `scripts/reports/closeout/track1/closeout_track1_forward_open_cell_repair_campaign.py`
- `config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/campaigns/track1/exact_paper/`

## Implementation Steps

1. Freeze the canonical residual inventory for the last `4` forward non-green
   cells from the benchmark and latest closeout report.
2. Write the planning report with the exact pair inventory and proposed retry
   budget.
3. Wait for explicit user approval before generating any campaign YAML,
   launcher, launcher note, or campaign-state update.
4. After approval, implement the campaign package and surface the exact launch
   command.
