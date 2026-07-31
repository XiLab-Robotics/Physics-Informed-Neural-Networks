# Wave 5.2R Cross-Surface Offline Leader Promotion Decision

## Decision

The official `Fw`, `Bw`, and direction-aware `global` TE Curve Verification
Pipeline refresh completed on `2026-07-31`. K01 seed `271828` passes the
cross-surface offline promotion gate and becomes the Wave 5.2R temporal
offline leader for all three surfaces. This is not a TwinCAT runtime or
deployable-leader claim.

H08 does not pass global promotion. It remains the preserved non-temporal
forward offline specialist because its harmonic and shape behavior is useful,
but its `Bw` and `global` raw-error and offset regressions prevent a global
leader claim.

The accepted periodic GRU and periodic harmonic MLP are retained unchanged as
the non-PINN temporal and non-temporal references. No incumbent artifact was
deleted, no accepted registry was overwritten, and the proposed four-global-
leader portfolio was not reached because only K01 passed the cross-surface
gate.

## Evaluation Scope

- Dataset: `polished_dataset`.
- Input mode: setpoints.
- Candidates: `24`, comprising `18` K01/H08 campaign checkpoints and six
  frozen incumbent controls.
- Curves: `97` forward, `97` backward, and `194` combined global curves.
- Seeds: `314159`, `271828`, and `161803`.
- Policy: multi-index curve-first, with raw error, centered shape, offset,
  peak-to-peak behavior, derivative fidelity, closure, harmonic amplitude,
  harmonic phase, seed stability, and visual evidence kept distinct.

## Selected-Candidate Evidence

Positive improvement means that the candidate is better than its matched
non-PINN lane incumbent.

| Lane | Surface | Candidate | Raw MAE [deg] | Offset [deg] | Shape MAE [deg] | Decision |
| --- | --- | --- | ---: | ---: | ---: | --- |
| temporal | `Fw` | K01 `271828` | 0.001358 (+16.07%) | 0.000491 (+28.84%) | 0.001209 (+12.52%) | pass |
| temporal | `Bw` | K01 `271828` | 0.001587 (+13.61%) | 0.000564 (+6.93%) | 0.001344 (+18.50%) | pass; P2P caveat |
| temporal | `global` | K01 `271828` | 0.001464 (+19.12%) | 0.000577 (+23.98%) | 0.001225 (+19.25%) | pass |
| non-temporal | `Fw` | H08 `161803` | 0.001688 (+0.35%) | 0.000862 (-4.48%) | 0.001320 (+5.04%) | forward specialist |
| non-temporal | `Bw` | H08 `161803` | 0.001933 (-1.10%) | 0.000704 (-15.03%) | 0.001658 (+1.13%) | fail global gate |
| non-temporal | `global` | H08 `314159` | 0.001871 (-7.90%) | 0.000837 (-22.01%) | 0.001517 (-2.78%) | fail global gate |

K01 also beats the matched GRU on harmonic amplitude, harmonic phase,
derivative fidelity, and closure on each selected surface. Its backward
peak-to-peak error is `8.100626%`, worse than the backward GRU's `6.640831%`;
this is retained as an explicit robustness caveat rather than hidden by the
aggregate decision.

H08 improves harmonic amplitude and phase substantially against the periodic
harmonic MLP, and it preserves useful forward centered-shape behavior. On
backward and global surfaces, however, those gains do not compensate for the
raw, offset, and associated envelope regressions. The global visual shortlist
also shows the larger high-dynamic-condition mismatch.

## Seed And Surface Interpretation

K01's three seeds remain ahead of the matched GRU on raw MAE, offset, and
centered shape for `Fw` and `global`. All three backward K01 seeds also improve
raw, offset, and centered shape, while the peak-to-peak caveat remains the
main directional weakness. Seed `271828` is selected because it is the best
diagnostic-ranked K01 checkpoint on each surface.

H08 is stable in scalar MAE across seeds but not uniformly strong across the
full multi-index surface. Its best forward seed is useful, whereas no backward
or global seed establishes a balanced win over the matched non-temporal
incumbent.

## Visual Evidence

- Forward four-model shortlist and curve collages.
- Backward four-model shortlist and curve collages.
- Direction-aware global four-model shortlist and curve collages.
- CVP 1.2 full-resolution curve-payload diagnostics for all `24` candidates.

The real generated collages were inspected after export. K01 preserves the
low-frequency envelope and much of the measured high-frequency structure on
both directions. H08 remains plausible on forward curves but exposes larger
offset and amplitude mismatch on backward and global high-dynamic examples.

## Portfolio State

The resulting portfolio is deliberately non-destructive:

- K01: promoted cross-surface temporal offline leader; TwinCAT runtime pending.
- H08: retained non-temporal forward offline specialist; not a global leader.
- periodic GRU: retained accepted non-PINN temporal reference.
- periodic harmonic MLP: retained accepted non-PINN non-temporal reference.

The four-global-leader target is therefore not declared achieved. All four
families remain available for future research and comparison, but their roles
are not falsely flattened into one acceptance class.

## Next Work

1. Qualify K01 in the repository-owned TwinCAT replay path before any
   deployable-leader claim.
2. Keep H08 frozen and diagnose its backward/global offset and envelope
   defect rather than retraining it blindly.
3. Prepare a separate approval-gated integrated-specialist roadmap covering
   K01, H08, F01, S01, H04, Stage 10 R00, and Stage 10 S01, with ablations that
   prove each imported component adds benefit without transferring its known
   defect.

## Artifacts

- Official decision YAML:
  `output/analysis/wave_5_2r/offline_leader_cross_surface_track2/official_promotion_decision.yaml`.
- Raw matrix summaries:
  `output/validation_checks/track2_reference_comparison/2026-07-31-13-23-15__wave52r_offline_leader_cross_surface_track2_wave52r_offline_leader_cross_surface_promotion_forward/validation_summary.yaml`,
  `2026-07-31-13-24-17...backward/validation_summary.yaml`, and
  `2026-07-31-13-25-20...global/validation_summary.yaml`.
- CVP 1.2 diagnostics:
  `output/analysis/wave_5_2r/offline_leader_cross_surface_track2/curve_payload_diagnostics/2026-07-31-13-29-13__track2c_curve_payload_diagnostics/`.
- Visual reports: the `forward`, `backward`, and `global` bundles under
  `doc/reports/analysis/model_development_waves/wave_5_2/offline_leader_global_promotion/visual_collages/`.
