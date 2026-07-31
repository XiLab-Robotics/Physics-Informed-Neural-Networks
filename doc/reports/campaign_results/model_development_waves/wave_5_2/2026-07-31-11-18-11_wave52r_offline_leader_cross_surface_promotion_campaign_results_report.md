# Wave 5.2R Offline Leader Cross-Surface Promotion Campaign Results

## Executive Summary

The approved campaign completed `27 / 27` runs with zero failed queue entries:
`18` K01/H08 promotion runs and `9` matched H04 analytical-anchor runs. Every
declared checkpoint is present.

K01 is the provisional scalar validation winner on `Fw` with seed `271828`
and test MAE `0.001355 deg`. Across the three seeds, K01 also has the lowest
mean test MAE on `Fw`, `Bw`, and direction-aware `global`. This is campaign
evidence only: no global promotion and no incumbent replacement is authorized.

## Campaign Contract

- Dataset: `polished_dataset`.
- Input mode: setpoints.
- Surfaces: `Fw`, `Bw`, and direction-aware `global`.
- Seeds: `314159`, `271828`, and `161803`.
- Promotion candidates: K01 and H08.
- Internal analytical anchor: H04.
- Runtime target-derived inputs: zero.
- Completed runs: `27`.
- Failed runs: `0`.

## Aggregate Raw-Error And Repeatability Results

| Surface | Candidate | Mean MAE [deg] | MAE SD [deg] | Best MAE [deg] |
| --- | --- | ---: | ---: | ---: |
| Fw | K01 | 0.001442 | 0.000088 | 0.001355 |
| Fw | H08 | 0.001690 | 0.000003 | 0.001686 |
| Fw | H04 | 0.001749 | 0.000040 | 0.001716 |
| Bw | K01 | 0.001636 | 0.000050 | 0.001580 |
| Bw | H08 | 0.001973 | 0.000028 | 0.001934 |
| Bw | H04 | 0.001995 | 0.000012 | 0.001978 |
| global | K01 | 0.001553 | 0.000067 | 0.001460 |
| global | H08 | 0.001869 | 0.000001 | 0.001868 |
| global | H04 | 0.001892 | 0.000011 | 0.001883 |

## Aggregate Shape And Offset Results

| Surface | Candidate | Centered MAE [deg] | Mean offset [deg] |
| --- | --- | ---: | ---: |
| Fw | K01 | 0.001243 | 0.000558 |
| Fw | H08 | 0.001349 | 0.000841 |
| Fw | H04 | 0.001365 | 0.000909 |
| Bw | K01 | 0.001407 | 0.000548 |
| Bw | H08 | 0.001683 | 0.000738 |
| Bw | H04 | 0.001716 | 0.000721 |
| global | K01 | 0.001317 | 0.000583 |
| global | H08 | 0.001521 | 0.000835 |
| global | H04 | 0.001544 | 0.000839 |

K01 leads mean raw MAE and mean centered MAE on every trained surface. H08 is
highly repeatable across seeds and improves the matched H04 raw MAE on every
surface, but its scalar offset advantage is surface-dependent. These aggregate
training/test metrics do not replace the required per-curve robustness,
harmonic, phase, continuity, and visual evidence.

## Provisional Winner

- Candidate: `K01`.
- Surface: `Fw`.
- Seed: `271828`.
- Run: `2026-07-31-10-45-41__stage9_k01__seed_271828`.
- Test MAE: `0.001354961 deg`.
- Centered MAE: `0.001205198 deg`.
- Offset absolute error: `0.000490818 deg`.
- Per-curve MAE P95: `0.003932765 deg`.
- Chunk-equivalence maximum difference: `3.948808e-07 deg`.
- Reset reproducibility maximum difference: `0 deg`.

The provisional winner is selected by the campaign's validation-only scalar
ordering. It cannot authorize promotion under the repository curve-first
policy.

## Integrity And Bookkeeping

All nine queue-state files report `completed`, all 27 result rows have matching
checkpoints, and the campaign state reports `27` completed and `0` failed. The
closeout repaired a bookkeeping omission where the nine successful K01 rows
lacked the CSV/YAML `status` field even though their queue states, metrics,
predictions, and checkpoints were complete. The campaign runner now writes
that field for future executions.

## Incumbent Preservation

Periodic GRU remains the accepted temporal non-PINN reference. Periodic
harmonic MLP remains the accepted non-temporal non-PINN reference. Neither is
deleted, overwritten, or demoted by this scalar campaign closeout.

## Promotion Decision

The campaign qualifies K01 and H08 for the separate official TE Curve
Verification Pipeline refresh. It does not yet establish that either model is
a global leader. The official review must keep `Fw`, `Bw`, and `global`
separate and compare raw error, centered shape, offset and continuity,
harmonic and phase fidelity, robustness, visual evidence, and deployment
readiness.

## Registry Decision

No accepted family or program leader registry changes in this normal closeout.
K01 remains the temporal offline leader and H08 remains the balanced
non-temporal offline leader pending official curve-first verification and
target-runtime acceptance.

## Future Integrated Specialist TODO

The roadmap retains the separate design study combining the complementary
strengths of K01, H08, F01, S01, H04, Stage 10 R00, and Stage 10 S01. This
closeout does not authorize that model or reopen physics-integrated Wave 6.

## Reproducibility Evidence

- Campaign directory: `output/training_campaigns/2026-07-31-10-39-08_wave52r_offline_leader_cross_surface_promotion_2026_07_30`.
- Leaderboard: `campaign_leaderboard.yaml`.
- Provisional winner: `campaign_best_run.yaml` and `campaign_best_run.md`.
- Result table: `campaign_results.csv`.
- Immutable run list: `campaign_artifact_path_list.txt`.

## Next Step

Prepare the operator-facing `Fw`/`Bw`/`global` TE Curve Verification Pipeline
launcher, run it separately, and accept or reject each candidate surface using
the official multi-index curve-first policy.
