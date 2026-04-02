# Wave 1 Structured Baseline Campaign Preparation

## Overview

Wave 1 is the next planned execution step of the TE model program.

Its purpose is to move from the already validated feedforward infrastructure toward the first broader family comparison across structured non-PINN baselines.

The selected Wave 1 scope is:

- harmonic regression baseline;
- periodic-feature feedforward MLP;
- residual MLP over a structured harmonic baseline;
- tree-based tabular benchmark.

Before any implementation or campaign execution, the repository needs a preparation layer that:

- fixes the comparison baseline;
- defines the first campaign scope;
- identifies the required implementation gates;
- states which candidate configurations should enter the exploratory campaign first.

## Technical Approach

Wave 1 should be split into two stages.

### Stage 1. Implementation And Verification Gate

Each selected family must first produce:

- implementation;
- one-batch validation;
- smoke-test;
- canonical `training_config.yaml` and `metrics_summary.yaml` artifacts where applicable.

No family should enter campaign execution before passing this gate.

### Stage 2. Exploratory Structured-Baseline Campaign

After the verification gate, the first Wave 1 campaign should compare a compact but informative candidate matrix across the four families.

The campaign should use the already formalized feedforward best historical run as the comparison anchor:

- `output/training_runs/feedforward/legacy__te_feedforward_stride5_long_large_batch/metrics_summary.yaml`
- `output/registries/families/feedforward/latest_family_best.yaml`
- `output/registries/program/current_best_solution.yaml`

This avoids wasting time on an unnecessary feedforward rerun before there is a real challenger.

The first Wave 1 campaign should be exploratory rather than exhaustive. The goal is to identify:

- whether structured periodic bias gives clear gains;
- whether residual decomposition improves accuracy/interpretability together;
- whether tree-based tabular models are strong enough to remain in scope beyond benchmarking;
- which family deserves a refined second-stage search.

## Involved Components

- `doc/running/te_model_live_backlog.md`
- `doc/running/active_training_campaign.yaml`
- `doc/reports/campaign_plans/`
- `scripts/models/`
- `scripts/training/`
- `config/training/`
- `scripts/models/model_factory.py`
- `output/registries/families/feedforward/latest_family_best.yaml`
- `output/registries/program/current_best_solution.yaml`

## Implementation Steps

1. Create the Wave 1 campaign planning report with the baseline reference, parameter rationale, and candidate configuration table.
2. Wait for user approval before implementing the new model families or generating campaign YAML files.
3. After approval, implement the four structured-baseline families and their validation/smoke-test paths.
4. Generate the campaign YAML files for the approved exploratory matrix and store the prepared campaign state in `doc/running/active_training_campaign.yaml`.
5. Provide the exact launch command for the campaign runner.
6. Execute the campaign only after the generated campaign package is explicitly approved.
