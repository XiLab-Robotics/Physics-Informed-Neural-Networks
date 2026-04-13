# Track 1 Extended Overnight Campaign Plan Report

## Overview

This report prepares the next `Track 1` campaign after the completed overnight
 gap-closure batch showed that the current harmonic-wise validation branch is
 fast enough to support a much larger search package.

The latest completed campaign established:

- completed runs: `20`
- observed launcher failures: `0`
- promoted winner: `track1_hgbm_h01_shallow_regularized`
- current best shared-evaluator test MPE: `8.774%`
- paper offline threshold: `4.7%`

That result confirms two things:

- the branch still improves through `HGBM`, especially around low-order and
  late-harmonic specialization;
- the current campaign/runtime budget is still too light to justify stopping at
  small portfolio sizes.

The next package should therefore be significantly larger and intentionally
 split into:

- `wide` search coverage;
- `heavy` specialization around the strongest branches;
- `bridge` runs that combine the best ideas instead of isolating them forever.

## Objective

The next campaign should answer five concrete questions:

1. can a materially heavier `HGBM` search around `h0/h1` break below the
   current `8.774%` plateau;
2. can stronger late-harmonic specialization around `162/240` close more of
   the paper-table gaps while also helping TE reconstruction;
3. do combined low-order plus late-harmonic bridge runs outperform isolated
   specializations;
4. is there still any narrow control value left in `RF` or engineered-feature
   branches;
5. does the branch still look tuning-limited after a much heavier overnight
   package, or is it time to escalate to a target-parameterization change.

## Current Baseline And Pressure Points

### Shared Evaluator Baseline

- current winner: `track1_hgbm_h01_shallow_regularized`
- current test MPE: `8.774%`
- current validation MPE: `9.611%`
- current oracle test MPE: `2.749%`
- remaining gap to paper threshold: `4.074 percentage points`

### Most Relevant Harmonic Pressure

The current benchmark evidence still points to these concentrations:

- dominant low-order pressure: `0`, `1`, `3`
- bridge/playback pressure: `39`, `40`, `78`, `81`
- late-harmonic pressure: `156`, `162`, `240`

Operational interpretation:

- `h0/h1` are still the best candidate for the main TE-level improvement;
- `162/240` remain the strongest late-harmonic blockers;
- `h3` and `h81` are still useful support targets because they interact with
  both paper-table status and reconstruction quality;
- the next campaign should not spend equal budget on every direction.

## Campaign Design

The proposed overnight package contains `48` runs, organized into `6` blocks.
This is large enough to exploit the current runtime headroom while still being
 structured and inspectable.

### Block A: Wide Low-Order HGBM Search

Purpose:

- expand coverage on the highest-value `h0/h1` direction;
- vary depth, leaf regularization, iteration budget, and targeted support
  harmonics.

<!-- markdownlint-disable MD013 -->
| Config ID | Planned Run Name | Estimator | Features | Main Overrides | Main Question |
| --- | --- | --- | --- | --- | --- |
| `A1` | `track1_hgbm_h01_wide_depth_1` | `HGBM` | base | `h0,h1` moderate depth, longer budget | Does a balanced deeper ladder still beat the current shallow regularized winner? |
| `A2` | `track1_hgbm_h01_wide_depth_2` | `HGBM` | base | `h0,h1` deeper with smaller leaves | Is the remaining gap still underfitting on the dominant low-order pair? |
| `A3` | `track1_hgbm_h01_wide_depth_3` | `HGBM` | base | `h0,h1` deeper with stronger regularization | Does a higher-capacity but guarded configuration generalize better overnight? |
| `A4` | `track1_hgbm_h013_wide_support_1` | `HGBM` | base | `h0,h1,h3` longer and deeper | Does bringing `h3` into the main low-order ladder improve both TE error and phase-table status? |
| `A5` | `track1_hgbm_h013_wide_support_2` | `HGBM` | base | `h0,h1,h3` guarded low learning rate | Is `h3` useful only when trained conservatively? |
| `A6` | `track1_hgbm_h0139_wide_anchor_1` | `HGBM` | base | `h0,h1,h3,h39` | Does anchoring on the paper-critical `h39` reduce reconstruction drift? |
| `A7` | `track1_hgbm_h014078_wide_anchor_1` | `HGBM` | base | `h0,h1,h40,h78` | Does playback-harmonic anchoring outperform the `h39` bridge? |
| `A8` | `track1_hgbm_h0181_wide_anchor_1` | `HGBM` | base | `h0,h1,h81` | Can support on `h81` improve both paper-family direction and TE error? |
| `A9` | `track1_hgbm_h013981_wide_anchor` | `HGBM` | base | `h0,h1,h3,h39,h81` | Does a richer early-harmonic anchor set unlock more stable reconstruction? |
| `A10` | `track1_hgbm_h01_long_budget_regularized` | `HGBM` | base | `h0,h1` longest balanced budget | If we simply lengthen the winner family path, does it still improve materially? |
| `A11` | `track1_hgbm_h01_small_leaf_extreme` | `HGBM` | base | `h0,h1` very small leaves | Is a finer partitioning of the low-order condition space worth the cost? |
| `A12` | `track1_hgbm_h01_high_bin_count` | `HGBM` | base | `h0,h1` finer histogram resolution | Is histogram resolution part of the remaining low-order bias? |
<!-- markdownlint-enable MD013 -->

