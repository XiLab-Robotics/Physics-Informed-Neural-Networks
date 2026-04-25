# Project Usage Guide

## Overview

This guide explains how to use the runnable workflows currently available in the repository.

At the moment, the implemented workflows are:

- dataset processing through the validated TE dataset utilities;
- dataset visualization through the TE plotting script;
- feedforward neural-network training, validation, held-out testing, and per-run reporting through a PyTorch Lightning baseline;
- structured static neural baselines through harmonic, periodic-feature, and residual-harmonic training configurations;
- tree-based structured baselines through `RandomForestRegressor` and `HistGradientBoostingRegressor`;
- offline Wave 1 family-best TE-curve prediction plotting and reporting from
  existing model artifacts;
- one-batch training-setup validation for the shared Wave 0 training infrastructure;
- minimal neural or tree smoke-test execution for the shared training infrastructure;
- persistent batch training campaigns through a queue-based runner;
- a short PowerShell launcher for the Wave 1 recovery campaign that keeps the same live terminal logging and per-run artifact behavior;
- a coordinated short PowerShell launcher for the paper-faithful `Track 1`
  reproduction campaign that chains exact-paper family-bank and harmonic-wise
  offline benchmark runs through the currently available repository-owned
  runners;
- explicit isolated-mode session management through a repository-owned tooling entry point with locked-file snapshots, staging roots, and manifest/checklist generation;
- timestamped technical-document scaffolding and index registration through a
  repository-owned tooling entry point;
- repository-owned Markdown warning checks for heading spacing, repeated blank lines, and single-title violations in source `.md` files;
- broader Markdownlint validation for canonical repository Markdown outside `reference/` through a tracked rule profile and terminal runner;
- styled PDF regeneration for the training-configuration analysis report through a dedicated report-export utility;
- real exported PDF validation through a dedicated page-rasterization utility;
- repository-owned TwinCAT/TestRig video-guide analysis through a local media inventory, transcription, frame extraction, and OCR pipeline.

The shared neural training entry point now prints model-specific configuration details for feedforward, harmonic regression, periodic-feature MLP, and residual-harmonic MLP runs instead of assuming every model uses the same dense-layer schema.

For the tree benchmark, the current workstation should use conservative `RandomForestRegressor` settings. A follow-up validation on a higher-memory machine is still required to check whether the previously observed memory failure is hardware-specific and whether a larger RAM budget allows stronger tree configurations.

Recurrent models, LSTM-based models, inference/export flows, and PINN-specific training are still planned future extensions. They are not yet exposed as runnable project workflows.

## Prerequisites

Before using the scripts, make sure the project environment is installed and activated.

If you are cloning on Windows, enable Git long-path support first from an
elevated PowerShell prompt:

```powershell
git config --system core.longpaths true
```

If the environment is not ready yet, install the tracked project dependencies first:

```powershell
conda create -y -n standard_ml_codex_env python=3.12
conda activate standard_ml_codex_env
python -m pip install --upgrade pip
python -m pip install torch --index-url https://download.pytorch.org/whl/cu130
python -m pip install -r requirements.txt
```

This keeps the dependency installation aligned with `requirements.txt` while still pulling the CUDA-enabled `torch` build from the official PyTorch wheel index for the current Windows setup.

If you are upgrading an existing `standard_ml_codex_env` from Python 3.10, rebuild the binary packages after the interpreter update:

```powershell
conda install -y -n standard_ml_codex_env python=3.12
conda activate standard_ml_codex_env
python -m pip install --force-reinstall --no-cache-dir -r requirements.txt
python -m pip install --force-reinstall --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cu130
```

### 1. Activate The Conda Environment

```powershell
conda activate standard_ml_codex_env
```

### 2. Verify The Main Dependencies

```powershell
python -c "import torch, lightning, pandas, matplotlib, colorama, fitz; print(torch.__version__); print(lightning.__version__); print(fitz.__doc__.split()[0])"
```

### 3. Check The Dataset Path

The current dataset path is configured in:

- `config/datasets/transmission_error_dataset.yaml`

The default repository setting is:

```yaml
paths:
  dataset_root: data/datasets
```

This path is interpreted relative to the repository root.

If the dataset is moved in the future, update this YAML file before running the scripts.

## Relevant Project Paths

The current usage flow mainly relies on these folders:

- `scripts/datasets/`
  Dataset processing and visualization utilities.

- `scripts/reports/`
  Styled report-export utilities.

- `scripts/reports/generate_training_results_master_summary.py`
  Repository-owned generator for the canonical always-updated training-results
  master summary.

- `scripts/reports/plot_wave1_best_model_te_curves.py`
  Offline evaluator that loads the current Wave 1 family-best model registry
  entries, predicts selected held-out TE test curves, writes prediction CSVs,
  saves overlay plots, and generates a Markdown comparison report.

- `scripts/training/`
  Static neural and tree training entry points, shared datamodule/regression infrastructure, campaign runner, and validation/smoke-test utilities.

- `scripts/campaigns/wave1/run_wave1_structured_baseline_recovery_campaign.ps1`
  Short PowerShell launcher for the Wave 1 recovery campaign.

- `scripts/campaigns/wave1/run_wave1_residual_harmonic_family_campaign.ps1`
  Canonical short PowerShell launcher for the Wave 1 residual-harmonic family campaign.

- `scripts/campaigns/track1/exact_paper/run_exact_paper_faithful_reproduction_campaign.ps1`
  Canonical coordinated launcher for the current paper-faithful `Track 1`
  reproduction campaign package.

- `scripts/models/`
  Neural-network backbones and the model factory.

- `scripts/tooling/`
  Repository-owned tooling utilities, now grouped by domain.

- `scripts/tooling/lan_ai/`
  Remote-node service, client helpers, CUDA-path setup, and the LAN-only
  dependency file.

- `scripts/tooling/video_guides/`
  TwinCAT/TestRig video-analysis, extraction, reporting, and tracked rerun
  tooling.

- `scripts/tooling/markdown/`
  Repository-owned Markdown validation helpers.

- `scripts/tooling/session/`
  Isolated-mode session tooling.

- `scripts/tooling/technical_documents/`
  Technical-document creation and index-registration tooling.

- `scripts/tooling/video_guides/analyze_video_guides.py`
  Video-guide analysis utility for `reference/video_guides/source_bundle/`,
  with inventory, quality-scored transcript extraction, frame sampling, and
  quality-gated OCR support.

- `scripts/tooling/video_guides/generate_video_guide_reports.py`
  Report-generation utility that turns analyzed TwinCAT/TestRig video artifacts into repository-owned Markdown reports with copied reference images.

- `scripts/tooling/video_guides/extract_video_guide_knowledge.py`
  High-quality three-stage workflow that can now use either cloud backends or a LAN AI node for transcript extraction, OCR, transcript cleanup, and final report synthesis.

- `scripts/tooling/lan_ai/lan_ai_node_server.py`
  Repository-owned FastAPI service intended for the second workstation, exposing `faster-whisper` transcription, `PaddleOCR`, and health endpoints over LAN.

- `doc/scripts/tooling/lan_ai/lan_ai_node_server.md`
  Canonical Windows-first setup guide for the remote workstation, including
  tokens, Git clone, CUDA, Miniconda, `LM Studio`, `OpenSSH Server`, and first
  health checks.

- `doc/scripts/tooling/video_guides/remote_high_quality_video_pipeline.md`
  Formal process note for the strongest currently validated TwinCAT/TestRig
  video-analysis workflow, including topology, launcher behavior, outputs,
  quality gates, and recovery policy.

- `doc/scripts/tooling/technical_documents/create_technical_document.md`
  Canonical usage note for creating a new timestamped technical document and
  registering it in the day-local technical index plus `doc/README.md`.

- `models/`
  Reserved root folder for trained checkpoints and exported model artifacts.

- `config/`
  YAML files grouped by dataset, visualization, and training workflows.

- `config/training/feedforward/presets/`
  Reusable feedforward training presets with explicit `model_family` identity for the shared training infrastructure.

- `config/training/wave1_structured_baselines/campaigns/`
  Wave 1 structured-baseline campaign YAML packages across harmonic, periodic-feature, residual, and tree families.

- `config/training/queue/`
  Persistent batch-training queue folders.

- `data/datasets/`
  Validated Transmission Error CSV dataset.

- `output/`
  Generated artifacts such as plots, logs, and model checkpoints.

- `output/training_runs/`
  Immutable per-run training artifacts grouped by model family.

- `output/validation_checks/`
  One-batch validation artifacts grouped by model family.

- `output/smoke_tests/`
  Minimal Lightning smoke-test artifacts grouped by model family.

- `output/training_campaigns/`
  Campaign-level manifests, markdown execution reports, and batch logs.

- `output/registries/`
  Family-level and program-level best-result registries.

- `doc/running/`
  Persistent state for the currently prepared or active training campaign.

- `doc/`
  Technical, script-level, and user-facing documentation.

- `doc/reports/analysis/`
  Analysis reports grouped by purpose (`training_analysis/`, `analytical_studies/`, `family_studies/`).

- `doc/reports/analysis/Training Results Master Summary.md`
  Canonical project-level summary of current status, best family results,
  recent campaign changes, and family-by-family ranked outcomes.

- `doc/guide/<Model Name>/`
  Canonical model guides with integrated explanation, technical reference content, guide-local assets, and PDF companions.

- `doc/guide/<Guide Name>/Italiano/`
  Italian `NotebookLM` guide exports for the topic, including concept and project outputs.

- `doc/guide/<Guide Name>/English/`
  English `NotebookLM` guide exports for the topic, currently used for the concept-track companion outputs.

- `doc/guide/<Guide Name>/assets/concept_video_package/`
  Neutral `NotebookLM` source package for explaining what the topic is, how it works, and how it is used outside the repository context.

- `doc/guide/<Guide Name>/assets/project_video_package/`
  Repository-specific `NotebookLM` source package for explaining why the topic exists in this TE project and what role it plays here.

- `isolated/active/`
  Active isolated-mode sessions with locked-file snapshots, staging trees, manifests, and checklists.

- `isolated/completed/`
  Completed isolated-mode sessions retained temporarily after successful integration when deletion is not requested.

## Short Launcher

The Wave 1 recovery campaign can also be launched through the short wrapper:

```powershell
.\scripts\\campaigns\\wave1\\run_wave1_structured_baseline_recovery_campaign.ps1
```

This wrapper only reduces typing. It preserves the same terminal output, logs, and campaign artifacts as the full runner command.
It also clears stale pending or running recovery YAML files from earlier failed launcher attempts before re-enqueuing the approved recovery set.

## Technical Document Helper

The repository now also exposes a small helper for the mandatory
technical-document-first workflow:

```powershell
python -B scripts/tooling/technical_documents/create_technical_document.py `
  --slug your_feature_name `
  --summary "Technical document for the approved repository change."
```

