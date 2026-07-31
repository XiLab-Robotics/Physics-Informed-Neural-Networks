# Wave 5.2R Offline Leader Promotion Gate Report

## Outcome

The local forward promotion gates completed with overall status
`qualified_for_conditional_cross_surface_campaign`.

- K01: `passed_local_promotion_gates`;
- H08: `passed_local_promotion_gates`;
- incumbent periodic GRU and periodic harmonic MLP: preserved unchanged;
- TwinCAT runtime acceptance: pending;
- backward and global promotion: not yet evaluated.

## K01

- checkpoint replay maximum curve difference:
  `2.86251307e-05 deg`;
- reset reproducibility maximum difference:
  `0 deg`;
- chunk/full-sequence maximum difference:
  `7.4505806e-09 deg`;
- mutated-future prefix difference:
  `0 deg`;
- ONNX curve maximum difference:
  `1.49011612e-08 deg`;
- ONNX hidden-state maximum difference:
  `5.96046448e-07`;
- state-carry functional effect:
  `0.0013447043 deg`;
- ONNX chunk P95:
  `271.850 us`;
- local `500 us` proxy:
  `True`.

K01 is locally export-qualified with an explicit stateful causal interface.
This is not yet a TwinCAT runtime pass.

## H08

- checkpoint replay maximum curve difference:
  `2.98023224e-08 deg`;
- checkpoint replay maximum coefficient difference:
  `7.4505806e-09 deg`;
- deterministic repeated-run difference:
  `0 deg`;
- ONNX curve maximum difference:
  `2.98023224e-08 deg`;
- ONNX coefficient maximum difference:
  `7.4505806e-09 deg`;
- ONNX condition-level P95:
  `60.705 us`.

H08 is locally export-qualified with inspectable harmonic coefficients and
explicit reconstruction outputs. This is not yet a TwinCAT runtime pass.

## Validity And Fallback

The shared input-envelope test classified
`5` cases and
routed all non-finite or out-of-envelope inputs to fallback. The incumbent
models remain the required operational fallback until the new candidates pass
the remaining gates.

## Decision

Local Gates A through C are sufficient only to decide whether a candidate may
enter the conditional `Fw`, `Bw`, and `global` campaign. They do not authorize
global leadership by themselves.

The next allowed step is to prepare the approved cross-surface campaign package
for every candidate with status `passed_local_promotion_gates`, keeping the
periodic GRU and periodic harmonic MLP as frozen controls.