### Block B: Heavy Low-Order HGBM Runs

Purpose:

- take the best low-order directions and make them materially heavier rather
  than only wider;
- test whether the branch is still budget-limited.

<!-- markdownlint-disable MD013 -->
| Config ID | Planned Run Name | Estimator | Features | Main Overrides | Main Question |
| --- | --- | --- | --- | --- | --- |
| `B1` | `track1_hgbm_h01_heavy_reference` | `HGBM` | base | winner-style `h0,h1` with heavy budget | Does the current winning shape improve further when pushed hard? |
| `B2` | `track1_hgbm_h013_heavy_reference` | `HGBM` | base | heavy `h0,h1,h3` | Is the heavier three-harmonic low-order path superior to the winner-like pair? |
| `B3` | `track1_hgbm_h0139_heavy_reference` | `HGBM` | base | heavy `h0,h1,h3,h39` | Is a heavy bridge to `h39` the best way to stabilize the curve globally? |
| `B4` | `track1_hgbm_h014078_heavy_reference` | `HGBM` | base | heavy `h0,h1,h40,h78` | Does a heavier playback-aligned anchor beat the low-order-only branch? |
| `B5` | `track1_hgbm_h0181_heavy_reference` | `HGBM` | base | heavy `h0,h1,h81` | Does `h81` deserve promotion into the strongest low-order heavy branch? |
| `B6` | `track1_hgbm_h01_ultraheavy_guarded` | `HGBM` | base | extreme but strongly regularized `h0,h1` | Is there still unexplored headroom in a truly heavy low-order run? |
<!-- markdownlint-enable MD013 -->

### Block C: Late-Harmonic Repair Expansion

Purpose:

- spend substantially more budget on the strongest remaining late-harmonic
  blockers from the paper tables;
- test whether the previous repair block was underexplored rather than wrong.

<!-- markdownlint-disable MD013 -->
| Config ID | Planned Run Name | Estimator | Features | Main Overrides | Main Question |
| --- | --- | --- | --- | --- | --- |
| `C1` | `track1_hgbm_h162_h240_wide_repair_1` | `HGBM` | base | deeper `h162,h240` | Does a stronger direct repair beat the last near-winner? |
| `C2` | `track1_hgbm_h162_h240_wide_repair_2` | `HGBM` | base | longer `h162,h240` budget | Is the late block budget-limited rather than structurally limited? |
| `C3` | `track1_hgbm_h081162240_bridge_1` | `HGBM` | base | `h81,h162,h240` | Does bringing `h81` into the late block help both family match and TE error? |
| `C4` | `track1_hgbm_h156162240_bridge_1` | `HGBM` | base | `h156,h162,h240` | Is the late block better treated as a coupled high-order cluster? |
| `C5` | `track1_hgbm_h39162240_bridge_1` | `HGBM` | base | `h39,h162,h240` | Does tying a strong playback harmonic to the late pair improve reconstruction coherence? |
| `C6` | `track1_hgbm_h240_isolation_heavy` | `HGBM` | base | strongest `h240` only | Is `h240` still the single best late-harmonic isolation target? |
| `C7` | `track1_hgbm_h162_isolation_heavy` | `HGBM` | base | strongest `h162` only | Is the late pressure actually dominated by `h162` instead of the pair? |
| `C8` | `track1_hgbm_h81156162240_cluster` | `HGBM` | base | `h81,h156,h162,h240` | Does a richer late cluster outperform the simpler repair sets? |
<!-- markdownlint-enable MD013 -->

