# Track 1 Overnight Gap-Closure Campaign Preparation

## Overview

This technical document defines the next `Track 1` preparation step after the
canonical `paper vs repository` replication of paper Tables `3`, `4`, `5`, and
`6`.

The repository now has an inspectable gap surface for:

- amplitude `RMSE` targets from Table `3`;
- phase `MAE` targets from Table `4`;
- phase `RMSE` targets from Table `5`;
- model-family selections from Table `6`.

The next practical step is not another broad status update. It is a
campaign-heavy overnight plan that targets the still-open harmonics and the
still-open TE-level offline benchmark tied to `Target A`.

The preparation must stay honest about the current software surface:

- the harmonic-wise `Track 1` evaluator is the only branch that emits the
  TE-level offline metric used for `Target A`;
- the current harmonic-wise pipeline supports `hist_gradient_boosting` and
  `random_forest` estimator families;
- exact-paper family-bank validation already covers the broader paper model
  inventory, but it is not the branch that closes `Target A`.

## Technical Approach

The overnight strategy should use a portfolio of narrow campaigns rather than
one monolithic sweep.

The campaigns should be grouped by failure mode:

1. `h0 / h1` recovery:
   - attack the largest low-order bias that still dominates TE reconstruction;
   - vary depth, iteration count, and leaf size mainly on harmonics `0` and
     `1`.
2. late-harmonic repair:
   - target the still-open paper-table gaps at `162` and `240`;
   - keep the full RCIM harmonic set while only specializing the problematic
     late harmonics.
3. family-swap diagnostics:
   - compare `hist_gradient_boosting` against `random_forest` under the shared
     offline evaluator;
   - determine whether the remaining TE-level error is mainly a model-family
     problem or a target-parameterization problem.
4. engineered-feature re-check:
   - re-test the engineered operating-condition terms only in combinations that
     preserve the current best harmonic-wise baseline as the anchor;
   - avoid another broad feature sweep detached from the paper-table gaps.

This document intentionally limits the immediate overnight plan to the current
launchable harmonic-wise surface. A future follow-up may add new target
parameterizations such as direct `amplitude / phase` training inside the shared
offline evaluator, but that requires implementation work first and should not
be mixed into the launch-ready overnight package.

No Codex subagent is planned for this preparation. The work stays local to the
current repository context.

## Involved Components

- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/validation_checks/track1/exact_paper/forward/shared/2026-04-12-17-00-28_paper_reimplementation_rcim_exact_model_bank_rcim_exact_paper_model_bank_exact_paper_validation_tables_3_4_5_6_exact_paper_model_bank_report.md`
- `doc/reports/campaign_results/track1/exact_paper/forward/2026-04-11-20-14-04_exact_paper_faithful_reproduction_campaign_results_report.md`
- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/`
- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`
- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_support.py`
- `doc/reports/campaign_plans/track1/harmonic_wise/2026-04-13-00-55-21_track1_overnight_gap_closure_campaign_plan_report.md`

## Implementation Steps

1. Freeze the gap priorities from the canonical Tables `3-6` comparison and
   map them to launchable harmonic-wise configuration families.
2. Prepare a campaign-planning report with a large but bounded overnight run
   matrix grouped by purpose instead of by ad hoc trial order.
3. After user approval, generate the campaign YAML package, the dedicated
   PowerShell launcher, the launcher note, and the campaign state entry in
   `doc/running/active_training_campaign.yaml`.
4. Launch the overnight batch and keep the shared offline evaluator as the
   winner gate for `Target A`.
5. After execution, produce the campaign-results report and update the
   canonical benchmark reports before any closure claim on `Track 1`.
