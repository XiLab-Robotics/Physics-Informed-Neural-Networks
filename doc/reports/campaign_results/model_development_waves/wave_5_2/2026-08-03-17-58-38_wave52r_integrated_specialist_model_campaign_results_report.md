# Wave 5.2R Integrated Specialist Model Campaign Results

## Executive Summary

The approved empirical Wave 5.2R campaign completed all `24 / 24` planned
entries with no failed queue item: three frozen replay controls, eighteen
single-branch training runs, and three conditional `A08` runs. All `21`
trained run directories contain the required checkpoint, training history,
test predictions, and metrics summary.

Only the forward-gated centered H08 branch (`A02`) passed its predeclared
specialty and multi-index non-regression gate. It passed for all three seeds,
so `A08` executed with `A02` as its only admitted branch and reproduced the
same predictions. The campaign outcome is therefore
`forward_harmonic_specialist_added`, not a multi-specialist qualification.

`A04`, seed `271828`, is the validation-only scalar winner with global
validation MAE `0.001539071 deg` and global test MAE `0.001456655 deg`.
However, `A04` failed both its centered-shape specialty gate and the
multi-index non-regression gate. It is recorded as a provisional family
winner only. No accepted model, incumbent, program registry, or deployment
status changes in this closeout.

## Campaign Contract

- Campaign: `wave52r_integrated_specialist_model_2026_08_02`.
- Execution: LAN-remote, CUDA-enabled campaign runner.
- Dataset and inputs: `polished_dataset + setpoints`.
- Surfaces: separate `Fw`, `Bw`, and direction-aware `global`.
- Seeds: `314159`, `271828`, and `161803`.
- Started: `2026-08-03T17:49:23+02:00`.
- Completed: `2026-08-03T17:58:38+02:00`.
- Runtime target-derived input count: `0` for every trained run.
- Selection boundary: validation-only scalar ordering plus predeclared
  branch-specific gates; no automatic promotion.

This remains an empirical integrated-specialist study. It is not a PINN,
does not reopen physics-integrated Wave 6, and does not establish TwinCAT or
TF3820 runtime readiness.

## Completion And Integrity

| Evidence | Expected | Observed | Result |
| --- | ---: | ---: | --- |
| Campaign entries | 24 | 24 | Pass |
| Frozen replay controls | 3 | 3 | Pass |
| Trained run directories | 21 | 21 | Pass |
| Queue-state files | 24 | 24 | Pass |
| Required campaign artifacts | 8 | 8 | Pass |
| Required trained-run artifacts | 84 | 84 | Pass |
| Failed queue entries | 0 | 0 | Pass |

The required campaign artifacts include the result CSV, gate summary,
leaderboard, explicit best-run YAML and Markdown, artifact path list, campaign
state, and baseline-topology comparison. Every trained run contains
`best_model.pt`, `training_history.csv`, `test_predictions.npz`, and
`metrics_summary.yaml`.

## Branch Results

The error values below are MAE in `1e-3 deg` and are means across the three
declared seeds for trained arms. Replay rows contain their single frozen
result. Lower is better.

| ID | Role | Runs | Gate outcome | Fw | Bw | Global |
| --- | --- | ---: | --- | ---: | ---: | ---: |
| `A00` | Frozen global K01 | 1 replay | Control | 1.401424 | 1.518885 | 1.460155 |
| `A00D` | Routed directional K01 | 1 replay | Control | 1.354961 | 1.579773 | 1.467367 |
| `A01` | Decomposed global K01 | 1 replay | Identity pass | 1.401424 | 1.518885 | 1.460155 |
| `A02` | Forward centered H08 | 3 | Pass, 3 of 3 seeds | 1.397912 | 1.518885 | 1.458399 |
| `A03` | H04 shape control | 3 | Specialty failed | 1.399311 | 1.511419 | 1.455365 |
| `A04` | F01 shape objective | 3 | Specialty and non-regression failed | 1.396812 | 1.513841 | 1.455327 |
| `A05` | S01 harmonic and closure | 3 | Non-regression failed | 1.398555 | 1.518347 | 1.458451 |
| `A06` | R00 dense condition library | 3 | Specialty and non-regression failed | 1.403949 | 1.518515 | 1.461232 |
| `A07` | S01 threshold control | 3 | Specialty failed | 1.400321 | 1.518046 | 1.459184 |
| `A08` | Passed branches only: A02 | 3 | Executed; equivalent to A02 | 1.397912 | 1.518885 | 1.458399 |