### Block D: Low-Order Plus Late Bridge Runs

Purpose:

- test the highest-value combined hypothesis directly;
- avoid another cycle where low-order and late-harmonic ladders improve only in
  isolation.

<!-- markdownlint-disable MD013 -->
| Config ID | Planned Run Name | Estimator | Features | Main Overrides | Main Question |
| --- | --- | --- | --- | --- | --- |
| `D1` | `track1_hgbm_h01_h162240_joint_balanced` | `HGBM` | base | `h0,h1,h162,h240` | Does the simplest joint bridge outperform isolated winners? |
| `D2` | `track1_hgbm_h013_h162240_joint_heavy` | `HGBM` | base | `h0,h1,h3,h162,h240` | Does adding `h3` close both low-order and phase-table pressure at once? |
| `D3` | `track1_hgbm_h0139_h162240_joint_heavy` | `HGBM` | base | `h0,h1,h3,h39,h162,h240` | Is this the strongest global bridge candidate for Target A? |
| `D4` | `track1_hgbm_h014078_h162240_joint` | `HGBM` | base | `h0,h1,h40,h78,h162,h240` | Does a playback-aligned joint bridge help more than the `h39` route? |
| `D5` | `track1_hgbm_h0181_h162240_joint` | `HGBM` | base | `h0,h1,h81,h162,h240` | Can `h81` act as a useful bridge between early and late pressure? |
| `D6` | `track1_hgbm_h013981_h162240_joint` | `HGBM` | base | `h0,h1,h3,h39,h81,h162,h240` | Does a broad but still selective bridge produce the first real step change? |
| `D7` | `track1_hgbm_h01_h156162240_joint` | `HGBM` | base | `h0,h1,h156,h162,h240` | Is the stronger late cluster the better partner for the low-order winner path? |
| `D8` | `track1_hgbm_h013_h081162240_joint` | `HGBM` | base | `h0,h1,h3,h81,h162,h240` | Can a slightly leaner bridge beat the broader variants by reducing interference? |
<!-- markdownlint-enable MD013 -->

### Block E: Engineered-Term Recheck Under Heavy Structure

Purpose:

- keep a narrow but fair control branch for engineered terms;
- test them only in the structures that still have a plausible rationale.

<!-- markdownlint-disable MD013 -->
| Config ID | Planned Run Name | Estimator | Features | Main Overrides | Main Question |
| --- | --- | --- | --- | --- | --- |
| `E1` | `track1_hgbm_h01_engineered_heavy` | `HGBM` | engineered | `h0,h1` heavy | Do engineered terms help only when the low-order branch is given enough budget? |
| `E2` | `track1_hgbm_h013_engineered_heavy` | `HGBM` | engineered | `h0,h1,h3` heavy | Can engineered terms now help the early phase-heavy block? |
| `E3` | `track1_hgbm_h162240_engineered_heavy` | `HGBM` | engineered | `h162,h240` heavy | Are late-harmonic misses conditioning-sensitive under a larger budget? |
| `E4` | `track1_hgbm_h013_h162240_engineered_joint` | `HGBM` | engineered | `h0,h1,h3,h162,h240` | Do engineered terms become useful only in the joint bridge regime? |
| `E5` | `track1_hgbm_h0139_h162240_engineered_joint` | `HGBM` | engineered | `h0,h1,h3,h39,h162,h240` | Can engineered terms help the strongest paper-aware bridge candidate? |
| `E6` | `track1_rf_h01_h81_engineered_control` | `RF` | engineered | `h0,h1,h81` | Is there any remaining niche where engineered RF control is still informative? |
<!-- markdownlint-enable MD013 -->

### Block F: Narrow RF Controls

Purpose:

- retain a minimal family-level sanity check without wasting most of the
  campaign budget on a weak direction.

