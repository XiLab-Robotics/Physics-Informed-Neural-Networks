# Track 1 Extended Overnight Campaign Preparation

## Overview

This document prepares a much larger and more aggressive `Track 1`
 harmonic-wise campaign after the latest overnight batch showed that the
 current validation runs are operationally cheap.

The key new planning fact is that the latest overnight campaign executed
 `20` runs in a short window while still leaving the branch far from the paper
 offline threshold. That means the practical bottleneck is no longer runtime
 alone. The branch can now support:

- wider campaign portfolios with many more queued runs;
- heavier individual runs with stronger estimator budgets;
- more deliberate separation between broad search, deep specialization, and
  targeted bridge experiments.

The campaign prepared from this document is therefore intended to be both
 broader and heavier than the previous overnight package.

No subagent is planned or required for this implementation.

## Technical Approach

The next campaign should not merely repeat the previous `20`-run package with
 small perturbations. It should explicitly split the search space into three
 coordinated regimes:

- `wide` runs to cover more structured hypotheses per night;
- `heavy` runs to materially increase model/training budget on the best
  `HGBM` directions;
- `bridge` runs to test whether combined low-order plus late-harmonic
  specialization produces a step change rather than another small incremental
  gain.

The campaign will remain inside the current repository-owned harmonic-wise
 pipeline and shared offline evaluator so the resulting winner is directly
 comparable to the current `8.774%` reference. At the same time, the candidate
 matrix will stay anchored to the canonical paper-table gaps tracked in
 `RCIM Paper Reference Benchmark.md`.

The planning priority is:

1. spend most of the runtime budget on `HGBM`, because that family still owns
   the strongest `Track 1` results;
2. retain only a narrow control budget for `RF` and engineered-feature
   branches;
3. allocate significantly more variants to `h0/h1` and to the late
   `162/240` block;
4. include bridge runs that combine those two directions instead of treating
   them as independent forever.

## Involved Components

- `doc/reports/campaign_results/track1/harmonic_wise/forward/2026-04-13-12-37-15_track1_overnight_gap_closure_campaign_results_report.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/running/te_model_live_backlog.md`
- `doc/reports/campaign_plans/track1/harmonic_wise/2026-04-13-13-27-37_track1_extended_overnight_campaign_plan_report.md`
- `doc/technical/2026-04/2026-04-13/README.md`

## Implementation Steps

1. Record this technical preparation document in the day-local technical index.
2. Create a campaign planning report that turns the extended strategy into a
   concrete candidate-run matrix.
3. After user approval, generate the corresponding YAML package under
   `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/campaigns/`.
4. After user approval, generate the dedicated PowerShell launcher and its
   repository documentation note.
5. After user approval, store the prepared campaign state in
   `doc/running/active_training_campaign.yaml`.
6. Provide the exact launch command for the operator-driven overnight run.
