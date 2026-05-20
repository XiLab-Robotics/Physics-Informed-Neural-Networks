# TE Model Live Backlog

## Program Overview

This file is the canonical operational backlog for the TE model implementation
program.

Use this document as the day-to-day source of truth for:

- current execution status;
- completed waves and tracks;
- next implementation targets;
- deferred and low-priority branches;
- promotion and comparison decisions.

Historical rationale and approval history remain in:

- `doc/technical/2026-03/2026-03-17/2026-03-17-15-34-08_te_model_family_roadmap.md`
- `doc/technical/2026-03/2026-03-17/2026-03-17-15-57-17_te_model_implementation_backlog.md`
- later TE-related technical notes under `doc/technical/`

## Current Status

- Program State: active.
- Active Campaign State: no protected prepared or active campaign is currently
  registered in `doc/running/active_training_campaign.yaml`.
- Current Completed Wave: `Wave 1` structured-baseline optimization pass,
  closed with `global`, `forward`, and `backward` model surfaces.
- Current Completed Track: `Track 1` RCIM paper-faithful model bank, closed as
  a faithful full-bank reproduction surface for Tables `2`-`5`.
- Current Focus: finish `Track 2` by closing the canonical direction-aware
  offline comparison between recovered original, retuned, `Track 1`, and
  `Wave 1` model surfaces.
- Current Best Implemented Family: `tree` / `hist_gradient_boosting`.
- Current Best Implemented Run Registry:
  `output/registries/program/current_best_solution.yaml`.

Current canonical status reports:

- `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`
- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
- `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`
- `doc/reports/analysis/Training Results Master Summary.md`

## Directional Rule

The repository now treats direction as a first-class evaluation surface.

The default rule for `Track 2`, `Wave 1`, and all future waves is:

| Surface | Training / archive scope | Evaluation scope |
| --- | --- | --- |
| `global` | forward and backward together | both directions, reported separately |
| `Fw` / `forward` | forward only | forward curves only |
| `Bw` / `backward` | backward only | backward curves only |

Exceptions require a new approved technical document. This rule applies whether
the candidate comes from a paper-reference bank, a retuned archive, a
repository-owned neural model, or a future deployable model package.

## Completed

### Planning Foundation

Status:

- completed.

Delivered:

- TE family roadmap approved.
- TE analytical family comparison report approved.
- TE implementation backlog approved.
- low-priority `Lightweight Transformer` and `Neural ODE` branches made
  explicit.
- additional family candidates added explicitly:
  - `State-Space Sequence Model`
  - `Mixture-of-Experts / Regime-Conditioned Model`
  - optional `Kernel Ridge / Gaussian Process` benchmark

### Wave 0 Shared Infrastructure

Status:

- completed.

Delivered:

- shared training infrastructure in
  `scripts/training/shared_training_infrastructure.py`;
- explicit `experiment.model_family` in feedforward presets;
- common artifact names:
  - `training_config.yaml`
  - `metrics_summary.yaml`
- category-specific output roots:
  - `output/training_runs/`
  - `output/validation_checks/`
  - `output/smoke_tests/`
  - `output/registries/`
- reusable one-batch validation entry point:
  `scripts/training/validate_training_setup.py`;
- reusable Lightning smoke-test entry point:
  `scripts/training/run_training_smoke_test.py`;
- feedforward training path updated to consume the shared infrastructure.

Verification:

- one-batch validation completed successfully;
- smoke test with checkpoint save/reload completed successfully;
- feedforward `trial` run completed successfully with the common metrics
  schema;
- Wave 0 `trial` artifacts are verification-only and are not the canonical
  program baseline.

### Recovered Original RCIM Pipeline

Status:

- completed and preserved as provenance evidence.

Delivered:

- recovered original RCIM workflow copied under
  `scripts/paper_reimplementation/rcim_ml_compensation/recovered_original_workflow/`;
