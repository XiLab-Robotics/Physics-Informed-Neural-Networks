# Wave 5.2R Stage 14 Cross-Formulation Forward Tournament

## Executive Decision

Stage 14 audited eleven formulation groups against all six tournament entry
requirements. H04, the bounded PF-A core-coefficient correction from Stage 5,
is the only eligible entrant.

H04 is nominated for Stage 15 official forward verification, not accepted or
promoted. The accepted periodic GRU `Fw` remains the incumbent. Registries are
unchanged.

## Tournament Contract

- Dataset: `polished_dataset`
- Input mode: setpoints
- Surface: `Fw`
- Split signature:
  `c1aa8718fb9bf88cc2021c121dc4f3b4010fc1d2e45ac90af5f4376aa64f8e16`
- Audited formulation groups: `11`
- Eligible entrants: `1`
- Frozen references: PF-A, accepted harmonic MLP `Fw`, accepted GRU `Fw`
- Training executed: none
- Official acceptance authorized: no

An entrant must pass every requirement:

1. isolated gate;
2. three-seed evaluation;
3. matched-control improvement;
4. leakage and causality checks;
5. complete full-curve payload;
6. inspectable inference path.

Missing evidence is a failed requirement. Synthetic certification cannot
substitute for real-data qualification.

## Entry Eligibility

| Formulation | Isolated gate | Three seeds | Matched control | Eligible |
| --- | --- | --- | --- | --- |
| Stage 4 hybrids | fail | no | fail | no |
| Stage 5 H04 | pass | yes | pass | **yes** |
| Stage 5 H08 | fail | no | raw only | no |
| Stage 6 spectral/Sobolev | fail | no | fail | no |
| Stage 7 mean/shape heads | fail | no | fail | no |
| Stage 8 compliance | fail | no | fail | no |
| Stage 9 K01 | fail | no | partial | no |
| Stage 10 sparse laws | fail | no | fail | no |
| Stage 11 trust | fail | no | fail | no |
| Stage 12 optimization | fail | no | fail | no |
| Stage 13 weak oracle | synthetic only | no | no | no |

| Formulation | Causal/leakage | Full curves | Inspectable |
| --- | --- | --- | --- |
| Stage 4 hybrids | pass | yes | yes |
| Stage 5 H04 | pass | yes | yes |
| Stage 5 H08 | pass | yes | yes |
| Stage 6 spectral/Sobolev | pass | yes | yes |
| Stage 7 mean/shape heads | pass | yes | yes |
| Stage 8 compliance | pass | yes | yes |
| Stage 9 K01 | pass | yes | yes |
| Stage 10 sparse laws | pass | yes | yes |
| Stage 11 trust | pass | yes | yes |
| Stage 12 optimization | pass | yes | yes |
| Stage 13 weak oracle | pass | no real payload | yes |

### Why H04 Enters

H04 passed all ten Stage 5 gates. Across seeds `314159`, `271828`, and
`161803`, its raw MAE values are:

- `0.001725884 deg`;
- `0.001716240 deg`;
- `0.001805115 deg`.

The mean is `0.001749080 deg` and the standard deviation is
`0.000039818 deg`. Every seed beats PF-A and its matched direct-coefficient
control. Runtime measured and target-derived inputs are absent, the complete
`97 x 2048` test payload is preserved, and the coefficient correction and
harmonic reconstruction path are explicit.

### Why K01 Does Not Enter

K01 is a useful research component and improves H04 strongly on several scalar
and curve metrics. It nevertheless failed the complete Stage 9 closure, P95,
and declared chunk-equivalence gate. Conditional stability was therefore
skipped. Stage 12 did not repair those failures. Scientific interest is not a
substitute for the Stage 14 entry contract.

### Why The Stage 13 Weak Residual Does Not Enter

The weak residual is implementation-valid and noise-robust on its analytical
oracle, but it has no isolated real-data training result, no three-seed
predictive evaluation, and no measured full-curve candidate payload. It remains
available for future matched testing only.

