# Wave 5.2R Integrated-Specialist Track 2 Official Decision

## Executive Decision

The Wave 5.2R integrated-specialist refresh completed separate `Fw`, `Bw`, and
direction-aware `global` matrices and passed the required curve-first review.
The official outcome remains `forward_harmonic_specialist_added`:

- recommend `wave52r_integrated_a02_seed_314159` as the verified offline `Fw`
  specialist and as the best routed `global` integrated candidate;
- retain `wave52r_promotion_k01_global_seed_271828` as the `Bw` recommendation
  and frozen temporal backbone;
- retain A03-A07 as diagnostic ablations because each failed its campaign
  branch gate, even when it wins an isolated Track 2 axis;
- keep all accepted periodic GRU and periodic harmonic MLP registries
  unchanged;
- make no TwinCAT runtime or deployment-readiness claim.

A02 is not a new backward model. Its backward prediction is effectively the
frozen K01 path, while its measurable benefit comes from the deterministic
forward-gated centered H08 contribution.

## Evidence Scope

The operator-run matrix evaluated the prepared 29-candidate inventory with
surface filtering:

| Surface | Curves | Candidates | New trained runs | Control role |
| --- | ---: | ---: | ---: | --- |
| `Fw` | 97 | 27 | 21 | K01 global, H08 Fw, and four compatible incumbent surfaces |
| `Bw` | 97 | 26 | 21 | K01 global and four compatible incumbent surfaces |
| `global` | 194 | 24 | 21 | K01 global and two global incumbent surfaces |

The CVP 1.2 shortlist contains the candidates that won at least one raw or
robustness axis, the only campaign-qualified branch, and the frozen K01/H08
controls. A08 is omitted as an independent shortlist entry because it contains
only A02 and is prediction-equivalent to it.

The visual shortlist adds the six accepted incumbent surfaces, for 15 plotted
candidates. The official comparison therefore preserves incumbent evidence
without treating a repeated full-payload diagnostic as a prerequisite for
their already established roles.

## Selection Method

The decision applies the canonical multi-index curve-first policy with bounded
within-surface rank normalization. Lower scores are better.

| Block | Weight | Metrics used |
| --- | ---: | --- |
| Shape and harmonic fidelity | 35% | centered MAE, peak-to-peak error, harmonic amplitude error, harmonic phase error |
| Raw operating error | 20% | curve MAE, RMSE, mean percentage error |
| Offset and continuity | 20% | absolute mean-offset error, closure mismatch |
| Robustness | 15% | P95 mean percentage error |
| Deployment readiness | 10% | causal/export evidence, added complexity, inspectability, campaign gate status |

Campaign branch-gate failure is a promotion veto. The frozen H08 candidate also
keeps its earlier raw/offset regression veto. These candidates remain visible
as axis winners but cannot become the final recommendation.

## Per-Surface Winners

| Surface | Best raw | Best shape | Best offset | Best P95 | Recommendation |
| --- | --- | --- | --- | --- | --- |
| `Fw` | A04 seed `161803` | A02 seed `314159` | A07 seed `161803` | A07 seed `314159` | A02 seed `314159` |
| `Bw` | A03 seed `161803` | A03 seed `161803` | A07 seed `161803` | A07 seed `161803` | K01 global seed `271828` |
| `global` | A04 seed `161803` | A04 seed `161803` | A07 seed `161803` | A06 seed `271828` | A02 seed `314159` |

A03, A04, A06, and A07 win diagnostic axes but remain vetoed by their failed
campaign gates. This is exactly the distinction required by the policy: an
isolated metric win does not override failed specialty or non-regression
evidence.

## Forward Decision

A02 seed `314159` improves over frozen global K01 on the forward matrix:

- raw MAE decreases from `0.001404833 deg` to `0.001400449 deg`, a `0.312%`
  improvement;
- P95 mean percentage error decreases by `0.669%`;
- centered-shape MAE decreases from `0.001153412 deg` to `0.001147969 deg`;
- mean harmonic-amplitude error decreases from `5.095826%` to `4.750917%`.

K01 remains slightly better on mean peak-to-peak error and mean harmonic phase
error. A02 nevertheless has the best veto-free multi-index score and is the
only added branch that passed the campaign gate for all three seeds.

A04 seed `161803` has the best forward raw MAE and centered-shape MAE, but its
campaign specialty and multi-index non-regression gates failed. A07 wins the
forward robustness axis but also failed its campaign gate. Neither is promoted.

The forward recommendation is therefore A02 seed `314159` as a verified
offline forward specialist. This does not yet replace an accepted deployment
registry.

## Backward Decision

A02 and frozen K01 are effectively tied on `Bw`:

- A02 raw MAE is `0.001523088 deg`;
- K01 raw MAE is `0.001523086 deg`;
- their P95 mean percentage errors differ by less than `0.004%` relative.

