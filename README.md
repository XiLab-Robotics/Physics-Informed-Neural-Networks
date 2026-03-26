# StandardML - Codex

Machine-learning workflows for rotational transmission error modeling in RV
reducers, with a repository structure aimed at reproducible experiments,
engineering-oriented documentation, and future physics-informed extensions.

## Overview

This repository studies **rotational transmission error (TE)** in RV reducers
used in industrial robotics.

The project combines:

- experimental TE datasets from a dedicated test rig;
- structured machine-learning baselines implemented in Python;
- reproducible training, validation, and campaign workflows;
- documentation aimed at both engineering use and future model extension;
- a roadmap toward more structured hybrid models and later full PINN work.

The repository name still reflects the long-term physics-informed direction, but
the current implemented surface already includes practical feedforward,
harmonic, periodic-feature, residual-harmonic, and tree-based baselines.

## Why This Repository Exists

Transmission error is a key indicator for reducer accuracy, vibration behavior,
and final robot joint positioning quality.

In this project, the goal is not only to fit data well. The goal is to build TE
models that are:

- accurate on measured operating conditions;
- interpretable enough for engineering analysis;
- structured enough to support future TwinCAT / PLC-friendly deployment;
- extensible toward hybrid and later physics-informed formulations.

## Current Status

Implemented today:

- validated TE dataset processing and visualization utilities;
- feedforward TE regression training with PyTorch Lightning;
- structured baselines for harmonic regression, periodic-feature MLP, and
  residual-harmonic MLP workflows;
- tree-based baselines for comparison;
- one-batch validation checks and smoke-test utilities;
- batch campaign execution and artifact tracking;
- styled report generation and PDF validation tooling;
- dual `NotebookLM` source-package tracks for guide-local concept videos and
  repository-specific project videos;
- repository-owned isolated-mode and Markdown validation tooling.

Planned or future work:

- broader sequence-aware models such as lagged-window, GRU, LSTM, and TCN
  families;
- additional hybrid TE model families;
- export and deployment hardening for production-oriented inference;
- full PINN formulation once the physics residual design is mature enough.

## Repository At A Glance

The most important folders for a new user are:

- `scripts/`
  Python entry points for training, reporting, and tooling.
- `config/`
  YAML configuration files for datasets, presets, and campaigns.
- `data/datasets/`
  Expected location for validated TE data.
- `output/`
  Training runs, validation checks, smoke tests, campaigns, and registries.
- `doc/`
  Main human-authored documentation, guides, reports, and technical notes.
- `reference/`
  External reference material and imported codebases kept outside the main
  canonical workflow.

If you only want to get started, begin with:

- [Project Usage Guide](./doc/guide/project_usage_guide.md)
- [Documentation Index](./doc/README.md)

## Quick Start

### 1. Create The Environment

```powershell
conda create -y -n standard_ml_codex_env python=3.12
conda activate standard_ml_codex_env
python -m pip install --upgrade pip
python -m pip install torch --index-url https://download.pytorch.org/whl/cu130
python -m pip install -r requirements.txt
```

### 2. Check The Dataset Root

The default dataset location is configured in
`config/datasets/transmission_error_dataset.yaml`:

```yaml
paths:
  dataset_root: data/datasets
```

Update that path if your validated TE dataset is stored elsewhere.

### 3. Run A First Training Command

For a lightweight verification run:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/trial.yaml
```

For the default feedforward baseline:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py
```

Artifacts are written under:

- `output/training_runs/<model_family>/<run_instance_id>/`

## Example Workflows