- original `v18` forward path and recovered pipeline structure documented in
  `doc/reports/analysis/rcim_paper_reference/RCIM Original Pipeline To Reimplementation Companion.md`;
- code-level audit documented in
  `doc/reports/analysis/rcim_paper_reference/RCIM Original Pipeline And Reimplementation Audit.md`;
- original ONNX release parity interpretation documented in
  `doc/reports/analysis/rcim_paper_reference/RCIM Original ONNX Release Parity Interpretation.md`;
- archive parity across `rcim_original`, `rcim_retuned`, and `rcim_track1`
  documented in
  `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Archive Parity Interpretation.md`.

Operational meaning:

- the recovered workflow is the code-level provenance anchor;
- the copied original workflow is not the active implementation surface;
- current comparisons use curated archives under `models/paper_reference/`.

### Retuned RCIM Reference Archive

Status:

- completed as the current recovered-original retuned baseline.

Delivered:

- retuned forward and backward paper-reference archives promoted under
  `models/paper_reference/rcim_retuned/`;
- retuned family-direction archive count: `22`;
- retuned closeout report:
  `doc/reports/analysis/rcim_paper_reference/rcim_retuned_reference_closeout/[2026-05-13]/rcim_retuned_reference_closeout_report.md`;
- retuned values integrated into the canonical RCIM Tables `2`-`5` benchmark
  and Track 2 comparison matrix.

Operational meaning:

- forward `Track 1` cells compare against the better value between paper
  original and paper retuned;
- backward `Track 1` cells compare against paper retuned, because the paper
  does not provide backward original tables.

### Track 1 RCIM Paper-Faithful Model Bank

Status:

- closed.

Delivered:

- faithful original-dataset exact-model-bank implementation under
  `scripts/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/`;
