# Track 1 LGBM19 Vs Feedforward Curve-Space Comparison

## Overview

This technical document defines the implementation plan for the first
repository-owned comparison between one paper-faithful RCIM reference bank and
one repository direct-TE baseline.

The approved initial scope is intentionally narrow:

- use the best current `feedforward` repository result as the direct-TE
  baseline;
- use the curated `19`-model `LGBM` exact-paper family archive as the
  paper-faithful harmonic reference bank;
- compare both approaches on a shared offline evaluation surface before any
  broader rollout to the other `Track 1` families or to the wider repository
  model zoo.

The reference reading and current repository evidence indicate that the paper
does not rely on one monolithic TE predictor. Instead, it separates:

- a prediction layer that estimates selected harmonic terms from the operating
  variables;
- a compensation or reconstruction layer that recomposes those terms into the
  TE signal used downstream.

For this reason, the first comparison must not be framed only as
`sub-model metric vs direct-curve metric`. The repository needs one common
evaluation layer in curve space so the assembled `LGBM` harmonic bank and the
best `feedforward` baseline can be compared on the same held-out TE curves.

This work must stay compatible with the currently prepared
`track1_remaining_yellow_cell_campaigns_2026_04_22_01_40_43` campaign state.
No protected campaign configuration, launcher, queue, or active-state file
listed in `doc/running/active_training_campaign.yaml` should be modified as
part of this implementation unless explicitly re-approved later.

No Codex subagent is planned for this work. If subagent use becomes desirable
later, it must be proposed explicitly, recorded in a follow-up technical
document update, and approved before launch.

## Technical Approach

The comparison should be implemented around one shared offline evaluator rather
than around family-specific metric tables.

The key design rule is:

- compare different model forms only after projecting them onto the same TE
  curve evaluation surface.

That means the implementation should distinguish three layers.

1. Prediction adapters

- `DirectCurveModelAdapter` for the best `feedforward` run.
- `HarmonicBankAdapter` for the curated `LGBM` `19`-model reference archive.

These adapters may expose different internal outputs, but they must both feed
the same downstream evaluator contract.

2. Reconstruction layer

- the `feedforward` adapter already emits a direct TE curve prediction;
- the `LGBM` adapter must:
  - load the archived amplitude and phase sub-models;
  - predict the selected harmonic terms on the common evaluation inputs;
  - reconstruct the TE curve from those predicted harmonics.

This assembled `LGBM` bank is the repository equivalent of the paper-side
selected model bank for the chosen initial family.

3. Shared curve-space evaluator

The evaluator should consume truth curves plus predicted curves from both
adapters and report one aligned metric bundle.

The primary metric should be the harmonic-wise branch target already present in
the repository:

- TE-curve `mean percentage error`.

The evaluator should also report supporting curve-space metrics:

- `curve_mae_deg`;
- `curve_rmse_deg`;
- `mean_percentage_error`;
- `p95_percentage_error`;
- per-scenario breakdown by operating condition and direction;
- a small preview set of representative `truth vs prediction` overlays.

To keep the first implementation reliable, the comparison should use one common
evaluation manifest built from the intersection of samples that both baselines
can evaluate correctly. This avoids a false comparison caused by mismatched
test coverage between:

- the best `feedforward` run artifacts;
- the `LGBM` exact-paper archive source split and dataset snapshot.

The implementation should also include one non-model baseline:

- `oracle_harmonic_truncation`.

This oracle is not a competing model. It is a diagnostic ceiling for the chosen
harmonic representation, so the report can separate:

- representation limit;
- sub-model prediction error;
- direct-TE baseline behavior.

The resulting architecture should remain extendable without redesign:

- today: `LGBM-19` assembled bank vs best `feedforward`;
- next: cherry-picked best-per-harmonic bank across the accepted `Track 1`
  family archives;
- later: broader repository model comparisons using the same curve-space
  evaluator and report format.

The first report should treat `Table 6` as supporting diagnostic context rather
than as the primary outcome surface. The main outcome must be the final curve
comparison on the common offline evaluator.

## Involved Components

- `reference/RCIM_ML-compensation.pdf`
- `doc/reference_summaries/03_RCIM_ML_Compensation_Project_Summary.md`
- `doc/reports/analysis/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/Training Results Master Summary.md`
- `doc/reports/analysis/validation_checks/track1/harmonic_wise/`
- `models/paper_reference/rcim_track1/lgbm_reference_models/`
- `models/paper_reference/rcim_track1/lgbm_reference_models/reference_inventory.yaml`
- `output/registries/families/feedforward/leaderboard.yaml`
- `output/training_runs/feedforward/2026-04-04-12-32-00__te_feedforward_stride1_high_compute_long_remote/`
- `scripts/paper_reimplementation/rcim_ml_compensation/`
- repository-owned evaluation and reporting scripts under `scripts/reports/`
- future comparison outputs under `doc/reports/analysis/` and/or
  `doc/reports/analysis/validation_checks/`
- `doc/running/active_training_campaign.yaml`
- `doc/technical/2026-04/2026-04-20/2026-04-20-23-21-36_track1_scope_separation_from_harmonic_wise_branch.md`

## Implementation Steps

1. Inspect the archived `LGBM` `19`-model reference inventory and the best
   `feedforward` run artifacts to define the exact common evaluation input and
   output contract.
2. Introduce one repository-owned comparison manifest that records the shared
   evaluation sample set and avoids silent dataset mismatch between the two
   baselines.
3. Implement a `HarmonicBankAdapter` that loads the curated `LGBM` archive,
   predicts the selected harmonic terms, and reconstructs the TE curve on the
   common evaluator input.
4. Implement or extend a `DirectCurveModelAdapter` for the selected best
   `feedforward` baseline so it emits the same evaluator-facing predicted-curve
   object shape.
5. Add one shared curve-space evaluator that computes:
   `curve_mae_deg`, `curve_rmse_deg`, `mean_percentage_error`,
   `p95_percentage_error`, per-scenario summaries, and representative preview
   curves.
6. Add an `oracle_harmonic_truncation` comparison line so the report can
   distinguish harmonic-representation ceiling from model error.
7. Generate one first-stage comparison report that presents:
   `LGBM-19 assembled bank`, best `feedforward`, and oracle truncation on the
   same held-out evaluation manifest.
8. Keep the resulting script and report structure generic enough that later
   cherry-picked banks and other `Track 1` family archives can be plugged into
   the same evaluator without redesign.
9. Run Markdown QA on the touched Markdown scope before requesting approval for
   the later implementation pass.
