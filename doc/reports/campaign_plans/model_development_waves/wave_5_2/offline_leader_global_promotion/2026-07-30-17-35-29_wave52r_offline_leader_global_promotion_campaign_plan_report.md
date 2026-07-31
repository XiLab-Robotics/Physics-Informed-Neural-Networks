# Wave 5.2R Offline Leader Global Promotion Campaign Plan

## Overview

This preliminary plan governed the conditional training portion of the K01 and
H08 promotion workflow. It was approved and the campaign later completed
`27 / 27` runs with zero failures on `2026-07-31`. The existing
forward-only checkpoints must first pass provenance, replay, causal, export,
parity, runtime, and PLC-preparation gates.

The campaign will be prepared only for candidates that pass those preliminary
tests. Its purpose is to determine whether a qualified Wave 5.2R candidate can
become a direction-aware `global` leader without replacing or deleting the
accepted periodic GRU and periodic harmonic MLP controls.

## Approval And Scope

- Technical document:
  `doc/technical/2026-07/2026-07-30/`
  `2026-07-30-17-35-29_wave52r_offline_leader_global_promotion_and_four_leader_portfolio.md`
- Technical-document approval: approved by the user on `2026-07-30`.
- Campaign-plan approval: approved by the user on `2026-07-30`.
- Execution status: completed and normally closed out on `2026-07-31`.
- Dataset: `polished_dataset`.
- Input mode: setpoints.
- Conditional candidate families: K01 and H08.
- Required surfaces: `Fw`, `Bw`, and `global`.
- Incumbent controls: periodic GRU and periodic harmonic MLP.
- Runtime target-derived inputs: zero.
- Registry replacement: prohibited before official post-campaign curve
  verification.

## Entry Gate

A candidate may enter training only if it has:

- a loadable immutable checkpoint and frozen provenance record;
- deterministic Python replay against its saved forward payload;
- no future-information or target-derived runtime dependency;
- candidate-specific reset, state, chunk, coefficient, and harmonic tests;
- a standalone portable export with declared numerical parity;
- bounded CPU runtime, memory, and model-size measurements;
- a documented PLC-facing inference contract and fallback behavior.

Failure of one candidate does not block testing or conditional advancement of
the other.

## Conditional Candidate Matrix

| Candidate family | `Fw` | `Bw` | `global` | Purpose |
| --- | --- | --- | --- | --- |
| K01 residual GRU | repeat | train | train | temporal promotion |
| H08 harmonic coefficient residual | repeat | train | train | non-temporal promotion |
| Periodic GRU | frozen control | frozen control | frozen control | incumbent temporal baseline |
| Periodic harmonic MLP | frozen control | frozen control | frozen control | incumbent non-temporal baseline |

The frozen campaign uses seeds `314159`, `271828`, and `161803` on each of the
`Fw`, `Bw`, and direction-aware `global` surfaces. It contains `18` promotion
runs, covering K01 and H08 on all surface/seed combinations, plus `9` matched
H04 anchor runs, for `27` runs in total. A single favorable rerun cannot
authorize promotion.

## Training And Evaluation Contract

- Use immutable timestamped `run_instance_id` output directories.
- Keep logical candidate names separate from physical run identifiers.
- Preserve the repository's frozen direction-aware split policy.
- Select hyperparameters on training and validation only.
- Evaluate the test surface once after selection is frozen.
- Keep `Fw` and `Bw` metrics visible even for a `global` checkpoint.
- Preserve speed, signed torque, oil temperature, angle, direction, encoder
  zeroing, and `DataValid` semantics.
- Save checkpoints, reconstructed predictions, per-curve metrics, runtime
  contract metadata, and split signatures.
- Detect exact prediction duplicates and invalid replays.

## Promotion Metrics

Each surface must report:

- raw MAE, RMSE, mean percentage error, P95, and worst curve;
- mean-centered shape fidelity;
- absolute offset and continuity behavior;
- derivative, closure, and peak-to-peak behavior;
- harmonic amplitude and phase fidelity;
- operating-band and tail robustness;
- causal replay, export parity, latency, memory, and fallback behavior.

Scalar MAE or a global aggregate alone cannot authorize promotion.

## Exit Gate

K01 or H08 qualifies for a four-leader portfolio decision only if:

1. its repeated runs are stable across the declared seeds;
2. its `Fw`, `Bw`, and `global` checkpoints satisfy the causal and deployment
   contract;
3. no direction is hidden by a favorable global aggregate;
4. it is non-inferior to the matching incumbent on critical robustness and
   harmonic gates;
5. it provides a material multi-index improvement on at least one declared
   surface;
6. the later official TE Curve Verification Pipeline refresh confirms the
   result;
7. export and runtime evidence is sufficient for the claimed promotion level.

Passing creates an additional leader; it does not delete or demote the
incumbent automatically.

## Required Campaign Package After Approval

If the entry gate passes, preparation must create:

- campaign YAML files under `config/training/`;
- a dedicated PowerShell launcher supporting local and `-Remote`;
- a matching launcher note documenting both command paths;
- persistent `doc/running/active_training_campaign.yaml` state;
- exact preflight and launch commands;
- expected winner, leaderboard, registry, report, and output paths.

The launcher will be prepared but not executed by default. The user will run it
and report completion before closeout inspection.

## Expected Closeout

Normal closeout will produce:

- `campaign_leaderboard.yaml`;
- `campaign_best_run.yaml`;
- `campaign_best_run.md`;
- campaign-results Markdown and validated PDF;
- family and program registry synchronization where justified;
- master-summary, backlog, and ledger synchronization.

The heavy global/Fw/Bw TE Curve Verification Pipeline remains a separate
operator-approved workflow after normal campaign closeout.

## Deferred Integrated-Model TODO

A separate future plan must evaluate whether K01, H08, F01, S01, H04, Stage 10
R00, and Stage 10 S01 can contribute complementary temporal, shape, harmonic,
offset, robustness, and interpretability mechanisms to one causal integrated
model. That future campaign is not part of this promotion campaign and remains
unauthorized until its own technical document and campaign plan are approved.