- completed forward paper-faithful grid-search campaign across
  `SVR`, `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `LGBM`, `XGBM`, and
  `ELM`;
- completed backward paper-faithful grid-search campaign across the same
  operational family bank;
- accepted forward archives refreshed under
  `models/paper_reference/rcim_track1/forward/`;
- accepted backward archives refreshed under
  `models/paper_reference/rcim_track1/backward/`;
- Tables `2`-`5` repopulated in
  `doc/reports/analysis/rcim_paper_reference/RCIM Paper Reference Benchmark.md`;
- Windows PowerShell and Linux Bash launcher surfaces documented for future
  reruns.

Closure rule:

- `Track 1` is closed because the faithful full-bank protocol was run in both
  directions and all benchmark cells were repopulated.
- Green-only status is not a `Track 1` closure requirement.
- Any all-green pursuit, restricted-dataset rerun, or target-parameterization
  search is a new optimization branch, not a reopening of closed `Track 1`.

Artifact rule:

- intermediate validation-model `.pkl` bundles under
  `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/`
  and
  `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`
  stay out of Git tracking and Git LFS;
- only curated accepted archives under `models/paper_reference/rcim_track1/`
  are the `Track 1` paper-reference model surface.

### Wave 1 Structured Static Baselines

Status:

- closed.

Delivered:

- completed `global`, `forward`, and `backward` surfaces for the implemented
  repository model families;
- completed directional best-hyperparameter search campaign;
- refreshed exported model surfaces under `models/exported/`;
- consolidated closeout report:
  `doc/reports/analysis/wave1/Wave 1 - Closeout Status.md`.

Current HPO leader:

- run: `te_hist_gbr_tabular_Fw_grid_depth6_lr008_leaf10`;
- family: `tree_fw`;
- scope: `forward`;
- test MAE: `0.002743 deg`.

Operational meaning:

- `Wave 1` is the closed structured-baseline stage for future model-family
  comparisons;
- future waves must either produce `global`, `forward`, and `backward` surfaces
  or explicitly justify why one of those surfaces is omitted;
- the oversized random-forest artifact class observed near `91 GB` remains
  deployment-incompatible and must not be promoted into future TwinCAT/PLC
  export candidate sets.

## In Progress

### Track 2 Directional Offline Comparison

Status:

- active closeout branch.

Canonical report:

- `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`

Current comparison surface:

- comparison mode: `full_directional_candidate_matrix`;
- candidate count: `75`;
- held-out curve count before candidate filtering: `194`;
- denominator for percentage error: `peak_to_peak_truth`;
- `Fw` candidates evaluate only on forward curves;
- `Bw` candidates evaluate only on backward curves;
- `global` candidates evaluate on both directions with separated metrics.

Candidate groups:

- accepted `Track 1` forward and backward family banks;
- recovered original forward family banks;
- retuned forward and backward family banks;
- `Wave 1` exported `global`, `forward`, and `backward` models;
- composed best-reference candidates for paper original, paper retuned, and
  `Track 1`.

Current Track 2 leaders by source:

| Direction | Source | Candidate | Mean percentage error [%] |
| --- | --- | --- | ---: |
| forward | paper original | `paper_original_best_Fw` | 6.250 |
| forward | paper retuned | `paper_retuned_best_Fw` | 4.109 |
| forward | Track 1 | `track1_best_Fw` | 6.819 |
| backward | paper retuned | `paper_retuned_best_Bw` | 7.572 |
| backward | Track 1 | `track1_best_Bw` | 11.860 |

Backward baseline rule:

- the paper does not provide a paper-original backward reference surface;
- `paper_retuned_best_Bw` is therefore the canonical paper-derived backward
  baseline for `Track 2` and `Target A`;
- future backward comparisons should report against this retuned baseline
  unless a later approved technical document defines a stronger backward paper
  proxy.

Best individual family candidates currently visible in Track 2:

| Direction | Candidate | Mean percentage error [%] |
| --- | --- | ---: |
| forward | `rcim_retuned_GBM19_Fw` | 2.372 |
| backward | `rcim_retuned_GBM19_Bw` | 5.398 |

Remaining closeout work:

- confirm the final Track 2 report wording after grouped source-table,
  composite-best visibility, and backward retuned-baseline fixes;
- keep the direction/truth and preview-curve audit notes attached to the final
  report package;
- decide whether Track 2 is closed as the canonical offline comparison matrix
  or whether one more explicitly approved comparison refinement is needed.

## Next Up

### Planned Next Step

After this cleaning and alignment, the next planned step is:

- close `Track 2` as the canonical direction-aware offline comparison report,
  using `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`
  as the source of truth.

The closeout should answer three concrete questions:

- which source surface is the current best offline reference for forward
  curves;
- confirm that `paper_retuned_best_Bw` is the canonical backward baseline
  because no paper-original backward reference exists;
- whether the next implementation branch should be `Wave 2` temporal models or
  another explicitly approved branch. `Target A` is no longer a blocking bridge
  because it is closed as an offline direction-qualified benchmark.

### Post-Track-2 Decision

Default decision path after Track 2 closeout:

- open `Wave 2` temporal models only after the Track 2 report is accepted as
  closed;
- keep the same `global`, `forward`, and `backward` surface rule for Wave 2;
- use `Wave 1` and Track 2 as the comparison baseline for every Wave 2 family;
- keep paper-alignment bridge work available only if the user explicitly
  reopens a narrower offline paper-alignment question before temporal-model
  exploration.

### Paper Alignment Targets

`Target A`: match or beat the paper on a comparable offline prediction
benchmark.

Status:

- closed as `closed_offline_direction_qualified`.
- closeout source of truth:
  `doc/reports/analysis/track2/Track 2 Directional Model Comparison.md`.

Required validation path:

- reproduce a TE-curve validation protocol comparable to the paper;
- report mean percentage error on unseen scenarios;
- reach `<= 4.7%` mean percentage error for the paper-comparable forward
  surface;
- use `paper_retuned_best_Bw` as the canonical paper-derived backward baseline,
  because the paper provides no paper-original backward reference surface.

Current offline evidence:

- paper retuned forward best composite is below the `4.7%` threshold at
  `4.109%`;
- paper retuned backward best composite is the accepted backward baseline at
  `7.572%`;
- retuned individual `GBM` forward and backward candidates are currently the
  strongest Track 2 offline family references;
- `Track 1` remains closed as faithful reproduction evidence, not as the
  optimized winner.

Closeout verdict:

- forward `Target A` is met against the paper-comparable `4.7%` offline
  threshold;
- backward `Target A` is closed against the approved retuned backward baseline;
- no additional offline paper-alignment bridge is required before opening the
  next modeling branch;
- online compensation remains outside `Target A` and is tracked under
  `Target B`.

`Target B`: reproduce the online compensation benchmark.

Required validation path:

- implement repository-owned online compensation tests;
- run `Robot` and `Cycloidal` style motion-profile validation;
- reach at least `83%` robot TE RMS reduction;
- reach at least `90%` cycloidal TE RMS reduction;
- report uncompensated and compensated TE RMS plus TE max in a Table 9 style
  comparison.

Until `Target B` is executed, present all paper comparisons as `offline-only`
rather than end-to-end equivalent.

## Deferred Branches

### Paper-Alignment Bridge

Status:

- deferred until Track 2 is closed or explicitly promoted.

Scope if promoted:

- harmonic-wise prediction of paper-style `A_k` and `phi_k` terms;
- TE reconstruction from predicted harmonic terms;
- offline motion-profile playback for `Robot` and `Cycloidal` style profiles;
- paper-comparable offline validation protocol that reports TE-curve
  percentage-error metrics and closes or rejects `Target A`.

Candidate script root:

- `scripts/paper_reimplementation/rcim_ml_compensation/harmonic_wise_comparison/`

Candidate artifact root:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/`

