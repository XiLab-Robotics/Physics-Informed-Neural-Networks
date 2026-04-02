# Comparative Training Campaign For Feedforward Variants

## Overview

The user requested execution of the main feedforward training configurations proposed in the recent training-configuration analysis report.

The goal is to run a comparative training campaign on the current workstation-oriented variants, keeping the workflow consistent across experiments and collecting the resulting metrics in a form suitable for later comparison.

The proof-run `trial` configuration has already been executed and documented. The pending configurations to run are therefore:

- `baseline`
  `config/feedforward_network_training.yaml`
- `high_density`
  `config/feedforward_network_training_high_density.yaml`
- `high_epoch`
  `config/feedforward_network_training_high_epoch.yaml`
- `high_compute`
  `config/feedforward_network_training_high_compute.yaml`

## Technical Approach

This task should be treated as an experiment-execution and reporting workflow, not as a modeling redesign.

The campaign should:

1. run the four selected configurations through the same training entry point:
   - `training/train_feedforward_network.py`
2. preserve the current file-level train/validation/test split so the runs remain comparable;
3. collect the same artifacts for each run:
   - config snapshot
   - best checkpoint
   - validation metrics
   - held-out test metrics
   - generated run report
4. summarize the final comparison in a single project-authored document after the runs complete.

The execution order should be:

1. `baseline`
2. `high_density`
3. `high_epoch`
4. `high_compute`

This order is technically reasonable because:

- `baseline` establishes the main non-trial reference first;
- `high_density` tests whether denser data sampling improves the result before model capacity is changed;
- `high_epoch` tests whether longer optimization alone improves the baseline;
- `high_compute` is the most expensive run and should be attempted after the lighter workstation variants have already produced usable references.

The comparison report after execution should at minimum record:

- run name;
- configuration file;
- point sampling settings;
- model hidden-layer settings;
- epoch budget and patience;
- best checkpoint path;
- validation MAE/RMSE;
- test MAE/RMSE;
- qualitative notes on runtime cost and apparent stability.

Because these runs can be long, the implementation should avoid changing the training code unless a concrete runtime blocker appears during execution.

## Involved Components

- `README.md`
  Main project document that must reference this technical document.
- `doc/README.md`
  Internal documentation index for technical documents.
- `doc/reports/analysis/2026-03-12-13-38-17_training_configuration_analysis_report.md`
  Existing report that defines the rationale behind the selected configurations.
- `doc/technical/2026-03/2026-03-12/2026-03-12-13-55-11_comparative_training_campaign_for_feedforward_variants.md`
  This technical execution-planning document.
- `config/feedforward_network_training.yaml`
  Current baseline configuration to execute.
- `config/feedforward_network_training_high_density.yaml`
  Denser sampling configuration to execute.
- `config/feedforward_network_training_high_epoch.yaml`
  Longer optimization configuration to execute.
- `config/feedforward_network_training_high_compute.yaml`
  Most aggressive workstation-oriented configuration to execute.
- `training/train_feedforward_network.py`
  Single training entry point used for all runs.
- `output/training_runs/feedforward/`
  Artifact root where the four new experiment outputs will be generated.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, execute the four pending configurations in the planned order:
   - baseline
   - high_density
   - high_epoch
   - high_compute
3. For each run, confirm that the expected artifacts are generated:
   - checkpoint files
   - `best_checkpoint_path.txt`
   - `training_test_metrics.yaml`
   - `training_test_report.md`
4. Collect the final validation and test metrics from all completed runs.
5. Write a comparison report that includes the already executed `trial` run as historical reference and the four newly executed runs as the main comparison set.
6. Update `doc/guide/project_usage_guide.md` only if the approved work changes the documented runnable workflow beyond adding executed results.
7. Create the required Git commit immediately after the approved run summary documentation is completed.