This command reads the real local timestamp, creates the timestamped document
under `doc/technical/`, writes the required four-section scaffold, updates the
day-local technical `README.md`, and registers the document from `doc/README.md`.

The Wave 1 residual-family follow-up also has a dedicated launcher:

```powershell
.\scripts\\campaigns\\wave1\\run_wave1_residual_harmonic_family_campaign.ps1
```

For approved campaigns, the repository workflow should now treat the launcher as
part of the mandatory preparation bundle, not as an optional convenience.
Campaign preparation is considered complete only when all of the following
exist:

- approved planning report;
- generated campaign YAML files;
- persistent state in `doc/running/active_training_campaign.yaml`;
- exact raw launch command;
- dedicated PowerShell launcher under `scripts/campaigns/`;
- launcher usage note under `doc/scripts/campaigns/`.

The current paper-faithful `Track 1` preparation also has a dedicated
coordinated launcher:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_exact_paper_faithful_reproduction_campaign.ps1
```

This launcher intentionally mixes:

- exact-paper family-bank runs through
  `run_exact_paper_model_bank_validation.py`;
- harmonic-wise benchmark runs through
  `run_harmonic_wise_comparison_pipeline.py`.

That reflects the current repository state: the branch is prepared for a
paper-faithful reproduction campaign, but the exact-paper structural runner and
the shared offline evaluator are not yet fused into one single Python entry
point.

The repository also exposes the first `Track 2` comparison entry point between
the curated `LGBM-19` exact-paper reference bank and the canonical best
direct-TE `feedforward` baseline:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/run_reference_family_vs_feedforward_comparison.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/reference_family_vs_feedforward/baseline.yaml `
  --output-suffix baseline_validation
```

This workflow is explicitly `result-level comparable`:

- the `LGBM-19` side remains paper-faithful at the harmonic-prediction level;
- the `feedforward` side remains a direct-TE predictor;
- both are compared only after projection onto the same held-out TE-curve
  metric surface.

The repository also exposes an offline Wave 1 family-best TE-curve plotting
workflow. It loads each current `latest_family_best.yaml` registry entry,
predicts a deterministic subset of the canonical held-out test curves, writes
per-curve prediction CSVs, saves overlay plots, and generates a Markdown
comparison report:

```powershell
conda run -n standard_ml_codex_env python scripts/reports/plot_wave1_best_model_te_curves.py
```

For a quick loader and plot smoke test, cap the selected curves:

```powershell
conda run -n standard_ml_codex_env python scripts/reports/plot_wave1_best_model_te_curves.py --max-curves 2
```

The repository also exposes a separate original-dataset exact-model-bank branch
for the bidirectional `Track 1` rebuild:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/baseline_forward.yaml `
  --output-suffix forward_validation
