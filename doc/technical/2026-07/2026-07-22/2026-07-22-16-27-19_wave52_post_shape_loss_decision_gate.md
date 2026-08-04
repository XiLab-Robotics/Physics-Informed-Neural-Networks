# Wave 5.2 Post-Shape-Loss Decision Gate

> Supersession note, `2026-08-04`: dirty-to-clean `Wave 5.2C` references in
> this historical plan are within-machine paired-dataset work, not the
> canonical Cross-Machine Backbone Adaptation future extension.

## Overview

This technical document defines the next step after the completed
shape-first training-rule distillation pilot and bounded Track 2 screen.

The latest evidence shows that directly turning `TE Curve Verification
Pipeline` shape-limit rules into training pressure did not beat the accepted
polished-setpoint forward baselines. The next step should therefore avoid a new
threshold-shaped loss and instead reopen the physics-informed `Wave 5.2`
decision path as a bounded design gate.

The purpose is to decide which branch is worth implementing next:

- a leakage-safe causal offset / mean calibration branch over the accepted
  `periodic_gru_sequence` path;
- a refreshed `Wave 5.2B` offset and harmonic guided branch only if it can
  target the observed raw-error, offset, harmonic-amplitude, and robustness
  regressions;
- a `Wave 5.2C` weak physics or within-machine dirty-to-clean branch only if
  the existing
  paired-dataset evidence justifies it;
- no new training branch, if the evidence says the next useful work is a
  narrower diagnostic.

This step is a design and evidence-integration gate, not a training campaign.
No subagent is planned. If review help becomes useful, the proposed subagent
name, reason, and delegated scope will be declared before asking for approval.

## Technical Approach

The gate will read the current repository evidence and produce a small
decision report. It will not create model classes, training YAML files, or
campaign launchers.

The decision report must compare three evidence groups:

1. Recent shape-loss evidence:
   the first shape-gate loss pilot, shape-gate loss v2, shape-objective pilot,
   and shape-first distillation pilot, including their bounded Track 2
   outcomes.
2. Existing `Wave 5.2A` / `Wave 5.2B` evidence:
   paired-dataset diagnostics, MMT parameter inventory, offset-and-harmonic
   guided training outcomes, and prior Track 2 decisions.
3. Accepted baseline evidence:
   `polished_setpoints_periodic_gru_sequence_Fw`,
   `polished_setpoints_periodic_mlp_harmonic_Fw`, and the current reduced
   active model set.

The report should make one concrete recommendation:

- implement a causal offset / mean calibration pilot;
- implement a revised `Wave 5.2B` feature or auxiliary-head pilot;
- implement a weak `Wave 5.2C` soft-constraint pilot;
- defer training and run a narrower diagnostic first.

The recommendation must preserve the standing project rule that both
time-windowed and non-windowed roads remain visible until curve-first evidence
separates them.

## Involved Components

Expected read-only inputs:

- `doc/running/active_training_campaign.yaml`;
- `doc/running/te_model_live_backlog.md`;
- `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`;
- `doc/reports/analysis/project_status/current/Training Results Master Summary.md`;
- `doc/reports/analysis/model_development_waves/wave_5_2/paired_dataset_diagnostics/`;
- `output/validation_checks/wave52a_paired_dataset_diagnostics/`;
- `doc/reports/analysis/model_development_waves/wave_5_2/model_design_gate/`;
- `output/validation_checks/wave52_model_design_gate/`;
- `scripts/reports/analysis/build_wave52a_paired_dataset_diagnostics.py`;
- `scripts/models/wave52b_offset_harmonic_guided_network.py`;
- recent bounded Track 2 reports and reranker artifacts for shape-gate,
  shape-objective, and shape-first distillation pilots.

Expected outputs after approval:

- a dated decision report under
  `doc/reports/analysis/model_development_waves/wave_5_2/post_shape_loss_decision_gate/[2026-07-22]/`;
- optional compact machine-readable summary under
  `output/validation_checks/wave52_post_shape_loss_decision_gate/`;
- synchronized entries in `doc/README.md`,
  `doc/running/te_model_live_backlog.md`,
  `doc/reports/analysis/project_status/current/TE Program Status And Closeout Ledger.md`,
  and `doc/reports/analysis/project_status/current/Training Results Master Summary.md`.

Deferred components:

- new model implementation files;
- new training campaign YAML files;
- new PowerShell training launchers;
- registry promotion;
- heavy `TE Curve Verification Pipeline` refreshes.

If the decision report recommends a training pilot, that future step must
create a separate campaign planning report and receive explicit approval before
any training is executed.

## Implementation Steps

1. Inspect the completed shape-gate, shape-objective, and shape-first
   distillation Track 2 screens and extract the common failure modes.
2. Inspect the existing `Wave 5.2A` paired dataset diagnostics and `Wave 5.2B`
   offset / harmonic guided evidence.
3. Compare the failure modes against the accepted polished-setpoint baselines,
   keeping time-windowed and non-windowed candidates separate.
4. Draft the post-shape-loss decision report with one recommended next branch
   and explicit rejection criteria for the alternatives.
5. If the recommendation is a training pilot, stop after the report and prepare
   a separate campaign plan only after explicit approval.
6. Update the backlog, ledger, master summary, and documentation index with the
   decision report path and selected next branch.
7. Run Markdown QA on all touched authored Markdown files.
