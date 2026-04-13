# Track 1 Overnight Gap-Closure Campaign Plan Report

## Overview

This report prepares the next `Track 1` overnight campaign package after the
canonical table-replication milestone.

The goal is no longer generic offline improvement. The goal is to close the
remaining gaps against paper Tables `3`, `4`, `5`, and `6` while still
improving the TE-level shared offline evaluator used for `Target A`.

The current baseline to beat remains:

- run: `track1_current_best_shared_evaluator_reference`;
- test mean percentage error: `8.877%`;
- paper offline threshold: `4.7%`.

The current exact-paper table status is:

- Table `3` amplitude `RMSE`: `6/10` harmonics already meet or beat the paper;
- Table `4` phase `MAE`: `5/9` harmonics already meet or beat the paper;
- Table `5` phase `RMSE`: `4/9` harmonics already meet or beat the paper;
- Table `6` target-level family match: `7/20`.

The highest-priority open harmonics remain:

- `0`
- `1`
- `3`
- `81`
- `162`
- `240`

## Campaign Intent

This overnight package should answer four concrete questions:

1. can the current harmonic-wise baseline be improved by specializing the
   dominant low-order terms `h0` and `h1`;
2. can the remaining late-harmonic paper gaps be reduced without dropping the
   full RCIM set;
3. does `random_forest` become competitive when the configuration is focused on
   the open harmonics instead of treated as a one-off diagnostic;
4. do the engineered operating-condition terms help only when combined with
   narrow harmonic overrides rather than as a broad all-target change.

## Current Gap Snapshot

### TE-Level Gap

- best shared-evaluator test MPE: `8.877%`
- paper threshold: `4.7%`
- remaining absolute gap: `4.177 percentage points`

### Harmonic Paper-Table Gap

Highest-priority unresolved targets from the canonical Tables `3-6` report:

- amplitude `RMSE`: `k=0`, `1`, `3`, `81`, `240`
- phase `MAE`: `k=1`, `3`, `162`, `240`
- phase `RMSE`: `k=1`, `3`, `39`, `162`, `240`
- family mismatch pressure: strongest at `k=0`, `1`, `3`, `40`, `81`, `156`

Interpretation:

- `k=0` and `k=1` remain the main candidates for TE-level error reduction;
- `k=162` and `k=240` are the main late-harmonic blockers for full table
  replication;
- `k=3` still matters because it is open in both phase tables and sits early in
  the harmonic stack;
- `k=81` matters because Table `6` still wants `RF` while the current exact
  branch does not fully stabilize that selection.

## Overnight Campaign Portfolio

The launch-ready portfolio is organized into `4` campaigns and `20` candidate
runs. All runs stay inside the currently implemented harmonic-wise pipeline and
therefore can be turned into YAML plus launcher artifacts without new model
code first.

### Campaign A: Low-Order HGBM Ladder

Purpose:

- attack the dominant `h0 / h1` residuals directly;
- keep the current baseline family and evaluator.

<!-- markdownlint-disable MD013 -->
| Config ID | Planned Run Name | Estimator | Features | Main Overrides | Main Question |
| --- | --- | --- | --- | --- | --- |
| `A1` | `track1_hgbm_h01_deeper_low_order` | `HGBM` | base | `h0,h1` deeper, more iterations, smaller leaves | Does more low-order capacity reduce TE error without destabilizing the rest? |
| `A2` | `track1_hgbm_h013_deeper_low_order` | `HGBM` | base | `h0,h1,h3` deeper and longer | Does extending the same treatment to `h3` close the phase-table gaps? |
| `A3` | `track1_hgbm_h01_ultradeep_guarded` | `HGBM` | base | `h0,h1` very deep but guarded by low learning rate | Is the remaining bias mostly underfitting on the first harmonics? |
| `A4` | `track1_hgbm_h01_shallow_regularized` | `HGBM` | base | `h0,h1` longer but less deep | Is the current gap actually variance-sensitive rather than capacity-limited? |
| `A5` | `track1_hgbm_h0139_low_order_anchor` | `HGBM` | base | `h0,h1,h3,h39` targeted anchor | Does adding the paper-critical `h39` improve reconstruction coherence? |
| `A6` | `track1_hgbm_h014078_low_order_anchor` | `HGBM` | base | `h0,h1,h40,h78` targeted anchor | Does stabilizing the paper playback harmonics help more than only deepening `h0 / h1`? |
<!-- markdownlint-enable MD013 -->

### Campaign B: Late-Harmonic Repair Ladder

Purpose:

- attack the still-open exact-paper targets at `162` and `240`;
- test whether late-harmonic specialization can improve both table replication
  and TE-level reconstruction.

<!-- markdownlint-disable MD013 -->
| Config ID | Planned Run Name | Estimator | Features | Main Overrides | Main Question |
| --- | --- | --- | --- | --- | --- |
| `B1` | `track1_hgbm_h162_h240_repair` | `HGBM` | base | `h162,h240` deeper and longer | Can we close the worst late-harmonic paper gaps directly? |
| `B2` | `track1_hgbm_h081_h162_h240_repair` | `HGBM` | base | `h81,h162,h240` | Does bringing `h81` into the repair set improve family alignment and TE error together? |
| `B3` | `track1_hgbm_h156_h162_h240_repair` | `HGBM` | base | `h156,h162,h240` | Is the late block better treated as a coupled high-order cluster? |
| `B4` | `track1_hgbm_h039_h162_h240_bridge` | `HGBM` | base | `h39,h162,h240` | Does tying one strong paper-matched harmonic to the late pair stabilize prediction? |
| `B5` | `track1_hgbm_h013_h162_h240_joint` | `HGBM` | base | `h0,h1,h3,h162,h240` | Does joint low-order plus late-harmonic specialization outperform isolated repair? |
| `B6` | `track1_hgbm_h240_extreme_focus` | `HGBM` | base | `h240` strongest specialization only | Is `h240` the single late harmonic most worth isolating? |
<!-- markdownlint-enable MD013 -->