```

Key differences against the recovered exact-paper branch:

- it reads from `data/datasets` through the dataset-processing config;
- it trains separate `forward` and `backward` banks;
- it keeps the paper-style feature schema `rpm`, `deg`, `tor`;
- it fixes the split policy to `70 / 20 / 10` at file level;
- it temporarily disables `SVR` grid search while keeping grid search enabled
  for the other families.

## TwinCAT Video-Guide Analysis

Use the repository-owned video-analysis utility when you want to extract
technical evidence from `reference/video_guides/source_bundle/` for
TwinCAT/TestRig integration work:

```powershell
python -B scripts/tooling/video_guides/analyze_video_guides.py
```

The generated raw artifacts are stored under:

- `.temp/video_guides/_analysis/`

The canonical tracked source media bundle for this workflow lives under:

- `reference/video_guides/source_bundle/`
- `reference/video_guides/source_bundle/README.md`

Useful scoped runs:

```powershell
python -B scripts/tooling/video_guides/analyze_video_guides.py --video-filter "Machine" --limit-videos 2
python -B scripts/tooling/video_guides/analyze_video_guides.py --disable-transcription
```

Important environment notes:

- local transcription uses `faster-whisper`, now with a stronger default model and persisted transcript quality scores;
- frame sampling uses `opencv-python-headless`;
- OCR requires both `pytesseract` and a local Tesseract executable installed on
  the machine;
- OCR is no longer copied naively from full frames; the script now evaluates
  multiple TwinCAT-oriented screen regions and keeps only the best candidate
  text per sampled frame;
- if one optional backend is missing, the script records the skipped phase in
  the generated inventory instead of failing silently.

Useful quality-oriented runs:

```powershell
python -B scripts/tooling/video_guides/analyze_video_guides.py --transcription-model medium --ocr-min-quality-score 42
python -B scripts/tooling/video_guides/analyze_video_guides.py --video-filter "Machine_Learning_2" --frame-interval-seconds 180 --max-frames-per-video 8 --force
```

To generate repository-owned reports from the analyzed artifacts:

```powershell
python -B scripts/tooling/video_guides/generate_video_guide_reports.py
```

## LAN AI Node Workflow

Use the LAN path when you want the current workstation to keep the repository
and reports while the stronger second workstation handles transcription, OCR,
and local LLM cleanup/report generation.

Full setup guide:

- `doc/scripts/tooling/lan_ai/lan_ai_node_server.md`

The validated remote-access path now uses an SSH alias on the current
workstation, for example:

```powershell
ssh xilab-remote
ssh xilab-remote "hostname"
```

The remote workstation now has its own dependency file:

- `scripts/tooling/lan_ai/requirements-lan-ai-node.txt`

Use that file for the `standard_ml_lan_node` environment instead of the main
`requirements.txt`. The remote guide also documents the persistent Conda
`activate.d` / `deactivate.d` setup used to prepend the NVIDIA CUDA 12 runtime
DLL directories to `PATH` automatically.

The validated LAN workflow also includes:

- automatic reclamation of port `8765` when a stale previous
  `lan_ai_node_server.py` process is still bound on the remote workstation;
- richer LM Studio failure diagnostics, including the requested model id, the
  available model ids from `/v1/models`, and the response body on chat
  completion failures.
- chunked LM Studio cleanup for LAN transcripts, built from timestamped
  `faster-whisper` segments returned by the remote node instead of a single
  full-transcript cleanup prompt.
- a tracked remote rerun launcher that processes one video at a time, writes a
  persistent per-video checklist, and stops on the first failing video.

At minimum, the current workstation needs these environment variables:

- `STANDARDML_LAN_AI_TOKEN`
- `LM_STUDIO_API_KEY`
- `STANDARDML_LAN_AI_BASE_URL`
- `LM_STUDIO_BASE_URL`

For local-only validation on the current workstation, you can keep the remote
variables unchanged and add:

- `LM_STUDIO_LOCAL_URL`

Example persistent setup on the current workstation:

```powershell
[System.Environment]::SetEnvironmentVariable("STANDARDML_LAN_AI_TOKEN", "PASTE_LAN_TOKEN_HERE", "User")
[System.Environment]::SetEnvironmentVariable("LM_STUDIO_API_KEY", "PASTE_LM_STUDIO_TOKEN_HERE", "User")
[System.Environment]::SetEnvironmentVariable("STANDARDML_LAN_AI_BASE_URL", "http://REMOTE_HOST:8765", "User")
[System.Environment]::SetEnvironmentVariable("LM_STUDIO_BASE_URL", "http://REMOTE_HOST:1234", "User")
[System.Environment]::SetEnvironmentVariable("LM_STUDIO_LOCAL_URL", "http://127.0.0.1:1234", "User")
```

Quick reachability checks from the current workstation:

```powershell
Test-NetConnection REMOTE_HOST -Port 22
Test-NetConnection REMOTE_HOST -Port 8765
Test-NetConnection REMOTE_HOST -Port 1234
curl.exe -H "Authorization: Bearer $env:STANDARDML_LAN_AI_TOKEN" "$env:STANDARDML_LAN_AI_BASE_URL/health"
curl.exe -H "Authorization: Bearer $env:LM_STUDIO_API_KEY" "$env:LM_STUDIO_BASE_URL/v1/models"
```

Canonical LAN-backed workflow command:

```powershell
python -B scripts/tooling/video_guides/extract_video_guide_knowledge.py --video-filter "Machine_Learning_2" --limit-videos 1 --transcript-provider lan --cleanup-provider lmstudio --report-provider lmstudio --ocr-provider lan --transcript-model large-v3 --cleanup-model YOUR_MODEL_ID --report-model YOUR_MODEL_ID --force
```

Tracked remote batch launcher:

```powershell
.\scripts\tooling\video_guides\run_remote_high_quality_video_rerun.ps1
```

The launcher uses the strongest currently validated practical path:

- remote `large-v3` transcription through the LAN AI node;
- remote `openai/gpt-oss-20b` cleanup and report generation through `LM Studio`;
- local OCR fallback for snapshot evidence;
- one video at a time with stop-on-failure behavior.

By default the launcher now auto-discovers all supported source videos under
`reference/video_guides/source_bundle/`, including `.mkv`, `.mov`, `.avi`, and
`.m4v`, instead of assuming only the original `.mp4` subset.

While active, it writes persistent runtime tracking into:

- `doc/running/remote_high_quality_video_rerun_status.json`
- `doc/running/remote_high_quality_video_rerun_checklist.md`

Once a rerun is closed and its artifacts are promoted, move that bookkeeping
into:

- `doc/reports/analysis/twincat_video_guides/[YYYY-MM-DD]/runtime_tracking/`

Formal runtime/process note:

- `doc/scripts/tooling/video_guides/remote_high_quality_video_pipeline.md`

Canonical local-validation command on the current workstation:

```powershell
python -B scripts/tooling/video_guides/extract_video_guide_knowledge.py --video-filter "Machine_Learning_2" --limit-videos 1 --transcript-provider lan --cleanup-provider lmstudio --report-provider lmstudio --ocr-provider local --transcript-model tiny --cleanup-model YOUR_LOCAL_MODEL_ID --report-model YOUR_LOCAL_MODEL_ID --lan-ai-base-url "http://127.0.0.1:8765" --lm-studio-base-url "$env:LM_STUDIO_LOCAL_URL" --force
```

The high-quality extraction script now also adds explicit terminal logging for:

- provider and model selection;
- selected LAN and LM Studio base URLs;
- transcript extraction progress;
- per-batch LM Studio cleanup requests;
- snapshot-selection progress;
- final transcript and report output paths.

When the requested LM Studio model is not loaded, the script now resolves a
compatible loaded generative model from `/v1/models` instead of failing
immediately on the first request.

For small local LM Studio models, the workflow now also applies a stricter
prompt budget during transcript cleanup through:

- `--lmstudio-max-cleanup-chunks-per-request`
- `--lmstudio-max-cleanup-chunk-characters`
- `--lmstudio-max-report-chunk-characters`

The generated report tree is stored under:

- `doc/reference_codes/video_guides/`

The report generator now surfaces only quality-gated transcript and OCR
highlights. Low-value OCR noise is kept out of the reports even when the
reference image itself is still useful.

## High-Quality Three-Stage Video Workflow

Use the new high-quality workflow when the goal is not coarse indexing but
canonical knowledge extraction from the TwinCAT/TestRig video guides.

Main entry point:

```powershell
python -B scripts/tooling/video_guides/extract_video_guide_knowledge.py --video-filter "Machine_Learning_2" --limit-videos 1
```

This workflow is organized around three explicit stages:

1. canonical transcript extraction through an external API speech-to-text path
   or through the LAN AI node;
2. evidence-driven snapshot selection for the report-local `assets/` folder;
3. OCR-assisted analysis used internally to support the final report rather
   than being dumped verbatim into it.

Prerequisites:

- `imageio-ffmpeg` is used to provide the local FFmpeg executable required for
  audio extraction;
- `opencv-python-headless` is still required for frame extraction;
- for the original cloud-backed route:
  - `GOOGLE_API_KEY` must be set in the environment;
  - `google-genai` must be installed;
- for the LAN route:
  - `LM_STUDIO_BASE_URL` must point to the remote `LM Studio` server;
  - `LM_STUDIO_API_KEY` must contain the configured `LM Studio` token;
  - `STANDARDML_LAN_AI_BASE_URL` must point to the remote
    `lan_ai_node_server.py` instance;
  - `STANDARDML_LAN_AI_TOKEN` must contain the bearer token used by that node;
- for local OCR fallback:
  - `pytesseract` plus a local Tesseract executable are still required.

Typical outputs:

- intermediate artifacts under `.temp/video_guides/_analysis_hq/`
- corrected transcript Markdown files under `doc/reference_codes/video_guides/<video_slug>/`
- report-local snapshot assets under `doc/reference_codes/video_guides/<video_slug>/assets/`
- final per-video reports under `doc/reference_codes/video_guides/<video_slug>/`

### Run Through The LAN AI Node

Use this mode when the second workstation is serving `LM Studio` plus the
repository-owned LAN AI node:

```powershell
python -B scripts/tooling/video_guides/extract_video_guide_knowledge.py --video-filter "Machine_Learning_2" --limit-videos 1 --transcript-provider lan --cleanup-provider lmstudio --report-provider lmstudio --ocr-provider lan --transcript-model large-v3 --cleanup-model qwen3:14b --report-model qwen3:14b
```

This keeps the repository and final artifacts on the current workstation while
delegating transcript extraction, OCR, and LLM synthesis to the remote node.

The LAN node OCR path now reports initialization and execution failures
explicitly. In particular, the previously observed PaddleOCR constructor crash
on `show_log` is handled by a compatibility probe in the node server instead of
surfacing as an opaque `500`.

For the full remote high-quality rerun, prefer the tracked launcher instead of a
manual loop:

```powershell
.\scripts\tooling\video_guides\run_remote_high_quality_video_rerun.ps1
```

### Run Through The Original Google Route

If the remote node is unavailable and quota allows it, the older cloud route is
still available:

```powershell
python -B scripts/tooling/video_guides/extract_video_guide_knowledge.py --video-filter "Machine_Learning_2" --limit-videos 1 --transcript-provider google --cleanup-provider google --report-provider google --ocr-provider local
```

### LAN AI Node Setup Reference

For the remote-node bootstrap procedure, service startup, and `ssh`-based
operation from the current workstation, use:

- `doc/scripts/tooling/lan_ai/lan_ai_node_server.md`
- `doc/scripts/tooling/video_guides/remote_high_quality_video_pipeline.md`

## NotebookLM Video Packages

The learning-guide tree now uses two distinct `NotebookLM` source-package
tracks per guide topic:

- `assets/concept_video_package/`
- `assets/project_video_package/`

Use the `concept` track when you want a neutral educational video about what the
model, concept, or workflow is, how it works, how training and testing operate,
and where it is used in general.

Use the `project` track when you want the repository-specific explanation of why
the topic exists in this TE project, what role it plays here, and what its
project-local strengths and weaknesses are.

Each package now contains:

- `video_source_brief.md`
- `video_terminology_sheet.md`
- `video_narration_outline.md`
- `video_figure_reference.md`
- `video_fact_boundary_notes.md`

And one track-specific scope file:

- `concept_video_scope_notes.md`
- `project_video_scope_notes.md`

For future approved guide-worthy topics, the default repository expectation is
now a full guide bundle unless the user explicitly narrows the scope:

- guide-local assets;
- canonical guide Markdown;
- guide-local PDF companion;
- `assets/concept_video_package/`;
- `assets/project_video_package/`;
- `assets/concept_video_package/notebooklm_concept_video_prompt.md`;
- `assets/project_video_package/notebooklm_project_video_prompt.md`.

The two final prompt files are the ready-to-paste commands intended for two
separate `NotebookLM` generation passes:

- one pass for the neutral `concept` video;
- one pass for the repository-specific `project` video.

Those prompt files should keep the repository prompt style stable:

- explicit goal;
- explicit required chapter order;
- explicit wording constraints;
- explicit fact-boundary compliance;
- explicit duration, tone, and visual-style targets.

When imported `NotebookLM` exports are stored under `Italiano/` or `English/`,
their filenames should declare the guide name, the track, and the artifact
type, for example:

- `FeedForward Network - Concept Mind Map.png`
- `FeedForward Network - Project Video Overview.mp4`

This avoids ambiguous filenames such as `Mind Map.png` or `Video Overview.mp4`.

## Styled Report PDF Export And Validation

## What The Styled PDF Export Does

The styled PDF export entry point is:

- `scripts/reports/generate_styled_report_pdf.py`

This utility:

- reads a canonical Markdown report;
- converts the supported Markdown structure into styled HTML;
- applies a print-oriented visual layout with stronger hierarchy and table rendering;
- preserves repository-local embedded report images such as conceptual model diagrams;
- exports the final PDF through headless Chrome or Edge.

The permanent validation entry point is:

- `scripts/reports/validate_report_pdf.py`

The repository also now exposes a diagram-generation utility used by the model explanatory reports:

- `scripts/reports/generate_model_report_diagrams.py`

The standardized orchestration entry point is:

- `scripts/reports/run_report_pipeline.py`

This utility:

- opens the real exported PDF artifact;
- rasterizes each PDF page to PNG through `PyMuPDF`;
- gives a deterministic validation output that can be inspected visually without rebuilding ad hoc tooling.

The diagram-generation utility:

- regenerates the repository-owned SVG figures used in the model explanatory reports;
- produces both conceptual diagrams and architecture-style diagrams;
- keeps the visual language and layout of those diagrams consistent across model families;
- enforces built-in fit checks so card content does not silently overflow;
- vertically centers each slide composition below the diagram header instead of compacting all content at the top;
- simplifies or removes dense neuron-to-neuron arrows when they hurt readability more than they help explanation;
- routes box-to-box connectors with 90-degree turns so arrows enter and leave cards perpendicularly;
- keeps arrowheads clear of the box border instead of letting the tip overlap the stroke;
- prefers multiline wrapping and spacing over over-aggressive text shrinking in compact cards;
- uses true directional connectors for architecture diagrams instead of pseudo-arrow text.

The report-pipeline runner:

- orchestrates diagram regeneration, PDF export, and PDF validation in one command;
- standardizes temporary artifacts under `.temp/report_pipeline/`;
- can use a repository-local validation environment under `.tools/report_pdf_env/`.

The current main target is:

- `doc/reports/analysis/training_analysis/Training Configuration Analysis.pdf`

Treat that PDF as the project golden standard for future styled analytical reports.

The same export direction now also applies to final campaign-results reports.

## Markdown Warning Check

The repository now exposes a dedicated Markdown warning checker:

- `scripts/tooling/markdown/markdown_style_check.py`

Use it to scan repository-authored Markdown sources for the warning classes that
commonly appear in the editor:

- `MD012/no-multiple-blanks`
- `MD022/blanks-around-headings`
- `MD025/single-title`

Operational rule for documentation work:

- when a task creates or modifies repository-owned Markdown files, re-run the
  warning checks on the touched Markdown scope before closing the task;
- fix warning regressions in those touched files when the fix is local and
  straightforward;
- confirm that the touched Markdown files do not end with an accidental doubled
  trailing blank line and keep only a normal single final newline;
- do not treat this as a requirement to clean the entire repository every time
  a small Markdown edit is made.

Repository quality target:

- Git-tracked authored Markdown should remain warning-free.
- For normal feature work, the mandatory gate is still the touched Markdown
  scope.
- When you need to prove repository-wide warning-free status, run both the
  structural checker and a Markdownlint pass over the full Git-tracked Markdown
  set.

### Run The Default Source Scan

```powershell
python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning
```

This scans the maintained Markdown source roots:

- `README.md`
- `AGENTS.md`
- `config/`
- `models/`
- `doc/`
- `site/`

It intentionally excludes generated or non-canonical paths such as:

- `site/_build/`
- `.temp/`
- `.tools/`
- `isolated/`
- `output/`

### Scan Specific Paths

```powershell
python -B scripts/tooling/markdown/markdown_style_check.py README.md doc site
```

This is useful after a focused documentation task when you only want to re-check
the affected files.

Recommended focused workflow after editing Markdown:

```powershell
python -B scripts/tooling/markdown/markdown_style_check.py README.md doc site
```

Or, for an even narrower task-specific scope, pass only the specific Markdown
paths that were touched.

## Broader Markdownlint Check

The repository also exposes a broader Markdownlint runner:

- `scripts/tooling/markdown/run_markdownlint.py`

Use it when you want a wider Markdownlint pass across canonical repository
Markdown outside `reference/`.

The tracked configuration file is:

- `.markdownlint-cli2.jsonc`

The current profile:

- excludes `reference/`;
- excludes generated or transient paths such as `site/_build/`, `.temp/`,
  `.tools/`, `isolated/`, and `output/`;
- disables `MD013/line-length` until the repository adopts an explicit
  wrapped-prose policy;
- disables `MD029/ol-prefix` so meaningful ordered-list numbering in technical
  documents is not flattened automatically;
- disables `MD041` inside `site/` wrapper files that intentionally start with
  MyST include directives;
- keeps duplicate-heading checks only for sibling headings.

### Run The Default Canonical Markdownlint Scan

```powershell
python -B scripts/tooling/markdown/run_markdownlint.py
```

### Apply Fixable Markdownlint Changes

```powershell
python -B scripts/tooling/markdown/run_markdownlint.py --fix
```

### Lint Specific Paths

```powershell
python -B scripts/tooling/markdown/run_markdownlint.py README.md doc site
```

### Audit The Full Git-Tracked Markdown Set

```powershell
$trackedMarkdownPathList = git ls-files '*.md'
$chunkSize = 80
for ($index = 0; $index -lt $trackedMarkdownPathList.Count; $index += $chunkSize) {
    $chunk = $trackedMarkdownPathList[$index..([Math]::Min($index + $chunkSize - 1, $trackedMarkdownPathList.Count - 1))]
    python -B scripts/tooling/markdown/run_markdownlint.py @chunk
}
```

Pair that with:

```powershell
python -B scripts/tooling/markdown/markdown_style_check.py --fail-on-warning
```

This is the recommended proof step when you want to assert that all tracked
Markdown in the repository is currently warning-free.

The runner uses `npx.cmd` on Windows, so the machine must have `node`, `npm`,
and `npx` available.

## Isolated Mode Workflow

The repository now exposes a dedicated isolated-mode manager:

- `scripts/tooling/session/isolated_mode.py`

Use this workflow when you want Codex to avoid touching every file that already
exists in the repository and to work only on newly created files inside a
session-local staging area.

### Start An Isolated Session

```powershell
python -B scripts/tooling/session/isolated_mode.py start-session `
  --session-label "feature_name" `
  --purpose "Prepare standalone artifacts for later integration." `
  --user-request "modalita isolata"
```