### Track 1 Restricted-Dataset Future Rerun

Status:

- deferred until much later.

Entry rule:

- do not use this branch to overwrite the closed full-dataset `Track 1` status;
- create new campaign names, output roots, archive namespaces, and comparison
  reports for every restricted-dataset level.

Required scope if promoted:

- rerun the closed `Track 1` paper-faithful model-bank protocol on one or more
  restricted dataset variants;
- keep the current full-dataset `Track 1` archive and benchmark as immutable
  comparison anchors;
- revisit the recovered-workflow pickle cache contract so restricted-dataset
  experiments use explicit cache partitioning;
- create a new Markdown comparison report that places full-dataset and
  restricted-dataset Tables `2`-`5` side by side.

### TwinCAT Deployment Evaluation

Status:

- deferred until after Track 2 closeout and the next approved modeling branch.

Planned scope:

- formalize a dedicated `TwinCAT deployment evaluation` execution branch;
- use `doc/reference_codes/testrig_twincat_ml_reference.md` as the canonical
  technical baseline for the imported TestRig PLC path;
- keep the legacy Beckhoff path in scope:
  - `TF38x0`
  - `FB_MllPrediction`
  - `XML/BML`
- compare the newer Beckhoff server path:
  - `TF3820` / `TF3830`
  - `FB_MlSvrPrediction`
  - `ONNX + JSON + PlcOpenXml`
- evaluate model acceptance, conversion success, workflow complexity, runtime
  behavior, maintainability, and engineering cost;
- exclude the already observed oversized random-forest artifact class unless a
  later explicitly lighter tree variant is produced.

### Repository Documentation Publication

Status:

- deferred.

Entry rule:

- keep the repository private for now;
- do not activate GitHub Pages publication until the repository is intentionally
  made public;
- after public activation, record the live documentation URL in the appropriate
  documentation entry points.

### Explicit Low-Priority Exploratory Families

Status:

- low priority.

Families:

