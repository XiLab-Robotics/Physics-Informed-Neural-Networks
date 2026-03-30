# Local LAN AI Inference And Transcription Architecture Report

## Overview

This technical note defines the approved scope for a repository-owned analysis
report about local and LAN-accessible AI infrastructure for TwinCAT/TestRig
video-guide processing and future repository workflows.

The immediate user goal is to stop depending on low free-tier API quotas for
video transcription while continuing to work from the current workstation. The
analysis must therefore compare local and self-hosted alternatives that can
provide:

- high-quality Italian technical transcript extraction for video guides;
- transcript cleanup and report-generation support through local LLMs;
- optional OCR and vision support for TwinCAT/TestRig screen analysis;
- a LAN-friendly serving model so a second workstation can act as an AI node;
- future reuse for training-adjacent requests or other repository tooling.

The requested deliverable is an in-repository analysis report, not an
implementation change yet.

## Technical Approach

The planned report will evaluate the problem as a multi-service architecture
decision rather than as a single-model choice.

The analysis will compare at least these families of options:

1. local speech-to-text pipelines such as `faster-whisper`, `whisper.cpp`, and
   related Whisper-compatible runtimes;
2. local LLM serving stacks such as `Ollama`, `LM Studio`, and comparable
   OpenAI-compatible local-serving solutions;
3. self-hosted or aggregator-style platforms that expose unified APIs, such as
   `LocalAI`, where relevant to transcript, OCR, or report generation;
4. hybrid workflows where STT is local while cleanup and report synthesis are
   served by a LAN-visible LLM endpoint;
5. the practical limits of continuing with Google GenAI free-tier usage as a
   fallback only, given the observed request quotas.

The report will be evidence-based and will combine:

- official product documentation for each serving/runtime option;
- repository context from the current video-guide workflow and TwinCAT/TestRig
  documentation;
- local empirical findings already observed in this workspace, such as the
  current `faster-whisper` smoke tests and CUDA-library limitations on the
  current machine;
- the hardware profile of the second workstation proposed as a LAN AI server.

The report will explicitly separate:

- what can be done entirely on the current PC;
- what is better delegated to the second PC over LAN;
- what remains cloud-dependent or quota-limited;
- what is recommended as the default production path for this repository.

## Involved Components

- `README.md`
  Register this technical note as required by the repository workflow.
- `doc/reports/analysis/`
  Planned location for the architecture comparison report.
- `.temp/video_guides/`
  Existing media source and analysis target that motivate the decision.
- `scripts/tooling/extract_video_guide_knowledge.py`
  Current high-quality workflow whose provider dependency is under review.
- `scripts/tooling/analyze_video_guides.py`
  Existing OCR and snapshot extraction support script.
- `doc/reference_codes/testrig_twincat_ml_reference.md`
  Existing TwinCAT/TestRig canonical reference context.
- `doc/reference_codes/testrig_twincat_video_guides_reference.md`
  Current repository-owned reference for the video-guide workflow.

No subagent usage is planned for this scope.

## Implementation Steps

1. Create and register this technical note in `README.md`.
2. Gather current official documentation for the candidate local and LAN
   serving options.
3. Consolidate the already observed local smoke-test results and hardware
   constraints into an implementation-facing comparison.
4. Write a canonical report under `doc/reports/analysis/` covering:
   architecture options, pros/cons, expected quality, deployment complexity,
   LAN-serving patterns, and a recommended path for this repository.
5. Run scoped Markdown checks on the created and modified repository-owned
   Markdown files before closing the task.