This creates a session under `isolated/active/<session_id>/` with:

- `session_context.md`
- `work_log.md`
- `locked_repository_snapshot.txt`
- `integration_manifest.yaml`
- `integration_checklist.md`
- `staging/`

The locked snapshot defines every pre-existing repository file as read-only for
the isolated session. That lock includes `README.md` and `AGENTS.md`.

### Stage New Session Files

Create new files only inside the current session root, preferably under:

- `isolated/active/<session_id>/staging/`

Mirror the future canonical structure inside `staging/` whenever possible. For
example, if the eventual target should be:

- `doc/guide/New Guide/New Guide.md`

then the isolated staging path should be:

- `isolated/active/<session_id>/staging/doc/guide/New Guide/New Guide.md`

### Register Manifest Items

After creating a staged artifact, register it in the session manifest:

```powershell
python -B scripts/tooling/session/isolated_mode.py add-manifest-item `
  --session-path isolated/active/<session_id> `
  --staging-path isolated/active/<session_id>/staging/doc/guide/New Guide/New Guide.md `
  --target-path doc/guide/New Guide/New Guide.md `
  --action create_new_file `
  --source-reason "Guide drafted entirely in isolated mode."
```

Supported actions are:

- `create_new_file`
- `derive_and_merge`
- `replace_generated_artifact`
- `manual_review_required`

## Codex Repo-Local Workflow Guide

The repository now also exposes a dedicated guide for the local Codex workflow:

- `doc/guide/Codex Repo-Local Workflow/Codex Repo-Local Workflow.md`

Use that guide when you want the repository-specific explanation of:

- which skills exist;
- which subagents exist;
- when skills are used automatically;
- when subagents may be proposed for approval;
- how the repo-local Codex workflow behaves in practice.

### Validate The Isolation Lock

```powershell
python -B scripts/tooling/session/isolated_mode.py validate-session `
  --session-path isolated/active/<session_id> `
  --fail-on-violation
```

This validation detects:

- modified locked files;
- deleted locked files;
- new files created outside the current isolated session root.

### Prepare Integration

When isolated work is ready and you want to integrate it later, regenerate the
review artifacts:

```powershell
python -B scripts/tooling/session/isolated_mode.py prepare-integration `
  --session-path isolated/active/<session_id> `
  --fail-on-violation
```

This updates:

- `latest_validation_report.yaml`
- `latest_integration_review.yaml`
- `integration_checklist.md`

The checklist is designed for a double verification pass:

- Pass A: revalidate the current canonical repository target state;
- Pass B: confirm that the staged intent was actually absorbed after the
  integration step.

### Close The Session

After successful integration, either move the session to `isolated/completed/`
or remove it:

```powershell
python -B scripts/tooling/session/isolated_mode.py close-session `
  --session-path isolated/active/<session_id> `
  --destination completed `
  --require-clean-validation
```

Or:

```powershell
python -B scripts/tooling/session/isolated_mode.py close-session `
  --session-path isolated/active/<session_id> `
  --destination delete `
  --require-clean-validation
```

## Regenerate The Styled Training-Configuration PDF

```powershell
python scripts/reports/generate_styled_report_pdf.py `
  --input-markdown-path "doc/reports/analysis/training_analysis/Training Configuration Analysis.md" `
  --output-pdf-path "doc/reports/analysis/training_analysis/Training Configuration Analysis.pdf" `
  --report-subtitle "Feedforward Transmission Error Baseline" `
  --report-category "Analysis Report"
```

What this does:

- preserves the Markdown file as the canonical content source;
- uses a temporary styled HTML preview internally for the browser export;
- overwrites the PDF with the improved visual layout.

If a persistent HTML preview is explicitly needed, request it on purpose:

```powershell
python scripts/reports/generate_styled_report_pdf.py `
  --input-markdown-path "doc/reports/analysis/training_analysis/Training Configuration Analysis.md" `
  --output-html-path "doc/reports/analysis/training_analysis/Training Configuration Analysis_preview.html" `
  --output-pdf-path "doc/reports/analysis/training_analysis/Training Configuration Analysis.pdf" `
  --report-subtitle "Feedforward Transmission Error Baseline" `
  --report-category "Analysis Report" `
  --keep-html
```

Notes:

- the script auto-detects local Chrome or Edge installations on Windows;
- repository-local Markdown image assets are now supported for styled reports, so explanatory model diagrams can appear in both Markdown and PDF form;
- future styled analytical PDFs should preserve the same design direction:
  - white page background with restrained blue accents;
  - rounded section cards and professional typography;
  - safe A4 margins with no clipped borders or overflowing content;
  - split comparison tables when necessary for readability;
  - repeated `Config` anchors across split comparison tables;
  - centered alignment for comparison matrices when it improves readability;
  - mandatory post-export inspection of the real PDF output;
  - explicit checks that `Config`-like identifier columns are not crushed while short numeric metric columns are not oversized;
  - explicit checks that metric headers do not get forced into wrapped or right-edge-stressed layouts by poor width allocation;
  - explicit checks that long headers wrap inside their own cells instead of spilling into adjacent columns;
  - explicit checks that wrapped identifier cells break at meaningful token boundaries rather than leaving isolated one- or two-letter fragments;
  - explicit checks that content stays comfortably inside each cell and does not sit almost on the borders;
  - explicit checks that table-cell content remains vertically centered, especially in rows mixing one-line and multi-line values;
  - explicit checks that major sections do not start near the bottom of a page and then immediately continue on the next page when a clean page-start is possible;
- if the PDF evidence is inconclusive, the report must not be considered validated yet.
- if both are missing, the export will fail until a compatible browser path is provided explicitly;
- the default workflow no longer leaves a persistent preview HTML file behind;
- temporary browser-profile directories are now standardized under `.temp/report_pipeline/browser_profiles/`.

## Run The Standardized Report Pipeline

Use the orchestration runner when you want one repository-owned command for:

- diagram regeneration;
- styled PDF export;
- raster validation of the real exported PDF.

For the current four structured-model explanatory reports:

```powershell
conda run -n standard_ml_codex_env python scripts/reports/run_report_pipeline.py `
  --use-model-explanatory-reports `
  --regenerate-diagrams `
  --validation-python-path C:\Users\XiLabTRig\miniconda3\envs\standard_ml_codex_env\python.exe
```

If the repository-local validation environment does not exist yet, bootstrap it once:

```powershell
python scripts/reports/run_report_pipeline.py `
  --use-model-explanatory-reports `
  --regenerate-diagrams `
  --bootstrap-tool-env
```

What this does:

- optionally regenerates the repository-owned explanatory SVGs;
- exports the matching PDFs;
- writes validation images under `.temp/report_pipeline/pdf_validation/`;
- avoids repeating the individual commands manually.

On Windows, the explicit validation interpreter can be preferable when `PyMuPDF` is already installed in the main Conda environment and you want to avoid bootstrapping a separate tool environment.

Useful options:

- `--clean-temp`
  Reset the standardized report-pipeline temp root before the run.
- `--cleanup-validation-images`
  Delete validation PNG pages after a successful run.
- `--validation-python-path`
  Use an explicit Python interpreter for PDF validation.
- `--skip-pdf-export`
  Reuse already exported PDFs and only validate them.
- `--skip-pdf-validation`
  Export PDFs without the validation step.

## Run The Presentation Export Pipeline

Use the presentation-pipeline runner when you want one repository-owned command
for:

- `.pptx` generation from a Markdown slide deck;
- PowerPoint-based slide PDF export on Windows;
- raster validation of the real exported slide PDF.

For the current project-status deck:

```powershell
python scripts/reports/run_presentation_pipeline.py `
  --input-markdown-path "doc/reports/analysis/project_status/[2026-03-27]/Project Status Presentation.md" `
  --clean-temp `
  --cleanup-validation-images
```

What this does:

- generates the `.pptx` presentation from the repository-owned Markdown deck;
- uses `reference/templates/Template_XiLab_Research.pptx` as the default base
  PowerPoint template for repository presentations;
- exports the `.pptx` to a slide PDF through Microsoft PowerPoint COM;
- checks that the exported PDF page count matches the Markdown slide count;
- writes validation images under `.temp/presentation_pipeline/pdf_validation/`.

Useful options:

- `--output-pptx-path`
  Override the default `.pptx` destination next to the Markdown deck.
- `--output-pdf-path`
  Override the default PDF destination next to the Markdown deck.
- `--skip-pptx-generation`
  Reuse an existing `.pptx` and only run later stages.
- `--skip-pdf-export`
  Reuse an existing PDF and only run the count check plus validation.
- `--skip-pdf-validation`
  Generate the `.pptx` and PDF without the raster-validation pass.

Current environment assumption:

- this workflow currently assumes Windows with Microsoft PowerPoint available
  through COM automation.

## Regenerate The Model Report Diagrams

```powershell
conda run -n standard_ml_codex_env python scripts/reports/generate_model_report_diagrams.py
```

This command regenerates the current SVG assets stored under:

- `doc/guide/<Model Name>/assets/`

Use it whenever:

- a conceptual or architecture diagram is updated;
- the layout of the model-report figures needs correction;
- the explanatory reports must be refreshed before PDF export.

## Validate The Real Exported PDF

After every styled report export, validate the real PDF artifact rather than relying only on the HTML preview.

```powershell
python scripts/reports/validate_report_pdf.py `
  --input-pdf-path "doc/reports/analysis/training_analysis/Training Configuration Analysis.pdf" `
  --output-image-directory .temp/pdf_validation_training_configuration_analysis `
  --clean-output-directory
