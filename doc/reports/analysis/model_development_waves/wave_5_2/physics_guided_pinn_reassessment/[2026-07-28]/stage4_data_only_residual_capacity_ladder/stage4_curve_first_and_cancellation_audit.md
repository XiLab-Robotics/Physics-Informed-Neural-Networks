# Stage 4 Curve-First And Cancellation Audit

## Overview

This audit applies the predeclared Stage 4 first-screen and opaque-
cancellation gates to the eighteen-run data-only campaign.

The primary surface contains `96` causal `supported_core` forward test
conditions. One sparse/corner condition remains visible outside the
promotion calculation. All decomposition checks span all `966` eligible
forward conditions.

## Frozen R0 Control

- supported-core raw MAE: `0.001824548 deg`;
- supported-core centered-shape MAE: `0.001394187 deg`;
- supported-core absolute offset error: `0.000981458 deg`;
- supported-core P95 curve MAE: `0.003970491 deg`.

## Primary Hybrid Decisions

| Hybrid | Control | MAE [deg] | R0 [deg] | Control [deg] | Residual/anchor RMS | Pass |
| --- | --- | --- | --- | --- | --- | --- |
| stage4_h01_r2_compact | stage4_c01_r1_compact | 0.060060 | 0.001825 | 0.001990 | 1.3883 | no |
| stage4_h02_r2_deep | stage4_c02_r1_deep | 0.059691 | 0.001825 | 0.002118 | 1.3812 | no |
| stage4_h03_r3_compact | stage4_c01_r1_compact | 0.014912 | 0.001825 | 0.001990 | 0.2687 | no |
| stage4_h04_r3_deep | stage4_c02_r1_deep | 0.015179 | 0.001825 | 0.002118 | 0.2707 | no |
| stage4_h05_r4_compact | stage4_c03_r1_compact | 0.060221 | 0.001825 | 0.001984 | 1.3885 | no |
| stage4_h06_r4_deep | stage4_c04_r1_deep | 0.060441 | 0.001825 | 0.001982 | 1.3929 | no |
| stage4_h07_r5_compact | stage4_c05_r1_compact | 0.059974 | 0.001825 | 0.001990 | 1.3871 | no |
| stage4_h08_r5_deep | stage4_c06_r1_deep | 0.060538 | 0.001825 | 0.001991 | 1.3955 | no |

## Decomposition

| Candidate | Formulation | Finite | Population RMS ratio | Max curve ratio | Max residual [deg] | Bound violations |
| --- | --- | --- | --- | --- | --- | --- |
| stage4_h01_r2_compact | R2 | 966/966 | 1.3883 | 1.6233 | 0.149070 | 0 |
| stage4_h02_r2_deep | R2 | 966/966 | 1.3812 | 1.6357 | 0.150376 | 0 |
| stage4_h03_r3_compact | R3 | 966/966 | 0.2687 | 0.5395 | 0.016872 | 0 |
| stage4_h04_r3_deep | R3 | 966/966 | 0.2707 | 0.5618 | 0.016859 | 0 |
| stage4_h05_r4_compact | R4 | 966/966 | 1.3885 | 1.6292 | 0.146525 | 0 |
| stage4_h06_r4_deep | R4 | 966/966 | 1.3929 | 1.6442 | 0.145899 | 0 |
| stage4_h07_r5_compact | R5 | 966/966 | 1.3871 | 1.6323 | 0.153954 | 0 |
| stage4_h08_r5_deep | R5 | 966/966 | 1.3955 | 1.6495 | 0.155966 | 0 |
| stage4_a01_r2_compact | R2 | 966/966 | 1.3828 | 1.6001 | 0.147786 | 0 |
| stage4_a02_r2_compact | R2 | 966/966 | 1.2802 | 1.4486 | 0.128398 | 0 |
| stage4_a03_r5_compact | R5 | 966/966 | 0.2525 | 0.3862 | 0.032551 | 0 |
| stage4_a04_r5_compact | R5 | 966/966 | 0.2942 | 0.3977 | 0.028862 | 0 |

## Exit Decision

No primary hybrid passes every first-screen gate.

Stage 4 therefore closes as a valid negative result with no residual architecture promoted and no stability-repeat campaign required.

The heavy official TE Curve Verification Pipeline was not run.
This is a bounded Stage 4 campaign-closeout diagnostic only.