## Compatible Metric Surface

| Model | Role | Raw MAE | Centered MAE | Offset error |
| --- | --- | ---: | ---: | ---: |
| H04 | eligible entrant | 0.001726 | **0.001356** | 0.000884 |
| PF-A | analytical reference | 0.001807 | 0.001385 | 0.000965 |
| Harmonic MLP `Fw` | accepted reference | 0.001694 | 0.001390 | 0.000825 |
| Sequence GRU `Fw` | incumbent reference | **0.001618** | 0.001382 | **0.000690** |

H04 improves PF-A by:

- `4.49%` on the frozen Stage 0 raw-MAE value;
- `2.11%` on centered MAE;
- `8.36%` on offset error.

Against the accepted GRU, H04:

- regresses raw MAE by `6.67%`;
- improves centered MAE by `1.92%`;
- regresses offset error by `28.17%`.

This is a real tradeoff, not a scalar victory. H04 supplies the best compatible
centered-shape value, while the GRU remains substantially stronger on raw and
offset behavior.

## Category Decisions

| Category | Entrant result | Reference result | Decision |
| --- | --- | --- | --- |
| Raw error | H04 is sole entrant | GRU better | retain incumbent |
| Centered shape | H04 best | H04 beats all references | H04 advantage |
| Offset | H04 beats PF-A | GRU better | retain incumbent |
| Harmonic fidelity | H04 metrics available | contracts use unlike units | defer ranking |
| Robustness | H04 passes three seeds | references not seed-matched here | certify H04 only |
| Interpretability | bounded explicit coefficients | PF-A is white box | H04 inspectable |
| TwinCAT readiness | compact graph, no parity yet | PF-A parity exists | Stage 15 required |
| Balanced recommendation | H04 only entrant | GRU incumbent | nominate H04 for verification |

The Stage 5 harmonic metrics use degree amplitude error and radian phase error.
The neural Stage 0 references use percentage amplitude error and degree phase
error. Ranking those values directly would be invalid. Stage 15 must regenerate
all candidates on one official metric contract.

## Interpretability And Deployment

H04 has an inspectable inference path:

1. normalize speed, torque, and oil temperature;
2. evaluate the PF-A coefficient surface;
3. infer nine bounded complex coefficient corrections;
4. add corrections to the PF-A anchor;
5. reconstruct the periodic curve from explicit harmonic orders.

This is favorable for TwinCAT because intermediate coefficients and bounds can
be exposed. It is not deployment-ready yet. The learned correction network has
no accepted ONNX export, Python/ONNX parity, TwinCAT graph, or PLC parity
evidence.

## Tournament Decision

Stage 14 closes as a single-entrant tournament with frozen references:

- eligible entrant: H04;
- balanced Stage 15 nominee: H04;
- incumbent accepted forward model: periodic GRU `Fw`;
- official acceptance: no;
- registry update: no;
- harmonic winner: unresolved pending common metrics;
- Stage 15: authorized.

H04 advances only to a separate official forward verification and deployment
preparation step. It must not replace the GRU unless Stage 15 curve-first
evidence and numerical parity justify acceptance.

## Stage 15 Requirements

Stage 15 must:

1. prepare a separate forward-only TE Curve Verification Pipeline launcher;
2. compare H04, PF-A, harmonic MLP, and GRU on one official curve-first surface;
3. normalize raw, shape, offset, harmonic, robustness, and visual evidence;
4. define and export the H04 inference graph;
5. prove Python/ONNX and PLC parity;
6. update registries only after an explicit acceptance decision.

## Reproducibility

The machine-readable closeout is under
`output/analysis/wave_5_2r/stage14_cross_formulation_forward_tournament/`.
It contains the entry matrix, hashed evidence inventory, compatible metric
comparison, category matrix, and final decision. The analysis script supports
both build and validation-only modes.