### Campaign C: Random-Forest Counterfactuals

Purpose:

- measure whether the remaining gap is estimator-family specific;
- probe the paper tendency toward `RF` on selected harmonics without rewriting
  the pipeline.

<!-- markdownlint-disable MD013 -->
| Config ID | Planned Run Name | Estimator | Features | Main Overrides | Main Question |
| --- | --- | --- | --- | --- | --- |
| `C1` | `track1_rf_full_rcim_reference` | `RF` | base | full-set balanced forest | Does a tuned full-RCIM RF get closer to Table `6` while staying viable on TE error? |
| `C2` | `track1_rf_h01_focus` | `RF` | base | `h0,h1` more trees and deeper split allowance | Is RF better suited than HGBM for the early harmonics? |
| `C3` | `track1_rf_h081_focus` | `RF` | base | `h81` stronger capacity | Can RF recover the paper preference around `k=81`? |
| `C4` | `track1_rf_h156_h162_h240_focus` | `RF` | base | late-harmonic focus | Does RF help on the phase-heavy late block where HGBM still misses? |
<!-- markdownlint-enable MD013 -->

### Campaign D: Engineered-Term Recovery

Purpose:

- re-evaluate engineered terms only where they have a plausible interaction
  with the open gaps;
- avoid repeating the previous broad engineered-feature disappointment.

<!-- markdownlint-disable MD013 -->
| Config ID | Planned Run Name | Estimator | Features | Main Overrides | Main Question |
| --- | --- | --- | --- | --- | --- |
| `D1` | `track1_hgbm_h01_engineered_recheck` | `HGBM` | full engineered set | `h0,h1` | Do engineered operating terms help specifically on the dominant low-order terms? |
| `D2` | `track1_hgbm_h013_engineered_recheck` | `HGBM` | full engineered set | `h0,h1,h3` | Can engineered terms reduce the still-open phase gaps at `1` and `3`? |
| `D3` | `track1_hgbm_h162_h240_engineered_recheck` | `HGBM` | full engineered set | `h162,h240` | Are the late-harmonic misses conditioning-sensitive rather than estimator-limited? |
| `D4` | `track1_rf_h01_h081_engineered_recheck` | `RF` | full engineered set | `h0,h1,h81` | Does RF benefit from engineered terms more than HGBM on the open paper-selected harmonics? |
<!-- markdownlint-enable MD013 -->

## Recommended Overnight Order

If only one batch can be launched overnight, use this priority:

1. Campaign `A`
2. Campaign `B`
3. Campaign `C`
4. Campaign `D`

Reason:

- Campaign `A` is the highest-probability path to reducing the shared offline
  error tied to `Target A`;
- Campaign `B` is the highest-probability path to closing the remaining
  canonical paper-table gaps at `162` and `240`;
- Campaign `C` tests the strongest family-level counterfactual still supported
  by the current code;
- Campaign `D` is useful, but should not displace the more direct structural
  tests unless runtime budget is abundant.

If the night budget is shorter, use this reduced package:

1. `A1`
2. `A2`
3. `A5`
4. `B1`
5. `B2`
6. `C2`
7. `C3`
8. `D1`

## Evaluation Rules

Every run in the overnight package should be scored on two levels.

### Primary Winner Gate

- shared offline evaluator `test_mean_percentage_error_pct`
- tie breakers:
  - `test_curve_mae_deg`
  - `test_curve_rmse_deg`
  - lexical `run_name`

### Secondary Diagnostic Gate

- change in canonical table status for Tables `3`, `4`, `5`, and `6`
- improvement on harmonics `0`, `1`, `3`, `81`, `162`, `240`
- change in robot and cycloidal playback summaries

This keeps `Target A` as the main gate while preventing a run from looking good
only because it shifts error away from the paper-critical harmonics.

## Success Criteria

The overnight package is successful if it produces at least one of these
outcomes:

1. a new shared-evaluator winner that improves materially over `8.877%`;
2. a run that closes at least two additional open harmonic targets in the
   canonical Tables `3-5`;
3. a clearer family-selection pattern for the open Table `6` harmonics;
4. a narrower next-step decision about whether `Track 1` now needs:
   - more harmonic-wise tuning inside the current coefficient-based pipeline; or
   - a new implementation step for direct `amplitude / phase` training under
     the shared evaluator.

## Expected Implementation Outputs

After approval of this planning report, the repository should generate:

1. a dedicated campaign YAML package under
   `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/campaigns/`;
2. a dedicated PowerShell launcher under `scripts/campaigns/`;
3. the matching launcher note under `doc/scripts/campaigns/`;
4. a prepared campaign-state record in
   `doc/running/active_training_campaign.yaml`;
5. the exact terminal command for the overnight launch.

## Next Step

If this report is approved together with the technical document, prepare the
overnight `Track 1` campaign package from this matrix instead of starting a new
ad hoc tuning round.
