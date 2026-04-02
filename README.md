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
- repository-owned TwinCAT/TestRig video-guide tooling for high-quality transcript extraction, evidence-driven snapshots, and OCR-assisted report synthesis through Google GenAI;
- a repository-owned LAN AI node path for remote `LM Studio`, `faster-whisper`, and `PaddleOCR` integration while keeping repository orchestration on the current workstation;
- explicit LAN OCR compatibility handling for current `PaddleOCR` versions, with clearer remote-node diagnostics instead of opaque OCR-side `500` crashes;
- repository-owned per-video report generation for analyzed TwinCAT/TestRig video guides;
- a formalized remote-strong TwinCAT/TestRig video-analysis pipeline with tracked reruns, promoted canonical artifacts, and cross-video knowledge synthesis;
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
- `reference/video_guides/source_bundle/`
  Canonical Git-tracked TwinCAT/TestRig video source bundle, with large media
  files stored through Git LFS.

If you only want to get started, begin with:

- [Project Usage Guide](./doc/guide/project_usage_guide.md)
- [Documentation Index](./doc/README.md)
- [LAN AI Node Server Setup Guide](./doc/scripts/tooling/lan_ai/lan_ai_node_server.md)

## Quick Start

### 0. Clone Safely On Windows

Before cloning on Windows, enable Git long-path support from an elevated
PowerShell prompt:

```powershell
git config --system core.longpaths true
```

Then clone the repository into a reasonably short path such as `C:\Work`.

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

### Use The Wave 1 Residual Launcher

```powershell
.\scripts\campaigns\run_wave1_residual_harmonic_family_campaign.ps1
```

### Check Markdown Quality For Repository Docs

```powershell
python -B scripts/tooling/markdown/run_markdownlint.py
python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning
```

### Analyze TwinCAT Video Guides

```powershell
python -B scripts/tooling/video_guides/analyze_video_guides.py
```

The canonical source media for this workflow now lives under:

- `reference/video_guides/source_bundle/`

### Extract High-Quality TwinCAT Video Knowledge

```powershell
python -B scripts/tooling/video_guides/extract_video_guide_knowledge.py --video-filter "Machine_Learning_2" --limit-videos 1
```

### Use The LAN AI Node For Video Knowledge Extraction

```powershell
python -B scripts/tooling/video_guides/extract_video_guide_knowledge.py --video-filter "Machine_Learning_2" --limit-videos 1 --transcript-provider lan --cleanup-provider lmstudio --report-provider lmstudio --ocr-provider lan
```

Before using the LAN path, complete:

- [LAN AI Node Server Setup Guide](./doc/scripts/tooling/lan_ai/lan_ai_node_server.md)

For the tracked remote high-quality rerun, use the repository-owned launcher:

```powershell
.\scripts\tooling\video_guides\run_remote_high_quality_video_rerun.ps1
```

This launcher processes one video at a time, writes persistent runtime
tracking, and stops on the first failing video instead of silently skipping
ahead.

The remote-strong process and current campaign sum-up are documented in:

- [Remote High-Quality TwinCAT Video Pipeline](./doc/scripts/tooling/video_guides/remote_high_quality_video_pipeline.md)
- [Remote High-Quality TwinCAT Video Campaign Sum-Up](./doc/reports/analysis/twincat_video_guides/%5B2026-04-02%5D/remote_high_quality_video_campaign_sum_up.md)

The remote node now uses its own dependency file:

```powershell
python -m pip install -r scripts/tooling/lan_ai/requirements-lan-ai-node.txt
```

For local-only validation on the current workstation, keep the remote
environment variables untouched and add:

```powershell
[System.Environment]::SetEnvironmentVariable("LM_STUDIO_LOCAL_URL", "http://127.0.0.1:1234", "User")
```

Then run the workflow with explicit local overrides, for example:

```powershell
python -B scripts/tooling/video_guides/extract_video_guide_knowledge.py --video-filter "Machine_Learning_2" --limit-videos 1 --transcript-provider lan --cleanup-provider lmstudio --report-provider lmstudio --ocr-provider local --transcript-model tiny --cleanup-model "nvidia/nemotron-3-nano-4b" --report-model "nvidia/nemotron-3-nano-4b" --lan-ai-base-url "http://127.0.0.1:8765" --lm-studio-base-url "$env:LM_STUDIO_LOCAL_URL" --force
```

## Documentation For New Users

If you are opening the repository for the first time, use this reading order:

1. [Project Usage Guide](./doc/guide/project_usage_guide.md)
   Main runnable-workflow reference.
2. [Documentation Index](./doc/README.md)
   Entry point for guides, reports, and technical notes.
3. [LAN AI Node Server Setup Guide](./doc/scripts/tooling/lan_ai/lan_ai_node_server.md)
   Full Windows-first setup for the remote `LM Studio` and LAN AI node
   workstation.
4. Model guides under `doc/guide/`
   Best place to understand the implemented model families at a conceptual
   level.
5. Analysis reports under `doc/reports/analysis/`
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

## Documentation Surface

The repository keeps its canonical human-authored documentation under `doc/`.
Use these entry points instead of treating `README.md` as an internal registry:

- [Documentation Index](./doc/README.md)
- [Tooling Documentation Index](./doc/scripts/tooling/README.md)
- [Project Usage Guide](./doc/guide/project_usage_guide.md)
- [LAN AI Node Server Setup Guide](./doc/scripts/tooling/lan_ai/lan_ai_node_server.md)

For the current TwinCAT/TestRig video-analysis stack, the key references are:

- [Remote High-Quality TwinCAT Video Pipeline](./doc/scripts/tooling/video_guides/remote_high_quality_video_pipeline.md)
- [Remote High-Quality TwinCAT Video Campaign Sum-Up](./doc/reports/analysis/twincat_video_guides/%5B2026-04-02%5D/remote_high_quality_video_campaign_sum_up.md)
- [TwinCAT Video Guides Reference](./doc/reference_codes/testrig_twincat_video_guides_reference.md)

Recent repository-structure decisions are tracked in:

- [2026-04-02-14-40-15_skill_frontmatter_bom_compatibility_fix.md](./doc/technical/2026-04-02/2026-04-02-14-40-15_skill_frontmatter_bom_compatibility_fix.md)
- [2026-04-02-14-24-24_readme_landing_page_and_registry_separation_rule.md](./doc/technical/2026-04-02/2026-04-02-14-24-24_readme_landing_page_and_registry_separation_rule.md)
- [2026-04-02-13-15-32_readme_tooling_lan_ai_documentation_reorganization.md](./doc/technical/2026-04-02/2026-04-02-13-15-32_readme_tooling_lan_ai_documentation_reorganization.md)
- [2026-04-02-13-04-40_move_closed_video_rerun_tracking_into_analysis_bundle.md](./doc/technical/2026-04-02/2026-04-02-13-04-40_move_closed_video_rerun_tracking_into_analysis_bundle.md)
- [2026-04-02-12-42-24_lan_ai_node_ocr_500_regression_check_and_paddleocr_compatibility_fix.md](./doc/technical/2026-04-02/2026-04-02-12-42-24_lan_ai_node_ocr_500_regression_check_and_paddleocr_compatibility_fix.md)

## Next Steps

The near-term direction of the repository is to strengthen structured TE
baselines, keep the training/reporting workflow reliable, and progressively move
toward richer hybrid and eventually physics-informed models once the formulation
is technically justified.
