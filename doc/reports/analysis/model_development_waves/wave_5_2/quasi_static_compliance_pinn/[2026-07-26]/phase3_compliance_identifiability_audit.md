# Phase 3 Compliance Identifiability Audit

## Executive Decision

- Entry gate: `pass`.
- Eligible directional curves: `1932`.
- Training targets were used only by training-split analytical probes.
- Validation and test curve means were evaluation-only.
- Ordered load-unload, reversal, hysteresis, and friction state remain unavailable and are excluded from Phase 3.

## Physical Scope

Phase 3 tests the bounded algebraic relation:

```text
elastic_TE = signed_torque / positive_effective_stiffness
```

Temperature-conditioned, nonlinear, hard-decomposition, and shared-
stiffness variants remain isolated ablations. No Phase 2 nonzero physics
weight is inherited.

## Directional Support

| Direction | Train / Val / Test | Signed Torque Range (Nm) | Temperature Range (C) | Train Low-Torque Curves | Torque-Temperature Correlation | Torque-Mean Correlation |
| --- | --- | --- | --- | ---: | ---: | ---: |
| `Fw` | 675 / 194 / 97 | -1800.610 to 0.114 | 24.259 to 37.642 | 34 | -0.022466 | 0.987341 |
| `Bw` | 675 / 194 / 97 | -0.290 to 1800.515 | 24.135 to 37.655 | 34 | 0.030924 | 0.987169 |

## Training-Only Analytical Probe Results

| Formulation | Surface | Test Mean MAE (deg) | Test Mean RMSE (deg) | Compliance (deg/Nm) | Stiffness (Nm/deg) | Positive / Monotonic |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| `C2` | `Bw` | 0.001531362 | 0.001939662 | 3.636675355e-05 | 27497.643 | `True` / `True` |
| `C1` | `Bw` | 0.001690064 | 0.002173314 | 3.667699346e-05 | 27265.048 | `True` / `True` |
| `C3` | `Bw` | 0.001692084 | 0.002175650 | 3.675738307e-05 | 27205.419 | `True` / `True` |
| `C0` | `Bw` | 0.017222085 | 0.020082212 | 0.000000000e+00 | 0.000 | `False` / `False` |
| `C3` | `Fw` | 0.001579591 | 0.002165037 | 3.566810757e-05 | 28036.251 | `True` / `True` |
| `C1` | `Fw` | 0.001630699 | 0.002260375 | 3.670516687e-05 | 27244.121 | `True` / `True` |
| `C2` | `Fw` | 0.001685282 | 0.002290676 | 3.665675995e-05 | 27280.098 | `True` / `True` |
| `C0` | `Fw` | 0.016815749 | 0.019729523 | 0.000000000e+00 | 0.000 | `False` / `False` |
| `C5` | `global` | 0.001659680 | 0.002216634 | 3.669108019e-05 | 27254.581 | `True` / `True` |

## Identifiability

| Formulation | Full Rank | Condition Number Pass | Unconstrained Physical Sign Pass |
| --- | --- | --- | --- |
| `c1_linear` | `True` | `True` | `True` |
| `c2_temperature` | `True` | `True` | `True` |
| `c3_nonlinear` | `True` | `True` | `True` |
| `c5_shared` | `True` | `True` | `True` |

A full-rank design only authorizes a bounded campaign test. It does
not establish a causal stiffness law. Any unconstrained negative
slope is evidence that positive stiffness must be enforced by
construction and judged on held-out transfer rather than fitted
training error.

## Entry Gate

- `paired_direction_contract`: `True`.
- `zero_torque_support`: `True`.
- `direction_torque_sign_contract`: `True`.
- `c1_full_rank`: `True`.
- `c2_full_rank`: `True`.
- `c3_full_rank`: `True`.
- `c5_full_rank`: `True`.
- `c1_condition_number`: `True`.
- `c2_condition_number`: `True`.
- `c3_condition_number`: `True`.
- `c5_condition_number`: `True`.

## Decision Boundary

The audit authorizes only `C0` through `C5`. It does not authorize
hysteresis, friction state, load-unload memory, contact state, wear,
or MMT parameter estimation. Phase 3 training may start only after
the deterministic equation tests and every queue-item preflight pass.
