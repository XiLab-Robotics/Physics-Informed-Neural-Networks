# Wave 5.2R Full-Candidate Track 2 Parallel Temporal And Non-Temporal Analysis

## Overview

This project will prepare and execute a bounded forward-only
`TE Curve Verification Pipeline` analysis over the complete eligible
`Wave 5.2R` trained-candidate inventory. The comparison will preserve two
parallel development lanes:

- temporal or windowed models, anchored by the accepted periodic GRU;
- non-temporal models, anchored by the accepted periodic harmonic MLP and
  including the Wave 5.2R grey-box H04 candidate.

The analysis will use `polished_dataset`, setpoint inputs, and the forward
surface because that is the frozen Wave 5.2R experimental contract. It will not
infer backward or global performance from forward-only checkpoints.

The phrase "all trained models" will be implemented as an auditable inventory,
not as an assumption that every campaign artifact is a TE predictor. Every
real-data candidate with an immutable checkpoint or prediction artifact, the
frozen `675 / 194 / 97` split, a causal input contract, and a reproducible
full-curve inference path will enter the matrix. Calibration-only wrappers,
diagnostic controls that do not produce a distinct TE curve, and Stage 13
synthetic oracle cases will remain visible in an eligibility appendix but will
not be misrepresented as real-data predictive candidates.

No training is authorized by this document. The heavy matrix will not be
executed during implementation preparation. After approval, Codex will prepare
a repository-owned PowerShell launcher with local and `-Remote` modes, provide
the exact commands, and wait for the user to execute it and report completion.

## Technical Approach

The first deliverable will be a machine-readable Wave 5.2R candidate inventory
reconstructed from the completed campaign manifests, leaderboards, run
metadata, checkpoints, saved prediction payloads, Stage 14 eligibility
evidence, and Stage 15 adapters. The inventory will record:

- stage, campaign, candidate identifier, formulation, and random seed;
- temporal, non-temporal, analytical, calibration-only, or synthetic class;
- checkpoint or immutable prediction source;
- split signature and held-out curve count;
- runtime inputs and causal validity;
- full-curve reconstruction method;
- eligibility decision and any exclusion reason.

Repeated stability seeds will remain separate robustness observations but will
not be silently counted as unrelated model formulations. Exact duplicate
predictions or frozen replays will be identified explicitly. Stage 11 entries
that preserve K01 as the prediction center will be evaluated as trust
diagnostics rather than duplicated K01 predictors. Stage 13 oracle entries will
be reported as synthetic certification evidence only.

The Track 2 matrix will include, at minimum:

- every eligible real-data predictive candidate trained in Wave 5.2R
  Stages 4 through 12;
- H04 and its valid stability seeds;
- K01 and other eligible temporal Stage 9 formulations;
- the frozen PF-A analytical anchor;
- `polished_setpoints_periodic_gru_sequence_Fw` as the accepted windowed
  reference;
- `polished_setpoints_periodic_mlp_harmonic_Fw` as the accepted non-windowed
  reference.

Candidate inference will reuse immutable full-curve payloads only when their
provenance, split, curve ordering, and angular grid exactly match the frozen
contract. Otherwise, the shared Track 2 support code will load the checkpoint
and reconstruct all `97 x 2048` forward test curves. Sequence models must
produce complete causal curves with deterministic hidden-state initialization;
truncated center-window outputs are not acceptable.

The official comparison will follow the canonical multi-index curve-first
policy. Results will be separated into:

- raw MAE, RMSE, mean percentage error, and P95 error;
- mean-centered shape fidelity;
- absolute offset and continuity behavior;
- peak-to-peak and closure behavior;
- harmonic amplitude and phase fidelity;
- derivative and smoothness behavior;
- operating-band and tail robustness;
- causal runtime and deployment readiness.

The decision report will identify category leaders and balanced
recommendations separately for the temporal and non-temporal lanes. It will
also provide a direct lane-to-lane comparison without forcing one model to
replace the other. Scalar campaign rank or scalar MAE alone will not authorize
promotion.

## Involved Components

The evidence inventory will inspect:

- `output/training_campaigns/` Wave 5.2R Stage 4 through Stage 13 packages;
- `output/training_runs/` checkpoints and run metadata referenced by those
  packages;
- `output/analysis/wave_5_2r/` stage closeouts and eligibility evidence;
- the Stage 14 tournament inventory;
- the Stage 15 official matrix, curve diagnostics, and H04 inference adapter;
- the accepted polished-setpoint GRU and periodic harmonic MLP archives.

The implementation is expected to involve:

- a dedicated compact matrix configuration under
  `config/paper_reimplementation/rcim_ml_compensation/`
  `reference_family_vs_feedforward/`;
- shared candidate support only where existing adapters cannot reproduce a
  trained Wave 5.2R formulation;
- a dedicated PowerShell launcher under `scripts/campaigns/track_2/`;
- a matching launcher note under `doc/scripts/campaigns/track_2/`;
- machine-readable inventory and eligibility artifacts under
  `output/analysis/wave_5_2r/`;
- dated matrix, CVP diagnostics, collage, overlay, and official decision
  reports under the canonical TE Curve Verification Pipeline report tree;
- validated PDF companions for the visual and official reports;
- project-status and backlog synchronization after the final decision.

The existing completed Stage 13 active-campaign record is protected but does
not block this work. Its status is `completed`; this project will not modify
its campaign configuration, launcher, model script, or output package.

No subagents are planned. If a specialist review is later proposed, its name,
scope, and reason must be declared to the user and approved before launch.

## Implementation Steps

1. Audit all Wave 5.2R campaign packages and build the complete trained-artifact
   inventory with explicit eligibility and exclusion reasons.
2. Freeze the expected distinct candidate count before changing the Track 2
   matrix.
3. Separate temporal/windowed, non-temporal, analytical, calibration-only, and
   synthetic-oracle lanes.
4. Verify checkpoint existence, split identity, causal inputs, curve ordering,
   angular grids, and full-curve reconstructability for every eligible
   candidate.
5. Extend shared inference support only for candidate kinds that cannot already
   be reconstructed by the Stage 15 or existing archive adapters.
6. Create a dedicated forward-only matrix containing all eligible Wave 5.2R
   candidates, PF-A, the accepted periodic GRU, and the accepted periodic
   harmonic MLP.
7. Add deterministic validation checks for candidate count, duplicate
   prediction detection, full-curve length, finite outputs, and direction
   restrictions.
8. Create and document a PowerShell launcher supporting local execution and
   `-Remote`, without starting the heavy matrix.
9. Run Python compilation, targeted configuration validation, launcher
   preflight, Markdown QA, and `git diff --check`.
10. Provide the exact local and remote commands, then stop until the user
    reports that the heavy analysis has completed.
11. Inspect the generated matrix and CVP diagnostic artifacts, confirming that
    all expected candidates and all 97 forward curves are present.
12. Generate temporal-lane, non-temporal-lane, and cross-lane category
    comparisons plus representative full-curve overlays and collages.
13. Write the official multi-index decision report, keeping raw error, shape,
    offset, harmonics, robustness, and deployment evidence separate.
14. Export and validate the real PDFs, rasterize representative pages, and
    repair any visible layout problem.
15. Synchronize the TE program ledger, training master summary, live backlog,
    relevant report indices, and Sphinx portal scope where required.
16. Run final Python, Markdown, PDF, Sphinx, path, and diff validation, then
    report completion without committing.

Implementation must not begin until the user explicitly approves this
technical document. A Git commit will require a separate explicit approval
after the completed analysis and QA have been reported.