This equivalence matches the deterministic design: the H08 contribution is
zero on backward curves. A03 seed `161803` improves raw and centered-shape
metrics, while A07 improves offset and P95 behavior, but both branches failed
their campaign gates.

The backward recommendation remains K01 global seed `271828`. There is no
distinct integrated-specialist backward promotion.

## Global Decision

A02 seed `314159` improves global raw MAE over K01 from `0.001463960 deg` to
`0.001461769 deg`, a `0.150%` improvement. Its CVP 1.2 diagnostic score is
`3.652449`, the best of the nine-candidate payload shortlist. The global gain is
the aggregation of a real forward improvement and an unchanged backward path;
it is not evidence for a new undifferentiated global expert.

A04 seed `161803` is the global raw and shape winner, and A06/A07 win robustness
and offset axes, but all retain campaign-gate vetoes. A02 is therefore the best
veto-free routed global integrated candidate. K01 remains the frozen temporal
backbone and the simpler backward recommendation.

## Visual Review

The reviewed A02 collage and forward/backward overlays show:

- continuous full-revolution predictions with no visible stitching failure;
- close agreement among the integrated variants on ordinary conditions;
- under-reproduction of high-frequency amplitude at the hardest high-speed,
  high-torque examples across both new and incumbent groups;
- a measurable but visually small forward benefit from the specialist branch;
- no distinct backward A02 behavior beyond K01-equivalent routing.

The plots therefore support the numerical recommendation but also show why the
offline improvement must not be described as a solved compensation problem.
The extreme-condition amplitude gap remains visible.

## Incumbent And Deployment Boundary

A02 raw MAE is lower than the accepted directional or global incumbent models
on every applicable matrix. Relative to the matching accepted directional
incumbents, its raw-MAE improvements are approximately:

- `13.47%` versus periodic GRU Fw and `17.31%` versus harmonic MLP Fw;
- `17.09%` versus periodic GRU Bw and `20.35%` versus harmonic MLP Bw;
- `19.25%` versus periodic GRU global and `15.69%` versus harmonic MLP global.

These are offline comparisons only. The accepted incumbents retain their
registry and deployment roles because A02 has not passed the separate export,
TwinCAT build, target activation, ADS, license, and commissioned runtime gates.
Static or host-side parity cannot substitute for those checks.

## Final Status

The official Track 2 decision is:

- `Fw`: A02 seed `314159` is a verified offline forward-specialist candidate;
- `Bw`: retain K01 global seed `271828`;
- `global`: A02 seed `314159` is the preferred routed integrated offline
  candidate, with benefit attributable only to its forward branch;
- A03-A07: retain as diagnostic failed-gate ablations;
- A08: retain as the prediction-equivalent A02 composition replay;
- accepted registries: unchanged;
- deployment readiness: not established.

The next model-facing step is export and TwinCAT qualification of the selected
A02 path if the project chooses to advance it. Manual standalone PLC testing
may continue in parallel without changing this offline decision.

The live backlog, training master summary, program closeout ledger, active
campaign state, and canonical directional overview were synchronized. The RCIM
Paper Reference Benchmark was checked and requires no content change because
this refresh contains no repository-owned online compensation result.

## Artifact Index

- Matrix summaries:
  `output/validation_checks/track2_reference_comparison/2026-08-03-21-58-09__wave52r_integrated_specialist_track2_wave52r_integrated_specialist_track2_forward/validation_summary.yaml`,
  `output/validation_checks/track2_reference_comparison/2026-08-03-21-59-38__wave52r_integrated_specialist_track2_wave52r_integrated_specialist_track2_backward/validation_summary.yaml`,
  and
  `output/validation_checks/track2_reference_comparison/2026-08-03-22-01-08__wave52r_integrated_specialist_track2_wave52r_integrated_specialist_track2_global/validation_summary.yaml`.
- CVP 1.2 diagnostics:
  `output/validation_checks/wave52r_integrated_specialist_track2_curve_payload_diagnostics/2026-08-04-00-31-50__track2c_curve_payload_diagnostics/`.
- Multi-index decision:
  `output/analysis/wave_5_2r/integrated_specialist_track2_decision/multi_index_surface_decision.yaml`.
- Candidate scores:
  `output/analysis/wave_5_2r/integrated_specialist_track2_decision/multi_index_candidate_scores.csv`.
- Collage report:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/wave52r_integrated_specialist_best_model_collage_report/[2026-08-04]/track2_best_model_collage_report.md`.
- Overlay report:
  `doc/reports/analysis/te_curve_verification_pipeline/02_visual_reports/wave52r_integrated_specialist_multi_model_curve_comparison_report/[2026-08-04]/track2_multi_model_curve_comparison_report.md`.