```

What this does:

- reads the exported PDF directly;
- rasterizes every page into `.png` images;
- overwrites the previous validation image folder when `--clean-output-directory` is used;
- uses compact page names such as `page_001.png`, which avoids Windows path-length failures in deep validation folders.

Use the generated page images to verify the actual PDF layout:

- borders are not clipped;
- section cards fit inside the A4 margins;
- long headers stay inside their own columns;
- identifier-like cells wrap at meaningful token boundaries;
- numeric columns are not oversized while identifier columns are crushed;
- major sections do not start at the bottom of a page unless the continuation remains visually coherent.

## Dataset Processing

## What The Processing Module Does

The dataset-processing logic lives in:

- `scripts/datasets/transmission_error_dataset.py`

This module:

- loads the validated TE CSV files already available in `data/datasets`;
- parses metadata from the file names and folder names;
- builds forward and backward directional samples;
- creates PyTorch `Dataset` and `DataLoader` objects;
- keeps helper functions ready for future raw-data TE reconstruction using:
  - `TE = theta_out - 81 * theta_in`
  - `DataValid` masks

Important dataset note:

- the CSV files currently present in the repository are already validated TE files;
- they do not contain raw encoder columns or `DataValid Forward` / `DataValid Backward` flags;
- the forward-position CSV header contains the original typo `Poisition_Output_Reducer_Fw`;
- the loader keeps compatibility with that original header and normalizes it internally to `position_output_reducer_fw_deg`.

## Shared Training Validation And Smoke-Test

## What Wave 0 Added

The repository now exposes two reusable pre-campaign training checks:

- `scripts/training/validate_training_setup.py`
- `scripts/training/run_training_smoke_test.py`

These utilities are intended to be reused across future model families, not only by the current feedforward baseline.

They rely on a shared training infrastructure that now standardizes:

- `experiment.model_family` in the training presets;
- a common metrics artifact schema;
- common output artifact names such as `training_config.yaml` and `metrics_summary.yaml`.

The same checks now also support the Wave 1 tree baselines through a reduced `scikit-learn` fit/predict path.

## Run The One-Batch Validation Check

```powershell
conda run -n standard_ml_codex_env python scripts/training/validate_training_setup.py `
  --config-path config/training/feedforward/presets/trial.yaml `
  --output-suffix validation_check
```

This command verifies:

- config loading;
- datamodule setup;
- model instantiation;
- batch shape correctness;
- finite loss and metrics on one batch.

For tree models, the check uses a reduced train/validation sample subset instead of the neural batch path.

It writes:

- `validation_summary.yaml` under `output/validation_checks/<model_family>/<run_instance_id>/`;
- one repository-owned Markdown validation report under `doc/reports/analysis/validation_checks/`.

## Run The Minimal Lightning Smoke Test

```powershell
conda run -n standard_ml_codex_env python scripts/training/run_training_smoke_test.py `
  --config-path config/training/feedforward/presets/trial.yaml `
  --output-suffix smoke_test `
  --fast-dev-run-batches 1
```

This command verifies:

- a minimal Lightning `fit` path;
- one-batch train/validation execution through `fast_dev_run`;
- manual checkpoint save;
- checkpoint reload.

For tree models, the check uses reduced train/eval subsets together with serialized model save/reload validation.

It writes:

- `smoke_test_summary.yaml`
- `smoke_test_checkpoint.ckpt`

under `output/smoke_tests/<model_family>/<run_instance_id>/`.

## Shared Training Artifacts

The feedforward training workflow now writes:

- `training_config.yaml`
- `metrics_summary.yaml`
- `run_metadata.yaml`

## Dataset Processing Configuration

The processing settings are stored in:

- `config/datasets/transmission_error_dataset.yaml`

Current configurable sections:

- `paths.dataset_root`
  Root folder of the CSV dataset, relative to the project root.

- `dataset.reduction_ratio`
  Reducer ratio used by the raw TE helper path.

- `dataset.angular_window_deg`
  Output-position window expected for valid rotation.

- `directions.use_forward_direction`
  Enables forward curves.

- `directions.use_backward_direction`
  Enables backward curves.

- `split.validation_split`
  Train/validation file split ratio.

- `split.test_split`
  Held-out test file split ratio.

- `split.random_seed`
  Seed used for split reproducibility.

- `dataloader.batch_size`
  Batch size used by the generated curve dataloaders.

- `dataloader.num_workers`
  Number of PyTorch dataloader workers.

## Use The Processing Module From Python

The most direct way to use the processing utilities is from Python.

### Example: Build Train, Validation, And Test Dataloaders From Config

```powershell
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config; bundle=create_transmission_error_dataloaders_from_config(); print(len(bundle['train_dataset'])); print(len(bundle['validation_dataset'])); print(len(bundle['test_dataset']))"
```

What this does:

- reads `config/datasets/transmission_error_dataset.yaml`;
- collects CSV files from the configured dataset root;
- creates forward and backward directional samples;
- splits the files into train, validation, and test sets;
- returns a dictionary containing:
  - `train_dataset`
  - `validation_dataset`
  - `test_dataset`
  - `train_dataloader`
  - `validation_dataloader`
  - `test_dataloader`

### Example: Inspect One Training Batch

```powershell
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config; bundle=create_transmission_error_dataloaders_from_config(); batch=next(iter(bundle['train_dataloader'])); print(batch['input_tensor'].shape); print(batch['target_tensor'].shape); print(batch['valid_mask'].shape)"
```

Expected batch content:

- `input_tensor`
  Padded tensor with features per point.

- `target_tensor`
  Padded tensor with TE targets.

- `angular_position_deg`
  Padded output-position tensor.

- `valid_mask`
  Boolean mask for valid points inside the padded batch.

- `sequence_length`
  Original sequence length for each curve.

- metadata tensors/lists for speed, torque, temperature, direction, and source file.

## Input Features Used In The Current Dataset Class

Each point currently includes these input features:

1. output angular position in degrees
2. speed in rpm
3. torque in Nm
4. oil temperature in degrees
5. direction flag (`+1` forward, `-1` backward)

The regression target is:

- Transmission Error in degrees

## Flatten A Padded Batch Into Point-Wise Tensors

If the model is trained point by point rather than sequence by sequence, you can flatten the padded batch.

```powershell
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config, flatten_curve_batch; bundle=create_transmission_error_dataloaders_from_config(); batch=next(iter(bundle['train_dataloader'])); flat=flatten_curve_batch(batch); print(flat['input_tensor'].shape); print(flat['target_tensor'].shape)"
```

This removes the padding using the batch validity mask.

## Dataset Visualization

## What The Visualization Script Does

The visualization entry point is:

- `scripts/datasets/visualize_transmission_error.py`

This script:

- reads the visualization config;
- resolves the dataset config;
- selects one CSV file;
- loads forward and backward TE curves;
- plots TE against output angular position;
- either opens the plot or saves it to an image file.

## Visualization Configuration

The visualization settings are stored in:

- `config/visualization/transmission_error_visualization.yaml`

Main configurable fields:

- `paths.dataset_config_path`
  Path to the dataset-processing YAML config, relative to the project root.

- `selection.file_index`
  Default file index when no explicit CSV path is provided.

- `plot.figure_width`
  Figure width in inches.

- `plot.figure_height`
  Figure height in inches.

- `plot.figure_dpi`
  Figure DPI used for saved plots.

- `output.save_path`
  Optional default output path for saved figures.

## Save A Plot To File

This is the most robust option in terminal or headless environments.

```powershell
python -m scripts.datasets.visualize_transmission_error --save-path output\te_curve.png
```

What happens:

- the script reads the default YAML files in `config/visualization/` and `config/datasets/`;
- it selects the dataset file indicated by `selection.file_index`;
- it generates forward and backward TE curves;
- it saves the image to `output\te_curve.png`.

## Visualize A Specific Dataset File

If you want to inspect one exact CSV:

```powershell
python -m scripts.datasets.visualize_transmission_error --csv-path "data\datasets\Test_35degree\1000rpm\1000.0rpm0.0Nm35.0deg.csv" --save-path output\sample_te_curve.png
```

This bypasses the default file index and directly uses the selected CSV file.

## Override The Default File Index

If you prefer to keep the configured dataset root but change the selected file:

```powershell
python -m scripts.datasets.visualize_transmission_error --file-index 10 --save-path output\te_curve_10.png
```

## Structured Baseline Training

## What The Training Workflows Do

The static neural training entry point is:

- `scripts/training/train_feedforward_network.py`

This workflow trains the static neural TE baselines implemented with PyTorch Lightning:

- `feedforward`
- `harmonic_regression`
- `periodic_mlp`
- `residual_harmonic_mlp`

The tree-based training entry point is:

- `scripts/training/train_tree_regressor.py`

This workflow trains the current tabular structured baselines:

- `random_forest`
- `hist_gradient_boosting`

The script now prints a structured terminal summary with colorized section headers on Windows terminals, so the training configuration and run artifacts are easier to inspect than with the earlier raw dictionary dump.

The structured baseline stack is composed of:

- `scripts/models/feedforward_network.py`
  Feedforward backbone with hidden layers, activation, optional layer normalization, and dropout.

- `scripts/models/harmonic_regression.py`
  Harmonic regression backbone with optional operating-condition terms.

- `scripts/models/periodic_feature_network.py`
  Periodic-feature MLP backbone using harmonic feature expansion before the residual MLP.

- `scripts/models/residual_harmonic_network.py`
  Harmonic structured head plus residual MLP refinement backbone.

- `scripts/models/model_factory.py`
  Model selection layer used to instantiate the requested architecture.

- `scripts/training/transmission_error_datamodule.py`
  Lightning datamodule that reuses the TE curve dataset and converts curves into point-wise batches.

- `scripts/training/transmission_error_regression_module.py`
  Generic Lightning regression module with normalization, loss computation, optimizer setup, and validation metrics.

- `scripts/training/tree_regression_support.py`
  Shared flattening, estimator, metrics, and serialization utilities for the tree baselines.

- `config/training/feedforward/presets/baseline.yaml`
  Main training configuration file for the baseline.

- `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/`
  First prepared structured-baseline campaign package for Wave 1.

## Current Structured-Baseline Assumptions

The current static baseline program:

- trains point-wise on TE curve samples rather than with recurrent sequence modeling;
- computes normalization statistics from the training split only;
- uses the normalized tensors during optimization and reports interpretable metrics on denormalized TE values;
- uses validation-based early stopping and checkpoint selection;
- reloads the best checkpoint for the final validation and held-out test evaluation;
- saves machine-readable and human-readable reports for each completed run;
- ranks all completed families through the shared registry artifacts.

This is the first baseline only. It does not replace the future need for LSTM, RNN, or PINN models.

## Training Configuration

The training settings are stored in:

- `config/training/feedforward/presets/baseline.yaml`

An additional lighter proof-run configuration is also available in:

- `config/training/feedforward/presets/trial.yaml`

More aggressive workstation-oriented variants are also available in:

- `config/training/feedforward/presets/high_density.yaml`
- `config/training/feedforward/presets/high_epoch.yaml`
- `config/training/feedforward/presets/high_compute.yaml`

The current recommended practical feedforward preset is:

- `config/training/feedforward/presets/best_training.yaml`

The first prepared Wave 1 structured campaign package is available in:

- `config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/`

Main configurable sections:

- `paths.dataset_config_path`
  Dataset-processing config used by the Lightning datamodule.

- `paths.output_root`
  Root output directory for immutable training runs.
  The current feedforward presets now point to `output/training_runs/feedforward`.

- `experiment.run_name`
  Name of the training run output folder.

- `experiment.model_type`
  Requested architecture name resolved by the model factory.

- `dataset.curve_batch_size`
  Number of directional curves loaded per batch before point extraction.

- `dataset.point_stride`
  Downsampling stride used when extracting point-wise samples from each curve.

- `dataset.maximum_points_per_curve`
  Optional cap on the number of points taken from each curve.

- `dataset.num_workers`
  PyTorch dataloader worker count.
  The current default is `4`, which is a conservative multiprocessing setting for this Windows-based training environment.

- `dataset.pin_memory`
  Pin-memory flag for the dataloaders.
  The current default is `true` to improve host-to-device transfer when training on GPU.

- `model.input_size`
  Expected point-wise feature dimension.

- `model.hidden_size`
  Hidden-layer sizes for the feedforward backbone.

- `model.output_size`
  Output dimension of the regression model.

- `model.activation_name`
  Activation function used in the hidden layers.

- `model.dropout_probability`
  Dropout probability used after hidden activations.

- `model.use_layer_norm`
  Enables or disables `LayerNorm` in the hidden stages.

- `training.learning_rate`
  Optimizer learning rate.

- `training.weight_decay`
  `AdamW` weight decay.

- `training.min_epochs`
  Minimum number of epochs.

- `training.max_epochs`
  Maximum number of epochs.

- `training.patience`
  Early-stopping patience.

- `training.min_delta`
  Minimum monitored improvement threshold.

- `training.log_every_n_steps`
  Lightning logging frequency.

- `training.fast_dev_run`
  Lightning developer-mode shortcut.

- `training.deterministic`
  Deterministic training flag.

- `runtime.accelerator`
  Lightning accelerator selection, typically `auto` or `gpu`.

- `runtime.devices`
  Lightning device selection, typically `auto` or an explicit GPU count.

- `runtime.precision`
  Trainer precision mode such as `"32"`, `"16-mixed"`, or `"bf16-mixed"`.

- `runtime.benchmark`
  Enables cuDNN benchmarking for stable-shape CUDA workloads.

- `runtime.use_non_blocking_transfer`
  Enables explicit non-blocking tensor transfer during batch-to-device movement when the host batch is pinned.

## Run The Default Training Command

From the project root:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py
```

The direct script execution shown above is supported from the repository root. The training entry point bootstraps the project root into `sys.path`, so the internal `scripts.models`, `scripts.training`, and `scripts.datasets` imports resolve correctly even when the file is launched directly.

This command:

- loads `config/training/feedforward/presets/baseline.yaml`;
- builds the datamodule from `config/datasets/transmission_error_dataset.yaml`;
- uses `validation_split` plus `test_split` from the dataset config to create three file-level subsets;
- uses `num_workers: 4` and `pin_memory: true` in the point-wise dataloaders by default;
- enables `persistent_workers` internally when dataloader multiprocessing is active;
- uses explicit recursive tensor transfer to the selected device, with optional `non_blocking=True` support controlled by the runtime config;
- computes training normalization statistics;
- creates the feedforward model;
- prints a compact colorized summary for configuration, dataset, normalization, runtime, and output artifacts;
- suppresses the current low-signal Lightning `litlogger` startup tip and the known `_pytree` sanity-check warning;
- starts Lightning training, validation, and held-out testing;
- reloads the best checkpoint before the final evaluation phase;
- writes artifacts under `output/training_runs/<model_family>/<run_instance_id>/`.

Typical artifacts now include:

- `training_config.yaml`
  Snapshot of the effective run configuration.

- `run_metadata.yaml`
  Explicit run-artifact identity including `run_instance_id`.

- `checkpoints/`
  Best and last Lightning checkpoints.

- `best_checkpoint_path.txt`
  Plain-text pointer to the selected best checkpoint.

- `metrics_summary.yaml`
  Machine-readable validation and test metrics.

- `training_test_report.md`
  Human-readable training and testing summary.

- family/program best-result registries under:
  - `output/registries/families/<model_family>/`
  - `output/registries/program/`

## Run The Lightweight Proof Configuration

If you want a faster verification run before trying the default baseline, use the trial config:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/trial.yaml
```

This proof configuration:

- uses `run_name: te_feedforward_trial`;
- increases `dataset.point_stride` to reduce the sampled points per curve;
- caps the point count with `dataset.maximum_points_per_curve: 200`;
- reduces the epoch budget to a short verification range;
- still executes validation, held-out testing, and report generation.

The trial preset keeps `runtime.use_non_blocking_transfer: false` because it also keeps `pin_memory: false`, so asynchronous host-to-device copies would provide little practical benefit there.

## Workstation-Oriented Training Variants

If the workstation has strong CPU and GPU resources, the repository now also provides three heavier training configurations.

### `config/training/feedforward/presets/high_density.yaml`

Use this when the first priority is denser sampling of each TE curve:

- lower `point_stride` than the baseline;
- larger `curve_batch_size`;
- higher dataloader worker count.

This is the recommended first upgrade over the baseline when the goal is to test whether more curve detail improves the results.

### `config/training/feedforward/presets/high_epoch.yaml`

Use this when the first priority is a longer convergence window:

- same basic data density as the baseline;
- longer epoch budget;
- higher early-stopping patience.

This is useful when the baseline appears stable but not yet fully converged.

### `config/training/feedforward/presets/high_compute.yaml`

Use this when the goal is to push both data density and model capacity:

- denser point sampling;
- larger curve batches;
- larger hidden layers;
- longer epoch budget.

This is the most compute-heavy feedforward variant currently defined in the repository and is best treated as an offline benchmark rather than as the first PLC-oriented baseline.

### `config/training/feedforward/presets/best_training.yaml`

Use this when you want the current best practical feedforward training preset derived from the completed mixed campaign:

- `point_stride = 5`
- `curve_batch_size = 4`
- standard `128-128-64` architecture
- long `20-250` epoch schedule
- no large-model complexity penalty

This preset is the current recommended default because it achieved the best held-out `test_mae` across the currently executed feedforward configurations while remaining relatively efficient.

## GPU Runtime Optimization Notes

The repository now exposes explicit runtime controls for the GPU path without forcing aggressive settings by default.

Recommended practical usage:

- keep `runtime.precision: "32"` as the accuracy-safe baseline;
- try `runtime.precision: "16-mixed"` only when the GPU path is already numerically stable and faster throughput matters;
- try `runtime.precision: "bf16-mixed"` only if the local GPU stack supports it reliably;
- keep `runtime.benchmark: true` for this feedforward workload because tensor shapes are stable enough to benefit;
- keep `runtime.use_non_blocking_transfer: true` only when `dataset.pin_memory: true` is also enabled.

The current optimization pass is aimed at reducing CPU-to-GPU transfer stalls and exposing useful Lightning runtime flags. It is not intended to force full GPU saturation if that adds instability or unnecessary complexity.

## Current Dataloader Runtime Defaults

The current feedforward-training config now uses these dataloader defaults:

- `dataset.num_workers: 4`
- `dataset.pin_memory: true`

These values were selected as the first practical tuning step after the initial stable baseline:

- `num_workers: 4` reduces dataloader bottlenecks without jumping immediately to aggressive multiprocessing values on Windows;
- `pin_memory: true` is appropriate when the training run uses CUDA, which is the current expected setup for this repository.

If the project is later executed on CPU-only hardware or on a different workstation, these values can still be adjusted directly in `config/training/feedforward/presets/baseline.yaml`.

## Run Training With A Custom Config Path

If you want to launch the same workflow with a different YAML file:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/baseline.yaml
```

The script now exposes `--config-path`, so custom YAML files can be launched directly without using `python -c`.

To launch the current best practical feedforward preset directly:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py --config-path config/training/feedforward/presets/best_training.yaml
```

To launch one prepared Wave 1 structured-neural candidate directly:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py `
  --config-path config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/07_residual_h12_small_frozen.yaml
```

To launch one prepared Wave 1 tree candidate directly:

```powershell
conda run -n standard_ml_codex_env python scripts/training/train_tree_regressor.py `
  --config-path config/training/wave1_structured_baselines/campaigns/2026-03-17_wave1_structured_baseline_campaign/09_random_forest_tabular.yaml
```

## Typical Training Outputs

The structured baselines write outputs under the configured family-specific training-run roots, for example:

- `output/training_runs/feedforward/`
- `output/training_runs/harmonic_regression/`
- `output/training_runs/periodic_mlp/`
- `output/training_runs/residual_harmonic_mlp/`
- `output/training_runs/tree/`

For the default run name, a typical output location is:

- `output/training_runs/feedforward/2026-03-17-20-05-11__te_feedforward_baseline/`

Typical generated artifacts include:

- a copy of the effective training config;
- TensorBoard logs;
- Lightning checkpoints;
- a text file containing the best checkpoint path;
- a run metadata snapshot;
- updated best-result registries.

## Inspect Neural Training Logs With TensorBoard

After a real training run, you can inspect logs with:

```powershell
tensorboard --logdir output\training_runs\feedforward
```

Then open the local TensorBoard URL shown in the terminal.

## Current Training Metrics

The static neural regression module currently logs:

- `train_loss`
- `train_mae`
- `train_rmse`
- `val_loss`
- `val_mae`
- `val_rmse`

The best checkpoint and early stopping are both driven by `val_mae`.

The tree baselines do not generate TensorBoard logs. Their ranking relies on the shared `metrics_summary.yaml` snapshots and the registry files.

## Batch Training Campaigns

## What The Batch Runner Does

The batch training entry point is:

- `scripts/training/run_training_campaign.py`

This runner:

- optionally copies one or more YAML files into the queue;
- executes queued YAML files sequentially;
- moves each configuration across `pending/`, `running/`, `completed/`, and `failed/`;
- keeps the same direct terminal logging behavior as the underlying single-run training script for supported model types;
- mirrors that live output into one terminal log per queue item;
- prints a compact campaign-progress summary before and after each run;
- generates a campaign manifest and markdown execution report under `output/training_campaigns/`.
- generates explicit `campaign_leaderboard.yaml`, `campaign_best_run.yaml`, and `campaign_best_run.md` files inside each campaign folder.
- refreshes the canonical `Training Results Master Summary.md` after local
  campaign completion so the global project snapshot stays aligned with the new
  registries and training artifacts.

## Queue Layout

The persistent queue folders are:

- `config/training/queue/pending/`
- `config/training/queue/running/`
- `config/training/queue/completed/`
- `config/training/queue/failed/`

Keep reusable presets under:

- `config/training/feedforward/presets/`

Copy presets into `pending/` when preparing a campaign. Do not move the canonical preset files themselves.

Campaign-specific YAML files can also be stored in dedicated folders such as:

- `config/training/feedforward/campaigns/2026-03-12_mixed_training_campaign/`

## Queue Presets Without Running Them Yet

```powershell
python scripts/training/run_training_campaign.py `
  config/training/feedforward/presets/baseline.yaml `
  config/training/feedforward/presets/high_epoch.yaml `
  --enqueue-only
```

