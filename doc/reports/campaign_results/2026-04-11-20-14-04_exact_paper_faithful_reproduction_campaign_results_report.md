# Exact Paper Faithful Reproduction Campaign Results Report

## Overview

This report closes the first coordinated `Track 1` paper-faithful reproduction campaign prepared in:

- `doc/reports/campaign_plans/2026-04-10-21-47-55_exact_paper_faithful_reproduction_campaign_plan_report.md`

The package executed `4` repository-owned validation runs through the dedicated paper-faithful launcher:

- completed runs: `4`
- failed runs: `0`
- execution window: `2026-04-10T22:49:06.1087937+02:00` to `2026-04-11T20:08:29.5330140+02:00`
- campaign artifact root:
  `output/training_campaigns/exact_paper_faithful_reproduction_campaign_2026_04_10_21_47_55/`

Unlike a single-runner paper benchmark, this package used a coordinated structure:

- `2` exact-paper family-bank support runs for recovered-training fidelity and ONNX surface validation;
- `2` harmonic-wise shared-evaluator runs for the TE-level offline benchmark tied to `Target A`.

## Objective And Outcome

The campaign had four concrete questions:

1. can the recovered exact-paper family-bank branch still run stably under the current stack?
2. can the amplitude/phase exact-paper handoff be serialized cleanly even when ONNX export is disabled?
3. can dominant-harmonic specialization improve the shared offline evaluator tied to `Target A`?
4. under one comparable offline evaluator, does the exact-paper-faithful direction beat the current repository baseline?

Outcome:

- both exact-paper support runs completed successfully and the recovered strict-support run exported `200` ONNX files with `0` failures;
- the harmonic-wise branch is now stable under the current Windows stack after threadpool hardening for `HistGradientBoostingRegressor`;
- the specialized exact-paper dominant-harmonic run completed, but did not beat the current shared-evaluator baseline;
- the canonical campaign winner is the shared-evaluator reference run `track1_current_best_shared_evaluator_reference`;
- `Target A` remains `not_yet_met` because the best test mean percentage error is `8.877%` versus the paper threshold `4.7%`.

## Ranking Policy

This campaign contains two metric domains, so the ranking policy uses an explicit eligibility gate.

- eligible winner set: runs that emit the shared offline evaluator tied to `Target A`;
- primary metric: `test_mean_percentage_error_pct`;
- first tie breaker: `test_curve_mae_deg`;
- second tie breaker: `test_curve_rmse_deg`;
- third tie breaker: lexical `run_name`;
- support-track note: exact-paper family-bank runs are serialized in the leaderboard, but they are not winner-eligible because they do not emit the TE-level shared evaluator metric.

## Comparable Offline Ranking

| Rank | Config | Target A | Test MPE [%] | Curve MAE [deg] | Curve RMSE [deg] |
| --- | --- | --- | ---: | ---: | ---: |
| `1` | `track1_current_best_shared_evaluator_reference` | `not_yet_met` | 8.877 | 0.002613 | 0.002812 |
| `2` | `exact_paper_dominant_harmonic_specialized` | `not_yet_met` | 9.123 | 0.002690 | 0.002885 |

| Config | Oracle MPE [%] | Robot TE RMS [deg] | Cycloidal TE RMS [deg] |
| --- | ---: | ---: | ---: |
| `track1_current_best_shared_evaluator_reference` | 2.749 | 0.041350 | 0.032767 |
| `exact_paper_dominant_harmonic_specialized` | 2.749 | 0.041317 | 0.032944 |

## Exact-Paper Support Runs

| Rank | Config | ONNX Export | Winner | Mean Component MAPE [%] | Mean Component MAE |
| --- | --- | --- | --- | ---: | ---: |
| `1` | `exact_paper_recovered_reference` | `yes` | `RF` | 18.369 | 0.056284 |
| `2` | `exact_paper_amplitude_phase_reference` | `no` | `RF` | 18.369 | 0.056284 |

| Config | Mean Component RMSE | ONNX Exported | Failed Exports |
| --- | ---: | ---: | ---: |
| `exact_paper_recovered_reference` | 0.144839 | 200 | 0 |
| `exact_paper_amplitude_phase_reference` | 0.144839 | 0 | 0 |

## Campaign Winner

The explicit campaign winner is:

- `track1_current_best_shared_evaluator_reference`

Its result was:

- test mean percentage error: `8.877%`
- test curve MAE: `0.002613 deg`
- test curve RMSE: `0.002812 deg`
- oracle test mean percentage error: `2.749%`
- Target A threshold: `4.7%`
- Target A status: `not_yet_met`

This run won because it is the lowest-error candidate inside the only metric domain that is directly comparable to the paper-facing offline benchmark used by this campaign.

## Interpretation By Experiment Block

### 1. The Exact-Paper Support Surface Is Now Operational

The exact-paper branch completed in both prepared forms during this campaign:

- `exact_paper_recovered_reference` kept the recovered family bank stable and exported `200` ONNX files with `0` failures;
- `exact_paper_amplitude_phase_reference` completed cleanly with export disabled, which now exercises the same report path without schema regressions.

Interpretation:

- the exact-paper branch is no longer blocked by the prior `HGBM` export issue or by the disabled-export report-builder bug;
- these runs now act as reusable support evidence for paper-faithful parameterization and deployment-facing artifact preparation.

### 2. The Shared Evaluator Still Favors The Current Repository Baseline

The comparable harmonic-wise ranking stayed in the same order as the pre-campaign repository state:

- `track1_current_best_shared_evaluator_reference`: `8.877%`
- `exact_paper_dominant_harmonic_specialized`: `9.123%`

Interpretation:

- the exact-paper-inspired specialization remains viable, but it did not beat the current best shared-evaluator reference;
- the gap is small enough to remain interesting, but the campaign does not justify promoting the specialized branch over the current baseline.

### 3. `Target A` Is Still Open

The campaign moved the exact-paper reproduction branch from fragile to runnable, but it did not close the paper threshold:

- best achieved test mean percentage error: `8.877%`
- paper threshold: `4.7%`
- verdict: `not_yet_met`

Interpretation:

- this campaign improves reproducibility and comparability more than raw offline accuracy;
- the next `Track 1` improvement cycle should focus on reducing TE-level curve error, not on more family-bank stabilization work.

### 4. Playback Remains Repository-Owned And Comparable

The winner keeps the playback path alive for both canonical offline styles:

- robot mean reconstructed TE RMS: `0.041350 deg`
- cycloidal mean reconstructed TE RMS: `0.032767 deg`

Interpretation:

- the campaign keeps the repository aligned with the paper-facing offline evaluation shape;
- however, these playback summaries still sit inside an offline-only comparison scope and do not yet constitute the paper online benchmark.

## Recommended Next Step

The correct next step is not another exact-paper export campaign. It is a new `Track 1` offline-improvement iteration that starts from the shared-evaluator winner and attacks the remaining TE-level error directly, while reusing the now-stable exact-paper support surface as evidence and artifact infrastructure.