### Run The Current Best Feedforward Preset

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/best_training.yaml
```

### Launch A Prepared Campaign

```powershell
python scripts/training/run_training_campaign.py
```

### Use The Short Wave 1 Recovery Launcher

```powershell
.\scripts\campaigns\run_wave1_structured_baseline_recovery_campaign.ps1
```

### Check Markdown Quality For Repository Docs

```powershell
python -B scripts/tooling/run_markdownlint.py
python -B scripts/tooling/markdown_style_check.py --fail-on-warning
```

## Documentation For New Users

If you are opening the repository for the first time, use this reading order:

1. [Project Usage Guide](./doc/guide/project_usage_guide.md)
   Main runnable-workflow reference.
2. [Documentation Index](./doc/README.md)
   Entry point for guides, reports, and technical notes.
3. Model guides under `doc/guide/`
   Best place to understand the implemented model families at a conceptual
   level.
4. Analysis reports under `doc/reports/analysis/`
   Useful when you want deeper training or model-family interpretation.

Recommended guide entry points:

- [Neural Network Foundations](./doc/guide/Neural%20Network%20Foundations/Neural%20Network%20Foundations.md)
- [Training, Validation, And Testing](./doc/guide/Training,%20Validation,%20And%20Testing/Training,%20Validation,%20And%20Testing.md)
- [TE Model Curriculum](./doc/guide/TE%20Model%20Curriculum/TE%20Model%20Curriculum.md)
- [FeedForward Network](./doc/guide/FeedForward%20Network/FeedForward%20Network.md)
- [Harmonic Regression](./doc/guide/Harmonic%20Regression/Harmonic%20Regression.md)
- [Periodic Feature Network](./doc/guide/Periodic%20Feature%20Network/Periodic%20Feature%20Network.md)
- [Residual Harmonic Network](./doc/guide/Residual%20Harmonic%20Network/Residual%20Harmonic%20Network.md)

## Main Implemented Model Families

- `feedforward`
  Point-wise MLP baseline for TE regression.
- `harmonic_regression`
  Structured harmonic baseline with explicit periodic bias.
- `periodic_mlp`
  Hybrid model combining periodic features with neural regression.
- `residual_harmonic_mlp`
  Structured-plus-residual decomposition for TE prediction.
- `tree`
  Tabular baselines for honest comparison against neural approaches.

## Output And Reproducibility

The repository separates artifacts by workflow type instead of mixing everything
into one flat output root.

Important locations:

- `output/training_runs/`
- `output/validation_checks/`
- `output/smoke_tests/`
- `output/training_campaigns/`
- `output/registries/families/`
- `output/registries/program/`

This keeps run identity, campaign outcomes, and best-result tracking explicit
and inspectable.

## Project Notes

- The canonical user-facing documentation lives in `doc/`, not in `reference/`.
- `reference/` is intentionally kept out of the main maintenance workflow.
- The GitHub-facing README redesign rationale is documented in
  [2026-03-25-14-31-40_readme_github_landing_page_redesign.md](./doc/technical/2026-03-25/2026-03-25-14-31-40_readme_github_landing_page_redesign.md).
- The README maintenance rule rationale is documented in
  [2026-03-25-14-51-40_readme_maintenance_rule.md](./doc/technical/2026-03-25/2026-03-25-14-51-40_readme_maintenance_rule.md).
- The Sphinx portal root rename rationale is documented in
  [2026-03-25-15-10-18_sphinx_portal_root_rename_from_docs.md](./doc/technical/2026-03-25/2026-03-25-15-10-18_sphinx_portal_root_rename_from_docs.md).
- The dual `NotebookLM` video-package strategy rationale is documented in
  [2026-03-25-15-50-58_dual_notebooklm_video_package_strategy_for_guides.md](./doc/technical/2026-03-25/2026-03-25-15-50-58_dual_notebooklm_video_package_strategy_for_guides.md).
- The future guide-bundle and `NotebookLM` prompt rule rationale is documented in
  [2026-03-25-16-57-23_future_guide_generation_and_notebooklm_prompt_rule.md](./doc/technical/2026-03-25/2026-03-25-16-57-23_future_guide_generation_and_notebooklm_prompt_rule.md).
- The concept-export integration rationale for the three new `NotebookLM` bundles is documented in
  [2026-03-25-17-30-31_integrate_concept_notebooklm_exports_for_three_guides.md](./doc/technical/2026-03-25/2026-03-25-17-30-31_integrate_concept_notebooklm_exports_for_three_guides.md).
- The Wave 1 recovery campaign PDF layout refinement rationale is documented in
  [2026-03-26-12-55-57_wave1_recovery_campaign_pdf_layout_refinement.md](./doc/technical/2026-03-26/2026-03-26-12-55-57_wave1_recovery_campaign_pdf_layout_refinement.md).

## Next Steps

The near-term direction of the repository is to strengthen structured TE
baselines, keep the training/reporting workflow reliable, and progressively move
toward richer hybrid and eventually physics-informed models once the formulation
is technically justified.