## Multi-Index Interpretation

Relative to the exact `A01` replay, `A02` provides a small forward raw-error
gain while remaining exactly inactive on `Bw`. Its global test MAE improves
from `0.001460155 deg` to `0.001458399 deg`, centered-shape MAE improves from
`0.001220701 deg` to `0.001218450 deg`, and closure error improves from
`0.000849561 deg` to `0.000820528 deg`. The offset surface is effectively
unchanged. Its declared validation phase specialty and all required
non-regression checks pass for every seed.

`A03` and `A04` show small test-set raw and shape gains, but neither passes
its predeclared validation specialty gate. `A04` additionally fails the
multi-index non-regression gate. `A05` improves closure and P95 behavior on
test, but violates its validation non-regression contract. The dense and
thresholded condition-library branches (`A06` and `A07`) do not qualify.

The routed directional K01 control (`A00D`) has the best forward replay MAE
and lower global offset error than the global K01 topology, but worse backward
MAE, global centered shape, and global P95. The campaign does not authorize a
deployment-topology switch from this mixed evidence.

## Provisional Scalar Winner

- Ablation: `A04`.
- Seed: `271828`.
- Run: `2026-08-03-17-52-59__a04__seed_271828`.
- Parameters: `1,022` trainable specialist parameters.
- Best epoch: `39`.
- Global validation MAE: `0.001539071 deg`.
- Global test MAE: `0.001456655 deg`.
- Global test centered-shape MAE: `0.001214986 deg`.
- Global test offset absolute error: `0.000577130 deg`.
- Global test P95 curve MAE: `0.004183546 deg`.
- Gate result: failed.

The scalar winner is not the accepted branch decision. Validation ordering
selects the checkpoint, while the predeclared branch gate governs whether a
specialist can advance. Only `A02` advances to later official review.

## Campaign Decision

The campaign decision is `forward_harmonic_specialist_added` at the empirical
candidate level. The centered H08 contribution is admitted only behind its
deterministic forward gate. It remains zero on `Bw`, excludes H08 `a0`, and
does not authorize the rejected global H08 formulation.

No second branch passed, so `multi_specialist_candidate_qualified` is false.
Because `A08` contains only `A02`, it supplies no additional integration gain
and should not be described as a distinct multi-specialist model.

## Registry And Incumbent Decision

The new `integrated_specialist_models` family registry records the campaign's
validation-only provisional winner and its failed-gate status. The program
registry remains unchanged. K01 remains the cross-surface temporal offline
leader, H08 remains the frozen forward-only non-temporal specialist, and the
accepted periodic GRU and periodic harmonic MLP remain the deployment
references.

No checkpoint is promoted into the curated accepted-model archive during this
normal closeout.

## Deployment Boundary

The campaign proves immutable artifact production, zero target-derived runtime
inputs, deterministic direction gating, and bounded inspectable specialist
heads in the Python workflow. It does not prove ONNX export for the new
combined candidate, TwinCAT compilation, target activation, TF3820 licensing,
ADS communication, PLC latency, or commissioned runtime compensation.

Manual PLC testing through the standalone TF3820 module remains a separate
parallel activity.

## Reproducibility Evidence

- Campaign root:
  `output/training_campaigns/2026-08-03-17-49-23_wave52r_integrated_specialist_model_2026_08_02`.
- Run root: `output/training_runs/integrated_specialist_models`.
- Result table: `campaign_results.csv`.
- Gate decision: `branch_gate_summary.yaml`.
- Scalar ordering: `campaign_leaderboard.yaml`.
- Provisional winner: `campaign_best_run.yaml` and `campaign_best_run.md`.
- Baseline topology evidence: `baseline_topology_comparison.yaml`.

## Closeout Status And Next Step

Normal campaign closeout is complete after Markdown, PDF, registry, status,
and active-state QA. The TE Program Status And Closeout Ledger was checked and
updated because the campaign changed the integrated-specialist decision.

The heavy TE Curve Verification Pipeline remains a separate optional
operator-run step. If approved, its launcher must support local and `-Remote`
execution and must evaluate `Fw`, `Bw`, and `global` separately under the
canonical multi-index curve-first policy. Until that later decision, A02 is a
qualified empirical candidate only and A04 remains an unpromoted scalar
winner.
