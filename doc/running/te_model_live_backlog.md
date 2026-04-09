# TE Model Live Backlog

## Program Overview

This file is the canonical operational backlog for the TE model implementation program.

Use this document as the day-to-day source of truth for:

- current execution status;
- completed waves;
- next implementation targets;
- deferred and low-priority branches;
- promotion and comparison decisions.

Historical rationale and approval history remain in:

- `doc/technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
- later TE-related technical notes under `doc/technical/2026-03/2026-03-17/`

## Current Status

- Program State: active
- Current Completed Wave: `Wave 1` structured-baseline familywise optimization pass
- Current Focus: the immediate implementation branch is now the offline
  `Harmonic-Wise Comparison Pipeline`; its job is to establish the paper-
  comparable harmonic baseline before `Wave 2` temporal models are opened
- Current Best Implemented Family: `tree` (`hist_gradient_boosting`)
- Current Best Implemented Run Registry: `output/registries/program/current_best_solution.yaml`
- Current Reference Feedforward Baseline Run:
  - `output/training_runs/feedforward/legacy__te_feedforward_stride5_long_large_batch/metrics_summary.yaml`
  - `output/training_runs/feedforward/legacy__te_feedforward_stride5_long_large_batch/training_test_report.md`
  - `output/registries/families/feedforward/latest_family_best.yaml`
- Wave 0 Verification Artifacts:
  - `output/training_runs/feedforward/2026-03-17-19-49-41__te_feedforward_trial/metrics_summary.yaml`
  - `output/validation_checks/feedforward/2026-03-17-19-49-04__te_feedforward_trial_registry_validation/validation_summary.yaml`
  - `output/smoke_tests/feedforward/2026-03-17-19-49-04__te_feedforward_trial_registry_smoke_test/smoke_test_summary.yaml`

## Completed

### Planning Foundation

- TE family roadmap approved.
- TE analytical family comparison report approved.
- TE implementation backlog approved.
- low-priority `Lightweight Transformer` and `Neural ODE` branches made explicit.
- additional family candidates added explicitly:
  - `State-Space Sequence Model`
  - `Mixture-of-Experts / Regime-Conditioned Model`
  - optional `Kernel Ridge / Gaussian Process` benchmark

### Wave 0

Status:

- completed

Delivered:

- shared training infrastructure in `scripts/training/shared_training_infrastructure.py`
- explicit `experiment.model_family` in feedforward presets
- common artifact names:
  - `training_config.yaml`
  - `metrics_summary.yaml`
- category-specific output roots:
  - `output/training_runs/`
  - `output/validation_checks/`
  - `output/smoke_tests/`
  - `output/registries/`
- reusable one-batch validation entry point:
  - `scripts/training/validate_training_setup.py`
- reusable Lightning smoke-test entry point:
  - `scripts/training/run_training_smoke_test.py`
- feedforward training path updated to consume the shared infrastructure
- documentation updated for the new runnable workflows

Verification:

- one-batch validation completed successfully
- smoke test with checkpoint save/reload completed successfully
- feedforward `trial` run completed successfully with the common metrics schema
- Wave 0 `trial` artifacts are verification-only and are not the canonical program baseline

## In Progress

- planning and implementation handoff from completed static structured
  baselines toward the intermediate paper-aligned harmonic-wise pipeline branch
- post-harmonic-pipeline decision staging for the later `Wave 2` temporal-model
  branch and the deferred TwinCAT deployment-evaluation branch

## Next Up

### Post-Wave 1 Follow-Up

Current next step:

- do not promote the oversized random-forest artifact class produced during the
  remote LAN validation path into future deployment/export candidate sets,
  because the observed `tree_model.pkl` size of roughly `91 GB` is incompatible
  with practical PLC/TwinCAT memory budgets
- use the consolidated `Wave 1` closeout report as the canonical summary when
  comparing future families against the current structured-baseline stage
- use `doc/reports/analysis/RCIM Paper Reference Benchmark.md` as the canonical
  paper-baseline reference while the repository still lacks online
  compensation validation
- treat the paper-aligned harmonic-wise pipeline as the immediate execution
  branch before opening `Wave 2` temporal models
- keep `Wave 2` temporal models planned, but only after the harmonic-wise
  comparison framework is implemented and reviewed

### Paper Alignment Targets

- `Target A`: match or beat the paper on a comparable offline prediction
  benchmark
  - required validation path:
    - reproduce a TE-curve validation protocol comparable to the paper
    - report mean percentage error on unseen scenarios
    - reach `<= 4.7%` mean percentage error
- `Target B`: reproduce the online compensation benchmark
  - required validation path:
    - implement repository-owned online compensation tests
    - run `Robot` and `Cycloidal` style motion-profile validation
    - reach at least `83%` robot TE RMS reduction
    - reach at least `90%` cycloidal TE RMS reduction
    - report uncompensated and compensated TE RMS plus TE max in a Table 9
      style comparison
- until `Target B` is executed, present all paper comparisons as `offline-only`
  rather than end-to-end equivalent

### Paper Pipeline Breakdown

Implement now:

- `Pipeline 1`: harmonic-wise prediction of paper-style `A_k` and `phi_k`
  terms for the selected harmonics across operating conditions
- `Pipeline 2`: TE reconstruction from the predicted harmonic terms so the
  repository can evaluate reconstructed TE curves instead of only direct
  end-to-end regressors
- `Pipeline 3`: offline motion-profile playback for `Robot` and `Cycloidal`
  style profiles using the reconstructed TE path
- `Pipeline 4`: paper-comparable offline validation protocol that reports
  TE-curve percentage-error metrics and closes `Target A`

Implement later in the deferred TestRig / online branch:

- `Pipeline 5`: online compensation loop applied during real motion execution
  inside the future TestRig/TwinCAT integration path
- `Pipeline 6`: uncompensated vs compensated `TE RMS` and `TE max`
  measurement path for the online compensation experiments
- `Pipeline 7`: final `Table 9` style benchmark report that closes `Target B`

Priority note:

- treat `Pipelines 1-4` as the immediate repository branch because they build
  the stable offline baseline required before any online compensation work
- treat this immediate branch as an explicit intermediate stage between
  completed `Wave 1` and the future `Wave 2` temporal-model branch
- treat `Pipelines 5-7` as follow-up work that belongs to the future TestRig /
  online integration branch after the offline baseline is implemented and
  reviewed

### Deferred Post-Wave TwinCAT Deployment Evaluation

Planned execution order after the harmonic-wise branch and the later next wave
are implemented and reviewed:

- formalize a dedicated `TwinCAT deployment evaluation` execution branch in the
  operational workstream
- use [testrig_twincat_ml_reference.md](../reference_codes/testrig_twincat_ml_reference.md)
  as the canonical technical baseline for the imported TestRig PLC path
- keep the legacy Beckhoff path as the main deployment target:
  - `TF38x0`
  - `FB_MllPrediction`
  - `XML/BML`
- open a separate comparison track for the newer Beckhoff server path:
  - `TF3820/TF3830`
  - `FB_MlSvrPrediction`
  - `ONNX + JSON + PlcOpenXml`
- evaluate both branches against repository-authored models instead of relying
  only on historical paper coverage
- compare at least:
  - model acceptance and conversion success
  - artifact workflow complexity
  - runtime behavior and timing suitability
  - maintainability and engineering cost
- include the later online-compensation execution branch for:
  - repository-owned compensation-loop execution
  - uncompensated vs compensated `TE RMS` / `TE max` measurements
  - final `Table 9` style paper benchmark closure
- exclude the oversized random-forest artifact class already observed at
  roughly `91 GB` from future export attempts, unless a later explicitly
  lighter tree variant is produced and re-evaluated as a separate candidate
- use isolated mode for preparatory or parallel experiments whenever campaign-
  sensitive repository areas should remain untouched

Entry conditions:

- the harmonic-wise intermediate branch has been implemented and reviewed;
- and the later next wave has then been implemented and reviewed;
- and the user then explicitly decides whether the TwinCAT branch should be
  activated immediately or deferred again;
- or the user explicitly approves isolated parallel preparation before full
  integration.

## Deferred / Low Priority

### Repository Documentation Publication

- keep the repository private for now
- keep GitHub Pages publication deferred until the repository is intentionally
  made public
- once the repository becomes public, activate the existing Sphinx publication
  workflow through GitHub Pages with `GitHub Actions`
- after activation, record the live documentation URL in the appropriate
  documentation entry points if that public link should be surfaced

Entry rule:

- do not activate this branch while the repository must remain private
- promote it when the user explicitly approves the public-repository transition

### Explicit Low-Priority Exploratory Families

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- optional `Kernel Ridge / Gaussian Process` benchmark

Entry rule:

- these families should not displace the main roadmap unless later evidence justifies them or the user explicitly promotes them.

## Wave Checklist

### Wave 0. Shared Infrastructure

- completed

### Wave 1. Structured Static Baselines

- planning report: completed
- implementation: completed
- smoke-tests: completed
- validation checks: completed
- campaign execution: completed
- results report: completed

### Wave 2. Temporal Models

- planned after the harmonic-wise intermediate branch
- temporal-model scope will start only after the harmonic-wise comparison
  framework is stable and reviewed

### Intermediate Branch. Harmonic-Wise Comparison Pipeline

- current primary implementation branch
- focused scope:
  - implement harmonic-wise prediction of `A_k` and `phi_k`
  - implement TE reconstruction from the predicted harmonic terms
  - add offline `Robot` and `Cycloidal` motion-profile playback
  - define comparable offline validation scenarios and TE-curve error metrics
  - close `Target A`
- initial repository-owned offline pipeline script should live under
  `scripts/training/run_harmonic_wise_comparison_pipeline.py`
- validation artifacts for this branch should live under
  `output/validation_checks/harmonic_wise_comparison/`

### Wave 3. Hybrid Structured Models

- pending
- paper-reproduction scope:
  - compare hybrid structured predictors against the paper-style harmonic stack
  - prepare the repository-owned deployable predictor package

### Wave 4. PINN Formulation And First PINN

- pending
- paper-reproduction scope:
  - implement the repository-side compensation-loop evaluation path in the
    future TestRig / online branch
  - implement uncompensated vs compensated `TE RMS` / `TE max` measurements
  - prepare the final online benchmark harness

### Wave 5. Cross-Wave Comparison And Best Solution

- pending
- paper-reproduction scope:
  - execute Table 9 style online compensation tests
  - evaluate `Target B`
  - finalize the real `paper vs repository` comparison with online results

## Decision Notes

- the live backlog is now the privileged operational view of the TE program
- technical documents remain the historical planning baseline and design rationale
- output artifacts now follow the privileged category-specific structure rather than the old flat family-root convention
- the canonical feedforward reference baseline is the registry-selected best historical run, not the Wave 0 `trial` verification run
- the currently tracked residual-harmonic family optimization belongs to `Wave 1` and its campaign assets have been realigned to the same naming
- the first cross-family `Wave 1` execution had a mixed operational outcome, but the missing branches were recovered and the wave now has campaign-specific reporting plus a consolidated closeout summary
- the remote LAN tree-validation path proved that an oversized random-forest
  artifact class can reach roughly `91 GB`; treat that class as
  deployment-incompatible and exclude it from future TwinCAT/PLC export work
- the TwinCAT deployment-evaluation branch is intentionally deferred until
  after the next wave is implemented and reviewed; re-evaluate that priority
  only after the next wave closes
- best-result visibility should be read from:
  - campaign-level `campaign_best_run.yaml`
  - family-level `latest_family_best.yaml`
  - program-level `current_best_solution.yaml`
- future updates to program status should land here whenever:
  - a wave starts or finishes
  - a model family is promoted or deferred
  - a campaign is approved, started, completed, or cancelled
  - the current best candidate changes
  - a paper-alignment target changes state
  - a TwinCAT deployment branch is promoted, deferred, or selected as the
    preferred deployment path