- `Lightweight Transformer`
- `State-Space Sequence Model`
- `Neural ODE`
- `Hamiltonian-Inspired Model`
- optional `Kernel Ridge / Gaussian Process` benchmark

Entry rule:

- these families should not displace the main roadmap unless later evidence
  justifies them or the user explicitly promotes them.

## Wave Checklist

### Wave 0. Shared Infrastructure

- completed.

### Wave 1. Structured Static Baselines

- planning report: completed;
- implementation: completed;
- smoke tests: completed;
- validation checks: completed;
- campaign execution: completed;
- directional HPO closeout: completed;
- exported `global`, `forward`, and `backward` surfaces: completed;
- results report: completed;
- status: closed.

### Track 1. RCIM Paper-Faithful Model Bank

- recovered original workflow: preserved;
- original-dataset reimplementation: completed;
- retuned reference archive: completed;
- forward campaign: completed;
- backward campaign: completed;
- paper-reference archives: refreshed;
- Tables `2`-`5`: repopulated;
- status: closed as faithful full-bank reproduction, not all-green
  optimization.

### Track 2. Directional Offline Comparison

- direction-aware loader and candidate matrix: completed;
- recovered original forward candidates: included;
- retuned forward and backward candidates: included;
- `Track 1` forward and backward candidates: included;
- `Wave 1` `global`, `forward`, and `backward` exports: included;
- grouped source tables: completed;
- composite best-reference visibility: completed;
- direction/truth and preview audit: completed;
- status: active closeout branch.

### Wave 2. Temporal Models

- status: planned after Track 2 closeout;
- mandatory rule: prepare or justify `global`, `forward`, and `backward`
  surfaces;
- baseline comparison: Track 2 plus closed Wave 1.

### Wave 3. Hybrid Structured Models

- status: pending;
- mandatory rule: prepare or justify `global`, `forward`, and `backward`
  surfaces;
- paper-reproduction scope:
  - compare hybrid structured predictors against the paper-style harmonic stack;
  - prepare the repository-owned deployable predictor package.

### Wave 4. PINN Formulation And First PINN

- status: pending;
- mandatory rule: prepare or justify `global`, `forward`, and `backward`
  surfaces;
- paper-reproduction scope:
  - implement the repository-side compensation-loop evaluation path in the
    future TestRig / online branch;
  - implement uncompensated vs compensated `TE RMS` / `TE max` measurements;
  - prepare the final online benchmark harness.

### Wave 5. Cross-Wave Comparison And Best Solution

- status: pending;
- mandatory rule: preserve direction-separated reporting;
- paper-reproduction scope:
  - execute Table 9 style online compensation tests;
  - evaluate `Target B`;
  - finalize the real `paper vs repository` comparison with online results.

## Decision Notes

- the live backlog is the privileged operational view of the TE program;
- technical documents remain the historical planning baseline and design
  rationale;
- output artifacts follow the privileged category-specific structure rather
  than the old flat family-root convention;
- best-result visibility should be read from campaign-level
  `campaign_best_run.yaml`, family-level `latest_family_best.yaml`, and
  program-level `current_best_solution.yaml`;
- the recovered original workflow is provenance evidence, while curated
  `models/paper_reference/` archives are the active comparison surface;
- `Track 1` is closed under the revised closure rule and should not be reopened
  for all-green optimization;
- `Track 2` is the active branch to finish before opening Wave 2;
- future wave planning must keep direction-separated modeling and reporting in
  scope from the start;
- the TwinCAT deployment-evaluation branch remains deferred until the next
  approved modeling branch has been closed or the user explicitly promotes it;
- future updates to program status should land here whenever:
  - a wave starts or finishes;
  - a model family is promoted or deferred;
  - a campaign is approved, started, completed, or cancelled;
  - the current best candidate changes;
  - a paper-alignment target changes state;
  - a TwinCAT deployment branch is promoted, deferred, or selected as the
    preferred deployment path.