<!-- markdownlint-disable MD013 -->
| Config ID | Planned Run Name | Estimator | Features | Main Overrides | Main Question |
| --- | --- | --- | --- | --- | --- |
| `F1` | `track1_rf_h01_heavy_control` | `RF` | base | `h0,h1` heavier forest | Does RF still fail even on the main low-order opportunity? |
| `F2` | `track1_rf_h81_heavy_control` | `RF` | base | `h81` heavy | Can RF recover the paper tendency around `h81` under a stronger budget? |
| `F3` | `track1_rf_h162240_heavy_control` | `RF` | base | `h162,h240` heavy | Is late-harmonic phase pressure somehow more RF-friendly than low-order pressure? |
| `F4` | `track1_rf_h013_h162240_joint_control` | `RF` | base | `h0,h1,h3,h162,h240` | Does RF only become viable in a joint bridge structure? |
| `F5` | `track1_rf_full_rcim_heavy_control` | `RF` | base | full-set heavier forest | Does a stronger full-RCIM RF remain clearly non-competitive? |
| `F6` | `track1_rf_h013981_bridge_control` | `RF` | base | `h0,h1,h3,h39,h81` | Is there any bridge subset where RF is still worth future attention? |
| `F7` | `track1_rf_h01_h81_bridge_control` | `RF` | base | `h0,h1,h81` | Does a narrower early-harmonic bridge give RF a more realistic paper-aligned niche? |
| `F8` | `track1_rf_h039_h162240_bridge_control` | `RF` | base | `h39,h162,h240` | Can RF leverage one stable playback anchor plus the late pair better than broader control sets? |
<!-- markdownlint-enable MD013 -->

## Recommended Execution Order

If the full overnight window is available, launch the blocks in this order:

1. Block `A`
2. Block `B`
3. Block `D`
4. Block `C`
5. Block `E`
6. Block `F`

Reason:

- `A` and `B` cover the two strongest independent directions already validated
  by the last campaign;
- `D` is the most important structural escalation because it directly tests the
  combined-hypothesis branch;
- `C` remains useful but is partially dominated by the stronger bridge runs;
- `E` and `F` are narrower controls and should not consume the earliest budget.

If a reduced overnight package is required, use this `18`-run subset:

1. `A2`
2. `A4`
3. `A9`
4. `A10`
5. `B1`
6. `B3`
7. `B8`
8. `D1`
9. `D2`
10. `D3`
11. `D5`
12. `D6`
13. `D8`
14. `E1`
15. `E4`
16. `F1`
17. `F2`
18. `F5`

## Evaluation Rules

### Primary Promotion Gate

Use the same explicit winner policy as the latest campaign:

- primary metric: `test_mean_percentage_error_pct`
- first tie breaker: `test_curve_mae_deg`
- second tie breaker: `test_curve_rmse_deg`
- third tie breaker: lexical `run_name`
- direction: minimize

### Secondary Decision Gate

Every run must also be interpreted against:

- paper-table progress on the still-open harmonics;
- whether the improvement came from low-order treatment, late repair, or a
  joint bridge;
- whether any engineered or `RF` branch still deserves future runtime budget.

This preserves `Target A` as the main gate while keeping the campaign aligned
with the canonical paper replication objective.

## Success Criteria

The extended campaign is successful if it achieves at least one of these:

1. produces a new promoted shared-evaluator winner below `8.6%`;
2. produces a clearly superior joint bridge winner over both isolated
   low-order and isolated late-harmonic paths;
3. closes additional canonical paper-table gaps on the high-priority harmonics
   `0`, `1`, `3`, `81`, `162`, `240`;
4. proves that the current harmonic-wise branch is no longer runtime-limited,
   which would justify escalating to a target-parameterization change instead
   of only running more light tuning campaigns.

## Expected Outputs After Approval

After approval of this planning report and the companion technical document,
the repository should generate:

1. a dedicated extended campaign YAML package under
   `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/campaigns/`;
2. a dedicated PowerShell launcher under `scripts/campaigns/`;
3. the matching launcher note under `doc/scripts/campaigns/`;
4. a prepared record in `doc/running/active_training_campaign.yaml`;
5. the exact terminal command for the next overnight launch.

## Next Step

If this report is approved together with the companion technical document,
prepare the extended `Track 1` overnight campaign package from this `48`-run
matrix and do not fall back to another small ad hoc batch.
