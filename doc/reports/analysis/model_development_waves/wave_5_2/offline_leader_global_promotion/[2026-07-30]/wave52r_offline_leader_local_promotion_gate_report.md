# Wave 5.2R Offline Leader Local Promotion Gate Report

## Executive Decision

K01 and H08 passed the local qualification gates required before a bounded
cross-surface promotion campaign. The result authorizes campaign execution; it
does not promote either candidate to global-leader status.

The accepted periodic GRU and periodic harmonic MLP remain unchanged. If the
new candidates later pass the `Fw`, `Bw`, direction-aware `global`, official
TE Curve Verification Pipeline, and target-runtime gates, the intended outcome
is a four-leader portfolio rather than replacement of the incumbents.

## Evaluated Candidates

| Lane | Candidate | Architecture role | Local gate result |
| --- | --- | --- | --- |
| Temporal | K01 | causal GRU residual over an analytical harmonic anchor | passed |
| Non-temporal | H08 | condition-dependent harmonic coefficient residual | passed |

K01 and H08 are Wave 5.2R physics-guided models. They are not interchangeable
with the two established non-PINN deployment references.

## K01 Local Evidence

The wider replay tolerance below applies only to the frozen CUDA-reference
payload; strict same-runtime Python/ONNX comparisons use the tighter tolerance.

| Check | Result | Interpretation |
| --- | ---: | --- |
| CPU replay versus saved CUDA payload, maximum | `2.8625131e-05 deg` | passed cross-device tolerance |
| CPU replay versus saved CUDA payload, mean | `3.8195753e-07 deg` | negligible average drift |
| CPU replay versus saved CUDA payload, P99 | `3.2027310e-06 deg` | bounded tail drift |
| Reset reproducibility | `0 deg` | deterministic reset |
| Chunked versus full-sequence output | `7.4505806e-09 deg` | stateful chunk equivalence passed |
| Mutated-future prefix difference | `0 deg` | causal-prefix gate passed |
| ONNX curve parity | `1.4901161e-08 deg` | Python/ONNX parity passed |
| ONNX hidden-state parity | `5.9604645e-07` | recurrent-state parity passed |
| State-carry effect | `0.0013447043 deg` | carried state measurably affects output |
| Chunk latency P95 | `271.85 us` | local `500 us` proxy passed |
| Chunk latency maximum | `364.4 us` | local proxy remained bounded |
| ONNX package size | `647963 bytes` | compact export package |
| Trainable parameters | `159891` | recorded deployment scale |

## H08 Local Evidence

| Check | Result | Interpretation |
| --- | ---: | --- |
| Saved curve replay | `2.9802322e-08 deg` | deterministic reconstruction passed |
| Saved coefficient replay | `7.4505806e-09` | coefficient replay passed |
| Repeat difference | `0` | deterministic repeat |
| ONNX curve parity | `2.9802322e-08 deg` | Python/ONNX parity passed |
| ONNX coefficient parity | `7.4505806e-09` | inspectable coefficient parity passed |
| Condition latency P95 | `60.705 us` | local latency proxy passed |
| Condition latency maximum | `197.2 us` | local proxy remained bounded |
| ONNX package size | `320299 bytes` | compact export package |
| Trainable parameters | `7651` | low-complexity non-temporal candidate |

The exported H08 path keeps the coefficients, residual correction, analytical
anchor, and reconstructed curve individually inspectable.

## Validity And Fallback Behavior

The validity probe covered five cases. The single in-envelope valid case was
accepted; four invalid or out-of-envelope cases were routed to the required
fallback. The local checks did not replace the established deployment
references and did not claim TwinCAT runtime acceptance.

## Prepared Cross-Surface Campaign

The approved campaign contains three seeds (`314159`, `271828`, and `161803`)
on three distinct surfaces:

- direction-specific `Fw`;
- direction-specific `Bw`;
- direction-aware `global`.

K01 and H08 contribute `18` promotion runs. Nine matched H04 analytical-anchor
runs make the full queue `27` runs. Each direction receives a training-only
analytical-anchor fit; a forward anchor is never reused as a backward or global
anchor.

The campaign is prepared and preflight-clean. Its scalar leaderboard is
bookkeeping evidence only. Promotion requires a separate official multi-index,
curve-first TE Curve Verification Pipeline refresh with distinct `global`,
`Fw`, and `Bw` decisions.

Post-gate status: the campaign completed `27 / 27` runs with zero failures on
`2026-07-31`. K01 is the provisional scalar `Fw` winner; official promotion
remains pending.

## Promotion Boundary

K01 or H08 may join the four-leader portfolio only after all of the following:

1. repeatable cross-seed training on every required surface;
2. acceptable raw, shape, offset, continuity, harmonic, phase, and robustness
   evidence;
3. no disqualifying direction-specific regression;
4. official curve-first verification;
5. sufficient export and target-runtime evidence.

Until then:

- K01 is the temporal offline leader;
- H08 is the balanced non-temporal offline leader;
- periodic GRU remains the accepted temporal non-PINN reference;
- periodic harmonic MLP remains the accepted non-temporal non-PINN reference.

## Integrated Specialist Model TODO

A next-step design study must evaluate whether one inspectable, PLC-conscious
architecture can combine complementary mechanisms without inheriting their
individual weaknesses:

- K01 temporal context, raw-error control, and offset behavior;
- H08 balanced harmonic and phase behavior;
- F01 centered-shape fidelity;
- S01 harmonic amplitude and phase specialization;
- H04 analytical interpretability and low-frequency structure;
- Stage 10 R00 sparse residual structure;
- Stage 10 S01 symbolic or compact correction structure.

This is a recorded future TODO, not authorization to start Wave 6 or a new
training campaign. It requires its own technical design and approval gate.

## Reproducibility Evidence

The canonical local evidence is stored under:

`output/validation_checks/wave52r_offline_leader_promotion/2026-07-30-19-24-35__wave52r_offline_leader_promotion/`

The package includes `promotion_gate_summary.yaml`,
`promotion_gate_report.md`, `artifact_inventory.csv`, and the two ONNX exports.