## Run Everything Currently Pending

```powershell
python scripts/training/run_training_campaign.py
```

When the queued model type is currently supported by the in-process runner layer, the terminal now shows the same structured sections and Lightning progress bars used by `scripts/training/train_feedforward_network.py`. This removes the earlier delayed startup silence and avoids the previous broken Unicode progress-bar output caused by piped subprocess capture.

## Queue And Run In One Command

```powershell
python scripts/training/run_training_campaign.py `
  config/training/feedforward/presets/baseline.yaml `
  config/training/feedforward/presets/high_density.yaml `
  --campaign-name feedforward_density_check
```

## Remote LAN Training Campaigns

Use the remote campaign launcher when you want to keep campaign preparation and
final review on the current workstation but execute the heavy training runtime
on the stronger LAN workstation.

Canonical launcher:

- `scripts/campaigns/infrastructure/run_remote_training_campaign.ps1`

This workflow is intended to mirror the repository-owned LAN AI operating
pattern:

- the current workstation remains the canonical repository and review surface;
- the remote workstation executes the campaign through SSH;
- the resulting campaign artifacts and registry updates are synchronized back
  into the local repository after the run.

Operationally, prepared LAN-remote campaigns now follow the same handoff model
used for local campaigns:

- Codex prepares the YAML package, dedicated PowerShell launcher, and launcher
  note;
- Codex provides the exact launch command from the repository root;
- the user runs that command manually in the terminal;
- the user later reports when the campaign has started and when it has
  finished.

Current remote assumptions:

- the remote workstation already has a synchronized clone of this repository;
- the remote workstation already has the expected dataset available;
- the remote workstation already has a working training Conda environment;
- the validated SSH alias path already works, for example:

```powershell
ssh xilab-remote
ssh xilab-remote "hostname"
```

Recommended convenience variables on the current workstation:

- `STANDARDML_REMOTE_TRAINING_REPO_PATH`
- `STANDARDML_REMOTE_TRAINING_CONDA_ENV`

Generic launcher example:

```powershell
.\scripts\\campaigns\\infrastructure\\run_remote_training_campaign.ps1 `
  -CampaignConfigPathList @(
      "config\training\residual_harmonic_mlp\campaigns\2026-03-26_wave1_residual_harmonic_family_campaign\01_residual_h08_small_frozen.yaml",
      "config\training\residual_harmonic_mlp\campaigns\2026-03-26_wave1_residual_harmonic_family_campaign\02_residual_h08_small_joint.yaml"
  ) `
  -CampaignName "remote_residual_test_campaign" `
  -PlanningReportPath "doc\reports\campaign_plans\2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md" `
  -RemoteHostAlias "xilab-remote"
```

The launcher now performs these stages explicitly:

- remote reachability and environment preflight;
- source sync of `scripts/`, `config/`, `doc/`, and `requirements.txt` to the
  remote repository path;
- remote `run_training_campaign.py` execution through `conda run`;
- remote sync-manifest generation on the LAN workstation;
- metadata-aware artifact sync back into the local repository.

The artifact return path now pulls the synchronized result set path by path
instead of packing the whole remote payload into one large multi-path archive.
This keeps the sync explicit and inspectable while avoiding the brittle
completion-path behavior seen in the first long remote follow-up run.

The sync phase is now hardened against stale manifest paths. If one run entry in
the campaign manifest no longer matches the real immutable output folder, the
remote helper recovers the canonical run directory from `run_metadata.yaml`
before the artifact pullback is finalized.

Tracking files written on the current workstation:

- `doc/running/remote_training_campaign_status.json`
- `doc/running/remote_training_campaign_checklist.md`
- `.temp/remote_training_campaigns/`

After the remote artifacts are synchronized back locally, the launcher should
also refresh:

- `doc/reports/analysis/Training Results Master Summary.md`

Use the paired launcher note for the exact sync contract and operational
details:

- `doc/scripts/campaigns/run_remote_training_campaign.md`

For prepared campaigns, the exact handoff command should be copied from:

- `doc/running/active_training_campaign.yaml`

Use `launch_command_list` as the canonical source when the operator needs the
exact short or explicit command to run.

### First Real Remote Validation Campaign

The first repository-owned real remote validation campaign is now available as a
validated five-run mixed package:

- `te_random_forest_remote_medium`
- `te_random_forest_remote_aggressive`
- `te_hist_gbr_remote_deep`
- `te_feedforward_high_compute_remote`
- `te_feedforward_stride1_big_remote`

Prepared campaign root:

- `config/training/remote_validation/campaigns/2026-04-03_remote_training_validation_campaign/`

Dedicated launcher:

- `scripts/campaigns/infrastructure/run_remote_training_validation_campaign.ps1`

Dedicated launcher note:

- `doc/scripts/campaigns/run_remote_training_validation_campaign.md`

Real preflight performed on `2026-04-03` already established:

- the SSH alias works because `ssh xilab-remote "hostname"` returned
  `DESKTOP-T7O45HF`;
- the remote repository path exists at
  `C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks`;
- the remote clone is currently at commit
  `8ff4bf90e0d7cbdc06778a749e1eb7db5843b8de`;
- the existing environment `standard_ml_lan_node` passes the repository
  validation check;
- the remote workstation has an NVIDIA RTX A4000 visible through `nvidia-smi`;
- the remote environment now exposes `torch==2.11.0+cu130`;
- `torch.cuda.is_available()` is now `True`, so mixed tree plus Lightning GPU
  validation campaigns are valid on the LAN node.

Recommended one-time remote setup:

```powershell
Set-Location "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks"
git checkout main
conda activate standard_ml_lan_node
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install --force-reinstall --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cu130
```

Recommended one-time current-workstation setup:

```powershell
[System.Environment]::SetEnvironmentVariable("STANDARDML_REMOTE_TRAINING_REPO_PATH", "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks", "User")
[System.Environment]::SetEnvironmentVariable("STANDARDML_REMOTE_TRAINING_CONDA_ENV", "standard_ml_lan_node", "User")
```

After reopening PowerShell, the validated campaign launcher can be reused with:

```powershell
.\scripts\\campaigns\\infrastructure\\run_remote_training_validation_campaign.ps1
```

If you prefer not to persist the current-workstation environment variables yet,
use:

```powershell
.\scripts\\campaigns\\infrastructure\\run_remote_training_validation_campaign.ps1 `
  -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" `
  -RemoteCondaEnvironmentName "standard_ml_lan_node" `
  -RemoteHostAlias "xilab-remote"
```

Before launching, confirm the campaign is still marked as prepared in:

- `doc/running/active_training_campaign.yaml`

If the task is being executed through the repository-local Codex workflow, a
dedicated skill now exists for this path:

- `.codex/skills/remote-lan-training-campaigns/SKILL.md`

### Targeted Remote Follow-Up Campaign

The next prepared LAN-remote campaign is a tighter mixed package aimed at the
highest-value branches left after the first validation pass:

- `te_residual_h12_deep_long_remote`
- `te_residual_h12_deep_dense_remote`
- `te_feedforward_high_compute_long_remote`
- `te_feedforward_stride1_high_compute_long_remote`
- `te_hist_gbr_remote_refined`

Prepared campaign root:

- `config/training/remote_followup/campaigns/2026-04-04_targeted_remote_followup_campaign/`

Dedicated launcher:

- `scripts/campaigns/infrastructure/run_targeted_remote_followup_campaign.ps1`

Dedicated launcher note:

- `doc/scripts/campaigns/run_targeted_remote_followup_campaign.md`

This package is intentionally selective:

- it keeps `residual_harmonic_mlp` in focus because that family is still the
  strongest neural branch;
- it keeps `feedforward` in focus because the remote GPU path already improved
  the family best once;
- it keeps one bounded `hist_gradient_boosting` refinement because the tree
  family still leads the whole program;
- it excludes `random_forest` because the first remote campaign already showed
  poor value relative to memory cost and artifact size.

If the local environment variables are already set, launch with:

```powershell
.\scripts\\campaigns\\infrastructure\\run_targeted_remote_followup_campaign.ps1
```

If you prefer the explicit form, use:

```powershell
.\scripts\\campaigns\\infrastructure\\run_targeted_remote_followup_campaign.ps1 `
  -RemoteRepositoryPath "C:\Users\Martina Salami\Documents\Davide\Physics-Informed-Neural-Networks" `
  -RemoteCondaEnvironmentName "standard_ml_lan_node" `
  -RemoteHostAlias "xilab-remote"
