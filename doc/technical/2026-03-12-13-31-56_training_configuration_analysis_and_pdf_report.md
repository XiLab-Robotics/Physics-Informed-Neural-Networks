# Training Configuration Analysis And PDF Report

## Overview

The user requested a new documentation deliverable focused on the training configuration choices used in the current feedforward baseline work.

The requested output is broader than the existing analytical report. It should explain, in detail:

- what each relevant training configuration field means;
- what each field does in the current implementation;
- what effect each field has on training behavior and on the resulting metrics;
- how the executed proof configuration differs from the current baseline configuration;
- which more aggressive training configurations should be tested on the available high-performance workstation;
- a comparative table covering the proof run, the baseline configuration, and additional heavier candidate configurations;
- a final PDF document suitable for reading or sharing.

This is not only a formatting task. It requires a technically correct interpretation of the repository configuration, datamodule behavior, model architecture, and current run artifacts.

## Technical Approach

The work should be documentation-first and should not change the training code unless local report generation requires a narrow utility addition.

The planned deliverable should have two layers:

1. a canonical project-authored Markdown report stored inside `doc/reports/`;
2. a PDF export derived from that report.

The report content should be organized in this order:

1. explain each relevant configuration group and field:
   - dataset loading and sampling parameters;
   - model architecture parameters;
   - optimization and early-stopping parameters;
   - output/logging parameters;
2. explain what each field changes in practice:
   - runtime cost;
   - memory pressure;
   - information density seen by the model;
   - convergence stability;
   - overfitting or underfitting risk;
3. compare the current proof run against the current baseline configuration;
4. propose `2-3` more ambitious configurations designed for a powerful workstation, with explicit rationale for:
   - more epochs;
   - denser point sampling;
   - larger curve batches or higher worker usage where appropriate;
   - potentially larger hidden layers or heavier model variants if justified;
5. summarize all configurations in a compact comparison table;
6. conclude with a practical recommendation for the next effective training campaign.

Because the user explicitly asked for a PDF, the report should be exported to PDF after the Markdown source is finalized.

Current local inspection shows that:

- `pandoc` is not available on the current machine path;
- `wkhtmltopdf` is not available on the current machine path.

This means the implementation should first create the Markdown source of truth, then use one of the following approved paths:

- a locally available Python-based PDF generation path if already supported by installed packages;
- a lightweight repository-local export utility added only if necessary;
- another local conversion path discoverable in the environment.

If no viable local PDF tool is available without adding dependencies, the report implementation should state that clearly and either:

- produce the Markdown report plus an HTML intermediary;
- or request the minimal approved dependency/tool addition needed for PDF export.

The configuration comparison section should include at least these variants:

- `trial`
  Current lightweight proof configuration already executed.
- `baseline`
  Current default baseline configuration in the repository.
- `high_density`
  More aggressive data sampling than the baseline.
- `high_epoch`
  Longer optimization schedule than the baseline.
- `high_compute`
  A workstation-oriented configuration combining denser data usage and longer training.

The exact parameter values should be chosen after reviewing the current datamodule behavior, dataset split sizes, and model cost so that the recommendations remain realistic rather than arbitrary.

## Involved Components

- `README.md`
  Main project document that must reference this technical document and, after approval, the final report artifact.
- `doc/README.md`
  Internal documentation index that must be updated for the new report.
- `doc/reports/2026-03-12-13-18-30_feedforward_trial_analytical_report.md`
  Existing analytical report that should be reused and extended rather than duplicated conceptually.
- `doc/technical/2026-03-12-13-31-56_training_configuration_analysis_and_pdf_report.md`
  This technical planning document.
- `config/feedforward_network_training_trial.yaml`
  Executed proof-run configuration.
- `config/feedforward_network_training.yaml`
  Current repository baseline configuration.
- `config/dataset_processing.yaml`
  Dataset split and data-root configuration used by the training workflows.
- `models/feedforward_network.py`
  Feedforward architecture definition whose parameters must be explained in the report.
- `models/model_factory.py`
  Model-selection layer for the current baseline architecture.
- `training/transmission_error_datamodule.py`
  DataModule where curve batching, point sampling, and normalization behavior are implemented.
- `training/transmission_error_regression_module.py`
  Lightning regression logic for normalization, loss, and metric computation.
- `training/train_feedforward_network.py`
  Main training entry point whose workflow and artifact generation behavior must be described.
- `output/feedforward_network/te_feedforward_trial/`
  Existing proof-run artifacts that should be cited in the report.

## Implementation Steps

1. Create this technical document and register it in the documentation indexes.
2. After user approval, inspect the current training configs, datamodule sampling logic, and model architecture in detail.
3. Write a new report in `doc/reports/` that explains each relevant configuration field one by one, including meaning, implementation role, and expected effect on training/results.
4. Add a comparative section covering:
   - the executed proof configuration;
   - the current baseline configuration;
   - `2-3` new heavier candidate configurations for a powerful workstation.
5. Define realistic heavier configurations with explicit rationale for batch size, point density, epochs, worker count, and possibly model width.
6. Add a final recommendation section that distinguishes:
   - what is appropriate for a quick verification run;
   - what is appropriate for a serious baseline benchmark;
   - what is appropriate for workstation-scale experimentation.
7. Export the final report to PDF using a viable local conversion path if available, otherwise document the exact export limitation and the fallback artifact produced.
8. Update the documentation indexes so the new report and PDF artifact are discoverable.
9. Create the required Git commit immediately after the approved documentation update is completed.