```

Before launching, confirm the active campaign state is still `prepared` in:

- `doc/running/active_training_campaign.yaml`

## Batch Runner Outputs

Each campaign writes a new folder under:

- `output/training_campaigns/`

Typical generated artifacts:

- `campaign_manifest.yaml`
  Machine-readable index of executed queue items and artifact paths.

- `campaign_execution_report.md`
  Human-readable execution report listing what was tested and where the per-run results are stored.

- `campaign_leaderboard.yaml`
  Ranked campaign-local comparison entries using the repository selection policy.

- `campaign_best_run.yaml`
  Machine-readable winner of the campaign.

- `campaign_best_run.md`
  Human-readable summary of the campaign winner.

- `logs/*.log`
  Full terminal output mirrored for each queued YAML file while the same output stays visible live in the active terminal.

Use the generated campaign execution report as the source index for the required final report in `doc/reports/campaign_results/`.

Final campaign-results deliverables must include:

- the canonical Markdown report;
- the styled PDF export;
- a real PDF validation pass before the task is closed.

## Active Campaign State

The currently prepared or active campaign is tracked in:

- `doc/running/active_training_campaign.yaml`

This state file stores:

- campaign name;
- planning report path;
- campaign configuration file list;
- launch commands;
- protected files that should not be modified silently while the campaign is active.

Operational rule:

- approved campaign preparation must now include generated YAML files, the exact launch command, the dedicated PowerShell launcher, and the matching launcher usage note;
- for LAN-remote campaigns, those launch commands are an operator handoff artifact: Codex prepares them, the user launches them manually, and the user later reports start and finish;
- when the user confirms that the campaign has started, the campaign state should be updated to `running`;
- while the campaign is prepared or running, any edit to a protected campaign file requires a `CRITICAL WARNING` and explicit user approval first;
- when the user says the campaign is finished, use the stored state to gather artifacts for the final results report;
- when the user cancels the campaign, inspect completed, failed, running, and pending items before deciding what to keep or stop.

Current finished Wave 1 residual-family follow-up campaign:

- campaign name: `wave1_residual_harmonic_family_campaign_2026_03_26_13_52_00`
- planning report: `doc/reports/campaign_plans/wave1/2026-03-26-13-52-00_wave1_residual_harmonic_family_campaign_plan_report.md`
- config package: `config/training/residual_harmonic_mlp/campaigns/2026-03-26_wave1_residual_harmonic_family_campaign/`
- canonical launcher: `scripts/campaigns/wave1/run_wave1_residual_harmonic_family_campaign.ps1`

## Typical Workflow For The Current Project

If you want to inspect the dataset and train the current baseline, use this sequence:

1. Activate the environment.
2. Check `config/datasets/transmission_error_dataset.yaml`.
3. Check `config/training/feedforward/presets/baseline.yaml`.
4. Inspect one dataset batch if needed.
5. Visualize one or more TE curves.
6. Start the selected structured baseline training run.
7. Inspect logs and checkpoints under `output/training_runs/` and check the best-result registries under `output/registries/`.

Example sequence:

```powershell
conda activate standard_ml_codex_env
python -c "from scripts.datasets.transmission_error_dataset import create_transmission_error_dataloaders_from_config; bundle=create_transmission_error_dataloaders_from_config(); print(len(bundle['train_dataset'])); print(len(bundle['validation_dataset']))"
python -m scripts.datasets.visualize_transmission_error --file-index 0 --save-path output\te_curve_0.png
conda run -n standard_ml_codex_env python scripts/training/train_feedforward_network.py
```

## Documentation Portal Build

The repository now includes the canonical `Sphinx + RTD` documentation portal under:

- `site/`

Current canonical scope:

- canonical `Sphinx` configuration;
- local build instructions and GitHub Pages publication notes;
- section shells for `Getting Started`, `Project Guide`, and `API Reference`.

Repository rule:

- when approved work adds or materially changes a script, feature, runnable
  workflow, or documentation entry point, update the affected `site/` content
  in the same task;
- regenerate the portal before closing the task;
- keep the warning-as-error build passing.

To build the local HTML portal:

```powershell
conda activate standard_ml_codex_env
python -m pip install -r requirements.txt
python -m sphinx -W -b html site site/_build/html
```

Successful output is written to:

- `site/_build/html`

The repository-owned publication path is now GitHub Pages through:

- `.github/workflows/publish-sphinx-pages.yml`
- `site/requirements-docs.txt`

The live public documentation portal is:

- `https://xilab-robotics.github.io/Physics-Informed-Neural-Networks/`

The GitHub Pages job intentionally uses a documentation-specific dependency set
instead of the full `requirements.txt` training environment. This keeps the CI
build light enough for hosted runners while preserving the local full
environment for real training, OCR, and video workflows.

The workflow now also opts into the GitHub Actions Node.js 24 runtime for
JavaScript-based actions, so the Pages pipeline is aligned with GitHub's
current deprecation path for Node.js 20 actions.

The canonical active GitHub branch is now:

- `main`

The remaining historical branches are retained only for provenance or old test
context:

- `base` -> legacy historical branch
- `test-manual-ml` -> legacy historical branch
- `test-codex-agent-pinns` -> legacy experimental/test branch

After the workflow is present in the default branch, configure the repository
Pages source to use `GitHub Actions` if that setting is not already enabled.

If the workflow `build` job succeeds but `deploy` is rejected with a message
that `main` is not allowed to deploy to `github-pages`, fix the
GitHub environment rule:

- open `Settings -> Environments -> github-pages`;
- inspect the deployment-branch protection settings;
- allow `main`, or remove the stale restrictive branch filter;
- rerun the workflow.

If the repository ruleset is already active, move its protected target from the
old canonical branch to `main`, keep `Repository Quality Checks` as the
required status check, and leave the temporary admin bypass in place only while
direct maintainer pushes are still intentionally allowed during development.

## Inference Status

Inference and export are not yet implemented as runnable project scripts.

This means there is currently no entry point such as:

- `inference/run_inference.py`
- `inference/export_onnx.py`
- `inference/runtime_validation.py`

So, at the moment, you cannot run a documented project inference or export command from this repository.

## What Is Already Ready For The Next Step

The repository now already has:

- a validated TE dataset;
- a YAML-driven dataset-processing configuration;
- PyTorch datasets and curve dataloaders;
- a TE visualization utility;
- a modular PyTorch Lightning feedforward training baseline;
- additional Wave 1 structured-neural baselines;
- tree-based structured benchmarks under the same artifact contract;
- a reusable datamodule and regression module structure for future architectures;
- an offline harmonic-wise comparison pipeline for paper-aligned baseline work;
- technical, script-level, and user-facing documentation aligned with the current structure.

## Harmonic-Wise Comparison Pipeline

The immediate post-`Wave 1` implementation branch is the offline
`Harmonic-Wise Comparison Pipeline`.

Its role is to create a paper-comparable baseline before opening the later
`Wave 2` temporal-model branch.

Canonical script:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py`

Canonical config:

- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/baseline.yaml`
- staged second-iteration presets:
  - `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/presets/track1_stage1_h013.yaml`
  - `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/presets/track1_stage2_h01340.yaml`
  - `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/presets/track1_stage3_h0134078.yaml`
  - `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/presets/track1_stage4_full_rcim_engineered.yaml`
  - `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/presets/track1_stage1_h013_random_forest_diagnostic.yaml`

Typical usage:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/run_harmonic_wise_comparison_pipeline.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/baseline.yaml `
  --output-suffix baseline_validation
```

Prepared comprehensive second-iteration campaign launcher:

```powershell
.\scripts\\campaigns\\track1\\harmonic_wise\\run_track1_second_iteration_harmonic_wise_campaign.ps1
```

Campaign package root:

- `config/paper_reimplementation/rcim_ml_compensation/harmonic_wise/campaigns/2026-04-09_track1_second_iteration_harmonic_wise_campaign/`

Campaign planning report:

- `doc/reports/campaign_plans/track1/harmonic_wise/2026-04-09-18-56-03_track1_second_iteration_harmonic_wise_campaign_plan_report.md`

Main outputs:

- `output/validation_checks/paper_reimplementation_rcim_harmonic_wise/forward/<run_instance_id>/`
- `doc/reports/analysis/validation_checks/track1/harmonic_wise/*_harmonic_wise_comparison_report.md`
- refreshed `doc/reports/analysis/Training Results Master Summary.md`

Current scope:

- harmonic-wise prediction of selected paper-aligned harmonic terms;
- TE reconstruction from the predicted harmonic stack;
- offline `Robot` and `Cycloidal` style playback;
- held-out offline percentage-error reporting for `Target A`.
- configurable engineered operating-condition features for the second Track 1
  iteration;
- per-harmonic error diagnostics in the validation summary and Markdown report.

Current non-scope:

- online compensation loop;
- uncompensated vs compensated runtime TE measurements;
- final `Table 9` style benchmark closure for `Target B`.

## Exact RCIM Paper Model Bank Validation

The stricter paper-faithful branch of `Track 1` is the
`Exact RCIM Paper Model Bank Validation` workflow.

Its role is to reconstruct the recovered paper family bank directly from the
recovered dataframe and exact `ampl_k` / `phase_k` target schema, rather than
only through the repository-owned harmonic-wise approximation branch.

Canonical script:

- `scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py`

Canonical config:

- `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml`

Main supporting report:

- `doc/reports/analysis/RCIM Exact Paper Model Bank Workflow.md`
- `doc/scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.md`

Typical usage:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/run_exact_paper_model_bank_validation.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/baseline.yaml `
  --output-suffix exact_paper_validation
```

Original-dataset bidirectional usage:

```powershell
conda run -n standard_ml_codex_env python scripts/paper_reimplementation/rcim_ml_compensation/run_original_dataset_exact_model_bank_validation.py `
  --config-path config/paper_reimplementation/rcim_ml_compensation/original_dataset_exact_model_bank/baseline_forward.yaml `
  --output-suffix forward_validation
```

Prepared batch launcher:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_exact_paper_model_bank_campaign.ps1
```

Optional PowerShell usage:

```powershell
.\scripts\\campaigns\\track1\\exact_paper\\run_exact_paper_model_bank_campaign.ps1 `
  -CondaEnvironmentName standard_ml_codex_env `
  -PythonExecutable python
```

Main outputs:

- `output/validation_checks/paper_reimplementation_rcim_exact_model_bank/forward/<run_instance_id>/`
- `doc/reports/analysis/validation_checks/track1/exact_paper/*_exact_paper_model_bank_report.md`
- `output/training_campaigns/track1/exact_paper/forward/uncategorized/shared/exact_paper_model_bank_campaign_2026_04_10_17_04_41/logs/`

Current scope:

- exact recovered input schema `rpm`, `deg`, `tor`;
- exact recovered target schema over `ampl_k` and `phase_k`;
- exact recovered family bank:
  `SVR`, `MLP`, `RF`, `DT`, `ET`, `ERT`, `GBM`, `HGBM`, `XGBM`, `LGBM`;
- family-wise `MultiOutputRegressor` fitting;
- one ONNX export per family and target;
- target-wise winner registry for later paper-style tabulation.
- prepared exact-paper campaign package under
  `config/paper_reimplementation/rcim_ml_compensation/exact_model_bank/campaigns/track1/exact_paper/forward/baseline_reproduction/shared/2026-04-10_exact_paper_model_bank_campaign/`;
- prepared launcher note:
  `doc/scripts/campaigns/run_exact_paper_model_bank_campaign.md`

Current non-scope:

- final target-wise deployed winner assembly;
- online compensation loop;
- TwinCAT/TestRig execution;
- `Track 2` direct-TE comparison.

This is enough to extend the project toward:

1. recurrent sequence models such as RNN or LSTM
2. evaluation entry points
3. inference/export utilities
4. PINN-specific losses and training flows

## Recommended Next Development Order

To extend the repository cleanly, the recommended order is:

1. execute and analyze the prepared Wave 1 structured-baseline campaign
2. add a sequence-aware recurrent baseline on top of the current `scripts/training/` and `scripts/models/` structure
3. add a dedicated evaluation entry point
4. add inference and export utilities
5. extend the regression module toward physics-informed loss composition
6. add PINN-specific training and validation workflows
